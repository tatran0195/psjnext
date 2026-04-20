/**
 * PSJ Command collector.
 *
 * Replaces the Rust `create_psj_cmd_list` function.
 * Walks a macro source directory, finds all .py files (with exclusions),
 * extracts `def` signatures, and derives their fully-qualified PSJ path.
 */

import { readdir, stat } from 'node:fs/promises';
import { extname, join } from 'node:path';

import type { PsjCommand } from '../types';

import { readLines } from '../utils';

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

    for (const entry of entries) {
        const fullPath = join(dir, entry);

        let fileStat;
        try {
            fileStat = await stat(fullPath);
        } catch {
            continue;
        }

        if (fileStat.isDirectory()) {
            if (!EXCLUDED_DIRS.has(entry)) {
                await walk(baseRoot, fullPath, out);
            }
            continue;
        }

        if (extname(entry) !== '.py') continue;
        if (EXCLUDED_FILES.has(entry)) continue;

        const commands = await extractCommandsFromFile(baseRoot, fullPath);
        out.push(...commands);
    }
}

/**
 * Given a .py file under macroRoot, extract all `def` lines and return the
 * corresponding PsjCommand entries.
 *
 * Path derivation (mirrors original Rust logic):
 *   fullPath = "C:/project/macro/Measurement/Section/area.py"
 *   relative from "macro/"  →  "Measurement/Section/area"
 *   replace path sep with "." → "Measurement.Section.area"
 *   strip "__init__." occurrences
 *   append the def name/signature
 */
async function extractCommandsFromFile(macroRoot: string, filePath: string): Promise<PsjCommand[]> {
    // Derive the module prefix from the path.
    // normalise to forward slashes for consistent slicing
    const normalRoot = macroRoot.replace(/\\/g, '/');
    const normalFile = filePath.replace(/\\/g, '/');

    // Find where "macro/" segment starts — the root itself ends right before it
    // We need the path *after* macroRoot:
    if (!normalFile.startsWith(normalRoot)) return [];

    const relative = normalFile.slice(normalRoot.length + 1); // e.g. "Measurement/Section/area.py"
    const withoutExt = relative.slice(0, -3); // strip ".py"
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
        // Skip comment lines; require both "def " and ":"
        if (trimmed.startsWith('#')) continue;
        if (!trimmed.includes('def ') || !trimmed.includes(':')) continue;

        const defIdx = trimmed.indexOf('def ');
        const colonIdx = trimmed.lastIndexOf(':');
        const defBody = trimmed.slice(defIdx + 4, colonIdx); // e.g. "doThing(arg1, arg2)"

        const namespace = modulePrefix.split('.');
        commands.push({ namespace, signature: defBody });
    }

    return commands;
}

// ---------------------------------------------------------------------------
// Serialize to the intermediate .py list format
// ---------------------------------------------------------------------------

/**
 * Serialize collected commands to the same text format that the original
 * Rust binary wrote to PSJCmdFull.py:
 *   "Namespace.path.FunctionName(params)"  — one per line
 */
export function serializePsjCommands(commands: PsjCommand[]): string {
    return commands.map((cmd) => `${cmd.namespace.join('.')}.${cmd.signature}`).join('\n');
}

/**
 * Parse a PSJCmdFull.py-format file back into an array of {@link PsjCommand}.
 * Used when the list file already exists and we skip re-scanning.
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
            // Everything before the last "." before "(" is namespace
            const beforeParen = line.slice(0, parenIdx);
            const dotIdx = beforeParen.lastIndexOf('.');
            const namespace = dotIdx === -1 ? [] : beforeParen.slice(0, dotIdx).split('.');
            const fnAndParams = line.slice(dotIdx + 1); // "FnName(params)"
            return { namespace, signature: fnAndParams };
        });
}
