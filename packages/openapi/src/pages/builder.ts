/**
 * Maps ResolvedItem[] → OutputEntry[] using the same OutputEntry union
 * that fumadocs-core source consumes.
 *
 * Hierarchy:
 *   OutputGroup (domain)
 *     OutputGroup (group within domain)  ← only if item.group is set
 *       PageOutput per item
 */
import type { Domain, JCallManifest, ResolvedItem } from '../types';

// ─── Output types (mirrored from old builder, kept minimal) ──────────────────

export interface BaseEntry {
    path: string;
    info: { title: string; description?: string };
}

export interface PageOutput extends BaseEntry {
    type: 'page';
    item: ResolvedItem;
}

export interface OutputGroup extends BaseEntry {
    type: 'group';
    entries: OutputEntry[];
    /** Domain id when this is a domain-level group */
    domain?: Domain;
}

export type OutputEntry = PageOutput | OutputGroup;

// ─── Builder ─────────────────────────────────────────────────────────────────

export interface BuilderOptions {
    /**
     * Controls output file path for each item.
     * Default: `{domain}/{id}.mdx`
     */
    name?: (item: ResolvedItem) => string;
    /** Convert display names to slugs for group paths */
    slugify?: (s: string) => string;
    manifest?: JCallManifest;
}

export function buildEntries(
    items: Map<string, ResolvedItem>,
    options: BuilderOptions = {},
): OutputEntry[] {
    const {
        slugify = (s) => s.replace(/\s+/g, '-').toLowerCase(),
        name = (item) => `${item.domain}/${item.id}.mdx`,
    } = options;

    // domain → group → items
    const domainGroups = new Map<Domain, Map<string | '__none__', ResolvedItem[]>>();

    for (const item of items.values()) {
        if (!domainGroups.has(item.domain)) {
            domainGroups.set(item.domain, new Map());
        }
        const groups = domainGroups.get(item.domain)!;
        const key = item.group ?? '__none__';
        if (!groups.has(key)) groups.set(key, []);
        groups.get(key)!.push(item);
    }

    const top: OutputEntry[] = [];

    for (const [domain, groupMap] of domainGroups) {
        const domainEntries: OutputEntry[] = [];

        for (const [groupKey, groupItems] of groupMap) {
            const pages: PageOutput[] = groupItems.map((item) => ({
                type: 'page',
                item,
                path: name(item),
                info: { title: item.title, description: item.description },
            }));

            if (groupKey === '__none__') {
                domainEntries.push(...pages);
            } else {
                const groupSlug = `${domain}/${slugify(groupKey)}`;
                domainEntries.push({
                    type: 'group',
                    path: groupSlug,
                    info: { title: groupKey },
                    entries: pages.map((p) => ({
                        ...p,
                        path: `${groupSlug}/${p.item.id}.mdx`,
                    })),
                });
            }
        }

        top.push({
            type: 'group',
            domain,
            path: slugify(domain),
            info: {
                title: options.manifest?.domains.find((d) => d.id === domain)?.title ?? domain,
            },
            entries: domainEntries,
        });
    }

    return top;
}
