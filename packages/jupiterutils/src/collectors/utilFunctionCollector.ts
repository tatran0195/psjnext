/**
 * Utility / GUI function collector.
 *
 * Replaces the Rust `create_util_list` function.
 *
 * Walks a directory of markdown files, finds files matching a given prefix
 * (e.g. "PSJ-Utility_" or "dlg-"), and extracts the function signature by
 * parsing the "## Inputs" … "## Return Code" section of each file.
 */

import { readdir } from 'node:fs/promises';
import { extname, join } from 'node:path';

import type { UtilFunction } from '../types';

import { readLines } from '../utils';

// ---------------------------------------------------------------------------
// Regex helpers (compiled once)
// ---------------------------------------------------------------------------

/** Matches a param name inside backticks: `paramName` */
const RE_BACKTICK_PARAM = /`([^`]+)`/g;

/** Matches "The default value is <value>" */
const RE_DEFAULT = /The default value is (.+)/;

/** Strips trailing "(…)" annotation: "value (some note)" → "value" */
const RE_STRIP_ANNOTATION = /^(.+?) \(.*$/;

/** Italic value: _value_ */
const RE_ITALIC = /^_(\w+)_$/;

/** Enum-style bracket: [EnumName] → "EnumName()" */
const RE_BRACKET_ENUM = /^\[(\w+)\]$/;

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Walk `docsDir`, find all `.md` files whose name contains `filePrefix`,
 * parse each for param info, and return an array of {@link UtilFunction}.
 */
export async function collectUtilFunctions(
    docsDir: string,
    filePrefix: string,
): Promise<UtilFunction[]> {
    let entries: string[];
    try {
        entries = await readdir(docsDir);
    } catch {
        return [];
    }

    const results: UtilFunction[] = [];

    for (const entry of entries) {
        if (extname(entry) !== '.md') continue;
        if (!entry.includes(filePrefix)) continue;

        const filePath = join(docsDir, entry);
        const fn = await parseUtilFile(filePath, entry, filePrefix);
        if (fn !== null) results.push(fn);
    }

    return results;
}

// ---------------------------------------------------------------------------
// Internal helpers
// ---------------------------------------------------------------------------

/**
 * Parse a single markdown file and extract its function name and parameters.
 * Returns null if the file has no "## Inputs" section.
 */
async function parseUtilFile(
    filePath: string,
    filename: string,
    filePrefix: string,
): Promise<UtilFunction | null> {
    let lines: string[];
    try {
        lines = await readLines(filePath);
    } catch {
        return null;
    }

    // Derive function name: strip prefix and ".md" extension
    const prefixIdx = filename.indexOf(filePrefix);
    const fnName = filename.slice(prefixIdx + filePrefix.length, -3); // remove .md

    const inputsIdx = lines.indexOf('## Inputs');
    if (inputsIdx === -1) return null;

    const returnIdx = lines.indexOf('## Return Code');
    if (returnIdx === -1) return null;

    // Parse params between ## Inputs and ## Return Code
    const params = parseParamsFromSection(lines.slice(inputsIdx + 1, returnIdx));
    const rawParams = params
        .map((p) => (p.defaultValue !== null ? `${p.name}=${p.defaultValue}` : p.name))
        .join(', ');

    return { name: fnName, rawParams };
}

// ---------------------------------------------------------------------------
// Param section parser
// ---------------------------------------------------------------------------

interface RawParam {
    name: string;
    defaultValue: string | null;
}

function parseParamsFromSection(lines: string[]): RawParam[] {
    const params: RawParam[] = [];

    for (const line of lines) {
        if (line.startsWith('###')) {
            // Extract param names from backticks: ### `paramName`
            RE_BACKTICK_PARAM.lastIndex = 0;
            let m: RegExpExecArray | null;
            while ((m = RE_BACKTICK_PARAM.exec(line)) !== null) {
                params.push({ name: m[1] ?? '', defaultValue: null });
            }
        } else if (line.includes('The default value is') && params.length > 0) {
            const lastParam = params[params.length - 1];
            if (lastParam === undefined) continue;

            const match = RE_DEFAULT.exec(line);
            if (!match || !match[1]) continue;

            lastParam.defaultValue = extractDefaultValue(match[1]);
        }
    }

    return params;
}

/**
 * Clean up a raw default-value string extracted from markdown prose.
 *
 * Handles these forms (matching the original Rust logic):
 *   "True"                  → "True"
 *   "True (some note)"      → "True"           (strip annotation)
 *   "_True_"                → "True"            (italic markdown)
 *   "[EnumName]"            → "EnumName()"      (enum constructor)
 *   "True."                 → "True"            (strip trailing period)
 */
function extractDefaultValue(raw: string): string {
    let value = raw.trim();

    // Strip trailing period
    if (value.endsWith('.')) {
        value = value.slice(0, -1);
    }

    // "value (annotation)" → "value"
    const annotMatch = RE_STRIP_ANNOTATION.exec(value);
    if (annotMatch?.[1]) {
        value = annotMatch[1];
    }

    // _value_ italic → value
    const italicMatch = RE_ITALIC.exec(value);
    if (italicMatch?.[1]) {
        return italicMatch[1];
    }

    // [EnumName] → EnumName()
    const bracketMatch = RE_BRACKET_ENUM.exec(value);
    if (bracketMatch?.[1]) {
        return `${bracketMatch[1]}()`;
    }

    return value;
}

// ---------------------------------------------------------------------------
// Serialize to intermediate list format
// ---------------------------------------------------------------------------

/**
 * Serialize to the same format that the Rust binary produced:
 *   "FunctionName(param1, param2=default)"  — one per line
 */
export function serializeUtilFunctions(fns: UtilFunction[]): string {
    return fns.map((f) => `${f.name}(${f.rawParams})`).join('\n');
}

/**
 * Parse a UtilityFull.py / DlgFull.py list file back into UtilFunction[].
 */
export function parseUtilFunctionList(content: string): UtilFunction[] {
    return content
        .split(/\r?\n/)
        .map((l) => l.trim())
        .filter((l) => l.length > 0)
        .map((line) => {
            const parenIdx = line.indexOf('(');
            if (parenIdx === -1) return { name: line, rawParams: '' };
            const name = line.slice(0, parenIdx);
            const rawParams = line.slice(parenIdx + 1, line.lastIndexOf(')')) ?? '';
            return { name, rawParams };
        });
}
