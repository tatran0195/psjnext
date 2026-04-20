/**
 * Entity type collector.
 */

import { join } from 'node:path';

import type { EntityEntry } from '@/types';

import { readLines } from '@/utils';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Read and parse an entity-type file from `inputDir/<fileType>.txt`.
 * Returns null if the file does not exist.
 */
export async function readEntityType(
    inputDir: string,
    fileType: string,
): Promise<EntityEntry[] | null> {
    const filePath = join(inputDir, `${fileType}.txt`);

    if (!(await Bun.file(filePath).exists())) return null;

    const lines = await readLines(filePath);
    return lines
        .map((line) => line.trim())
        .filter((line) => line.length > 0)
        .map(parseEntityLine)
        .filter((e): e is EntityEntry => e !== null);
}

// ---------------------------------------------------------------------------
// Internal
// ---------------------------------------------------------------------------

/**
 * Parse a single line like "3: JPT.EntityType.BODY"
 * → { varName: "BODY", value: "3" }
 */
function parseEntityLine(line: string): EntityEntry | null {
    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) return null;

    const value = line.slice(0, colonIdx).trim();
    const rest = line.slice(colonIdx + 1).trim(); // "JPT.EntityType.BODY"
    const lastDot = rest.lastIndexOf('.');
    if (lastDot === -1) return null;

    const varName = rest.slice(lastDot + 1).trim();
    if (!varName) return null;

    return { varName, value };
}
