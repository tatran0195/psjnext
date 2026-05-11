import type { DataTypeFile, Domain, ItemFile, ProcessedSdk, PSJAPIServer } from '../../types';

// ─── Output entry types ───────────────────────────────────────────────────────

interface BaseEntry {
    path: string;
    info: {
        title: string;
        description?: string;
    };
}

export interface ItemOutput extends BaseEntry {
    type: 'item';
    item: ItemRef;
}

export interface GroupOutput extends BaseEntry {
    type: 'group';
    entries: OutputEntry[];
}

export interface PageOutput extends BaseEntry {
    type: 'page';
    items: ItemRef[];
}

export type OutputEntry = ItemOutput | GroupOutput | PageOutput;

export interface ItemRef {
    /** "<domain>/<id>" */
    key: string;
    domain: Domain | 'data-type';
    id: string;
}

// ─── Builder config ───────────────────────────────────────────────────────────

export interface PsjPagesBuilderConfig {
    /**
     * Produce one page per item (default) or one page per group.
     */
    per?: 'item' | 'group' | 'domain';

    /**
     * Custom file-name transform.  Receives the item id and must return a
     * forward-slash path (no extension).
     */
    name?: (item: ItemFile) => string;
}

// ─── Path helpers ─────────────────────────────────────────────────────────────

function slugify(str: string): string {
    return str
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
}

/**
 * Convert an item id to a URL-safe kebab-case path segment.
 *
 * Handles three common id styles:
 *   PascalCase      AdvcStaticProcess          → advc-static-process
 *   Dot-delimited   Analysis.ADVC.MakeProcess  → analysis-advc-make-process
 *   Hyphen-delimited Analysis-ADVC-MakeProcess → analysis-advc-make-process
 */
function idToSlug(id: string): string {
    return id
        .replace(/([a-z])([A-Z])/g, '$1-$2') // camelCase → kebab
        .replace(/([A-Z]+)([A-Z][a-z])/g, '$1-$2') // consecutive caps: ADVCStatic → ADVC-Static
        .replace(/[._]+/g, '-') // dots / underscores → hyphen
        .toLowerCase()
        .replace(/--+/g, '-')
        .replace(/^-|-$/g, '');
}

// ─── fromSdk ──────────────────────────────────────────────────────────────────

/**
 * Build a flat/grouped list of OutputEntry objects from a ProcessedSdk.
 *
 * Called once per schema (analogous to `fromSchema` in openapi/builder.ts).
 */
