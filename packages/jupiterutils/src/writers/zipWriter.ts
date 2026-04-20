/**
 * IDEData.zip writer.
 *
 * Replaces the `7z.exe` call in the original Makefile.
 * Uses the `archiver` package to create a zip archive of all .dat files
 * in the IDEData directory.
 */

import { createWriteStream } from 'node:fs';
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
    // Dynamic import so the module is optional at type-check time
    const mod = await import('archiver');
    const archiver = (mod as unknown as { default: typeof mod }).default ?? mod;

    const entries = await readdir(ideDataDir);
    const datFiles = entries.filter((f) => extname(f) === '.dat');

    if (datFiles.length === 0) {
        console.warn(`[zip] No .dat files found in ${ideDataDir} — skipping IDEData.zip`);
        return;
    }

    await new Promise<void>((resolve, reject) => {
        const output = createWriteStream(outputZipPath);
        const archive = archiver('zip', { zlib: { level: 9 } });

        output.on('close', resolve);
        output.on('error', reject);
        archive.on('error', reject);

        archive.pipe(output);

        for (const file of datFiles) {
            archive.file(join(ideDataDir, file), { name: file });
        }

        archive.finalize();
    });

    console.log(`[zip] Created ${outputZipPath} (${datFiles.length} .dat files)`);
}
