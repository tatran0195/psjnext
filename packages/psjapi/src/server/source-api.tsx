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
    PageTreeTransformer,
    Source,
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
                    const label = domainBadge(meta.domain);
                    if (label) {
                        node.name = (
                            <>
                                {node.name}{' '}
                                <span className="ms-auto border border-current px-1 rounded-lg text-xs text-nowrap font-mono">
                                    {label}
                                </span>
                            </>
                        );
                    }
                }

                return node;
            },
        },
    };
}

function domainBadge(domain: string): string | null {
    const map: Record<string, string> = {
        macro: 'macro',
        'psj-command': 'cmd',
        'psj-utility': 'util',
        'psj-gui': 'gui',
    };
    return map[domain] ?? null;
}

// ─── Page data ────────────────────────────────────────────────────────────────

export interface PSJPageData extends PageData {
    /**
     * Resolve the item for this page.
     *
     * In an i18n setup the locale is already baked into the page from the
     * per-locale virtual file — just call `page.data.getItem(version)`.
     *
     * In a non-i18n setup you can still pass locale explicitly.
     */
    getItem: (version?: string, locale?: string) => Promise<ResolvedItem | undefined>;
    /** Keys for multi-item pages (per: 'group' | 'domain') */
    itemKeys?: string[];
    structuredData: StructuredData;
    toc: TOCItemType[];
}

// ─── Options ──────────────────────────────────────────────────────────────────

export type I18nParser = 'dir' | 'dot';

export type PsjSourceOptions = PsjPagesBuilderConfig & {
    baseDir?: string;
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
};

// ─── Path helpers ─────────────────────────────────────────────────────────────

function stripExt(p: string): string {
    return p.endsWith('.mdx') ? p.slice(0, -4) : p;
}

function localeFilePath(
    baseDir: string,
    entryPath: string,
    localeId: string,
    parser: I18nParser,
): string {
    const base = baseDir ? `${baseDir}/` : '';
    if (parser === 'dir') {
        return `${base}${localeId}/${entryPath}`;
    }
    // dot parser
    const withoutExt = stripExt(entryPath);
    return `${base}${withoutExt}.${localeId}.mdx`;
}

// ─── psjSource ───────────────────────────────────────────────────────────────

export async function psjSource(
    server: PSJAPIServer,
    options: PsjSourceOptions = {},
): Promise<
    Source<{
        metaData: MetaData;
        pageData: PSJPageData;
    }>
> {
    const { baseDir = '', meta = false, i18nParser } = options;

    const files: VirtualFile<{
        pageData: PSJPageData;
        metaData: MetaData;
    }>[] = [];

    const sdk = await server.getProcessedSdk();
    const locales: LocaleEntry[] = i18nParser ? sdk.manifest.locales : [];
    // Non-i18n: emit once with empty locale id
    const emitLocales = locales.length > 0 ? locales : [{ id: '', label: '' }];

    const allEntries = await fromServer(server, options);

    for (const [, list] of Object.entries(allEntries)) {
        function onEntry(entry: ItemOutput | PageOutput) {
            const psjMeta: InternalPsjMeta =
                entry.type === 'item'
                    ? { domain: entry.item.domain }
                    : entry.type === 'page' && entry.items.length > 0
                        ? { domain: entry.items[0].domain }
                        : {};

            for (const locale of emitLocales) {
                const localeId = locale.id;

                const filePath =
                    i18nParser && localeId
                        ? localeFilePath(baseDir, entry.path, localeId, i18nParser)
                        : `${baseDir ? `${baseDir}/` : ''}${entry.path}`;

                files.push({
                    type: 'page',
                    path: filePath,
                    data: {
                        title: entry.info.title,
                        description: entry.info.description,
                        _psjapi: psjMeta,

                        // locale is baked in — callers only need to pass version
                        async getItem(version?: string, explicitLocale?: string) {
                            const resolvedLocale = explicitLocale ?? (localeId || undefined);

                            if (entry.type === 'item') {
                                return server.resolveItem(entry.item.key, version, resolvedLocale);
                            }
                            if (entry.type === 'page' && entry.items.length > 0) {
                                return server.resolveItem(
                                    entry.items[0].key,
                                    version,
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
                            headings: [{ content: entry.info.title, id: entry.path }],
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

        function onEntries(entries: OutputEntry[], parent?: OutputEntry) {
            if (!meta) {
                for (const entry of entries) {
                    if (entry.type === 'group') {
                        onEntries(entry.entries, entry);
                    } else {
                        onEntry(entry as ItemOutput | PageOutput);
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
                    onEntries(entry.entries, entry);
                    if (folderStyle === 'folder') {
                        pages.push(relativePath);
                    } else {
                        pages.push(`---${entry.info.title}---`, `...${relativePath}`);
                    }
                } else {
                    onEntry(entry as ItemOutput | PageOutput);
                    pages.push(stripExt(relativePath));
                }
            }

            if (pages.length === 0) return;

            // Emit meta.json per locale for dir parser
            for (const locale of emitLocales) {
                const localeId = locale.id;
                const metaPath =
                    i18nParser === 'dir' && localeId
                        ? path.join(baseDir, localeId, parent?.path ?? '', 'meta.json')
                        : path.join(baseDir, parent?.path ?? '', 'meta.json');

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

        onEntries(list);
    }

    return { files };
}

/** @deprecated use psjPlugin() */
export function transformerPsj(): PageTreeTransformer {
    return psjPlugin().transformPageTree!;
}
