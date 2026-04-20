/**
 * pyjdg.py generator.
 *
 * Generates the JDGCreator class with all dialog method stubs,
 * plus the spin / size_behavior enums.
 */

import type { Config, UtilFunction } from '../types';

import { readDocSection } from '../collectors/docReader';
import {
    buildCursorExpansion,
    fmtArgs,
    fmtPlaceholders,
    parseSignature,
    renderCursorSetup,
} from '../utils';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Generate the full content of pyjdg.py.
 */
export async function generatePyjdg(dlgFunctions: UtilFunction[], config: Config): Promise<string> {
    const chunks: string[] = [];

    chunks.push(renderHeader());

    for (const fn of dlgFunctions) {
        const methodSrc = await renderDlgMethod(fn, config);
        chunks.push(methodSrc);
    }

    return chunks.join('');
}

// ---------------------------------------------------------------------------
// Renderers
// ---------------------------------------------------------------------------

function renderHeader(): string {
    return `from jupiterutils.Utility import JPT_RUN_LINE, JPT_RUN_CODE
from enum import Enum

class spin(Enum):
    integer = 0
    double = 1

class size_behavior(Enum):
    greedy = 0
    vertical = 1
    horizontal = 4
    fixed = 5

class JDGCreator:
    def __init__(self, title, resizable, validation):
        JPT_RUN_CODE("from pyjdg import *")
        message = "dlg=JDGCreator(title='{}',resizable={},validation={})".format(title, resizable, validation)
        JPT_RUN_CODE(message)

`;
}

async function renderDlgMethod(fn: UtilFunction, config: Config): Promise<string> {
    const { fnName, params } = parseSignature(`${fn.name}(${fn.rawParams})`);
    const { cursorParams, cursorSetupLines } = buildCursorExpansion(params);

    const paramList = fn.rawParams ? `self, ${fn.rawParams}` : 'self';
    const defLine = `    def ${fnName}(${paramList}):\n`;

    // Docstring
    const docKey = `dlg-${fnName}.md`;
    const docLines = await readDocSection(docKey, config);
    const docContent = docLines
        ? docLines.map((l) => `        ${l}`).join('\n')
        : '        To be updated';
    const docstring = `        r"""\n${docContent}\n        """\n`;

    const cursorBlock =
        cursorSetupLines.length > 0 ? renderCursorSetup(cursorSetupLines) + '\n' : '';

    const placeholders = fmtPlaceholders(cursorParams);
    const formatArgs = fmtArgs(cursorParams);
    const messageTemplate = `dlg.${fnName}(${placeholders.join(', ')})`;
    const messageLine = `        message = "${messageTemplate}".format(${formatArgs})\n`;
    const returnLine = `        JPT_RUN_LINE(message)\n\n`;

    return defLine + docstring + cursorBlock + messageLine + returnLine;
}
