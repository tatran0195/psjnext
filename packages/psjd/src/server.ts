// psjd/src/server.ts
// Fumadocs v16 Loader API integration.
// Server-side only — freely uses Node.js builtins.

import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';

import type { ItemFile, ParamGroupFile, ParsedSDK, ResolvedItem, SDKManifest } from './types.js';

import { resolveAll } from './resolve.js';
import { applySidecars } from './sidecar.js';

// ─── createPsjd factory ──────────────────────────────────────────────────────
//
// Mirrors createOpenAPI() from fumadocs-openapi/server.
// Holds configuration and is passed to psjdSource().
//
// Usage:
//   // lib/psjd.ts
//   import { createPsjd } from 'psjd/server';
//   export const psjd = createPsjd({ input: './content/psjd/sdk.psjd.yaml' });

export interface createPsjdOptions {
    /**
     * Path to sdk.psjd.yaml (absolute or cwd-relative).
     */
    input: string;
    /**
     * Root directory containing _groups/ and domain folders.
     * Defaults to the directory of `input`.
     */
    baseDir?: string;
    /**
     * Supported locale codes, e.g. ['en', 'ja'].
     * When provided, createSDK is called once per locale and each locale's
     * items/groups are merged with the corresponding sidecar translations.
     * The first entry becomes the default locale.
     */
    locales?: string[];
    /**
     * If true, sidecar validation errors throw instead of logging a warning.
     * Recommended for CI.
     */
    strict?: boolean;
}

/** Opaque handle returned by createPsjd(). Pass it to psjdSource(). */
export interface PsjdInstance {
    readonly _options: createPsjdOptions;
}

/**
 * Create a psjd instance from configuration.
 *
 * @example
 * // lib/psjd.ts
 * import { createPsjd } from 'psjd/server';
 *
 * export const psjd = createPsjd({
 *   input: './content/psjd/sdk.psjd.yaml',
 *   locales: ['en', 'ja'],
 * });
 */
export function createPsjd(options: createPsjdOptions): PsjdInstance {
    return { _options: options };
}

// ─── SDK loader ───────────────────────────────────────────────────────────────

/**
 * Parse the full psjd v2 file tree into an in-memory ParsedSDK.
 *
 * @param sdkYamlPath  Path to sdk.psjd.yaml (absolute or cwd-relative).
 * @param baseDir      Root containing _groups/ and domain folders.
 *                     Defaults to the directory of sdkYamlPath.
 * @param options.locale  BCP-47 locale tag (e.g. "ja"). When provided,
 *                        sidecar files (<id>.<locale>.yaml) are loaded
 *                        alongside base files and their translations merged in.
 * @param options.strict  If true, sidecar validation errors throw instead of warn.
 */
