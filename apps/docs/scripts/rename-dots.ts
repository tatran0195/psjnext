import fs from 'node:fs';
import path from 'node:path';
import { glob } from 'tinyglobby';

/**
 * Script to rename files by replacing dots (.) with hyphens (-) in their names,
 * while preserving the file extension.
 *
 * Usage: bun scripts/rename-dots.ts [directory]
 */

async function main() {
    const args = process.argv.slice(2);
    const dryRun = args.includes('--dry-run');
    const targetDir = args.find((arg) => !arg.startsWith('-')) || '.';
    const absoluteTargetDir = path.resolve(targetDir);

    console.log(`🚀 Scanning directory: ${absoluteTargetDir}${dryRun ? ' (DRY RUN)' : ''}`);

    const files = await glob(['**/*.*'], {
        cwd: absoluteTargetDir,
        absolute: true,
        onlyFiles: true,
        // Avoid renaming the script itself and common hidden/config folders
        ignore: ['**/node_modules/**', '**/.next/**', '**/.git/**', '**/rename-dots.ts'],
    });

    let count = 0;

    for (const file of files) {
        const dir = path.dirname(file);
        const fileName = path.basename(file);

        // Skip hidden files (like .gitignore)
        if (fileName.startsWith('.')) continue;

        const ext = path.extname(file);
        const baseName = path.basename(file, ext);

        if (baseName.includes('.')) {
            const newBaseName = baseName.replace(/\./g, '-');
            const newName = newBaseName + ext;
            const newPath = path.join(dir, newName);

            if (fs.existsSync(newPath)) {
                console.warn(`⚠️ Skipping: ${newName} already exists.`);
                continue;
            }

            console.log(`${dryRun ? '[DRY RUN] Would rename' : '📝 Renaming'}: ${fileName}  ->  ${newName}`);

            if (!dryRun) {
                fs.renameSync(file, newPath);
            }
            count++;
        }
    }

    console.log(`\n✅ Finished! ${dryRun ? 'Would have renamed' : 'Renamed'} ${count} files.`);
    if (dryRun && count > 0) {
        console.log('💡 Run without --dry-run to apply changes.');
    }
}

main().catch((err) => {
    console.error('❌ Error:', err);
    process.exit(1);
});
