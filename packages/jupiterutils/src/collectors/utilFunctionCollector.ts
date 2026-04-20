/**
 * Utility / GUI function collector.
 */

import { readdir } from 'node:fs/promises';
import { extname, join } from 'node:path';

import type { UtilFunction } from '@/types';

import { readLines } from '@/utils';

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

    const candidates = entries.filter((e) => extname(e) === '.md' && e.includes(filePrefix));

    // Parse all matching files concurrently
    const results = await Promise.all(
        candidates.map((entry) => parseUtilFile(join(docsDir, entry), entry, filePrefix)),
    );

    return results.filter((fn): fn is UtilFunction => fn !== null);
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

    const prefixIdx = filename.indexOf(filePrefix);
    const fnName = filename.slice(prefixIdx + filePrefix.length, -3);

    const inputsIdx = lines.indexOf('## Inputs');
    if (inputsIdx === -1) return null;

    const returnIdx = lines.indexOf('## Return Code');
    if (returnIdx === -1) return null;

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
 */
function extractDefaultValue(raw: string): string {
    let value = raw.trim();

    if (value.endsWith('.')) value = value.slice(0, -1);

    const annotMatch = RE_STRIP_ANNOTATION.exec(value);
    if (annotMatch?.[1]) value = annotMatch[1];

    const italicMatch = RE_ITALIC.exec(value);
    if (italicMatch?.[1]) return italicMatch[1];

    const bracketMatch = RE_BRACKET_ENUM.exec(value);
    if (bracketMatch?.[1]) return `${bracketMatch[1]}()`;

    return value;
}

// ---------------------------------------------------------------------------
// Serialize to intermediate list format
// ---------------------------------------------------------------------------

export function serializeUtilFunctions(fns: UtilFunction[]): string {
    return fns.map((f) => `${f.name}(${f.rawParams})`).join('\n');
}

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