export async function createSDK(
    sdkYamlPath: string,
    baseDir?: string,
    options: { locale?: string; strict?: boolean } = {},
): Promise<ParsedSDK> {
    const resolvedYaml = path.resolve(process.cwd(), sdkYamlPath);

    if (!fs.existsSync(resolvedYaml)) {
        throw new Error(`sdk.psjd.yaml not found at: ${resolvedYaml}`);
    }

    const root = baseDir ? path.resolve(process.cwd(), baseDir) : path.dirname(resolvedYaml);

    const manifest: SDKManifest = parseYaml(fs.readFileSync(resolvedYaml, 'utf8'));

    if (manifest.psjd !== '2.0') {
        throw new Error(`Unsupported psjd version: "${manifest.psjd}". Expected "2.0".`);
    }

    // ── Load param groups ──────────────────────────────────────────────────────
    const groups = new Map<string, ParamGroupFile>();
    const groupsDir = path.join(root, '_groups');

    if (fs.existsSync(groupsDir)) {
        for (const f of fs.readdirSync(groupsDir).sort()) {
            if (!f.endsWith('.yaml') && !f.endsWith('.yml')) continue;
            // Sidecar files are <id>.<locale>.yaml — stem has a dot. Skip them here.
            const stem = f.replace(/\.ya?ml$/, '');
            if (stem.includes('.')) continue;
            const raw = fs.readFileSync(path.join(groupsDir, f), 'utf8');
            const g: ParamGroupFile = parseYaml(raw);
            if (g.kind !== 'param_group') {
                throw new Error(
                    `File "${f}" in _groups/ has kind "${g.kind}" instead of "param_group"`,
                );
            }
            if (groups.has(g.id)) {
                throw new Error(`Duplicate param group id: "${g.id}" (in ${f})`);
            }
            groups.set(g.id, g);
        }
    }

    // ── Load item files from each domain folder ────────────────────────────────
    const items = new Map<string, ItemFile>();
    const domainIds = manifest.domains.map((d) => d.id);

    for (const domainId of domainIds) {
        const domainDir = path.join(root, domainId);
        if (!fs.existsSync(domainDir)) continue;

        for (const f of fs.readdirSync(domainDir).sort()) {
            if (!f.endsWith('.yaml') && !f.endsWith('.yml')) continue;
            // Skip sidecar files (<id>.<locale>.yaml) — stem contains a dot.
            const stem = f.replace(/\.ya?ml$/, '');
            if (stem.includes('.')) continue;
            const raw = fs.readFileSync(path.join(domainDir, f), 'utf8');
            const item: ItemFile = parseYaml(raw);

            if (!item.id) {
                throw new Error(`Item file "${f}" in ${domainId}/ is missing an "id" field`);
            }
            if (items.has(item.id)) {
                throw new Error(`Duplicate item id: "${item.id}" (in ${domainId}/${f})`);
            }
            items.set(item.id, item);
        }
    }

    const sdk: ParsedSDK = {
        manifest,
        items,
        groups,
        currentVersion: manifest.current_version,
        versionIds: manifest.versions.map((v) => v.id),
    };

    // ── Apply sidecar translations ─────────────────────────────────────────────
    if (options.locale) {
        applySidecars({
            items,
            groups,
            rootDir: root,
            domainIds,
            locale: options.locale,
            strict: !!options.strict,
        });
    }

    return sdk;
}

// ─── Virtual Source for Fumadocs Loader API (v16) ─────────────────────────────
//
// Page data contains only serializable primitives — no Map/Set objects.
// The locale field integrates with Fumadocs' i18n loader machinery:
// loader({ i18n }) generates a separate page tree for each locale using
// the `locale` tag on each SourceFile.

export interface PsjdSourceOptions {
    /**
     * SDK version for page tree generation. Defaults to sdk.currentVersion.
     */
    version?: string;
    /**
     * How to organise the sidebar tree. Defaults to 'namespace'.
     */
    groupBy?: 'namespace' | 'domain' | 'group';
    /**
     * The base directory path segment used in virtual file paths.
     * Mirrors the `baseDir` option in openapiSource().
     * Defaults to 'psjd'.
     */
    baseDir?: string;
}

/** Serializable page data for a psjd item page. */
export interface PsjdPageData {
    readonly type: 'psjd';
    readonly psjdId: string;
    readonly version: string;
    readonly locale: string;
    readonly title: string;
    readonly description?: string;
    readonly domain: string;
    readonly namespace?: string;
}

type SourceFile =
    | { type: 'page'; path: string; locale?: string; data: PsjdPageData }
    | { type: 'meta'; path: string; locale?: string; data: { title: string; pages: string[] } };

/**
 * Create a Fumadocs v16 Source from a PsjdInstance.
 * Async — loads all locale SDKs and emits locale-tagged virtual files.
 *
 * Usage (with multiple sources and i18n):
 *
 * ```ts
 * // lib/source.ts
 * import { loader, multiple } from 'fumadocs-core/source';
 * import { psjdSource, psjdPlugin } from 'psjd/server';
 * import { docs } from 'collections/server';
 * import { i18n } from '@/lib/i18n';
 * import { psjd } from '@/lib/psjd';
 *
 * export const source = loader(
 *   multiple({
 *     docs: docs.toFumadocsSource(),
 *     psjd: await psjdSource(psjd),
 *   }),
 *   {
 *     baseUrl: '/docs',
 *     i18n,
 *     plugins: [psjdPlugin()],
 *   },
 * );
 * ```
 */
