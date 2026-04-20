/**
 * PSJ_Classes.py generator.
 *
 * Traverses the ClassTree (up to 4 namespace levels deep) and emits:
 *   - Leaf classes:    concrete Python classes with method stubs
 *   - Branch classes:  Python classes that expose sub-namespace instances
 */

import type { ClassTree, Config } from '@/types';

import { readDocSection } from '@/collectors/docReader';
import { getChild, ownMethods, subKeys } from '@/generators/classTreeBuilder';
import {
    buildCursorExpansion,
    fmtArgs,
    fmtPlaceholders,
    parseSignature,
    renderCursorSetup,
} from '@/utils';

// ---------------------------------------------------------------------------
// Header
// ---------------------------------------------------------------------------

const FILE_HEADER = `from jupiterutils.Utility import JPT_RUN_LINE
from jupiterutils.macro_defs import *
from jupiterutils.macro_material import *
from jupiterutils.macroTypes import *

########################################################################
# PSJ Classes
########################################################################

`;

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Generate the full content of PSJ_Classes.py.
 *
 * @param tree   - Class tree built from PSJ commands
 * @param config - Tool configuration (for doc resolution)
 */
export async function generatePsjClasses(tree: ClassTree, config: Config): Promise<string> {
    const chunks: string[] = [FILE_HEADER];

    const l1Keys = subKeys(tree);

    // ----- Pass 1: emit all leaf / sub-leaf classes (deepest first) -----

    for (const l1 of l1Keys) {
        const l1Node = getChild(tree, l1);
        if (!l1Node) continue;

        for (const l2 of subKeys(l1Node)) {
            const l2Node = getChild(l1Node, l2);
            if (!l2Node) continue;

            for (const l3 of subKeys(l2Node)) {
                const l3Node = getChild(l2Node, l3);
                if (!l3Node) continue;

                for (const l4 of subKeys(l3Node)) {
                    const l4Node = getChild(l3Node, l4);
                    if (!l4Node) continue;

                    // Depth-4 leaf class: class l3_l4
                    chunks.push(
                        await renderLeafClass(
                            `${l3}_${l4}`,
                            ownMethods(l4Node),
                            [l1, l2, l3, l4],
                            config,
                        ),
                    );
                }
            }
        }
    }

    // ----- Pass 2: depth-3 branch classes -----

    for (const l1 of l1Keys) {
        const l1Node = getChild(tree, l1);
        if (!l1Node) continue;

        for (const l2 of subKeys(l1Node)) {
            const l2Node = getChild(l1Node, l2);
            if (!l2Node) continue;

            for (const l3 of subKeys(l2Node)) {
                const l3Node = getChild(l2Node, l3);
                if (!l3Node) continue;

                // class l2_l3 — exposes l4 children + own methods
                chunks.push(
                    await renderBranchClass(
                        `${l2}_${l3}`,
                        l3Node,
                        ownMethods(l3Node),
                        [l1, l2, l3],
                        config,
                    ),
                );
            }
        }
    }

    // ----- Pass 3: depth-2 branch classes -----

    for (const l1 of l1Keys) {
        const l1Node = getChild(tree, l1);
        if (!l1Node) continue;

        for (const l2 of subKeys(l1Node)) {
            const l2Node = getChild(l1Node, l2);
            if (!l2Node) continue;

            // class l1_l2 — exposes l3 children + own methods
            chunks.push(
                await renderBranchClass(
                    `${l1}_${l2}`,
                    l2Node,
                    ownMethods(l2Node),
                    [l1, l2],
                    config,
                ),
            );
        }
    }

    // ----- Pass 4: top-level classes -----

    for (const l1 of l1Keys) {
        const l1Node = getChild(tree, l1);
        if (!l1Node) continue;

        chunks.push(await renderTopLevelClass(l1, l1Node, config));
    }

    return chunks.join('');
}

// ---------------------------------------------------------------------------
// Class renderers
// ---------------------------------------------------------------------------

