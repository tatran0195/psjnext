import { watch } from 'chokidar';
import { mkdir, writeFile } from 'node:fs/promises';
import * as path from 'node:path';

import type { JCallServer } from './server';

import {
    buildEntries,
    type BuilderOptions,
    type OutputEntry,
    type OutputGroup,
} from './pages/builder';
import { toText, type ToTextOptions } from './pages/to-text';

export interface OutputFile {
    path: string;
    content: string;
}

interface MetaOptions {
    groupStyle?: 'folder' | 'separator';
}

interface IndexItem {
    /** Output path of the index page */
    path: string;
    title?: string;
    description?: string;
}

export interface GenerateConfig extends ToTextOptions, BuilderOptions {
    input: JCallServer;
    /** Output directory */
    output: string;
    /** Generate `meta.json` files */
    meta?: boolean | MetaOptions;
    /** Generate an index overview page */
    index?: {
        items: IndexItem[];
        url: string | ((filePath: string) => string);
    };
    /**
     * Re-generate on file changes.
     */
    watch?: boolean;
    /** Hook called before writing */
    beforeWrite?: (files: OutputFile[]) => void | Promise<void>;
}

export type GenerateFilesOnlyConfig = Omit<GenerateConfig, 'output' | 'watch'>;

// ─── Public API ───────────────────────────────────────────────────────────────

export async function generateFiles(config: GenerateConfig): Promise<void> {
    if (config.watch) {
        const sub: GenerateConfig = { ...config, watch: false };
        await generateFiles(sub);
        const paths = config.input._getWatchPaths();
        console.log(`[JCALL] watching ${paths.join(', ')}`);
        watch(paths, { ignoreInitial: true }).on('all', () => generateFiles(sub));
        return;
    }

    const files = await generateFilesOnly(config);
    await Promise.all(
        files.map(async (file) => {
            const filePath = path.join(config.output, file.path);
            await mkdir(path.dirname(filePath), { recursive: true });
            await writeFile(filePath, file.content);
            console.log(`[JCALL] Generated: ${filePath}`);
        }),
    );
}

export async function generateFilesOnly(config: GenerateFilesOnlyConfig): Promise<OutputFile[]> {
    const resolvedItems = await config.input.getResolvedItems();
    const entries = buildEntries(resolvedItems, config);
    const files: OutputFile[] = [];

    scan(entries, files, config);

    if (config.meta) {
        files.push(...generateMeta(entries, config.meta === true ? {} : config.meta));
    }

    if (config.index) {
        files.push(...generateIndex(entries, config.index));
    }

    await config.beforeWrite?.(files);
    return files;
}

// ─── Internal helpers ─────────────────────────────────────────────────────────

function scan(entries: OutputEntry[], files: OutputFile[], config: GenerateFilesOnlyConfig) {
    for (const entry of entries) {
        if (entry.type === 'group') {
            scan(entry.entries, files, config);
        } else {
            files.push({ path: entry.path, content: toText(entry, config) });
        }
    }
}

function generateMeta(entries: OutputEntry[], options: MetaOptions): OutputFile[] {
    const { groupStyle = 'folder' } = options;
    const files: OutputFile[] = [];

    function scanMeta(list: OutputEntry[], parent?: OutputGroup) {
        const pages: string[] = [];

        for (const entry of list) {
            const rel = parent ? path.relative(parent.path, entry.path) : entry.path;
            const relSlash = rel.replace(/\\/g, '/');

            if (entry.type === 'group') {
                scanMeta(entry.entries, entry);
                if (groupStyle === 'folder') {
                    pages.push(relSlash);
                } else {
                    pages.push(`---${entry.info.title}---`, `...${relSlash}`);
                }
            } else {
                pages.push(relSlash.replace(/\.[^.]+$/, ''));
            }
        }

        if (!pages.length) return;
        files.push({
            path: parent ? path.join(parent.path, 'meta.json') : 'meta.json',
            content: JSON.stringify(
                { title: parent?.info.title, description: parent?.info.description, pages },
                null,
                2,
            ),
        });
    }

    scanMeta(entries);
    return files;
}

function generateIndex(
    entries: OutputEntry[],
    indexConfig: NonNullable<GenerateConfig['index']>,
): OutputFile[] {
    const files: OutputFile[] = [];
    const urlFn =
        typeof indexConfig.url === 'function'
            ? indexConfig.url
            : (p: string) => `${indexConfig.url}/${p}`;

    const allPages: { path: string; title: string; description?: string }[] = [];
    function collectPages(list: OutputEntry[]) {
        for (const e of list) {
            if (e.type === 'group') collectPages(e.entries);
            else
                allPages.push({
                    path: e.path,
                    title: e.info.title,
                    description: e.info.description,
                });
        }
    }
    collectPages(entries);

    for (const item of indexConfig.items) {
        const cards = allPages
            .map((p) => {
                const descAttr = p.description ? ` description="${p.description}"` : '';
                return `<Card href="${urlFn(p.path)}" title="${p.title}"${descAttr} />`;
            })
            .join('\n');

        const filePath = item.path.endsWith('.mdx') ? item.path : `${item.path}.mdx`;
        const fm = [
            '---',
            `title: "${item.title ?? 'Overview'}"`,
            item.description ? `description: "${item.description}"` : '',
            '---',
        ]
            .filter(Boolean)
            .join('\n');

        files.push({ path: filePath, content: `${fm}\n\n<Cards>\n${cards}\n</Cards>` });
    }

    return files;
}
