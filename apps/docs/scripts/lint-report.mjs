import { spawnSync } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import path from 'node:path';

/**
 * Runs markdownlint-cli2 and converts the output to a Markdown table.
 */
function generateLintReport() {
    console.log('Running markdownlint...');
    
    // Run markdownlint-cli2. It usually exits with code 1 if errors are found.
    // We capture stderr where the errors are typically reported.
    const result = spawnSync('bunx', ['markdownlint-cli2', 'content/**/*.{md,mdx}'], {
        encoding: 'utf-8',
        shell: true,
    });

    const output = result.stderr || result.stdout;
    const lines = output.split('\n');
    
    const errors = [];
    // Regex to match markdownlint output format:
    // content/path/to/file.md:line:col [optional-column] MDXXX/rule-name Description
    // Some versions or outputs include the word "error" after the line/col.
    const errorRegex = /^(.*?):(\d+)(?::(\d+))?\s+(?:error\s+)?(MD\d+\/[^\s]+)\s+(.*)$/;

    for (const line of lines) {
        const match = line.match(errorRegex);
        if (match) {
            const [_, filePath, lineNum, colNum, rule, description] = match;
            errors.push({
                file: filePath,
                line: lineNum,
                column: colNum || '-',
                rule: rule,
                description: description
            });
        }
    }

    if (errors.length === 0) {
        console.log('No linting errors found!');
        writeFileSync('lint-report.md', '# Markdown Lint Report\n\n✅ No errors found.');
        return;
    }

    // Generate Markdown Table
    let markdown = '# Markdown Lint Report\n\n';
    markdown += `Total Errors: ${errors.length}\n\n`;
    markdown += '| File | Line | Col | Rule | Description |\n';
    markdown += '| :--- | :--- | :-- | :--- | :---------- |\n';

    for (const err of errors) {
        const fileLink = `[${path.basename(err.file)}](${err.file})`;
        markdown += `| ${fileLink} | ${err.line} | ${err.column} | \`${err.rule}\` | ${err.description} |\n`;
    }

    writeFileSync('lint-report.md', markdown);
    console.log(`Report generated: lint-report.md (${errors.length} errors)`);
}

generateLintReport();
