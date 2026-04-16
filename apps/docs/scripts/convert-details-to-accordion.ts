// scripts/convert-details-to-accordion.ts

import * as fs from 'fs';
import * as path from 'path';

const IMPORT_LINE = "import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';";

/**
 * Extract all <details>...</details> blocks from MDX source.
 */
function extractDetailBlocks(source: string): { raw: string; title: string; body: string }[] {
    const blocks: { raw: string; title: string; body: string }[] = [];
    let i = 0;

    while (i < source.length) {
        const openStart = source.indexOf('<details', i);
        if (openStart === -1) break;

        const openEnd = source.indexOf('>', openStart);
        if (openEnd === -1) break;

        let depth = 1;
        let cursor = openEnd + 1;

        while (cursor < source.length && depth > 0) {
            const nextOpen = source.indexOf('<details', cursor);
            const nextClose = source.indexOf('</details>', cursor);

            if (nextClose === -1) break;

            if (nextOpen !== -1 && nextOpen < nextClose) {
                depth++;
                cursor = nextOpen + 8;
            } else {
                depth--;
                if (depth === 0) {
                    const closeEnd = nextClose + '</details>'.length;
                    const raw = source.slice(openStart, closeEnd);
                    const inner = source.slice(openEnd + 1, nextClose);

                    // Parse summary and body
                    const summaryMatch = inner.match(/<summary>([\s\S]*?)<\/summary>/);
                    const title = summaryMatch
                        ? summaryMatch[1].replace(/\*\*/g, '').replace(/`/g, '').trim()
                        : 'Details';
                    const body = summaryMatch
                        ? inner.replace(summaryMatch[0], '').trim()
                        : inner.trim();

                    blocks.push({ raw, title, body });
                    i = closeEnd;
                    break;
                }
                cursor = nextClose + '</details>'.length;
            }
        }

        if (depth !== 0) break;
    }

    return blocks;
}

/**
 * Convert MDX source: replace <details> with <Accordion>, group consecutive ones.
 */
function convertSource(source: string): string {
    const blocks = extractDetailBlocks(source);
    if (blocks.length === 0) return source;

    // Replace each <details> block with <Accordion>
    let result = source;
    for (const block of blocks) {
        const accordion = `<Accordion title="${block.title}">\n${block.body}\n</Accordion>`;
        result = result.replace(block.raw, accordion);
    }

    // Group consecutive <Accordion> blocks in <Accordions>
    result = result.replace(
        /(<Accordion[\s\S]*?<\/Accordion>)(\s*\n\s*\n\s*<Accordion[\s\S]*?<\/Accordion>)+/g,
        (match) => {
            const inner = match.trim().replace(/^/gm, '  ');
            return `<Accordions>\n${inner}\n</Accordions>`;
        },
    );

    // Inject import after frontmatter
    if (!result.includes(IMPORT_LINE)) {
        const fmMatch = result.match(/^---[\s\S]*?---\n/);
        if (fmMatch) {
            result =
                result.slice(0, fmMatch[0].length) +
                '\n' +
                IMPORT_LINE +
                '\n' +
                result.slice(fmMatch[0].length);
        } else {
            result = IMPORT_LINE + '\n\n' + result;
        }
    }

    return result;
}

// ─── CLI ──────────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
const dry = args.includes('--dry');
const files = args.filter((a) => !a.startsWith('--'));

if (files.length === 0) {
    console.error('Usage: npx tsx scripts/convert-details-to-accordion.ts [--dry] <file.mdx> ...');
    process.exit(1);
}

for (const file of files) {
    const resolved = path.resolve(file);

    if (!fs.existsSync(resolved)) {
        console.error(`Not found: ${resolved}`);
        continue;
    }

    const converted = convertSource(fs.readFileSync(resolved, 'utf-8'));

    if (dry) {
        console.log(`\n── ${resolved} ──\n${converted}`);
    } else {
        fs.writeFileSync(resolved, converted, 'utf-8');
        console.log(`✓ ${resolved}`);
    }
}
