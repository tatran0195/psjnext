// psjd/src/index.ts
// Static MDX file generation — run at build time.
// This entry point imports Node.js builtins (fs, path) intentionally.

import fs from 'node:fs';
import path from 'node:path';

import type { ParsedSDK, ResolvedItem } from './types.js';

import { resolveAll } from './resolve.js';
import { createSDK } from './server.js';

// ─── Public API ───────────────────────────────────────────────────────────────

export interface GenerateFilesOptions {
    /**
     * Path to sdk.psjd.yaml, or a pre-parsed ParsedSDK object.
     * When a string, _groups/ and domain folders are resolved relative to it.
     */
    input: string | ParsedSDK;

    /** Directory where .mdx files will be written (created if absent). */
    output: string;

    /**
     * Page granularity:
     * - 'item'      → one .mdx per callable (default)
     * - 'namespace' → one .mdx per dotted namespace (all items inline)
     * - 'domain'    → one .mdx per domain
     */
    per?: 'item' | 'namespace' | 'domain';

    /**
     * SDK version to render. Items introduced after this version are excluded.
     * Defaults to sdk.current_version.
     */
    version?: string;

    /**
     * Copy item.description into MDX frontmatter.
     * Disable if descriptions contain characters that break YAML parsing.
     */
    includeDescription?: boolean;

    /**
     * Custom output path resolver.
     * Return a path relative to `output`, without extension.
     */
    name?: (item: ResolvedItem, sdk: ParsedSDK) => string;

    /**
     * Generate index pages with links to all items in each namespace group.
     */
    index?: boolean;

    /**
     * Extra import statements injected at the top of every generated MDX file.
     */
    imports?: Array<{ names: string[]; from: string }>;
}

export async function generateFiles(options: GenerateFilesOptions): Promise<void> {
    const {
        input,
        output,
        per = 'item',
        includeDescription = true,
        name: customName,
        imports = [],
    } = options;

    const sdk: ParsedSDK = typeof input === 'string' ? await createSDK(input) : input;

    const version = options.version ?? sdk.currentVersion;
    const items = resolveAll(sdk, version);

    fs.mkdirSync(output, { recursive: true });

    if (per === 'item') {
        for (const item of items) {
            const rel = customName ? customName(item, sdk) : defaultItemPath(item);
            const outPath = path.join(output, rel + '.mdx');
            fs.mkdirSync(path.dirname(outPath), { recursive: true });
            fs.writeFileSync(outPath, renderItemPage(item, version, includeDescription, imports));
        }
        if (options.index) {
            writeIndexPages(items, output, imports);
        }
    } else {
        const grouped = groupBy(items, per);
        for (const [groupKey, groupItems] of grouped) {
            const slug = groupKey.toLowerCase().replace(/[^a-z0-9]+/g, '-');
            const outPath = path.join(output, slug + '.mdx');
            fs.writeFileSync(outPath, renderGroupPage(groupKey, groupItems, version, imports));
        }
    }

    const count = per === 'item' ? items.length : groupBy(items, per).size;
    console.info(`[psjd] Generated ${count} page(s) at SDK ${version} → ${output}`);
}

// ─── MDX rendering helpers ────────────────────────────────────────────────────

function renderItemPage(
    item: ResolvedItem,
    version: string,
    includeDescription: boolean,
    imports: Array<{ names: string[]; from: string }>,
): string {
    const fm: Record<string, string> = {
        title: JSON.stringify(item.title),
        psjdId: JSON.stringify(item.id),
        psjdVersion: JSON.stringify(version),
    };
    if (includeDescription && item.description) {
        const safe = item.description.replace(/\n+/g, ' ').replace(/"/g, '\\"').trim();
        fm['description'] = JSON.stringify(safe);
    }

    const frontmatter = Object.entries(fm)
        .map(([k, v]) => `${k}: ${v}`)
        .join('\n');

    const importLines = [
        `import { CallablePage } from 'psjd/ui';`,
        ...imports.map((i) => `import { ${i.names.join(', ')} } from '${i.from}';`),
    ].join('\n');

    return `---\n${frontmatter}\n---\n\n${importLines}\n\n<CallablePage id="${item.id}" version="${version}" />\n`;
}

function renderGroupPage(
    groupKey: string,
    items: ResolvedItem[],
    version: string,
    imports: Array<{ names: string[]; from: string }>,
): string {
    const importLines = [
        `import { CallablePage } from 'psjd/ui';`,
        ...imports.map((i) => `import { ${i.names.join(', ')} } from '${i.from}';`),
    ].join('\n');

    const pages = items
        .map((it) => `<CallablePage id="${it.id}" version="${version}" />`)
        .join('\n\n');

    return `---\ntitle: ${JSON.stringify(groupKey)}\n---\n\n${importLines}\n\n${pages}\n`;
}

function writeIndexPages(
    items: ResolvedItem[],
    output: string,
    _imports: Array<{ names: string[]; from: string }>,
): void {
    const grouped = groupBy(items, 'namespace');
    for (const [groupKey, groupItems] of grouped) {
        const slug = groupKey.toLowerCase().replace(/[^a-z0-9]+/g, '-');
        const outPath = path.join(output, slug, 'index.mdx');
        fs.mkdirSync(path.dirname(outPath), { recursive: true });
        const links = groupItems
            .map((it) => `- [${it.title}](./${it.id.toLowerCase()})`)
            .join('\n');
        fs.writeFileSync(outPath, `---\ntitle: ${JSON.stringify(groupKey)}\n---\n\n${links}\n`);
    }
}

function defaultItemPath(item: ResolvedItem): string {
    const ns = (item.namespace ?? item.domain).toLowerCase().replace(/\./g, '-');
    const id = item.id.toLowerCase();
    return `${ns}/${id}`;
}

function groupBy(items: ResolvedItem[], key: 'namespace' | 'domain'): Map<string, ResolvedItem[]> {
    const map = new Map<string, ResolvedItem[]>();
    for (const item of items) {
        const k = key === 'namespace' ? (item.namespace ?? item.domain) : item.domain;
        const arr = map.get(k);
        if (arr) arr.push(item);
        else map.set(k, [item]);
    }
    return map;
}

// Re-export types and core utilities consumers may need
export type { ItemFile, ParamGroupFile, ParsedSDK, ResolvedItem, ResolvedParam } from './types.js';
// createPsjd factory + createSDK (advanced use)
export { resolveAll, resolveItem, semverCompare } from './resolve.js';
export { createPsjd, createSDK } from './server.js';
export type { createPsjdOptions, PsjdInstance, PsjdPageData, PsjdSourceOptions } from './server.js';
// Sidecar support
export {
    applySidecars,
    mergeGroupSidecar,
    mergeItemSidecar,
    sidecarPath,
    tryLoadSidecar,
    validateGroupSidecar,
    validateItemSidecar,
} from './sidecar.js';
export type {
    SidecarEnumValue,
    SidecarItemFile,
    SidecarParam,
    SidecarParamGroupFile,
    SidecarReturns,
    SidecarValidationError,
    SidecarVersionDelta,
} from './sidecar.js';
