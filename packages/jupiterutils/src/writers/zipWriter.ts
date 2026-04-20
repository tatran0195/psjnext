/**
 * IDEData.zip writer.
 *
 * Bun changes:
 *   - Replaced `archiver` (Node streams + third-party) with `fflate` —
 *     a pure-JS DEFLATE library that works seamlessly in Bun with no
 *     native bindings or stream wrappers needed.
 *   - File I/O uses Bun.file().arrayBuffer() for zero-copy reads and
 *     Bun.write() for the final zip output.
 *   - readdir replaced with Bun.readdir() (Bun ≥1.1 native).
 *   - No `node:fs` createWriteStream needed.
 *
 * Install: `bun add fflate`
 */

import { zipSync } from 'fflate';
import { extname, join } from 'node:path';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Create (or overwrite) `outputZipPath` containing every `.dat` file found
 * in `ideDataDir`.
 *
 * @param ideDataDir    - Directory containing the .dat files
 * @param outputZipPath - Destination zip file path
 */
export async function createIdeDataZip(ideDataDir: string, outputZipPath: string): Promise<void> {
    const entries = await Bun.readdir(ideDataDir);
    const datFiles = entries.filter((f) => extname(f) === '.dat');

    if (datFiles.length === 0) {
        console.warn(`[zip] No .dat files found in ${ideDataDir} — skipping IDEData.zip`);
        return;
    }

    // Read all .dat files concurrently using Bun.file()
    const fileEntries = await Promise.all(
        datFiles.map(async (filename) => {
            const bytes = await Bun.file(join(ideDataDir, filename)).arrayBuffer();
            return [filename, new Uint8Array(bytes)] as const;
        }),
    );

    // Build the zip synchronously — fflate's zipSync is fast enough for .dat files
    const zipInput: Record<string, Uint8Array> = Object.fromEntries(fileEntries);
    const zipped = zipSync(zipInput, { level: 9 });

    await Bun.write(outputZipPath, zipped);

    console.log(`[zip] Created ${outputZipPath} (${datFiles.length} .dat files)`);
}
