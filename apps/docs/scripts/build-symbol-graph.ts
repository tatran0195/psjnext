/**
 * build-symbol-graph.ts
 *
 * Extracts linkable symbols from docs/data-type/psj-command and writes
 * docs/.generated/symbol-graph.json.
 *
 * SOURCE TYPES (all under docs/data-type/psj-command/):
 *
 *   A. Page-level symbols  -- one whole page IS the symbol
 *      * parameter-types/Data-Type_JPT_*.md   -> symbol = frontmatter `id`  (e.g. "BASIC")
 *      * material-property/{subdir}/Class_*.md  -> symbol = frontmatter `id`  (e.g. "Elastic")
 *
 *   B. Enum row symbols    -- table rows inside a page define individual symbols
 *      * built-in-types.md     -> col 1 "Jupiter Macro/API data type"  (e.g. "Integer")
 *                                col 2 abbrev inside backticks          (e.g. "int")
 *      * element-types.md      -> backtick-wrapped values in Kind/Type cols (e.g. "ELEMKIND_2D")
 *      * entity-types.md       -> backtick-wrapped values in Type col       (e.g. "BODY")
 *      * material-types.md     -> col 2 "Key Name" plain text               (e.g. "YOUNGS_MODULUS")
 *      * material-unit-types.md -> col 2 "Key Name" plain text              (e.g. "Length_mm")
 */

import fs from 'node:fs';
import path from 'node:path';
import { glob } from 'tinyglobby';

// -- Public types (imported by symbol-resolver.ts) -------------------------

export interface SymbolEntry {
    /** Display name used in tooltips and aria labels */
    name: string;
    /** Absolute URL path for the link href */
    href: string;
    /** One-line description shown in hover tooltip */
    description: string;
    /** Relative path to source file for debugging */
    sourceFile: string;
    /**
     * Symbol category -- lets the remark plugin apply different styling
     * or filtering per category.
     */
    category: 'parameter-type' | 'class' | 'built-in' | 'element' | 'entity' | 'material-key' | 'unit-key' | 'enum'; // Added enum category for auto-detected symbols
    /**
     * Optional scope (usually page ID) for disambiguating symbols.
     * Scoped symbols are stored as "scope.name".
     */
    scope?: string;
}

export interface SymbolGraph {
    /** Primary index: symbol name -> entry */
    symbols: Record<string, SymbolEntry>;
    /** Alternate-name index: abbreviation / alias -> canonical name */
    aliases: Record<string, string>;
    version: number;
    builtAt: string;
}

// -- Paths -----------------------------------------------------------------

// -- Paths -----------------------------------------------------------------

const DATA_TYPE_ROOT = 'content/docs/data-type';
const OUTPUT_PATH = 'content/docs/.generated/symbol-graph.json';

// -- Utilities -------------------------------------------------------------

/** Extract YAML frontmatter value for a given key. */
function frontmatter(text: string, key: string): string | null {
    const m = new RegExp(`^${key}:\\s*(.+)`, 'm').exec(text);
    return m ? m[1].trim() : null;
}

