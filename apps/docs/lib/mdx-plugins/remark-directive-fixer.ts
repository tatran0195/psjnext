import { visit } from 'unist-util-visit';

import type { Paragraph, Root } from 'mdast';
import type { Transformer } from 'unified';

/**
 * Remark Plugin to transform `:::name title` into `:::name[title]`.
 * This allows `remark-directive` to correctly parse directives even without brackets.
 */
export function remarkDirectiveFixer(): Transformer<Root, Root> {
    return (tree) => {
        visit(tree, 'paragraph', (node: Paragraph) => {
            const firstChild = node.children[0];
            if (!firstChild || firstChild.type !== 'text') return;

            // Pattern: start with :::, then name, then one or more spaces.
            // We only match if it's not already using brackets.
            const match = firstChild.value.match(/^:::([a-z]+)\s+/i);
            if (!match) return;

            const nameEndIndex = match[0].length;
            if (firstChild.value[nameEndIndex] === '[') return;

            // 1. Insert '[' after ':::name '
            firstChild.value = firstChild.value.slice(0, nameEndIndex - 1) + '[' + firstChild.value.slice(nameEndIndex);

            // 2. Find the end of the first line (newline or end of paragraph) and insert ']'
            let foundNewline = false;
            for (let i = 0; i < node.children.length; i++) {
                const child = node.children[i];
                if (child.type === 'text') {
                    const newlineIndex = child.value.indexOf('\n');
                    if (newlineIndex !== -1) {
                        child.value = child.value.slice(0, newlineIndex) + ']' + child.value.slice(newlineIndex);
                        foundNewline = true;
                        break;
                    }
                }
            }

            // 3. If no newline was found, append ']' to the last child if it's text.
            if (!foundNewline) {
                const lastChild = node.children[node.children.length - 1];
                if (lastChild && lastChild.type === 'text') {
                    // Check if it ends with the closing ::: to avoid merging it into the label
                    if (lastChild.value.endsWith('\n:::')) {
                        const index = lastChild.value.lastIndexOf('\n:::');
                        lastChild.value = lastChild.value.slice(0, index) + ']' + lastChild.value.slice(index);
                    } else if (lastChild.value.endsWith(':::')) {
                        const index = lastChild.value.lastIndexOf(':::');
                        lastChild.value = lastChild.value.slice(0, index) + ']' + lastChild.value.slice(index);
                    } else {
                        lastChild.value += ']';
                    }
                }
            }
        });
    };
}
