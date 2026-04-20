/**
 * IDE calltip .dat file generators.
 *
 * Produces three IDE data files:
 *   PSJCommandCalltips.dat  — one entry per PSJ command API function
 *   PSJUtilityCalltips.dat  — one entry per JPT utility function
 *   PSJGuiTooltip.dat       — one entry per dialog function
 */

import { readFile } from 'node:fs/promises';

import type { Config, PsjCommand, UtilFunction } from '../types';

import { readDocSection } from '../collectors/docReader';

const SEPARATOR_CMD = '--------------------------------------------------------------------------';
const SEPARATOR_DLG = '------------------------------------------------------------';

// ---------------------------------------------------------------------------
// PSJCommandCalltips.dat
// ---------------------------------------------------------------------------

/**
 * Generate PSJCommandCalltips.dat content.
 *
 * Format per entry:
 *   Function: Ns.Sub.FnName()
 *   <separator>
 */
export function generateCommandCalltips(commands: PsjCommand[]): string {
    const lines: string[] = [
        `////////////////////////////////////////////////////////////////////////////////////////////////////////////`,
        `// `,
        `//    PSJ Command calltips (${commands.length} API functions) `,
        `//  `,
        `///////////////////////////////////////////////////////////////////////////////////////////////////////////`,
    ];

    for (const cmd of commands) {
        const { namespace, signature } = cmd;

        // Derive the clean function name (strip params) for the calltip header
        const parenIdx = signature.indexOf('(');
        const fnName = parenIdx === -1 ? signature : signature.slice(0, parenIdx);
        const fqName = [...namespace, `${fnName}()`].join('.');

        lines.push(`Function: ${fqName}`);
        lines.push(SEPARATOR_CMD);
    }

    return lines.join('\n') + '\n';
}

// ---------------------------------------------------------------------------
// PSJUtilityCalltips.dat
// ---------------------------------------------------------------------------

export interface UtilityCalltipsInput {
    utilFunctions: UtilFunction[];
    baseCalltipsPath: string;
    config: Config;
}

/**
 * Generate PSJUtilityCalltips.dat content (async — reads doc sections).
 */
export async function generateUtilityCalltips(input: UtilityCalltipsInput): Promise<string> {
    const { utilFunctions, baseCalltipsPath, config } = input;

    // Read the base class documentation block
    let baseContent = '';
    try {
        baseContent = await readFile(baseCalltipsPath, 'utf8');
    } catch {
        // base file is optional
    }

    const lines: string[] = [
        `////////////////////////////////////////////////////////////////////////////////////////////////////////////`,
        `// `,
        `//  #PSJ Utility calltips (${utilFunctions.length} API functions) `,
        `//  #Base class: DItem`,
        `//  #Child classes: DFace, DBody, DEdge, DNode, DGroup, DElem, DCoord, DLoadBC, DConnect, DItemPair...`,
        `//  #List classes: DItemVector, BodyVector, NodeVector, ElemVector, `,
        `//  FaceVector, EdgeVector, GroupVector, ConnectVector, CoordVector, LoadBCVector, DItemPairVector,... `,
        `//  #Param types: DTableType, EntityType (DItemType), UnitType, `,
        `//  ElemType, ElemKind, BoolType, PathType, AssociateType, ...`,
        `//  #Debugger: JPT.Debugger() ,JPT.PrintAppPathInfo(), print()`,
        `//  `,
        `///////////////////////////////////////////////////////////////////////////////////////////////////////////`,
        baseContent.trim(),
        '',
    ];

    for (const fn of utilFunctions) {
        const docKey = `PSJ-Utility_${fn.name}.md`;
        const docLines = await readDocSection(docKey, config);

        const docBlock = docLines
            ? docLines
                  .map((l) => (l.startsWith('## ') ? l.replace('## ', '').concat(':') : l))
                  .slice(0, 30)
                  .concat('Read more in document...')
                  .join('\n')
            : 'To be updated\nRead more in document...';

        lines.push(`Function: JPT.${fn.name}`);
        lines.push(docBlock);
        lines.push(SEPARATOR_CMD);
    }

    return lines.join('\n') + '\n';
}

// ---------------------------------------------------------------------------
// PSJGuiTooltip.dat
// ---------------------------------------------------------------------------

/**
 * Generate PSJGuiTooltip.dat content (async — reads doc sections).
 */
export async function generateGuiTooltip(
    dlgFunctions: UtilFunction[],
    config: Config,
): Promise<string> {
    const lines: string[] = [
        `////////////////////////////////////////////////////////////////////////////////////////////////////////////`,
        `// `,
        `//  #PSJ GUI calltips (${dlgFunctions.length} API functions) `,
        `//  `,
        `///////////////////////////////////////////////////////////////////////////////////////////////////////////`,
    ];

    for (const fn of dlgFunctions) {
        const docKey = `dlg-${fn.name}.md`;
        const docLines = await readDocSection(docKey, config);

        const docBlock = docLines
            ? docLines
                  .map((l) => (l.startsWith('## ') ? l.replace('## ', '').concat(':') : l))
                  .slice(0, 30)
                  .concat('Read more in document...')
                  .join('\n')
            : 'To be updated\nRead more in document...';

        lines.push(`Function: dlg.${fn.name}`);
        lines.push(docBlock);
        lines.push(SEPARATOR_DLG);
    }

    return lines.join('\n') + '\n';
}