/** Extract the first ## Description paragraph (text only, no markdown). */
function extractDescription(text: string): string {
    const m = /^## Description\s*\n+([\s\S]*?)(?=\n##|\n```|$)/m.exec(text);
    if (!m) return '';
    return m[1]
        .replace(/!\[.*?\]\(.*?\)/g, '') // strip images
        .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // links -> text
        .replace(/[*`]/g, '') // strip inline formatting (keep _ in identifiers)
        .replace(/\s+/g, ' ')
        .trim()
        .slice(0, 120);
}

/** Extract backtick-wrapped tokens from a markdown table cell value. */
function backtickTokens(cell: string): string[] {
    const results: string[] = [];
    const re = /`([^`]+)`/g;
    let m: RegExpExecArray | null;
    while ((m = re.exec(cell)) !== null) results.push(m[1]);
    return results;
}

/**
 * Strip markdown formatting from a cell value, preserving underscores.
 * Underscores are meaningful in PSJ identifiers (e.g. RotateStiff_mNmm_deg).
 * Only asterisks and backticks are removed.
 */
function stripMarkdown(s: string): string {
    return s.replace(/[*`]/g, '').trim();
}

/**
 * Convert a LaTeX math string to a readable plain-text description.
 * Strips delimiters, converts backslash-prefixed letters to plain letters,
 * maps superscripts (^2 -> unicode), replaces * with middle-dot.
 * Example: "$kgf*s^2/mm$" -> "kgf\u00B7s\u00B2/mm"
 */
function cleanLatex(s: string): string {
    const SUPERSCRIPTS: Record<string, string> = {
        '0': '\u2070',
        '1': '\u00B9',
        '2': '\u00B2',
        '3': '\u00B3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079',
    };
    return s
        .replace(/\\\$/g, '') // remove escaped \$ (e.g. trailing \$)
        .replace(/\$/g, '') // remove all remaining $ delimiters
        .replace(/\\([a-zA-Z])/g, '$1') // \N -> N, \mN -> mN (stray backslash prefix only)
        .replace(/\^([0-9])/g, (_, d) => SUPERSCRIPTS[d] ?? d) // ^2 -> \u00B2
        .replace(/\*/g, '\u00B7') // * -> middle dot
        .replace(/[{}]/g, '') // strip any remaining braces
        .replace(/\/+/g, '/') // collapse double-slashes (source typos)
        .trim();
}

/** Split a markdown table row into trimmed cell strings (no leading/trailing |). */
function splitRow(line: string): string[] {
    return line
        .replace(/^\||\|$/g, '')
        .split('|')
        .map((c) => c.trim());
}

/**
 * Split a 4-column unit-type row (ID | KeyName | Usage | Description),
 * handling malformed rows where the Usage cell itself contains an extra pipe.
 *
 * Two documented malformations in material-unit-types.md:
 *
 *   TimeUnit rows:
 *     | 0 |Time_s|JPT.TimeUnit.|Time_s| $s$ |
 *     cells = [ID, Key, "JPT.TimeUnit.", "Time_s", "$s$"]   <- 5 cells
 *     Usage was split on the dot: "JPT.TimeUnit." | "Time_s"
 *     Description is the LAST cell.
 *
 *   HeatGenerationUnit rows:
 *     | 1 |HeatGeneration_mW_mm3|JPT.HeatGenerationUnit.|HeatGeneration_mW_mm3|$mW/mm^3$|
 *     cells = [ID, Key, "JPT...Unit.", "HeatGeneration_mW_mm3", "$mW/mm^3$"]  <- 5 cells
 *     Same pattern -- description is the LAST cell.
 *
 * Strategy for any row with 5+ cells: keep [0] ID, [1] Key, and take the
 * LAST cell as the description (it is always the LaTeX math expression).
 * Everything between [2] and [last-1] is the Usage column (possibly split).
 */
function splitUnitRow(line: string): string[] | null {
    const cells = splitRow(line);
    if (cells.length === 4) return cells;
    if (cells.length >= 5) {
        // Reconstruct as canonical 4-column form: [ID, Key, Usage, Desc]
        const id = cells[0];
        const key = cells[1];
        const desc = cells[cells.length - 1]; // last cell = description
        const usage = cells.slice(2, cells.length - 1).join('|'); // middle cells = usage (reassembled)
        return [id, key, usage, desc];
    }
    return null;
}

/** True if a row is a separator (| --- | --- |). */
function isSeparator(line: string): boolean {
    return /^\|[\s|:\\-]+\|$/.test(line);
}

// -- Graph builder ---------------------------------------------------------

class GraphBuilder {
    readonly graph: SymbolGraph = {
        symbols: {},
        aliases: {},
        version: 1,
        builtAt: new Date().toISOString(),
    };

    private warnings = 0;
    private currentScope: string | null = null;

    /** Set the scope for subsequent registrations (usually the page ID). */
    setScope(scope: string | null): void {
        this.currentScope = scope;
    }

    // -- Registration helpers -----------------------------------------------

    private register(entry: SymbolEntry): void {
        const symbolKey = entry.scope ? `${entry.scope}.${entry.name}` : entry.name;
        const existing = this.graph.symbols[symbolKey];

        if (existing) {
            // Same file + same description = true source duplicate (e.g. D1 in material-types.md).
            // Silently skip. Only warn when the conflict is across different files or descriptions,
            // because that signals a real naming collision that needs attention.
            const sameFile = existing.sourceFile === entry.sourceFile;
            const sameDescription = existing.description === entry.description;
            if (!sameFile || !sameDescription) {
                console.warn(
                    `[symbols] WARN Duplicate symbol "${symbolKey}" in ${entry.sourceFile}` +
                        ` (already from ${existing.sourceFile})`,
                );
                this.warnings++;
            }
            return;
        }
        this.graph.symbols[symbolKey] = entry;
    }

    private registerAlias(alias: string, canonicalName: string): void {
        if (!this.graph.aliases[alias]) {
            this.graph.aliases[alias] = canonicalName;
        }
    }

    // -- Source type A: whole-page symbols ---------------------------------

    /**
     * Each file in data-type/ represents a single named type.
     * The frontmatter `id` is the symbol name.
     */
    processPageSymbol(file: string, category: SymbolEntry['category']): void {
        const text = fs.readFileSync(file, 'utf8');
        const id = frontmatter(text, 'id');
        const title = frontmatter(text, 'title');

        if (!id) {
            this.currentScope = null;
            return; // Silently skip files without an id
        }

        this.currentScope = id;

        // Build href relative to content/docs/
        const afterDocs = path
            .relative('content/docs', file)
            .replace(/\.mdx?$/, '')
            .replace(/\\/g, '/');

        const description = extractDescription(text) || (title ? `${title} data type` : `${id} type`);

        this.register({
            name: id,
            href: `/${afterDocs}`,
            description,
            sourceFile: path.relative(process.cwd(), file),
            category,
            scope: undefined, // Page-level symbols themselves are always global
        });
    }

    /**
     * Scans a file for markdown tables and extracts potential symbols.
     * Looks for backtick-wrapped identifiers like JPT.* or ELEM*
     */
    processAutoEnums(file: string): void {
        const text = fs.readFileSync(file, 'utf8');
        const lines = text.split('\n').map((l) => l.trim());

        // Calculate base href for anchors
        const afterDocs = path
            .relative('content/docs', file)
            .replace(/\.mdx?$/, '')
            .replace(/\\/g, '/');
        const href = `/${afterDocs}`;

        for (const line of lines) {
            if (!line.startsWith('|')) continue;
            if (isSeparator(line)) continue;

            const cells = splitRow(line);
            for (let i = 0; i < cells.length; i++) {
                const cell = cells[i];
                const tokens = backtickTokens(cell);

                for (const token of tokens) {
                    // Smart detection:
                    // 1. Starts with JPT.
                    // 2. Starts with ELEMKIND_ or ELEMTYPE_
                    // 3. Is all uppercase with underscores (likely a constant) and length > 3
                    const isJPT = token.startsWith('JPT.');
                    const isElement = token.startsWith('ELEMKIND_') || token.startsWith('ELEMTYPE_');
                    const isConstant = /^[A-Z][A-Z0-9_]{3,}$/.test(token);

                    if (isJPT || isElement || isConstant) {
                        // Find description in adjacent columns
                        const possibleDesc =
                            stripMarkdown(cells[i + 1] ?? '') || stripMarkdown(cells[i - 1] ?? '') || token;

                        this.register({
                            name: token,
                            href: `${href}#${token.toLowerCase()}`,
                            description: possibleDesc.slice(0, 120),
                            sourceFile: path.relative(process.cwd(), file),
                            category: isElement ? 'element' : 'enum',
                            scope: this.currentScope ?? undefined,
                        });
                    }
                }
            }
        }
    }

    // -- Source type B: built-in-types.md ----------------------------------

    /**
     * Registers both the full type name (col 1) and its abbreviation (col 2
     * backtick value) as linked symbols. The abbreviation is stored as an
     * alias pointing to the full-name anchor.
     *
     * Column order: | Type Name | `abbrev` | Prefix+VarName | Description |
     */
    processBuiltInTypes(file: string): void {
        const text = fs.readFileSync(file, 'utf8');
        const lines = text.split('\n').map((l) => l.trim());
        const href = '/data-type/psj-command/built-in-types';

        for (const line of lines) {
            if (!line.startsWith('|')) continue;
            if (isSeparator(line)) continue;

            const cells = splitRow(line);
            if (cells.length < 2) continue;

            const typeName = cells[0].replace(/[*_`]/g, '').trim();
            if (!typeName || typeName === 'Jupiter Macro/API data type') continue;

            // Description is the last cell
            const description =
                cells[cells.length - 1]
                    .replace(/\s+/g, ' ')
                    .replace(/<br\s*\/?>/gi, ' ')
                    .replace(/[*`]/g, '')
                    .trim()
                    .slice(0, 120) || `${typeName} built-in type`;

            const anchor = typeName.toLowerCase().replace(/\s+/g, '-');

            this.register({
                name: typeName,
                href: `${href}#${anchor}`,
                description,
                sourceFile: path.relative(process.cwd(), file),
                category: 'built-in',
                scope: this.currentScope ?? undefined,
            });

            // Register abbreviation(s) inside backticks in col 2
            const abbrevTokens = backtickTokens(cells[1] ?? '');
            for (const abbrev of abbrevTokens) {
                if (abbrev !== typeName) {
                    this.registerAlias(abbrev, typeName);
                }
            }
        }
    }

    // -- Source type B: element-types.md -----------------------------------

    /**
     * Registers backtick-wrapped ELEMKIND_* and ELEMTYPE_* tokens.
     * These appear in the Kind and Type columns of the two-part table.
     *
     * Column order:
     *   | ElemKind Int | `ELEMKIND_*` | Kind Description | ElemType Int | `ELEMTYPE_*` | Type Description |
     */
    processElementTypes(file: string): void {
        const text = fs.readFileSync(file, 'utf8');
        const lines = text.split('\n').map((l) => l.trim());
        const href = '/data-type/psj-command/element-types';

        for (const line of lines) {
            if (!line.startsWith('|')) continue;
            if (isSeparator(line)) continue;

            const cells = splitRow(line);

            // ELEMKIND column (index 1) and ELEMTYPE column (index 4)
            const kindTokens = backtickTokens(cells[1] ?? '');
            const typeTokens = backtickTokens(cells[4] ?? '');

            for (const token of kindTokens) {
                if (!token.startsWith('ELEMKIND_')) continue;
                const description = stripMarkdown(cells[2] ?? '') || token;
                this.register({
                    name: token,
                    href: `${href}#${token.toLowerCase()}`,
                    description,
                    sourceFile: path.relative(process.cwd(), file),
                    category: 'element',
                    scope: this.currentScope ?? undefined,
                });
            }

            for (const token of typeTokens) {
                if (!token.startsWith('ELEMTYPE_')) continue;
                const description = stripMarkdown(cells[5] ?? '') || token;
                this.register({
                    name: token,
                    href: `${href}#${token.toLowerCase()}`,
                    description,
                    sourceFile: path.relative(process.cwd(), file),
                    category: 'element',
                    scope: this.currentScope ?? undefined,
                });
            }
        }
    }

    // -- Source type B: entity-types.md ------------------------------------

    /**
     * Registers backtick-wrapped DItemType tokens from the Type column.
     *
     * Column order: | Int Notation | `TYPE_NAME` | Description |
     */
    processEntityTypes(file: string): void {
        const text = fs.readFileSync(file, 'utf8');
        const lines = text.split('\n').map((l) => l.trim());
        const href = '/data-type/psj-command/entity-types';

        for (const line of lines) {
            if (!line.startsWith('|')) continue;
            if (isSeparator(line)) continue;

            const cells = splitRow(line);
            if (cells.length < 3) continue;

            const tokens = backtickTokens(cells[1] ?? '');
            const description = stripMarkdown(cells[2] ?? '');

            for (const token of tokens) {
                if (!token || token === 'Type of DItem') continue;
                this.register({
                    name: token,
                    href: `${href}#${token.toLowerCase()}`,
                    description: description || token,
                    sourceFile: path.relative(process.cwd(), file),
                    category: 'entity',
                    scope: this.currentScope ?? undefined,
                });
            }
        }
    }

    // -- Source type B: material-types.md ----------------------------------

    /**
     * Registers KEY NAME values (plain text, no backticks) from col 2.
     *
     * Column order: | Int Notation | Key Name | Description |
     */
    processMaterialTypes(file: string): void {
        const text = fs.readFileSync(file, 'utf8');
        const lines = text.split('\n').map((l) => l.trim());
        const href = '/data-type/psj-command/material-types';

        const HEADER_NAMES = new Set(['Key Name', 'Int Notation']);

        for (const line of lines) {
            if (!line.startsWith('|')) continue;
            if (isSeparator(line)) continue;

            const cells = splitRow(line);
            if (cells.length < 3) continue;

            const keyName = stripMarkdown(cells[1]);
            const description = stripMarkdown(cells[2]);

            if (!keyName || HEADER_NAMES.has(keyName)) continue;

            this.register({
                name: keyName,
                href: `${href}#${keyName.toLowerCase()}`,
                description: description || `${keyName} material property`,
                sourceFile: path.relative(process.cwd(), file),
                category: 'material-key',
                scope: this.currentScope ?? undefined,
            });
        }
    }

    // -- Source type B: material-unit-types.md -----------------------------

    /**
     * Registers Key Name values from the unit tables.
     *
     * Column order: | ID | Key Name | Usage | Description |
     */
    processMaterialUnitTypes(file: string): void {
        const text = fs.readFileSync(file, 'utf8');
        const lines = text.split('\n').map((l) => l.trim());
        const href = '/data-type/psj-command/material-unit-types';

        const HEADER_NAMES = new Set(['Key Name', 'ID']);

        for (const line of lines) {
            if (!line.startsWith('|')) continue;
            if (isSeparator(line)) continue;

            const cells = splitUnitRow(line);
            if (!cells) continue;

            const keyName = stripMarkdown(cells[1]);
            if (!keyName || HEADER_NAMES.has(keyName)) continue;

            // cells[3] is the LaTeX description (e.g. "$N*mm/rad$" -> "N\u00B7mm/rad").
            // For rows where the source has "$$" (empty math), try the Usage column (cells[2])
            // which normally contains "JPT.UnitGroup.KeyName" -- take the last dot-segment.
            // Only use it if it actually differs from the key name (some rows have the key
            // name copied verbatim into Usage, which adds no information).
            const latexDesc = cleanLatex(cells[3]);
            const usageSegment = (cells[2].split('.').pop() ?? '').replace(/\$/g, '').trim();
            const usageFallback = usageSegment !== keyName ? usageSegment : '';
            const description = latexDesc || usageFallback || `${keyName} unit`;

            this.register({
                name: keyName,
                href: `${href}#${keyName.toLowerCase()}`,
                description,
                sourceFile: path.relative(process.cwd(), file),
                category: 'unit-key',
                scope: this.currentScope ?? undefined,
            });
        }
    }

    // -- Reporting ----------------------------------------------------------

    summary(fileCount: number): void {
        const total = Object.keys(this.graph.symbols).length;
        const aliases = Object.keys(this.graph.aliases).length;
        console.log(
            `[symbols] Extracted ${total} symbols + ${aliases} aliases` +
                ` from ${fileCount} files` +
                (this.warnings ? ` (${this.warnings} warnings)` : ''),
        );
    }
}