export function fromSdk(sdk: ProcessedSdk, config: PsjPagesBuilderConfig = {}): OutputEntry[] {
    const { per = 'item', name: nameFn } = config;
    const entries: OutputEntry[] = [];

    // Collect all items into a map keyed by domain→group→items
    type DomainMap = Map<string, Map<string, ItemFile[]>>; // domain → (group → items[])
    const byDomain: DomainMap = new Map();

    for (const [_, item] of sdk.items) {
        if (!byDomain.has(item.domain)) byDomain.set(item.domain, new Map());
        const domainMap = byDomain.get(item.domain)!;
        const g = item.group ?? '__ungrouped__';
        if (!domainMap.has(g)) domainMap.set(g, []);
        domainMap.get(g)!.push(item);
    }

    // Collect data-types into categories/groups
    const dtMap = new Map<string, DataTypeFile[]>();
    if (sdk.dataTypes && sdk.dataTypes.size > 0) {
        for (const [_, dt] of sdk.dataTypes) {
            const groupName = dt.id.includes('/') ? dt.id.slice(0, dt.id.lastIndexOf('/')) : '__ungrouped__';
            if (!dtMap.has(groupName)) dtMap.set(groupName, []);
            dtMap.get(groupName)!.push(dt);
        }
    }

    if (per === 'item') {
        for (const [domain, groupMap] of byDomain) {
            // Separate ungrouped items from grouped items
            const ungroupedEntries: OutputEntry[] = [];
            const namedGroupEntries = new Map<string, OutputEntry[]>();

            for (const [group, items] of groupMap) {
                for (const item of items) {
                    const filePath = nameFn ? nameFn(item) : `${domain}/${idToSlug(item.id)}`;
                    const output = makeItemOutput(item, `${filePath}.mdx`);

                    if (group === '__ungrouped__') {
                        ungroupedEntries.push(output);
                    } else {
                        if (!namedGroupEntries.has(group)) namedGroupEntries.set(group, []);
                        namedGroupEntries.get(group)!.push(output);
                    }
                }
            }

            // Build domain-level entries: ungrouped items first, then named sub-groups
            const domainEntries: OutputEntry[] = [...ungroupedEntries];
            for (const [group, groupItems] of namedGroupEntries) {
                const groupSlug = slugify(group);
                domainEntries.push({
                    type: 'group',
                    path: `${domain}/${groupSlug}`,
                    info: { title: group },
                    entries: groupItems,
                });
            }

            entries.push({
                type: 'group',
                path: domain,
                info: { title: domainTitle(sdk, domain as Domain) },
                entries: domainEntries,
            });
        }

        if (dtMap.size > 0) {
            const dtDomainEntries: OutputEntry[] = [];
            const ungroupedDtEntries: OutputEntry[] = [];
            const namedDtGroupEntries = new Map<string, OutputEntry[]>();

            for (const [group, dts] of dtMap) {
                for (const dt of dts) {
                    const filePath = `data-type/${idToSlug(dt.id)}`;
                    const output: ItemOutput = {
                        type: 'item',
                        path: `${filePath}.mdx`,
                        info: { title: dt.title, description: dt.description },
                        item: { key: `data-type/${dt.id}`, domain: 'data-type', id: dt.id },
                    };

                    if (group === '__ungrouped__') {
                        ungroupedDtEntries.push(output);
                    } else {
                        if (!namedDtGroupEntries.has(group)) namedDtGroupEntries.set(group, []);
                        namedDtGroupEntries.get(group)!.push(output);
                    }
                }
            }

            dtDomainEntries.push(...ungroupedDtEntries);
            for (const [group, groupItems] of namedDtGroupEntries) {
                const meta = sdk.groupMetas?.get(`data-type/${group}`);
                dtDomainEntries.push({
                    type: 'group',
                    path: `data-type/${group}`, // Group is already relative path like pre/enum
                    info: { title: meta?.title ?? group },
                    entries: groupItems,
                });
            }

            entries.push({
                type: 'group',
                path: 'data-type',
                info: { title: 'Data Types' },
                entries: dtDomainEntries,
            });
        }
    } else if (per === 'group') {
        // One page per group; list items on that page
        const byGroup = new Map<string, ItemFile[]>();
        for (const [, groupMap] of byDomain) {
            for (const [group, items] of groupMap) {
                if (!byGroup.has(group)) byGroup.set(group, []);
                byGroup.get(group)!.push(...items);
            }
        }
        for (const [group, items] of byGroup) {
            const groupLabel = group === '__ungrouped__' ? 'Miscellaneous' : group;
            const filePath = slugify(groupLabel);
            entries.push({
                type: 'page',
                path: `${filePath}.mdx`,
                info: { title: groupLabel },
                items: items.map((item) => ({
                    key: `${item.domain}/${item.id}`,
                    domain: item.domain,
                    id: item.id,
                })),
            });
        }

        for (const [group, dts] of dtMap) {
            const meta = sdk.groupMetas?.get(`data-type/${group}`);
            const groupLabel = group === '__ungrouped__' ? 'Data Types' : (meta?.title ?? group);
            const filePath = `data-type-${slugify(groupLabel)}`;
            entries.push({
                type: 'page',
                path: `${filePath}.mdx`,
                info: { title: groupLabel },
                items: dts.map((dt) => ({
                    key: `data-type/${dt.id}`,
                    domain: 'data-type',
                    id: dt.id,
                })),
            });
        }
    } else {
        // per === 'domain' — one page per domain
        for (const [domain, groupMap] of byDomain) {
            const allItems: ItemFile[] = [];
            for (const items of groupMap.values()) allItems.push(...items);
            entries.push({
                type: 'page',
                path: `${domain}.mdx`,
                info: { title: domainTitle(sdk, domain as Domain) },
                items: allItems.map((item) => ({
                    key: `${item.domain}/${item.id}`,
                    domain: item.domain,
                    id: item.id,
                })),
            });
        }

        if (dtMap.size > 0) {
            const allDts: DataTypeFile[] = [];
            for (const dts of dtMap.values()) allDts.push(...dts);
            entries.push({
                type: 'page',
                path: `data-type.mdx`,
                info: { title: 'Data Types' },
                items: allDts.map((dt) => ({
                    key: `data-type/${dt.id}`,
                    domain: 'data-type',
                    id: dt.id,
                })),
            });
        }
    }

    return entries;
}

function makeItemOutput(item: ItemFile, filePath: string): ItemOutput {
    return {
        type: 'item',
        path: filePath,
        info: {
            title: item.title,
            description: item.description,
        },
        item: {
            key: `${item.domain}/${item.id}`,
            domain: item.domain,
            id: item.id,
        },
    };
}

function domainTitle(sdk: ProcessedSdk, domain: Domain): string {
    const entry = sdk.manifest.domains.find((d) => d.id === domain);
    return entry?.title ?? domain;
}

// ─── fromServer ───────────────────────────────────────────────────────────────

export async function fromServer(
    server: PSJAPIServer,
    config: PsjPagesBuilderConfig = {},
): Promise<Record<string, OutputEntry[]>> {
    const sdk = await server.getProcessedSdk();
    return { sdk: fromSdk(sdk, config) };
}
