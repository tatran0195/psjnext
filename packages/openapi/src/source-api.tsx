import {
    type LoaderPlugin,
    type MetaData,
    type PageData,
    type Source,
    type VirtualFile
} from 'fumadocs-core/source';
import * as fs from 'node:fs/promises';
import * as path from 'node:path';
import { buildEntries, type OutputEntry, type OutputGroup, type PageOutput } from './pages/builder';
import type { JCallServer } from './server';
import type { Domain, ResolvedItem } from './types';

declare module 'fumadocs-core/source' {
    export interface PageData {
        /** Added by the JCALL source integration */
        _jcall?: InternalJCallMeta;
    }
}

export interface InternalJCallMeta {
    id: string;
    domain: Domain;
    group?: string;
    version: string;
    deprecated?: boolean;
}

export interface JCallPageData extends PageData {
    type?: 'jcall';
    getItem: () => ResolvedItem;
    structuredData: { headings: { id: string; depth: number; text: string }[]; contents: { heading?: string; content: string }[] };
    toc: { depth: number; title: string; url: string }[];
}

export interface JCallSourceOptions {
    baseDir?: string;
    rootTitle?: string;
    rootDescription?: string;
    /** Generate meta.json virtual files */
    meta?: boolean | { folderStyle?: 'folder' | 'separator' | 'extract' };
}

/**
 * Generates virtual pages for Fumadocs Source API from a JCallServer.
 */
export async function jcallSource(
    server: JCallServer,
    options: JCallSourceOptions = {},
): Promise<Source<{ metaData: MetaData; pageData: JCallPageData }>> {
    const { baseDir = '', meta = false, rootTitle = 'API Reference', rootDescription } = options;
    const sdk = await server.getSDK();
    const resolvedItems = await server.getResolvedItems();

    if (sdk.rootDir) {
        for (const item of resolvedItems.values()) {
            if (!item.examples) continue;
            for (const ex of item.examples) {
                if (ex.file && !ex.code) {
                    const fp = path.join(sdk.rootDir, item.domain, ex.file);
                    try {
                        ex.code = await fs.readFile(fp, 'utf-8');
                    } catch (err) {
                        console.warn(`[JCALL] Could not read example file: ${fp}`);
                        ex.code = `// Error: Could not read example file: ${ex.file}`;
                    }
                }
            }
        }
    }

    const entries = buildEntries(resolvedItems, { manifest: sdk.manifest });

    const files: VirtualFile<{ pageData: JCallPageData; metaData: MetaData }>[] = [];

    function onPage(entry: PageOutput) {
        const item = entry.item;
        files.push({
            type: 'page',
            path: path.join(baseDir, entry.path).replace(/\\/g, '/'),
            data: {
                title: item.title,
                description: item.description,
                type: 'jcall',
                getItem() {
                    return item;
                },
                // Minimal structured data so search works
                structuredData: {
                    headings: [],
                    contents: [{ content: item.description }],
                },
                toc: [],
                _jcall: {
                    id: item.id,
                    domain: item.domain,
                    group: item.group,
                    version: item.resolved_version,
                    deprecated: item.deprecated,
                },
            },
        });
    }

    function onEntries(list: OutputEntry[], parent?: OutputEntry) {
        if (!meta) {
            for (const entry of list) {
                if (entry.type === 'group') onEntries(entry.entries, entry);
                else onPage(entry);
            }
            return;
        }

        const { folderStyle = 'folder' } = meta === true ? {} : meta;
        const pages: string[] = [];

        for (const entry of list) {
            const rel = parent
                ? path.relative(parent.path, entry.path).replace(/\\/g, '/')
                : entry.path;

            if (entry.type === 'group') {
                onEntries(entry.entries, entry);
                pages.push(folderStyle === 'extract' ? `...${rel}` : rel);
                if (folderStyle === 'separator') {
                    pages.unshift(`---${entry.info.title}---`);
                }
            } else {
                onPage(entry);
                pages.push(rel.replace(/\.[^.]+$/, ''));
            }
        }

        if (!pages.length) return;
        files.push({
            type: 'meta',
            path: path.join(baseDir, (parent as OutputGroup | undefined)?.path ?? '', 'meta.json').replace(/\\/g, '/'),
            data: {
                title: parent ? parent.info.title : rootTitle,
                description: parent ? undefined : rootDescription,
                root: !parent,
                pages,
            },
        });
    }

    onEntries(entries);

    return { files };
}

/**
 * Fumadocs loader plugin — adds a domain badge to page-tree nodes.
 */
export function jcallPlugin(): LoaderPlugin {
    return {
        name: 'psj:jcall',
        enforce: 'pre',
        transformPageTree: {
            file(node, filePath) {
                if (!filePath) return node;
                const file = this.storage.read(filePath);
                if (!file || file.format !== 'page') return node;

                const jcall = file.data._jcall as InternalJCallMeta | undefined;
                if (!jcall) return node;

                const domainShort: Record<string, string> = {
                    macro: 'MCR',
                    'psj-command': 'CMD',
                    'psj-utility': 'UTL',
                    'psj-gui': 'GUI',
                };
                const domainColors: Record<string, string> = {
                    macro: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400',
                    'psj-command': 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400',
                    'psj-utility': 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-400',
                    'psj-gui': 'bg-orange-100 text-orange-700 dark:bg-orange-900/30 dark:text-orange-400',
                };

                const shortName = domainShort[jcall.domain] || jcall.domain;
                const colorClass = domainColors[jcall.domain] || 'bg-fd-muted text-fd-foreground';

                node.name = (
                    <span className="flex w-full items-center gap-2">
                        <span className="truncate">{node.name}</span>
                        <span className={`shrink-0 ms-auto rounded px-1.5 py-0.5 text-[10px] font-bold tracking-wider ${colorClass}`}>
                            {shortName}
                        </span>
                    </span>
                ) as never;

                return node;
            },
        },
    };
}