// -- Main ------------------------------------------------------------------

/** Recursively find all markdown files in a directory. */
async function walk(dir: string): Promise<string[]> {
    return glob(`${dir}/**/*.md`);
}

async function buildGraph(): Promise<void> {
    const builder = new GraphBuilder();
    let fileCount = 0;

    const root = DATA_TYPE_ROOT;

    // Fail fast with a clear message if the script is run from the wrong directory
    if (!fs.existsSync(root)) {
        console.error(
            `[symbols] ERROR: "${root}" not found.\n` +
                `  cwd: ${process.cwd()}\n` +
                `  Run this script from your project root, e.g.:\n` +
                `    tsx scripts/build-symbol-graph.ts`,
        );
        process.exit(1);
    }

    const allFiles = await walk(root);

    // Specific handlers for legacy files or files needing special extraction (LaTeX etc)
    const specializedHandlers: Record<string, (f: string) => void> = {
        'built-in-types.md': (f) => builder.processBuiltInTypes(f),
        'element-types.md': (f) => builder.processElementTypes(f),
        'entity-types.md': (f) => builder.processEntityTypes(f),
        'material-types.md': (f) => builder.processMaterialTypes(f),
        'material-unit-types.md': (f) => builder.processMaterialUnitTypes(f),
    };

    for (const f of allFiles) {
        const basename = path.basename(f);
        const category: SymbolEntry['category'] = f.includes('parameter-types')
            ? 'parameter-type'
            : f.includes('material-property')
              ? 'class'
              : 'enum';

        // 1. Always process page-level symbol (ID in frontmatter)
        builder.processPageSymbol(f, category);

        // 2. Process table-based symbols
        if (specializedHandlers[basename]) {
            // Specific global lists are treated as unscoped so they serve as fallsbacks
            builder.setScope(null);
            specializedHandlers[basename](f);
        } else {
            builder.processAutoEnums(f);
        }

        fileCount++;
    }

    builder.summary(fileCount);

    fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
    fs.writeFileSync(OUTPUT_PATH, JSON.stringify(builder.graph, null, 2));
    console.log(`[symbols] -> ${OUTPUT_PATH}`);
}

buildGraph().catch((e) => {
    console.error('[symbols] Build failed:', e);
    process.exit(1);
});
