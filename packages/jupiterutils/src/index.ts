/**
 * psj-editor entry point.
 *
 * Pipeline:
 *
 *  1. Load config (.env)
 *  2. COLLECT
 *     a. Walk macro sources → PSJ commands
 *     b. Walk psj-utility docs → util funcs
 *     c. Walk psj-gui docs → dialog funcs
 *     d. Read input/*.txt entity type enums
 *  3. WRITE intermediate list files → output/
 *     (PSJCmdFull.py, UtilityFull.py, DlgFull.py — kept for debuggability)
 *  4. GENERATE Python source files → jupiterutils/  (live package, pip -e .)
 *     a. PSJ_Classes.py
 *     b. Utility.py
 *     c. pyjdg.py
 *     d. __init__.py
 *  5. GENERATE IDE calltip .dat files → IDEData/
 *     a. PSJCommandCalltips.dat
 *     b. PSJUtilityCalltips.dat
 *     c. PSJGuiTooltip.dat
 *  6. ZIP IDEData/*.dat → IDEData.zip
 */

import { mkdir } from 'node:fs/promises';
import { join } from 'node:path';

import type { EntityEntry } from './types/index.js';

import { readEntityType } from './collectors/entityTypeCollector.js';
import { collectPsjCommands, serializePsjCommands } from './collectors/psjCommandCollector.js';
import {
    collectUtilFunctions,
    serializeUtilFunctions,
} from './collectors/utilFunctionCollector.js';
import { loadConfig } from './config.js';
import {
    generateCommandCalltips,
    generateGuiTooltip,
    generateUtilityCalltips,
} from './generators/calltipsGenerator.js';
import { buildClassTree } from './generators/classTreeBuilder.js';
import { generateInit } from './generators/initGenerator.js';
import { generatePsjClasses } from './generators/psjClassesGenerator.js';
import { generatePyjdg } from './generators/pyjdgGenerator.js';
import { ENTITY_TYPES, generateUtility } from './generators/utilityGenerator.js';
import { logger } from './logger.js';
import { writeMany } from './writers/fileWriter.js';
import { createIdeDataZip } from './writers/zipWriter.js';

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
    // ── 1. Config ─────────────────────────────────────────────────────────────
    const config = loadConfig();
    const { projectRoot, webRoot, macroRoot } = config;

    const outputDir = join(projectRoot, 'output'); // intermediate debug files
    const inputDir = join(projectRoot, 'input'); // entity .txt + calltips base
    const pkgDir = join(projectRoot, 'jupiterutils'); // live Python package (pip -e .)
    const ideDataDir = join(projectRoot, 'IDEData'); // .dat files for IDE

    await Promise.all([
        mkdir(outputDir, { recursive: true }),
        mkdir(pkgDir, { recursive: true }),
        mkdir(ideDataDir, { recursive: true }),
    ]);

    logger.info('psj-editor starting', { webRoot, macroRoot });

    // ── 2. Collect ────────────────────────────────────────────────────────────

    logger.step('Collecting PSJ commands from macro sources…');
    const psjCommands = await collectPsjCommands(macroRoot);
    logger.ok(`Collected ${psjCommands.length} PSJ commands`);

    logger.step('Collecting PSJ-Utility functions from docs…');
    const utilityDocsDir = join(webRoot, 'docs', 'psj-utility');
    const utilFunctions = await collectUtilFunctions(utilityDocsDir, 'PSJ-Utility_');
    logger.ok(`Collected ${utilFunctions.length} utility functions`);

    logger.step('Collecting dialog functions from docs…');
    const guiDocsDir = join(webRoot, 'docs', 'psj-gui');
    const dlgFunctions = await collectUtilFunctions(guiDocsDir, 'dlg-');
    logger.ok(`Collected ${dlgFunctions.length} dialog functions`);

    logger.step('Reading entity type definitions…');
    const entityMap = new Map<string, EntityEntry[]>();
    await Promise.all(
        ENTITY_TYPES.map(async (entityType) => {
            const entries = await readEntityType(inputDir, entityType);
            if (entries !== null) entityMap.set(entityType, entries);
        }),
    );
    logger.ok(`Loaded ${entityMap.size} entity type definitions`);

    // ── 3. Intermediate list files ────────────────────────────────────────────

    logger.step('Writing intermediate list files to output/…');
    await writeMany([
        [join(outputDir, 'PSJCmdFull.py'), serializePsjCommands(psjCommands)],
        [join(outputDir, 'UtilityFull.py'), serializeUtilFunctions(utilFunctions)],
        [join(outputDir, 'DlgFull.py'), serializeUtilFunctions(dlgFunctions)],
    ]);
    logger.ok('Intermediate list files written');

    // ── 4. Generate Python source files → jupiterutils/ ──────────────────────

    logger.step('Building class tree…');
    const classTree = buildClassTree(psjCommands);

    logger.step('Generating Python source files…');
    const [psjClassesSrc, utilitySrc, pyjdgSrc] = await Promise.all([
        generatePsjClasses(classTree, config),
        generateUtility({ entityMap, utilFunctions, config }),
        generatePyjdg(dlgFunctions, config),
    ]);
    const initSrc = generateInit(classTree);

    await writeMany([
        [join(pkgDir, 'PSJ_Classes.py'), psjClassesSrc],
        [join(pkgDir, 'Utility.py'), utilitySrc],
        [join(pkgDir, 'pyjdg.py'), pyjdgSrc],
        [join(pkgDir, '__init__.py'), initSrc],
    ]);
    logger.ok('Python source files written to jupiterutils/');

    // ── 5. Generate IDE calltip .dat files → IDEData/ ────────────────────────

    logger.step('Generating IDE calltip files…');
    const [cmdCalltips, utilCalltips, guiTooltip] = await Promise.all([
        Promise.resolve(generateCommandCalltips(psjCommands)),
        generateUtilityCalltips({
            utilFunctions,
            baseCalltipsPath: join(inputDir, 'PSJUtilityCalltipsBase.dat'),
            config,
        }),
        generateGuiTooltip(dlgFunctions, config),
    ]);

    await writeMany([
        [join(ideDataDir, 'PSJCommandCalltips.dat'), cmdCalltips],
        [join(ideDataDir, 'PSJUtilityCalltips.dat'), utilCalltips],
        [join(ideDataDir, 'PSJGuiTooltip.dat'), guiTooltip],
    ]);
    logger.ok('IDE calltip files written to IDEData/');

    // ── 6. Create IDEData.zip ─────────────────────────────────────────────────

    logger.step('Creating IDEData.zip…');
    try {
        await createIdeDataZip(ideDataDir, join(projectRoot, 'IDEData.zip'));
        logger.ok('IDEData.zip created');
    } catch (err) {
        logger.warn(`Could not create IDEData.zip: ${String(err)}`);
    }

    logger.ok('✅  All done.');
}

main().catch((err) => {
    logger.error('Fatal error', err);
    process.exit(1);
});
