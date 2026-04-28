import type { Domain, ItemFile, ProcessedSdk, PSJAPIServer } from '../../types';

// ─── Output entry types ───────────────────────────────────────────────────────

interface BaseEntry {
    path: string;
    schemaId: string;
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
    domain: Domain;
    id: string;
}

// ─── Builder config ───────────────────────────────────────────────────────────

export type GroupBy = 'domain' | 'group' | 'none';

export interface PsjPagesBuilderConfig {
    /**
     * How to group items in the output:
     * - 'domain' — one folder per domain (macro, psj-command, …)
     * - 'group'  — one folder per `group:` field value; ungrouped items at root
     * - 'none'   — flat list, one page per item (default)
     */
    groupBy?: GroupBy;

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

function defaultItemPath(item: ItemFile): string {
    return `${item.domain}/${idToSlug(item.id)}`;
}

// ─── fromSdk ──────────────────────────────────────────────────────────────────

/**
 * Build a flat/grouped list of OutputEntry objects from a ProcessedSdk.
 *
 * Called once per schema (analogous to `fromSchema` in openapi/builder.ts).
 */
export function fromSdk(
    schemaId: string,
    sdk: ProcessedSdk,
    config: PsjPagesBuilderConfig = {},
): OutputEntry[] {
    const { groupBy = 'none', per = 'item', name: nameFn } = config;
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

    if (per === 'item') {
        if (groupBy === 'none') {
            // Flat list, one OutputEntry per item
            for (const [_, item] of sdk.items) {
                const filePath = nameFn ? nameFn(item) : defaultItemPath(item);
                entries.push(makeItemOutput(schemaId, item, `${filePath}.mdx`));
            }
        } else if (groupBy === 'domain') {
            for (const [domain, groupMap] of byDomain) {
                const domainEntries: OutputEntry[] = [];
                for (const [, items] of groupMap) {
                    for (const item of items) {
                        const filePath = nameFn ? nameFn(item) : `${domain}/${idToSlug(item.id)}`;
                        domainEntries.push(makeItemOutput(schemaId, item, `${filePath}.mdx`));
                    }
                }
                entries.push({
                    type: 'group',
                    path: domain,
                    schemaId,
                    info: { title: domainTitle(domain as Domain) },
                    entries: domainEntries,
                });
            }
        } else {
            // groupBy === 'group'
            // Collect all groups across domains
            const byGroup = new Map<string, ItemFile[]>();
            for (const [, groupMap] of byDomain) {
                for (const [group, items] of groupMap) {
                    if (!byGroup.has(group)) byGroup.set(group, []);
                    byGroup.get(group)!.push(...items);
                }
            }
            for (const [group, items] of byGroup) {
                const groupEntries: OutputEntry[] = items.map((item) => {
                    const filePath = nameFn
                        ? nameFn(item)
                        : `${slugify(group === '__ungrouped__' ? 'misc' : group)}/${idToSlug(item.id)}`;
                    return makeItemOutput(schemaId, item, `${filePath}.mdx`);
                });
                const groupLabel = group === '__ungrouped__' ? 'Miscellaneous' : group;
                entries.push({
                    type: 'group',
                    path: slugify(groupLabel),
                    schemaId,
                    info: { title: groupLabel },
                    entries: groupEntries,
                });
            }
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
                schemaId,
                info: { title: groupLabel },
                items: items.map((item) => ({
                    key: `${item.domain}/${item.id}`,
                    domain: item.domain,
                    id: item.id,
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
                schemaId,
                info: { title: domainTitle(domain as Domain) },
                items: allItems.map((item) => ({
                    key: `${item.domain}/${item.id}`,
                    domain: item.domain,
                    id: item.id,
                })),
            });
        }
    }

    return entries;
}

function makeItemOutput(schemaId: string, item: ItemFile, filePath: string): ItemOutput {
    return {
        type: 'item',
        path: filePath,
        schemaId,
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

function domainTitle(domain: Domain): string {
    const map: Record<Domain, string> = {
        macro: 'Macros',
        'psj-command': 'PSJ Commands',
        'psj-utility': 'PSJ Utilities',
        'psj-gui': 'PSJ GUI',
    };
    return map[domain] ?? domain;
}

// ─── fromServer ───────────────────────────────────────────────────────────────

export async function fromServer(
    server: PSJAPIServer,
    config: PsjPagesBuilderConfig = {},
): Promise<Record<string, OutputEntry[]>> {
    const sdk = await server.getProcessedSdk();
    const schemaId = server.options.root;
    return { [schemaId]: fromSdk(schemaId, sdk, config) };
}
