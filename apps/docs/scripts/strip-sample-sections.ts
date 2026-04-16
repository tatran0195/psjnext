/**
 * strip-sample-sections.ts
 *
 * One-time migration script.
 *
 * Removes `## Sample Code` sections from every .md file under content/docs/cli/
 * when the section contains either:
 *   - a code fence with `include="..."` (the generated path-based includes)
 *   - an empty code fence (no content between the backticks)
 *
 * Hand-written inline code sections (non-empty fence, no `include=`) are preserved.
 *
 * Usage:
 *   bun scripts/strip-sample-sections.ts
 */

import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { glob } from 'glob';

// ---------------------------------------------------------------------------
// Paths
// ---------------------------------------------------------------------------
const DOCS_ROOT = path.resolve(import.meta.dirname, '..');
const CONTENT_CLI_DIR = path.join(DOCS_ROOT, 'content', 'docs', 'cli');

// ---------------------------------------------------------------------------
// Core stripping logic
// ---------------------------------------------------------------------------

interface StripResult {
    changed: boolean;
    result: string;
}

/**
 * Strips ## Sample Code sections that are auto-generated (include= fence or empty fence).
 * Returns the cleaned content and whether any change was made.
 */
function stripSampleSection(content: string): StripResult {
    const lines = content.split(/\r?\n/);
    const out: string[] = [];
    let i = 0;
    let changed = false;

    while (i < lines.length) {
        const line = lines[i];

        if (/^## Sample Code\s*$/.test(line)) {
            // Peek ahead: skip blank lines
            let j = i + 1;
            while (j < lines.length && lines[j].trim() === '') j++;

            if (j < lines.length) {
                const fenceOpenMatch = lines[j].match(/^(`{3,}|~{3,})/);

                if (fenceOpenMatch) {
                    const fenceMarker = fenceOpenMatch[1];
                    const isInclude = lines[j].includes('include="');

                    // Find the closing fence
                    let k = j + 1;
                    const fenceContent: string[] = [];
                    while (k < lines.length && !lines[k].startsWith(fenceMarker)) {
                        fenceContent.push(lines[k]);
                        k++;
                    }
                    // k is the closing fence line index (or past EOF)

                    const isEmpty = fenceContent.every((l) => l.trim() === '');

                    if (isInclude || isEmpty) {
                        // Skip heading + blanks + fence open + content + fence close
                        i = k + 1;
                        // Skip one trailing blank line if present
                        if (i < lines.length && lines[i].trim() === '') i++;
                        changed = true;
                        continue;
                    }
                }
            }
            // Hand-written non-empty code → fall through and keep the heading
        }

        out.push(line);
        i++;
    }

    // Normalise: trim trailing blank lines, ensure single trailing newline
    const result = out.join('\n').trimEnd() + '\n';
    return { changed, result };
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
    const mdFiles = await glob('**/*.md', { cwd: CONTENT_CLI_DIR, absolute: true });

    let stripped = 0;
    let skipped = 0;

    for (const mdFile of mdFiles) {
        const raw = await readFile(mdFile, 'utf-8');
        const { changed, result } = stripSampleSection(raw);

        if (changed) {
            await writeFile(mdFile, result, 'utf-8');
            stripped++;
        } else {
            skipped++;
        }
    }

    console.log(`Done.`);
    console.log(`  Stripped Sample Code sections: ${stripped}`);
    console.log(`  Unchanged (no auto-generated section): ${skipped}`);
    console.log(`  Total files scanned: ${mdFiles.length}`);
}

main();
