/**
 * IDEData.zip writer.
 */

import { zipSync } from 'fflate';
import { readdir } from 'node:fs/promises';
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
    const entries = await readdir(ideDataDir);
    const datFiles = entries.filter((f) => extname(f) === '.dat');

    if (datFiles.length === 0) {
        console.warn(`[zip] No .dat files found in ${ideDataDir} — skipping IDEData.zip`);
        return;
    }

    // Read all .dat files concurrently using Bun.file()
    const fileEntries = await Promise.all(
        datFiles.map(async (filename: string) => {
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
