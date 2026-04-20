/**
 * Utility.py generator.
 *
 * Generates:
 *   - Helper functions (JPT_RUN_LINE, JPT_RUN_FILE, JPT_RUN_CODE)
 *   - Enum classes for each entity type (AssociateType, BoolType, …)
 *   - The main `JPT` class with enum attributes, D_ENTITY factory methods,
 *     and all utility method stubs
 */

import type { Config, EntityEntry, UtilFunction } from '../types';

import { readDocSection } from '../collectors/docReader';
import {
    buildCursorExpansion,
    fmtArgs,
    fmtPlaceholders,
    parseSignature,
    renderCursorSetup,
} from '../utils';

// ---------------------------------------------------------------------------
// Constants mirrored from original index.ts
// ---------------------------------------------------------------------------

export const ENTITY_TYPES = [
    'AssociateType',
    'BoolType',
    'DItemType',
    'DTableType',
    'ElemKind',
    'ElemType',
    'EntityType',
    'MsgBoxType',
    'PathType',
    'SelectMethodType',
    'UnitType',
] as const;

export const D_ENTITIES = [
    'DItem',
    'DFace',
    'DBody',
    'DEdge',
    'DElem',
    'DGroup',
    'DNode',
    'VersionInfo',
    'TVector3d',
    'DItemVector',
    'BodyVector',
    'FaceVector',
    'ElemVector',
    'GroupVector',
    'NodeVector',
    'EdgeVector',
    'DItemPairVector',
] as const;

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

export interface UtilityGeneratorInput {
    entityMap: Map<string, EntityEntry[]>;
    utilFunctions: UtilFunction[];
    config: Config;
}

/**
 * Generate the full content of Utility.py.
 */
export async function generateUtility(input: UtilityGeneratorInput): Promise<string> {
    const { entityMap, utilFunctions, config } = input;
    const chunks: string[] = [];

    // Header imports + helper functions
    chunks.push(renderHeader());

    // Enum classes
    for (const entityType of ENTITY_TYPES) {
        const entries = entityMap.get(entityType) ?? [];
        chunks.push(renderEnumClass(entityType, entries));
    }

    // JPT class opening
    chunks.push('class JPT:\n');

    // Enum attribute instances
    for (const entityType of ENTITY_TYPES) {
        chunks.push(`    ${entityType} = ${entityType}()\n`);
    }
    chunks.push('\n');

    // D_ENTITY factory methods
    for (const dEntity of D_ENTITIES) {
        chunks.push(renderDEntityMethod(dEntity));
    }

    // Utility method stubs
    for (const fn of utilFunctions) {
        const methodSrc = await renderUtilMethod(fn, config);
        chunks.push(methodSrc);
    }

    return chunks.join('');
}

// ---------------------------------------------------------------------------
// Renderers
// ---------------------------------------------------------------------------

function renderHeader(): string {
    return `from jupiterutils.PSJ_Interpreter import RUN_FILE, RUN_DEBUG, RUN_CODE
import win32gui

########################################################################
# PSJ Utilities
########################################################################

def JPT_RUN_LINE(message):
    return RUN_DEBUG(message, False)

def JPT_RUN_FILE(message):
    RUN_FILE(message, False)

def JPT_RUN_CODE(message):
    RUN_CODE(message, False)

`;
}

function renderEnumClass(name: string, entries: EntityEntry[]): string {
    const lines: string[] = [`class ${name}:\n`, `    values = "JPT.${name}.values"\n`];

    for (const entry of entries) {
        lines.push(`    ${entry.varName} = ${entry.value}\n`);
    }

    lines.push('\n');
    return lines.join('');
}

function renderDEntityMethod(name: string): string {
    return `    def ${name}():\n        return "JPT.${name}()"\n\n`;
}

async function renderUtilMethod(fn: UtilFunction, config: Config): Promise<string> {
    const { fnName, params } = parseSignature(`${fn.name}(${fn.rawParams})`);
    const { cursorParams, cursorSetupLines } = buildCursorExpansion(params);

    const paramList = fn.rawParams;
    const defLine = `    def ${fnName}(${paramList}):\n`;

    // Docstring
    const docKey = `PSJ-Utility_${fnName}.md`;
    const docLines = await readDocSection(docKey, config);
    const docContent = docLines
        ? docLines.map((l) => `        ${l}`).join('\n')
        : '        To be updated';
    const docstring = `        r"""\n${docContent}\n        """\n`;

    const cursorBlock =
        cursorSetupLines.length > 0 ? renderCursorSetup(cursorSetupLines) + '\n' : '';

    const placeholders = fmtPlaceholders(cursorParams);
    const formatArgs = fmtArgs(cursorParams);
    const messageTemplate = `JPT.${fnName}(${placeholders.join(', ')})`;
    const messageLine = `        message = "${messageTemplate}".format(${formatArgs})\n`;
    const returnLine = `        return JPT_RUN_LINE(message)\n\n`;

    return defLine + docstring + cursorBlock + messageLine + returnLine;
}
