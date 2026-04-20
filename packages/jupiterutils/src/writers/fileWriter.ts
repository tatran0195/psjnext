/**
 * File writer utilities.
 *
 * Provides atomic write helpers so that partially-written files are never
 * left on disk if the process crashes mid-write.
 *
 * Strategy: write to a `.tmp` sibling first, then `rename` (atomic on POSIX;
 * best-effort on Windows since Node.js uses MoveFileEx with REPLACE_EXISTING).
 */

import { randomBytes } from 'node:crypto';
import { writeFile, rename, mkdir } from 'node:fs/promises';
import { dirname, join } from 'node:path';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Write `content` to `filePath`, creating parent directories as needed.
 * The write is atomic: content is first written to a temp file in the same
 * directory, then renamed to the final path.
 */
export async function writeAtomic(filePath: string, content: string): Promise<void> {
    const dir = dirname(filePath);
    await mkdir(dir, { recursive: true });

    const tmpPath = join(dir, `.tmp-${randomBytes(6).toString('hex')}`);
    try {
        await writeFile(tmpPath, content, 'utf8');
        await rename(tmpPath, filePath);
    } catch (err) {
        // Best-effort cleanup of the temp file
        try {
            const { unlink } = await import('node:fs/promises');
            await unlink(tmpPath);
        } catch {
            // ignore cleanup failure
        }
        throw err;
    }
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
