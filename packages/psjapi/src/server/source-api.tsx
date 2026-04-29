import { PathUtils } from 'fumadocs-core/source';
import * as path from 'node:path';

import type { LocaleEntry, PSJAPIServer, ResolvedItem } from '../types';
import type {
    ItemOutput,
    OutputEntry,
    PageOutput,
    PsjPagesBuilderConfig,
} from '../utils/pages/builder';

import { fromServer } from '../utils/pages/builder';

import type { StructuredData } from 'fumadocs-core/mdx-plugins';
import type {
    LoaderPlugin,
    MetaData,
    PageData,
    StaticSource,
    VirtualFile,
} from 'fumadocs-core/source';
import type { TOCItemType } from 'fumadocs-core/toc';

// ─── Augment PageData ─────────────────────────────────────────────────────────

declare module 'fumadocs-core/source' {
    interface PageData {
        _psjapi?: InternalPsjMeta;
    }
}

export interface InternalPsjMeta {
    domain?: string;
    group?: string;
}

// ─── Plugin ───────────────────────────────────────────────────────────────────

export function psjPlugin(): LoaderPlugin {
    return {
        name: 'fumadocs:psjapi',
        enforce: 'pre',
        transformPageTree: {
            file(node, filePath) {
                if (!filePath) return node;
                const file = this.storage.read(filePath);
                if (!file || file.format !== 'page') return node;

                const meta = file.data._psjapi;
                if (!meta || typeof meta !== 'object') return node;

                if (meta.domain) {
                    node.name = <span className="font-mono text-xs">{node.name}</span>;
                }

                return node;
            },
        },
    };
}

// ─── Page data ────────────────────────────────────────────────────────────────

export interface PSJPageData extends PageData {
    /**
     * Resolve the item for this page.
     *
     * Version and locale are baked in from the virtual file path when
     * `i18nParser` and/or `versionInUrl` are set — call with no args.
     *
     * Override either by passing explicitly:
     *   page.data.getItem()                  // uses baked-in version + locale
     *   page.data.getItem('5.0.1')           // override version
     *   page.data.getItem(undefined, 'ja')   // override locale
     */
    getItem: (version?: string, locale?: string) => Promise<ResolvedItem | undefined>;
    /** SDK version baked into this virtual file (when versionInUrl: true) */
    sdkVersion?: string;
    /** Locale baked into this virtual file (when i18nParser is set) */
    sdkLocale?: string;
    /** Keys for multi-item pages (per: 'group' | 'domain') */
    itemKeys?: string[];
    structuredData: StructuredData;
    toc: TOCItemType[];
}

// ─── Options ──────────────────────────────────────────────────────────────────

export type I18nParser = 'dir' | 'dot';

export type PsjSourceOptions = PsjPagesBuilderConfig & {
    /** Generate meta.json files */
    meta?: boolean | { folderStyle?: 'folder' | 'separator' };
    /**
     * Set this to match the `i18n.parser` value passed to Fumadocs loader().
     *
     * - 'dir' → one file per locale under a language prefix dir (en/, ja/, …)
     * - 'dot' → one file per locale with a language suffix  (.en.mdx, .ja.mdx)
     * - unset → single file, no locale in path (no i18n)
     *
     * When set, psjSource reads the locales from sdk.psjapi.yaml and emits
     * one virtual file per locale so Fumadocs builds a per-locale page tree.
     */
    i18nParser?: I18nParser;

    /**
     * Embed the SDK version in the virtual file path.
     *
     * When true, psjSource emits one file per version per locale:
     *
     *   dir parser:  en/5.1.0/psj-command/Foo.mdx
     *   no i18n:     5.1.0/psj-command/Foo.mdx
     *
     * Combined with a Next.js route of `[lang]/sdk/[version]/[[...slug]]`,
     * this produces clean versioned URLs:
     *   /en/sdk/5.1.0/psj-command/analysis-advc-makeprocess-static
     *   /ja/sdk/5.0.0/macro/advc-static-process
     *
     * The version and locale are baked into each page's `getItem()` closure —
     * no need to pass them manually from the page component.
     *
     * @default false
     */
    versionInUrl?: boolean;
};

// ─── Path helpers ─────────────────────────────────────────────────────────────

function stripExt(p: string): string {
    return p.endsWith('.mdx') ? p.slice(0, -4) : p;
}

function localeFilePath(entryPath: string, localeId: string, parser: I18nParser): string {
    if (parser === 'dir') {
        return `${localeId}/${entryPath}`;
    }
    // dot parser
    const withoutExt = stripExt(entryPath);
    return `${withoutExt}.${localeId}.mdx`;
}

// ─── psjSource ───────────────────────────────────────────────────────────────

export async function psjSource(
    server: PSJAPIServer,
    options: PsjSourceOptions = {},
): Promise<
    StaticSource<{
        metaData: MetaData;
        pageData: PSJPageData;
    }>
