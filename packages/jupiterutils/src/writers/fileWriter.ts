/**
 * File writer utilities.
 */

import { mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Write `content` to `filePath`, creating parent directories as needed.
 *
 * Bun.write() is the idiomatic path: it auto-creates parent dirs and performs
 * an atomic rename-on-write internally on supported platforms.
 *
 * We keep an explicit mkdir for the dir in case the parent doesn't exist yet
 * (Bun.write creates the file but not always deep parent chains on all OSes).
 */
export async function writeAtomic(filePath: string, content: string): Promise<void> {
    // Bun.write() handles parent dir creation on Bun ≥1.0, but we keep mkdir
    // as a belt-and-suspenders guard for deep nested paths.
    await mkdir(dirname(filePath), { recursive: true });
    await Bun.write(filePath, content);
}

/**
 * Write multiple files concurrently.
 * Entries are `[filePath, content]` pairs.
 */
export async function writeMany(
    entries: Array<[filePath: string, content: string]>,
): Promise<void> {
    await Promise.all(entries.map(([path, content]) => writeAtomic(path, content)));
}
