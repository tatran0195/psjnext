/**
 * remark-include-code.ts
 *
 * Remark plugin with two capabilities:
 *
 * 1. INCLUDE RESOLUTION (legacy / transition): Resolves `include="path/to/file.py"` meta
 *    on code fences.  At build time, for any code node whose meta contains `include="..."`:
 *      a. Reads the referenced .py file relative to the current .md file
 *      b. Strips the header comment block (# Title:, # Desc:, # Version:, # Docs:)
 *      c. Scans for `# [hl]`, `# [hl:start]`, `# [hl:end]` markers
 *      d. Strips those markers from the code body
 *      e. Computes the Shiki {N} highlight spec from marker positions
 *      f. Updates the code node with the clean code + computed meta
 *
 * 2. AUTO-INJECT: For .md files under content/docs/cli/ that do NOT already have a
 *    `## Sample Code` heading and have a matching .py in examples/cli/ (same relative
 *    path, .md → .py), automatically appends `## Sample Code` + the populated code block
 *    at the end of the AST.  Manual sections always take precedence.
 */

import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import type { Code, Heading, Root, Text } from 'mdast';
import type { Plugin } from 'unified';
import type { VFile } from 'vfile';
import { visit } from 'unist-util-visit';

// ---------------------------------------------------------------------------
// Marker parsing
// ---------------------------------------------------------------------------

const HL_SINGLE = /\s+#\s+\[hl\]$/;
const HL_START = /\s+#\s+\[hl:start\]$/;
const HL_END = /\s+#\s+\[hl:end\]$/;

interface ParseResult {
    cleanCode: string;
    /** Shiki-compatible spec like "{6,9,12}" or "" if no highlights */
    hlSpec: string;
}

function parseHlMarkers(code: string): ParseResult {
    const rawLines = code.split('\n');
    const singles: number[] = [];
    const ranges: Array<[number, number]> = [];
    let rangeStart: number | null = null;

    const cleanLines = rawLines.map((line, i) => {
        const lineNum = i + 1; // 1-indexed

        if (HL_SINGLE.test(line)) {
            singles.push(lineNum);
            return line.replace(HL_SINGLE, '');
        }
        if (HL_START.test(line)) {
            rangeStart = lineNum;
            return line.replace(HL_START, '');
        }
        if (HL_END.test(line)) {
            if (rangeStart !== null) {
                ranges.push([rangeStart, lineNum]);
                rangeStart = null;
            }
            return line.replace(HL_END, '');
        }
        return line;
    });

    // Build Shiki spec string: ranges first, then singles (sorted)
    const parts: string[] = [
        ...ranges.map(([s, e]) => `${s}-${e}`),
        ...singles.sort((a, b) => a - b).map(String),
    ];
    const hlSpec = parts.length > 0 ? `{${parts.join(',')}}` : '';

    return { cleanCode: cleanLines.join('\n'), hlSpec };
}

// ---------------------------------------------------------------------------
// Header stripping
// ---------------------------------------------------------------------------

const HEADER_SENTINEL = /^# ---\s*$/;
const HEADER_LINE = /^# (Title|Desc|Version|Docs):\s*/;

/** Strip the auto-generated header block up to and including the `# ---` sentinel line and the blank line after. */
function stripHeader(content: string): string {
    const lines = content.split('\n');
    // Find the sentinel line `# ---`
    const sentinelIdx = lines.findIndex((l) => HEADER_SENTINEL.test(l));
    if (sentinelIdx === -1) {
        // Fallback: skip leading lines that look like header lines
        let i = 0;
        while (i < lines.length && HEADER_LINE.test(lines[i])) i++;
        // Skip one blank line after
        if (i < lines.length && lines[i].trim() === '') i++;
        return lines.slice(i).join('\n');
    }
    // Skip sentinel + following blank line
    let start = sentinelIdx + 1;
    if (start < lines.length && lines[start].trim() === '') start++;
    return lines.slice(start).join('\n');
}

// ---------------------------------------------------------------------------
// Auto-inject helpers
// ---------------------------------------------------------------------------

