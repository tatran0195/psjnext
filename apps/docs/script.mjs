import fs from 'fs';
import path from 'path';

const changelogDir = path.resolve('content/changelog');
const files = fs.readdirSync(changelogDir).filter((f) => f.endsWith('.mdx'));

for (const file of files) {
    const filePath = path.join(changelogDir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    const tipRegex = /:::tip[Highlight updates]\n([\s\S]*?)\n:::/g;
    const tipRegexAlt = /:::tip[Highlight updates]([\s\S]*?)###/g; // sometimes missing ending :::

    // reset regexes just in case
    tipRegex.lastIndex = 0;

    let match = tipRegex.exec(content);
    if (!match) {
        // try to find just the start if ::: is missing, up to next ###
        // wait the tip block is standard Fumadocs, it should perfectly end with :::
    }

    if (match) {
        let block = match[1];
        const listRegex = /^[*\-]\s+(.*)$/gm;
        let itemMatch;
        const highlights = [];
        while ((itemMatch = listRegex.exec(block)) !== null) {
            highlights.push(itemMatch[1].trim());
        }

        if (highlights.length > 0) {
            content = content.replace(tipRegex, '');

            const fmRegex = /^---\n([\s\S]*?)\n---/;
            const fmMatch = fmRegex.exec(content);
            if (fmMatch) {
                const fmContent = fmMatch[1];
                let newFmContent = fmContent.trim();
                newFmContent += '\nhighlights:\n';
                highlights.forEach((h) => {
                    newFmContent += `  - ${JSON.stringify(h)}\n`;
                });

                content = content.replace(fmRegex, `---\n${newFmContent.trim()}\n---`);
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Migrated ${file} with ${highlights.length} highlights`);
            }
        }
    } else {
        // try looking for it without newlines
        // not found, skipping
        console.log(`No tip block found in ${file}`);
    }
}
