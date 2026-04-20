/**
 * Markdown documentation reader.
 *
 * Bun changes:
 *   - `access()` existence check replaced with `Bun.file().exists()` —
 *     the idiomatic Bun API; avoids importing from node:fs/promises.
 *   - readLines() already uses Bun.file() (see utils.ts).
 */

import { extname, join } from 'node:path';

import type { Config } from '../types';

import { readLines } from '../utils';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Read the documentation section (from "## Description" to EOF) for a given
 * fully-qualified function reference.
 *
 * @param fqName - Fully-qualified name such as:
 *   - "Measurement.Section.getArea"         → psj-command doc
 *   - "PSJ-Utility_GetAllByTypeID.md"        → utility doc (filename)
 *   - "dlg-show.md"                          → GUI doc (filename)
 * @param config - Tool configuration (paths)
 *
 * @returns Lines of the description section, or null if the file is absent.
 */
export async function readDocSection(fqName: string, config: Config): Promise<string[] | null> {
    const filePath = resolveDocPath(fqName, config);
    if (filePath === null) return null;

    // Bun.file().exists() is the idiomatic existence check — no try/catch needed
    if (!(await Bun.file(filePath).exists())) return null;

    const lines = await readLines(filePath);
    const descIdx = lines.indexOf('## Description');
    if (descIdx === -1) return null;

    return lines.slice(descIdx);
}

// ---------------------------------------------------------------------------
// Internal helpers
// ---------------------------------------------------------------------------

/**
 * Resolve the filesystem path of the markdown document for a given reference.
 *
 * Three cases:
 *
 *  1. Utility function:  `PSJ-Utility_FnName` (or full filename ending .md)
 *     → `{webRoot}/docs/psj-utility/{fqName}[.md]`
 *
 *  2. GUI / dialog:      `dlg-FnName` (or full filename ending .md)
 *     → `{webRoot}/docs/psj-gui/{fqName}[.md]`
 *
 *  3. PSJ command:       `Namespace.SubNs.FnName`
 *     → `{webRoot}/docs/psj-command/{folder}/{fqName}.md`
 *     where `folder` = first segment kebab-cased by PascalCase split
 */
function resolveDocPath(fqName: string, config: Config): string | null {
    const { webRoot } = config;

    if (fqName.includes('PSJ-Utility_')) {
        return join(webRoot, 'docs', 'psj-utility', ensureMd(fqName));
    }

    if (fqName.includes('dlg-')) {
        return join(webRoot, 'docs', 'psj-gui', ensureMd(fqName));
    }

    // PSJ command: "Measurement.Section.getArea"
    const parts = fqName.split('.');
    const firstSegment = parts[0];
    if (!firstSegment) return null;

    const folder = splitPascalCase(firstSegment);
    return join(webRoot, 'docs', 'psj-command', folder, `${fqName}.md`);
}

function ensureMd(name: string): string {
    return extname(name) === '.md' ? name : `${name}.md`;
}

/**
 * Split a PascalCase word into a kebab-case string.
 * "MeasurementSection" → "measurement-section"
 */
function splitPascalCase(word: string): string {
    return word
        .replace(/([A-Z][a-z])/g, '-$1')
        .replace(/^-/, '')
        .toLowerCase();
}
