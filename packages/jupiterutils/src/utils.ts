/**
 * Shared utility helpers used across collectors and generators.
 */

import { readFile } from 'node:fs/promises';

import type { Param } from './types';

// ---------------------------------------------------------------------------
// File helpers
// ---------------------------------------------------------------------------

/** Read a UTF-8 text file and split into trimmed lines. */
export async function readLines(filePath: string): Promise<string[]> {
    const content = await readFile(filePath, 'utf8');
    return content.split(/\r?\n/);
}

/** Read a UTF-8 text file and split into non-empty trimmed lines. */
export async function readNonEmptyLines(filePath: string): Promise<string[]> {
    const lines = await readLines(filePath);
    return lines.filter((l) => l.trim() !== '');
}

// ---------------------------------------------------------------------------
// Parameter parsing
// ---------------------------------------------------------------------------

/**
 * Parse a raw function-call string like:
 *   "doThing(arg1, arg2=SomeVal(), arg3)"
 *
 * Returns:
 *   fnName  → "doThing"
 *   params  → [{ name: "arg1", defaultValue: null }, ...]
 *
 * Handles the tricky case where default values may contain nested commas
 * (e.g. "arg=Foo(x, y)").  We accumulate tokens by tracking parenthesis
 * depth instead of naively splitting on commas.
 */
export function parseSignature(raw: string): {
    fnName: string;
    params: Param[];
} {
    const parenStart = raw.indexOf('(');
    if (parenStart === -1) {
        return { fnName: raw, params: [] };
    }

    const fnName = raw.slice(0, parenStart).trim();

    // Strip the outer parens and any trailing type annotation (e.g. "):").
    const inner = raw.slice(parenStart + 1);
    const parenEnd = inner.lastIndexOf(')');
    const paramStr = parenEnd === -1 ? inner : inner.slice(0, parenEnd);

    // Strip inline comment after #
    const withoutComment = paramStr.split('#')[0] ?? paramStr;

    const params = splitParams(withoutComment).map(parseParam);

    return { fnName, params };
}

/**
 * Split a raw param string on commas while respecting nested parentheses.
 * Returns an array of raw token strings (may contain "=").
 */
export function splitParams(raw: string): string[] {
    const tokens: string[] = [];
    let depth = 0;
    let current = '';

    for (const ch of raw) {
        if (ch === '(' || ch === '[') {
            depth++;
            current += ch;
        } else if (ch === ')' || ch === ']') {
            depth--;
            current += ch;
        } else if (ch === ',' && depth === 0) {
            tokens.push(current);
            current = '';
        } else {
            current += ch;
        }
    }

    if (current.trim() !== '') {
        tokens.push(current);
    }

    return tokens;
}

/**
 * Parse a single raw token like "arg2=SomeVal()" into a Param.
 * Cleans up Python type annotations (": str", "):").
 */
export function parseParam(raw: string): Param {
    // Remove ): type-annotation artefacts and ": str" style annotations
    const cleaned = raw
        .trim()
        .replace(/\):/g, '')
        .replace(/:\s*str\b/g, '')
        .replace(/:\s*\w+/g, '')
        .trim();

    const eqIdx = cleaned.indexOf('=');
    if (eqIdx === -1) {
        return { name: cleaned, defaultValue: null };
    }

    return {
        name: cleaned.slice(0, eqIdx).trim(),
        defaultValue: cleaned.slice(eqIdx + 1).trim(),
    };
}

// ---------------------------------------------------------------------------
// Cursor parameter expansion
// ---------------------------------------------------------------------------

/**
 * For params whose names start with "cr" (cursor objects) we:
 *   - rename the runtime variable to `<name>Cursor`
 *   - emit a pre-call assignment that calls `.getPSJStr()` or builds a list
 *     comprehension for "crl" (cursor-list) params
 *
 * Returns:
 *   cursorParams        – param names after substitution (used in format())
 *   cursorSetupLines    – Python assignment lines to emit before the message
 */
export function buildCursorExpansion(params: Param[]): {
    cursorParams: string[];
    cursorSetupLines: string[];
} {
    const cursorParams: string[] = [];
    const cursorSetupLines: string[] = [];

    for (const p of params) {
        if (p.name.startsWith('crl')) {
            const cursor = `${p.name}Cursor`;
            cursorParams.push(cursor);
            cursorSetupLines.push(
                `${cursor} = f"[{', '.join(crl.getPSJStr() for crl in ${p.name})}]"`,
            );
        } else if (p.name.startsWith('cr')) {
            const cursor = `${p.name}Cursor`;
            cursorParams.push(cursor);
            cursorSetupLines.push(`${cursor} = "" if ${p.name} == None else ${p.name}.getPSJStr()`);
        } else {
            cursorParams.push(p.name);
        }
    }

    return { cursorParams, cursorSetupLines };
}

/**
 * Render the setup-lines block as indented Python source (8-space indent).
 */
export function renderCursorSetup(lines: string[]): string {
    return lines.map((l) => `        ${l}`).join('\n');
}

// ---------------------------------------------------------------------------
// Python format-string helpers
// ---------------------------------------------------------------------------

/**
 * For each param name determine the format placeholder:
 *   - names containing "str" → `'{}'`  (string placeholder)
 *   - everything else       → `{}`     (bare placeholder)
 */
export function fmtPlaceholders(paramNames: string[]): string[] {
    return paramNames.map((n) => (n.includes('str') ? "'{}'" : '{}'));
}

/**
 * Render the `.format(...)` arguments from a list of cursor-expanded param names.
 * Empty params list → `''`
 */
export function fmtArgs(cursorParams: string[]): string {
    const names = cursorParams.map((p) => p.split('=')[0] ?? p);
    if (names.length === 1 && names[0] === '') return "''";
    return names.join(', ');
}
