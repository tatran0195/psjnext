import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { glob } from 'tinyglobby';

// ---------------------------------------------------------------------------
// Paths
// ---------------------------------------------------------------------------
const DOCS_ROOT = path.resolve(import.meta.dirname, '..');
const CONTENT_CLI_DIR = path.join(DOCS_ROOT, 'content', 'docs', 'cli');
const DOCS_DIR = path.join(DOCS_ROOT, 'content', 'docs');
const EXAMPLES_DIR = path.join(DOCS_ROOT, 'examples');

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------
interface HighlightEntry {
    type: 'single';
    line: number;
}
interface HighlightRange {
    type: 'range';
    start: number;
    end: number;
}
type HighlightItem = HighlightEntry | HighlightRange;

interface SampleBlock {
    fenceStartLine: number;
    fenceEndLine: number;
    lang: string;
    highlights: HighlightItem[];
    codeLines: string[];
}

interface Frontmatter {
    title?: string;
    description?: string;
    id?: string;
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
function parseHighlightSpec(spec: string): HighlightItem[] {
    const inner = spec.replace(/^\{|\}$/g, '').trim();
    if (!inner) return [];

    const items: HighlightItem[] = [];
    for (const part of inner.split(',')) {
        const trimmed = part.trim();
        if (!trimmed) continue;

        if (trimmed.includes('-')) {
            const [a, b] = trimmed.split('-');
            const start = parseInt(a, 10);
            const end = parseInt(b, 10);
            if (!isNaN(start) && !isNaN(end)) {
                items.push({ type: 'range', start, end });
            }
        } else {
            const n = parseInt(trimmed, 10);
            if (!isNaN(n)) {
                items.push({ type: 'single', line: n });
            }
        }
    }
    return items;
}

function addHighlightMarkers(codeLines: string[], highlights: HighlightItem[]): string[] {
    const out = [...codeLines];

    for (const item of highlights) {
        if (item.type === 'single') {
            const idx = item.line - 1;
            if (idx >= 0 && idx < out.length) {
                out[idx] += '  # [hl]';
            }
        } else {
            const startIdx = item.start - 1;
            const endIdx = item.end - 1;

            if (startIdx >= 0 && startIdx < out.length) {
                out[startIdx] += '  # [hl:start]';
            }
            if (endIdx >= 0 && endIdx < out.length && endIdx !== startIdx) {
                out[endIdx] += '  # [hl:end]';
            }
        }
    }

    return out;
}

function parseFrontmatter(content: string): Frontmatter {
    const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    if (!match) return {};

    const fm: Frontmatter = {};
    for (const line of match[1].split(/\r?\n/)) {
        const kv = line.match(/^(\w+):\s*(.+)$/);
        if (!kv) continue;

        const key = kv[1] as keyof Frontmatter;
        if (key === 'title' || key === 'description' || key === 'id') {
            fm[key] = kv[2].trim();
        }
    }
    return fm;
}

// ---------------------------------------------------------------------------
// Link normalization
// ---------------------------------------------------------------------------
function normalizeDocLink(href: string, currentFile: string): string {
    if (/^(https?:)?\/\//.test(href)) return href;
    if (href.startsWith('#')) return href;

    const clean = href.replace(/\.md$/, '');

    if (clean.startsWith('/docs/')) return clean;

    const absPath = path.resolve(path.dirname(currentFile), clean);

    const relCli = path.relative(CONTENT_CLI_DIR, absPath);
    if (!relCli.startsWith('..')) {
        return '/docs/cli/' + relCli.replace(/\\/g, '/');
    }

    const relDocs = path.relative(DOCS_DIR, absPath);
    return '/docs/' + relDocs.replace(/\\/g, '/');
}

function rewriteLinks(line: string, mdPath: string): string {
    return line.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, text, href) => {
        const newHref = normalizeDocLink(href, mdPath);
        return `[${text}](${newHref})`;
    });
}