/**
 * Derive the matching .py path from a .md file path under content/docs/cli/.
 *
 * content/docs/cli/{version}/{...}/{Name}.md
 *   → examples/cli/{version}/{...}/{Name}.py
 *
 * Returns the absolute path if the file exists, otherwise null.
 */
function findMatchingPy(mdFilePath: string): string | null {
    const normalized = path.resolve(mdFilePath);
    const parts = normalized.split(path.sep);

    // Locate the content/docs/cli segment
    const cliIdx = parts.findIndex(
        (p, i) =>
            p === 'content' &&
            i + 2 < parts.length &&
            parts[i + 1] === 'docs' &&
            parts[i + 2] === 'cli',
    );
    if (cliIdx === -1) return null;

    // Everything before 'content' is the docs-app root
    const docsRoot = parts.slice(0, cliIdx).join(path.sep);

    // Relative path from cli/ with .md → .py
    const relParts = [...parts.slice(cliIdx + 3)];
    if (relParts.length === 0) return null;
    relParts[relParts.length - 1] = relParts[relParts.length - 1].replace(/\.md$/, '.py');

    const pyPath = path.join(docsRoot, 'examples', 'cli', ...relParts);
    return existsSync(pyPath) ? pyPath : null;
}

/** Return true if the AST already contains a ## Sample Code heading. */
function hasSampleCodeHeading(tree: Root): boolean {
    let found = false;
    visit(tree, 'heading', (node: Heading) => {
        if (found || node.depth !== 2) return;
        const text = node.children
            .filter((c): c is Text => c.type === 'text')
            .map((c) => c.value)
            .join('');
        if (text.trim() === 'Sample Code') found = true;
    });
    return found;
}

// ---------------------------------------------------------------------------
// Plugin
// ---------------------------------------------------------------------------

export const remarkIncludeCode: Plugin<[], Root> = () => {
    return (tree: Root, file: VFile) => {
        // ── 1. Resolve explicit include="path" fences (legacy / transition) ─
        visit(tree, 'code', (node: Code) => {
            if (!node.meta) return;

            const includeMatch = node.meta.match(/include="([^"]+)"/);
            if (!includeMatch) return;

            const includePath = includeMatch[1];

            // Resolve path relative to the current .md file
            const basePath = file.path ? path.dirname(file.path) : process.cwd();
            const absPath = path.resolve(basePath, includePath);

            let rawContent: string;
            try {
                rawContent = readFileSync(absPath, 'utf-8');
            } catch {
                console.warn(`[remark-include-code] Cannot read: ${absPath}`);
                node.value = `# ERROR: could not read ${includePath}`;
                return;
            }

            // Strip the header block
            const codeOnly = stripHeader(rawContent);

            // Parse and strip # [hl] markers, compute Shiki spec
            const { cleanCode, hlSpec } = parseHlMarkers(codeOnly);

            // Trim trailing newline so Shiki doesn't add an extra blank line
            node.value = cleanCode.replace(/\n$/, '');

            // Rebuild meta: remove include="..." part, prepend highlight spec
            const metaWithoutInclude = node.meta.replace(/include="[^"]+"\s?/, '').trim();
            const newMeta = [hlSpec, metaWithoutInclude].filter(Boolean).join(' ');
            node.meta = newMeta || null;
        });

        // ── 2. Auto-inject ## Sample Code from examples/cli/ ────────────────
        if (!file.path) return;

        // If a manual ## Sample Code section already exists, respect it
        if (hasSampleCodeHeading(tree)) return;

        const pyPath = findMatchingPy(file.path);
        if (!pyPath) return;

        let rawContent: string;
        try {
            rawContent = readFileSync(pyPath, 'utf-8');
        } catch {
            console.warn(`[remark-include-code] Cannot read: ${pyPath}`);
            return;
        }

        const codeOnly = stripHeader(rawContent);
        const { cleanCode, hlSpec } = parseHlMarkers(codeOnly);
        const finalCode = cleanCode.replace(/\n$/, '');

        const headingNode: Heading = {
            type: 'heading',
            depth: 2,
            children: [{ type: 'text', value: 'Sample Code' }],
        };

        const codeNode: Code = {
            type: 'code',
            lang: 'psj',
            meta: hlSpec || null,
            value: finalCode,
        };

        tree.children.push(headingNode, codeNode);
    };
};
