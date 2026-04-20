/**
 * __init__.py generator.
 *
 * Generates the jupiterutils package __init__.py that re-exports all
 * top-level classes from PSJ_Classes.py plus the standard utility modules.
 */

import type { ClassTree } from '../types';

import { subKeys } from './classTreeBuilder';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Generate the content of __init__.py.
 *
 * @param tree - Class tree (used to enumerate top-level class names)
 */
export function generateInit(tree: ClassTree): string {
    const parentClasses = subKeys(tree);

    const importLines = [
        'from jupiterutils.Utility import JPT, JPT_RUN_LINE, JPT_RUN_FILE, JPT_RUN_CODE',
        'from jupiterutils.macro_defs import *',
        'from jupiterutils.macro_material import *',
        'from jupiterutils.macroTypes import *',
        'from jupiterutils.table_material import *',
        'from jupiterutils.pyjdg import *',
        'from jupiterutils.macro_mesh_cleanup import *',
        'from jupiterutils.FileMenu import *',
        'from jupiterutils.LabPreRelease import *',
    ];

    // Build the multi-class import from PSJ_Classes
    const classImportItems = parentClasses.join(', ');
    importLines.push(`from jupiterutils.PSJ_Classes import (${classImportItems})`);

    return importLines.join('\n') + '\n';
}
