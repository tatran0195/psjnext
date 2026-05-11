import * as fs from 'node:fs';
import * as path from 'node:path';
import { glob } from 'tinyglobby';

// Mapping of Docusaurus admonition types to Fumadocs Callout types
const ADMONITION_TYPE_MAP: Record<string, string> = {
    note: 'info',
    tip: 'info',
    info: 'info',
    caution: 'warn',
    warning: 'warn',
    danger: 'error',
    important: 'warn',
};

/**
 * Process the content of a markdown/mdx file, replacing all Docusaurus
 * admonition blocks with Fumadocs Callout components.
 */
function processContent(content: string): { result: string; changed: boolean } {
    const admonitionBlockRegex = /^:::([\w-]+)(?:\s+(.+?))?\s*\n([\s\S]*?)^:::\s*$/gm;

    let changed = false;

    const result = content.replace(
        admonitionBlockRegex,
        (fullMatch: string, type: string, title: string | undefined, innerContent: string) => {
            const admonitionType = type.toLowerCase();

            if (!(admonitionType in ADMONITION_TYPE_MAP)) {
                console.warn(`  ⚠ Unknown admonition type: "${admonitionType}", skipping.`);
                return fullMatch;
            }

            changed = true;

            const calloutType = ADMONITION_TYPE_MAP[admonitionType];
            const trimmedContent = innerContent.trim();
            const titleAttr = title?.trim() ? ` title="${title.trim()}"` : '';

            return `<Callout type="${calloutType}"${titleAttr}>\n${trimmedContent}\n</Callout>`;
        },
    );

    return { result, changed };
}

/**
 * Process a single file.
 */
function processFile(filePath: string, dryRun: boolean = false): boolean {
    const content = fs.readFileSync(filePath, 'utf-8');
    const { result, changed } = processContent(content);

    if (!changed) {
        return false;
    }

    if (dryRun) {
        console.log(`\n--- ${filePath} (dry run) ---`);
        console.log(result);
        console.log(`--- end ---\n`);
    } else {
        fs.writeFileSync(filePath, result, 'utf-8');
    }

    return true;
}

/**
 * Main function to process all markdown files in a directory.
 */
async function main(): Promise<void> {
    const args = process.argv.slice(2);

    if (args.length === 0 || args.includes('--help')) {
        console.log(`
Usage: npx ts-node convert-admonitions.ts <path> [options]

Arguments:
  <path>        Path to a file or directory to process

Options:
  --dry-run     Preview changes without writing to files
  --ext         File extensions to process (default: md,mdx)
  --help        Show this help message

Examples:
  npx ts-node convert-admonitions.ts ./docs
  npx ts-node convert-admonitions.ts ./docs/my-file.mdx
  npx ts-node convert-admonitions.ts ./docs --dry-run
`);
        process.exit(0);
    }

    const targetPath = args[0];
    const dryRun = args.includes('--dry-run');
    const extIndex = args.indexOf('--ext');
    const extensions = extIndex !== -1 && args[extIndex + 1] ? args[extIndex + 1].split(',') : ['md', 'mdx'];

    if (!fs.existsSync(targetPath)) {
        console.error(`❌ Path not found: ${targetPath}`);
        process.exit(1);
    }

    const stats = fs.statSync(targetPath);
    let files: string[];

    if (stats.isFile()) {
        files = [targetPath];
    } else if (stats.isDirectory()) {
        const pattern = `${targetPath}/**/*.{${extensions.join(',')}}`;
        files = await glob(pattern, { onlyFiles: true });
    } else {
        console.error(`❌ Invalid path: ${targetPath}`);
        process.exit(1);
    }

    if (files.length === 0) {
        console.log('No matching files found.');
        process.exit(0);
    }

    console.log(`🔍 Found ${files.length} file(s) to process${dryRun ? ' (dry run)' : ''}...\n`);

    let changedCount = 0;
    let skippedCount = 0;

    for (const file of files) {
        const relativePath = path.relative(process.cwd(), file);
        const wasChanged = processFile(file, dryRun);

        if (wasChanged) {
            console.log(`  ✅ ${relativePath}`);
            changedCount++;
        } else {
            skippedCount++;
        }
    }

    console.log(`\n📊 Summary:`);
    console.log(`  Modified: ${changedCount}`);
    console.log(`  Skipped (no admonitions): ${skippedCount}`);
    console.log(`  Total: ${files.length}`);

    if (dryRun && changedCount > 0) {
        console.log(`\n💡 Run without --dry-run to apply changes.`);
    }
}

main();