export async function psjdSource(
    psjd: PsjdInstance,
    options: PsjdSourceOptions = {},
): Promise<{ files: SourceFile[] }> {
    const { input, baseDir: inputBaseDir, locales, strict } = psjd._options;
    const { groupBy = 'namespace', baseDir: virtualBase = 'psjd' } = options;

    // Determine which locales to load.
    // If no locales configured, load the base file once with no locale tag.
    const localesToLoad: Array<string | undefined> =
        locales && locales.length > 0 ? locales : [undefined];

    const files: SourceFile[] = [];

    for (const locale of localesToLoad) {
        const sdk = await createSDK(input, inputBaseDir, {
            locale: locale ?? 'en',
            strict: strict ?? false,
        });

        const version = options.version ?? sdk.currentVersion;
        const resolvedItems = resolveAll(sdk, version);
        const grouped = groupResolvedItems(resolvedItems, groupBy);
        const usedSlugs = new Set<string>();
        const effectiveLocale = locale ?? sdk.manifest.domains[0]?.id ?? 'en';

        for (const [groupKey, groupItems] of grouped) {
            const folderSlug = toSlug(groupKey, usedSlugs);
            const pageNames: string[] = [];

            for (const item of groupItems) {
                const itemSlug = toSlug(item.id, usedSlugs);
                pageNames.push(itemSlug);

                const pageData: PsjdPageData = {
                    type: 'psjd',
                    psjdId: item.id,
                    version,
                    locale: effectiveLocale,
                    title: item.title,
                    description: item.description,
                    domain: item.domain,
                    namespace: item.namespace ?? '',
                };

                files.push({
                    type: 'page',
                    // Virtual path format: <virtualBase>/<folder>/<item>.mdx
                    path: `${virtualBase}/${folderSlug}/${itemSlug}.mdx`,
                    // locale tag triggers Fumadocs i18n machinery — omit for non-i18n
                    // ...(effectiveLocale !== undefined ? { locale: effectiveLocale } : {}),
                    locale: effectiveLocale,
                    data: pageData,
                });
            }

            files.push({
                type: 'meta',
                path: `${virtualBase}/${folderSlug}/meta.json`,
                // ...(effectiveLocale !== undefined ? { locale: effectiveLocale } : {}),
                locale: effectiveLocale,
                data: {
                    title: groupKey,
                    pages: pageNames,
                },
            });
        }
    }

    return { files };
}

// ─── Loader plugin ────────────────────────────────────────────────────────────

/**
 * Optional Fumadocs v16 loader plugin for psjd sources.
 * Pass to loader({ plugins: [psjdPlugin()] }).
 * Extend to attach badges, icons, or custom page tree transforms.
 */
export function psjdPlugin(): Record<string, never> {
    return {};
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

/** Slugify and guarantee uniqueness within the given set. */
function toSlug(s: string, used: Set<string>): string {
    const base = s
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');

    let slug = base;
    let n = 2;
    while (used.has(slug)) {
        slug = `${base}-${n++}`;
    }
    used.add(slug);
    return slug;
}

function groupResolvedItems(
    items: ResolvedItem[],
    groupBy: 'namespace' | 'domain' | 'group',
): Map<string, ResolvedItem[]> {
    const map = new Map<string, ResolvedItem[]>();

    for (const item of items) {
        const key =
            groupBy === 'namespace'
                ? (item.namespace ?? item.domain)
                : groupBy === 'group'
                  ? (item.group ?? item.domain)
                  : item.domain;

        const existing = map.get(key);
        if (existing) {
            existing.push(item);
        } else {
            map.set(key, [item]);
        }
    }

    return map;
}
