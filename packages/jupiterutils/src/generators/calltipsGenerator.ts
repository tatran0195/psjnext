/**
 * IDE calltip .dat file generators.
 */

import type { Config, PsjCommand, UtilFunction } from '@/types';

import { readDocSection } from '@/collectors/docReader';

const SEPARATOR_CMD = '--------------------------------------------------------------------------';
const SEPARATOR_DLG = '------------------------------------------------------------';

// ---------------------------------------------------------------------------
// PSJCommandCalltips.dat
// ---------------------------------------------------------------------------

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

export async function generateUtilityCalltips(input: UtilityCalltipsInput): Promise<string> {
    const { utilFunctions, baseCalltipsPath, config } = input;

    // Bun.file().text() replaces readFile(path, 'utf8')
    let baseContent = '';
    try {
        baseContent = await Bun.file(baseCalltipsPath).text();
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
