/**
 * PSJ Command collector.
 */

import { readdir, stat } from 'node:fs/promises';
import { extname, join } from 'node:path';

import type { PsjCommand } from '@/types';

import { readLines } from '@/utils';

// ---------------------------------------------------------------------------
// Constants
// ---------------------------------------------------------------------------

/** Files to skip during the walk (exact filename match). */
const EXCLUDED_FILES = new Set([
    'macro_defs.py',
    'macro_material.py',
    'macroTypes.py',
    'Out.py',
    'table_material.py',
]);

/** Directory segments to skip entirely. */
const EXCLUDED_DIRS = new Set(['Report']);

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Walk `macroRoot` recursively, collect all PSJ command signatures, and
 * return them as an array of {@link PsjCommand} objects.
 */
export async function collectPsjCommands(macroRoot: string): Promise<PsjCommand[]> {
    const results: PsjCommand[] = [];
    await walk(macroRoot, macroRoot, results);
    return results;
}

// ---------------------------------------------------------------------------
// Internal helpers
// ---------------------------------------------------------------------------

async function walk(baseRoot: string, dir: string, out: PsjCommand[]): Promise<void> {
    let entries: string[];
    try {
        entries = await readdir(dir);
    } catch {
        return;
    }

    // Process all entries concurrently for better throughput on large trees
    await Promise.all(
        entries.map(async (entry) => {
            const fullPath = join(dir, entry);

            let fileStat;
            try {
                fileStat = await stat(fullPath);
            } catch {
                return;
            }

            if (fileStat.isDirectory()) {
                if (!EXCLUDED_DIRS.has(entry)) {
                    await walk(baseRoot, fullPath, out);
                }
                return;
            }

            if (extname(entry) !== '.py') return;
            if (EXCLUDED_FILES.has(entry)) return;

            const commands = await extractCommandsFromFile(baseRoot, fullPath);
            // push is safe: Promise.all runs concurrently but push is synchronous
            out.push(...commands);
        }),
    );
}

/**
 * Given a .py file under macroRoot, extract all `def` lines and return the
 * corresponding PsjCommand entries.
 */
async function extractCommandsFromFile(macroRoot: string, filePath: string): Promise<PsjCommand[]> {
    const normalRoot = macroRoot.replace(/\\/g, '/');
    const normalFile = filePath.replace(/\\/g, '/');

    if (!normalFile.startsWith(normalRoot)) return [];

    const relative = normalFile.slice(normalRoot.length + 1);
    const withoutExt = relative.slice(0, -3);
    const modulePrefix = withoutExt
        .replace(/\//g, '.')
        .replace(/\\/g, '.')
        .replace(/\.__init__/g, '')
        .replace(/__init__\./g, '');

    let lines: string[];
    try {
        lines = await readLines(filePath);
    } catch {
        return [];
    }

    const commands: PsjCommand[] = [];

    for (const line of lines) {
        const trimmed = line.trimStart();
        if (trimmed.startsWith('#')) continue;
        if (!trimmed.includes('def ') || !trimmed.includes(':')) continue;

        const defIdx = trimmed.indexOf('def ');
        const colonIdx = trimmed.lastIndexOf(':');
        const defBody = trimmed.slice(defIdx + 4, colonIdx);

        const namespace = modulePrefix.split('.');
        commands.push({ namespace, signature: defBody });
    }

    return commands;
}

// ---------------------------------------------------------------------------
// Serialize to the intermediate .py list format
// ---------------------------------------------------------------------------

/**
 * Serialize collected commands to the same text format:
 *   "Namespace.path.FunctionName(params)"  — one per line
 */
export function serializePsjCommands(commands: PsjCommand[]): string {
    return commands.map((cmd) => `${cmd.namespace.join('.')}.${cmd.signature}`).join('\n');
}

/**
 * Parse a PSJCmdFull.py-format file back into an array of {@link PsjCommand}.
 */
export function parsePsjCommandList(content: string): PsjCommand[] {
    return content
        .split(/\r?\n/)
        .map((l) => l.trim())
        .filter((l) => l.length > 0)
        .map((line) => {
            const parenIdx = line.indexOf('(');
            if (parenIdx === -1) {
                return { namespace: line.split('.'), signature: '' };
            }
            const beforeParen = line.slice(0, parenIdx);
            const dotIdx = beforeParen.lastIndexOf('.');
            const namespace = dotIdx === -1 ? [] : beforeParen.slice(0, dotIdx).split('.');
            const fnAndParams = line.slice(dotIdx + 1);
            return { namespace, signature: fnAndParams };
        });
}
