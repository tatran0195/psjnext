/**
 * TextMate Language Definition generator for PSJ.
 */

import type { ClassTree } from '@/types/index.js';

import { ownMethods, subKeys } from '@/generators/classTreeBuilder.js';
import { parseSignature } from '@/utils.js';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Generate a psj.tmLanguage.json containing keywords for PSJ classes and methods.
 *
 * @param tree - Class tree built from PSJ commands
 */
export function generateTmLanguage(tree: ClassTree): string {
    const classNames = new Set<string>();
    const methodNames = new Set<string>();

    // Recursively collect classes and methods
    function collect(node: ClassTree) {
        for (const childKey of subKeys(node)) {
            // It's a namespace / class key
            classNames.add(childKey);

            const childNode = node[childKey];
            if (childNode && !Array.isArray(childNode) && typeof childNode === 'object') {
                collect(childNode as ClassTree);
            }
        }

        // Methods are in "own"
        const methods = ownMethods(node);
        for (const sig of methods) {
            const { fnName } = parseSignature(sig);
            methodNames.add(fnName);
        }
    }

    collect(tree);

    // Build the JSON structure
    const tmLanguage = {
        $schema: 'https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json',
        name: 'psj',
        patterns: [
            {
                include: '#classes',
            },
            {
                include: '#methods',
            },
        ],
        repository: {
            classes: {
                patterns: [
                    {
                        match: '\\b(' + Array.from(classNames).join('|') + ')\\b',
                        name: 'support.class.psj',
                    },
                ],
            },
            methods: {
                patterns: [
                    {
                        match: '\\b(' + Array.from(methodNames).join('|') + ')\\b',
                        name: 'support.function.psj',
                    },
                ],
            },
        },
        scopeName: 'source.psj',
    };

    return JSON.stringify(tmLanguage, null, 4);
}