> {
    const { meta = false, i18nParser, versionInUrl = false } = options;

    const files: VirtualFile<{
        pageData: PSJPageData;
        metaData: MetaData;
    }>[] = [];

    const sdk = await server.getProcessedSdk();

    // Locales to emit — empty string means no locale prefix
    const locales: LocaleEntry[] = i18nParser ? sdk.manifest.locales : [];
    const emitLocales = locales.length > 0 ? locales : [{ id: '', label: '' }];

    // Versions to emit — empty string means no version prefix
    const versions = versionInUrl ? sdk.manifest.versions.map((v) => v.id) : [''];

    const allEntries = await fromServer(server, options);

    // Build a version-order index so we can compare version_introduced vs versionId.
    // Lower index = older version. We use this to skip items not yet introduced.
    const versionOrder = new Map<string, number>(
        sdk.manifest.versions.map((v, i) => [v.id, i] as [string, number]),
    );

    function isAvailableInVersion(entry: ItemOutput | PageOutput, versionId: string): boolean {
        // No version filtering when versionInUrl is off
        if (!versionId) return true;
        const targetIdx = versionOrder.get(versionId) ?? 0;

        if (entry.type === 'item') {
            const item = sdk.items.get(entry.item.key);
            if (!item?.version_introduced) return true;
            const introIdx = versionOrder.get(item.version_introduced) ?? 0;
            return introIdx <= targetIdx;
        }
        if (entry.type === 'page') {
            // Show page if at least one of its items is available
            return entry.items.some((ref) => {
                const item = sdk.items.get(ref.key);
                if (!item?.version_introduced) return true;
                const introIdx = versionOrder.get(item.version_introduced) ?? 0;
                return introIdx <= targetIdx;
            });
        }
        return true;
    }

    for (const [, list] of Object.entries(allEntries)) {
        function onEntry(entry: ItemOutput | PageOutput, parentGroup?: string) {
            const psjMeta: InternalPsjMeta =
                entry.type === 'item'
                    ? { domain: entry.item.domain, group: parentGroup }
                    : entry.type === 'page' && entry.items.length > 0
                      ? { domain: entry.items[0].domain, group: parentGroup }
                      : {};

            for (const locale of emitLocales) {
                const localeId = locale.id;

                for (const versionId of versions) {
                    // Skip items not yet introduced in this version
                    if (versionInUrl && versionId && !isAvailableInVersion(entry, versionId)) {
                        continue;
                    }

                    // Build path: [locale/][version/]entry.path
                    // e.g. en/5.1.0/psj-command/Foo.mdx  or just  psj-command/Foo.mdx
                    let filePath = entry.path;

                    if (versionInUrl && versionId) {
                        filePath = `${versionId}/${filePath}`;
                    }

                    if (i18nParser && localeId) {
                        filePath = localeFilePath(filePath, localeId, i18nParser);
                    }

                    files.push({
                        type: 'page',
                        path: filePath,
                        data: {
                            title: entry.info.title,
                            description: entry.info.description,
                            _psjapi: psjMeta,
                            sdkVersion: versionId || undefined,
                            sdkLocale: localeId || undefined,

                            // Both version and locale are baked in — call with no args
                            async getItem(overrideVersion?: string, overrideLocale?: string) {
                                const resolvedVersion = overrideVersion ?? (versionId || undefined);
                                const resolvedLocale = overrideLocale ?? (localeId || undefined);

                                if (entry.type === 'item') {
                                    return server.resolveItem(
                                        entry.item.key,
                                        resolvedVersion,
                                        resolvedLocale,
                                    );
                                }
                                if (entry.type === 'page' && entry.items.length > 0) {
                                    return server.resolveItem(
                                        entry.items[0].key,
                                        resolvedVersion,
                                        resolvedLocale,
                                    );
                                }
                                return undefined;
                            },

                            itemKeys:
                                entry.type === 'page'
                                    ? entry.items.map((i) => i.key)
                                    : [entry.type === 'item' ? entry.item.key : ''],

                            structuredData: {
                                headings: [],
                                contents: [
                                    {
                                        content: entry.info.description ?? entry.info.title,
                                        heading: entry.info.title,
                                    },
                                ],
                            },
                            toc: [],
                        } satisfies PSJPageData,
                    });
                }
            }
        }

        function onEntries(entries: OutputEntry[], parent?: OutputEntry, groupLabel?: string) {
            if (!meta) {
                for (const entry of entries) {
                    if (entry.type === 'group') {
                        // Pass group label down — only propagate if it's a sub-group of a domain
                        const nextGroupLabel =
                            parent && parent.type === 'group' ? entry.info.title : undefined;
                        onEntries(entry.entries, entry, nextGroupLabel);
                    } else {
                        onEntry(entry as ItemOutput | PageOutput, groupLabel);
                    }
                }
                return;
            }

            const { folderStyle = 'folder' } = meta === true ? {} : meta;
            const pages: string[] = [];

            for (const entry of entries) {
                const relativePath = PathUtils.slash(
                    parent ? path.relative(parent.path, entry.path) : entry.path,
                );

                if (entry.type === 'group') {
                    // Determine if this is a group sub-folder (parent is also a group)
                    const nextGroupLabel =
                        parent && parent.type === 'group' ? entry.info.title : undefined;
                    onEntries(entry.entries, entry, nextGroupLabel);
                    if (folderStyle === 'folder') {
                        pages.push(relativePath);
                    } else {
                        pages.push(`---${entry.info.title}---`, `...${relativePath}`);
                    }
                } else {
                    onEntry(entry as ItemOutput | PageOutput, groupLabel);
                    pages.push(stripExt(relativePath));
                }
            }

            if (pages.length === 0) return;

            // Emit meta.json per locale × version combination
            for (const locale of emitLocales) {
                const localeId = locale.id;
                for (const versionId of versions) {
                    let metaPath = path.join(parent?.path ?? '', 'meta.json');
                    if (versionInUrl && versionId) {
                        metaPath = path.join(versionId, metaPath);
                    }
                    if (i18nParser === 'dir' && localeId) {
                        metaPath = path.join(localeId, metaPath);
                    }

                    files.push({
                        type: 'meta',
                        path: metaPath,
                        data: {
                            title: parent?.info.title,
                            description: parent?.info.description,
                            pages,
                        },
                    });
                }
            }
        }

        onEntries(list);
    }

    return { files };
}