/**
 * Render a leaf class (only "own" methods, no sub-class attributes).
 */
async function renderLeafClass(
    className: string,
    methods: string[],
    namespacePath: string[],
    config: Config,
): Promise<string> {
    if (methods.length === 0) return '';

    const lines: string[] = [`class ${className}:\n`];

    for (const sig of methods) {
        const methodSrc = await renderMethod(sig, namespacePath, config, true);
        lines.push(methodSrc);
    }

    return lines.join('') + '\n';
}

/**
 * Render a branch class: sub-class instance attributes + own methods.
 */
async function renderBranchClass(
    className: string,
    node: ClassTree,
    methods: string[],
    namespacePath: string[],
    config: Config,
): Promise<string> {
    const lines: string[] = [`class ${className}:\n`];

    // Sub-class instance attributes
    for (const childKey of subKeys(node)) {
        const parentNs = namespacePath.slice(-1)[0] ?? '';
        lines.push(`    ${childKey} = ${parentNs}_${childKey}()\n\n`);
    }

    // Own methods
    for (const sig of methods) {
        const methodSrc = await renderMethod(sig, namespacePath, config, true);
        lines.push(methodSrc);
    }

    return lines.join('') + '\n';
}

/**
 * Render a top-level class (e.g. `class Measurement:`).
 */
async function renderTopLevelClass(
    className: string,
    node: ClassTree,
    config: Config,
): Promise<string> {
    const lines: string[] = [`class ${className}:\n`];

    // Sub-namespace attributes
    for (const l2 of subKeys(node)) {
        lines.push(`    ${l2} = ${className}_${l2}()\n\n`);
    }

    // Own methods on the top-level class
    for (const sig of ownMethods(node)) {
        const methodSrc = await renderMethod(sig, [className], config, false);
        lines.push(methodSrc);
    }

    return lines.join('') + '\n';
}

// ---------------------------------------------------------------------------
// Method renderer
// ---------------------------------------------------------------------------

/**
 * Render a single Python method, including docstring and message dispatch.
 *
 * @param signature     - Raw signature string, e.g. "doThing(arg1, arg2=0)"
 * @param namespacePath - Full namespace context for building the message string
 * @param config        - Config (for doc lookup)
 * @param withSelf      - Whether to prepend `self` to the parameter list
 */
async function renderMethod(
    signature: string,
    namespacePath: string[],
    config: Config,
    withSelf: boolean,
): Promise<string> {
    const { fnName, params } = parseSignature(signature);
    const { cursorParams, cursorSetupLines } = buildCursorExpansion(params);

    const paramList = params
        .map((p) => (p.defaultValue !== null ? `${p.name}=${p.defaultValue}` : p.name))
        .join(', ');
    const selfPrefix = withSelf ? 'self, ' : '';
    const defLine = `    def ${fnName}(${selfPrefix}${paramList}):\n`;

    // Docstring
    const fqDocName = [...namespacePath, fnName].join('.');
    const docLines = await readDocSection(fqDocName, config);
    const docContent = docLines
        ? docLines.map((l) => `        ${l}`).join('\n')
        : '        To be updated';
    const docstring = `        r"""\n${docContent}\n        """\n`;

    // Cursor setup
    const cursorBlock =
        cursorSetupLines.length > 0 ? renderCursorSetup(cursorSetupLines) + '\n' : '';

    // Message string
    const nsStr = namespacePath.join('.');
    const placeholders = fmtPlaceholders(cursorParams);
    const formatArgs = fmtArgs(cursorParams);
    const messageTemplate = `${nsStr}.${fnName}(${placeholders.join(', ')})`;
    const messageLine = `        message = "${messageTemplate}".format(${formatArgs})\n`;

    const returnLine = `        return JPT_RUN_LINE(message)\n\n`;

    return defLine + docstring + cursorBlock + messageLine + returnLine;
}
