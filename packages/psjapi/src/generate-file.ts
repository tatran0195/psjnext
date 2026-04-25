/**
 * psjapi static file generator
 *
 * Analogous to fumadocs-openapi's generateFiles() / generateFilesOnly().
 * Produces .mdx files on disk from a PSJAPIServer.
 */

import { mkdir, writeFile } from 'node:fs/promises';
import * as path from 'node:path';

import type { PSJAPIServer } from './types';
import type {
    PsjPagesBuilderConfig,
    OutputEntry,
    ItemOutput,
    PageOutput,
} from './utils/pages/builder';

import { fromServer } from './utils/pages/builder';
import { toText, type PsjToTextOptions } from './utils/pages/to-text';

export interface OutputFile {
    path: string;
    content: string;
}

export interface GenerateFilesConfig extends PsjToTextOptions, PsjPagesBuilderConfig {
    /** The PSJAPIServer instance */
    input: PSJAPIServer;

    /** Output directory */
    output: string;

    /**
     * Re-generate when YAML files change (uses chokidar).
     * Only works for simple cases — use chokidar directly for advanced setups.
     */
    watch?: boolean;

    /**
     * Generate meta.json files.
     */
    meta?: boolean | { groupStyle?: 'folder' | 'separator' };

    /**
     * Mutate or extend output files before writing.
     */
    beforeWrite?: (files: OutputFile[]) => void | Promise<void>;
}

export async function generateFiles(options: GenerateFilesConfig): Promise<void> {
    if (options.watch) {
        const { watch } = await import('chokidar');
        const subOptions: GenerateFilesConfig = { ...options, watch: false };
        await generateFiles(subOptions);

        const rootDir = options.input.options.root.endsWith('.yaml')
            ? path.dirname(options.input.options.root)
            : options.input.options.root;

        console.log(`[fumadocs-psjapi] watching ${rootDir}`);
        watch(rootDir, { ignoreInitial: true, ignored: '**/*.mdx' }).on('all', () =>
            generateFiles(subOptions),
        );
        return;
    }

    const files = await generateFilesOnly(options);

    await Promise.all(
        files.map(async (file) => {
            const filePath = path.join(options.output, file.path);
            await mkdir(path.dirname(filePath), { recursive: true });
            await writeFile(filePath, file.content, 'utf-8');
            console.log(`[fumadocs-psjapi] generated: ${filePath}`);
        }),
    );
}

export async function generateFilesOnly(
    options: Omit<GenerateFilesConfig, 'output'>,
): Promise<OutputFile[]> {
    const allEntries = await fromServer(options.input, options);
    const files: OutputFile[] = [];

    function scan(entry: OutputEntry) {
        if (entry.type === 'group') {
            for (const child of entry.entries) scan(child);
            return;
        }
        files.push({
            path: entry.path,
            content: toText(entry as ItemOutput | PageOutput, options),
        });
    }

    for (const list of Object.values(allEntries)) {
        for (const entry of list) scan(entry);
    }

    if (options.meta) {
        // meta.json generation handled inside psjSource for virtual files;
        // for static generation we produce them here too
        for (const list of Object.values(allEntries)) {
            generateMetaFiles(list, options, files);
        }
    }

    await options.beforeWrite?.(files);
    return files;
}

function generateMetaFiles(
    entries: OutputEntry[],
    options: Pick<GenerateFilesConfig, 'meta'>,
    out: OutputFile[],
    parent?: OutputEntry,
) {
    const { groupStyle = 'folder' } = typeof options.meta === 'object' ? options.meta : {};
    const pages: string[] = [];

    for (const entry of entries) {
        const relativePath = parent
            ? path.relative(parent.path, entry.path).replace(/\\/g, '/')
            : entry.path;

        if (entry.type === 'group') {
            generateMetaFiles(entry.entries, options, out, entry);
            if (groupStyle === 'folder') {
                pages.push(relativePath);
            } else {
                pages.push(`---${entry.info.title}---`, `...${relativePath}`);
            }
        } else {
            pages.push(relativePath.slice(0, -path.extname(entry.path).length));
        }
    }

    if (pages.length === 0) return;

    out.push({
        path: path.join(parent?.path ?? '', 'meta.json'),
        content: JSON.stringify(
            {
                title: parent?.info.title,
                description: parent?.info.description,
                pages,
            },
            null,
            2,
        ),
    });
}