// ---------------------------------------------------------------------------
// Parser (FIXED)
// ---------------------------------------------------------------------------
function findSampleBlock(lines: string[]): SampleBlock | null {
    let inSampleSection = false;
    let fenceStartLine = -1;
    let fenceEndLine = -1;
    let fenceMarker = '';
    let lang = 'psj';
    let highlightSpec = '';
    const codeLines: string[] = [];

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        if (/^## Sample Code\s*$/.test(line.trim())) {
            inSampleSection = true;
            continue;
        }

        if (!inSampleSection) continue;

        if (fenceStartLine === -1) {
            const openMatch = line.match(/^(`{3,}|~{3,})\s*(psj(?:-[\w-]+)?|python|py)(\s+(.*))?$/);

            if (openMatch) {
                fenceMarker = openMatch[1];
                lang = openMatch[2];
                const meta = (openMatch[3] ?? '').trim();

                if (meta.includes('include=')) return null;

                const hlMatch = meta.match(/(\{[^}]+\})/);
                if (hlMatch) highlightSpec = hlMatch[1];

                fenceStartLine = i;
            }
            continue;
        }

        if (line.trim().startsWith(fenceMarker)) {
            fenceEndLine = i;
            break;
        }

        codeLines.push(line);
    }

    if (fenceStartLine === -1 || fenceEndLine === -1) return null;

    const nonEmpty = codeLines.some((l) => l.trim().length > 0);
    if (!nonEmpty) return null;

    return {
        fenceStartLine,
        fenceEndLine,
        lang,
        highlights: parseHighlightSpec(highlightSpec),
        codeLines,
    };
}

// ---------------------------------------------------------------------------
// Processor
// ---------------------------------------------------------------------------
async function processFile(mdPath: string) {
    const raw = await readFile(mdPath, 'utf-8');
    const lines = raw.split(/\r?\n/);

    const block = findSampleBlock(lines);
    if (!block) return null;

    const fm = parseFrontmatter(raw);

    const relFromCliDir = path.relative(CONTENT_CLI_DIR, mdPath);
    const version = relFromCliDir.split(path.sep)[0];
    const pyRelFromCli = relFromCliDir.replace(/\.md$/, '.py');
    const pyAbsPath = path.join(EXAMPLES_DIR, 'cli', pyRelFromCli);

    const mdDir = path.dirname(mdPath);
    const includeRel = path
        .relative(mdDir, pyAbsPath)
        .replace(/\\/g, '/')
        .replace(/^([^./])/g, './$1');

    const docsPath = '/docs/cli/' + relFromCliDir.replace(/\.md$/, '').replace(/\\/g, '/');

    const markedLines = addHighlightMarkers(block.codeLines, block.highlights);

    const header = [
        `# Title:   ${fm.title ?? path.basename(mdPath, '.md')}`,
        `# Desc:    ${fm.description ?? ''}`,
        `# Version: ${version}`,
        `# Docs:    ${docsPath}`,
        `# ---`,
        '',
    ].join('\n');

    const pyContent = header + markedLines.join('\n') + '\n';

    await mkdir(path.dirname(pyAbsPath), { recursive: true });
    await writeFile(pyAbsPath, pyContent, 'utf-8');

    const newFenceLines = [`\`\`\`${block.lang} include="${includeRel}"`, '```'];

    const newLines = [
        ...lines.slice(0, block.fenceStartLine),
        ...newFenceLines,
        ...lines.slice(block.fenceEndLine + 1),
    ].map((line) => rewriteLinks(line, mdPath));

    await writeFile(mdPath, newLines.join('\n'), 'utf-8');

    return { pyPath: pyAbsPath };
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
async function main() {
    const mdFiles = await glob('**/*.md', {
        cwd: CONTENT_CLI_DIR,
        absolute: true,
    });

    for (const mdFile of mdFiles) {
        await processFile(mdFile);
    }

    console.log('Done.');
}

main();
