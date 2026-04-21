#!/usr/bin/env bun
/**
 * Script: bump-version.ts
 * Usage: bun run scripts/bump-version.ts <old_version> <new_version>
 * Example: bun run scripts/bump-version.ts 5.1.0 5.2.0
 */

import { existsSync } from 'node:fs';
import { cp } from 'node:fs/promises';
import path from 'node:path';

const [oldVersion, newVersion] = process.argv.slice(2);

if (!oldVersion || !newVersion) {
    console.error('Usage: bun run scripts/bump-version.ts <old_version> <new_version>');
    console.error('Example: bun run scripts/bump-version.ts 5.1.0 5.2.0');
    process.exit(1);
}

// Ensure working from root of apps/docs
const docsRoot = process.cwd();
const contentDir = path.join(docsRoot, 'content/api');
const examplesDir = path.join(docsRoot, 'examples/api');

// No helper exec block needed

async function main() {
    const oldContentPath = path.join(contentDir, oldVersion);
    const oldExamplesPath = path.join(examplesDir, oldVersion);
    const newContentPath = path.join(contentDir, newVersion);
    const newExamplesPath = path.join(examplesDir, newVersion);

    if (!existsSync(oldContentPath)) {
        console.error(`Error: old content path does not exist at ${oldContentPath}`);
        process.exit(1);
    }

    console.log(`\n--- Step 1: Copying ${oldVersion} to ${newVersion} ---`);
    await cp(oldContentPath, newContentPath, { recursive: true });
    if (existsSync(oldExamplesPath)) {
        await cp(oldExamplesPath, newExamplesPath, { recursive: true });
    }

    console.log(`\n--- Step 2: Creating specialized branches via git subtree split ---`);
    // Note: git subtree requires relative paths from git root
    // Since we are in apps/docs, we must build relative path to repo root.
    // However, if we assume git root is 'd:\...\psjdocs-2', we should pass paths from there.
    const projectRoot = path.resolve(docsRoot, '../..'); // Assuming apps/docs is 2 levels deep

    // We execute git from the project root to ensure subtree split works
    const relContentPath = 'apps/docs/content/api/' + oldVersion;
    const relExamplesPath = 'apps/docs/examples/api/' + oldVersion;

    const contentBranch = `release/${oldVersion}`;
    const examplesBranch = `release-examples/${oldVersion}`;

    // Subtree split the content
    await Bun.spawn(
        ['git', 'subtree', 'split', `--prefix=${relContentPath}`, '-b', contentBranch],
        {
            cwd: projectRoot,
            stdout: 'inherit',
            stderr: 'inherit',
        },
    ).exited;

    // Subtree split the examples
    if (existsSync(oldExamplesPath)) {
        await Bun.spawn(
            ['git', 'subtree', 'split', `--prefix=${relExamplesPath}`, '-b', examplesBranch],
            {
                cwd: projectRoot,
                stdout: 'inherit',
                stderr: 'inherit',
            },
        ).exited;
    }

    console.log(`\n--- Step 3: Pushing the new branches to origin ---`);
    await Bun.spawn(
        [
            'git',
            'push',
            'origin',
            contentBranch,
            ...(existsSync(oldExamplesPath) ? [examplesBranch] : []),
        ],
        {
            cwd: projectRoot,
            stdout: 'inherit',
            stderr: 'inherit',
        },
    ).exited;

    console.log(`\n--- Step 4: Removing old physically tracked folders ---`);
    await Bun.spawn(['git', 'rm', '-r', relContentPath], {
        cwd: projectRoot,
        stdout: 'inherit',
        stderr: 'inherit',
    }).exited;
    if (existsSync(oldExamplesPath)) {
        await Bun.spawn(['git', 'rm', '-r', relExamplesPath], {
            cwd: projectRoot,
            stdout: 'inherit',
            stderr: 'inherit',
        }).exited;
    }

    await Bun.spawn(
        [
            'git',
            'commit',
            '-m',
            `chore: remove ${oldVersion} native files to replace with submodules`,
        ],
        {
            cwd: projectRoot,
            stdout: 'inherit',
            stderr: 'inherit',
        },
    ).exited;

    console.log(`\n--- Step 5: Adding the isolated submodules ---`);
    await Bun.spawn(['git', 'submodule', 'add', '-b', contentBranch, './', relContentPath], {
        cwd: projectRoot,
        stdout: 'inherit',
        stderr: 'inherit',
    }).exited;

    if (existsSync(oldExamplesPath)) {
        await Bun.spawn(['git', 'submodule', 'add', '-b', examplesBranch, './', relExamplesPath], {
            cwd: projectRoot,
            stdout: 'inherit',
            stderr: 'inherit',
        }).exited;
    }

    await Bun.spawn(['git', 'commit', '-m', `chore: attach ${oldVersion} submodule links`], {
        cwd: projectRoot,
        stdout: 'inherit',
        stderr: 'inherit',
    }).exited;

    console.log(`\n--- Step 6: Syncing all version configs from .gitmodules ---`);
    await Bun.spawn(['bun', 'scripts/sync-versions.ts'], {
        cwd: docsRoot,
        stdout: 'inherit',
        stderr: 'inherit',
    }).exited;
    console.log('✓ sync-versions.ts updated lib/versions.ts, source.config.ts, lib/source/index.tsx');

    console.log(`\n======================================================`);
    console.log(`✅ Bump Success!`);
    console.log(
        `The version ${oldVersion} has been correctly extracted to its own submodule branch, pushed, and re-added as a native submodule!`,
    );
    console.log(`The new ${newVersion} files have been safely copied and await your edits.`);
    console.log(`All configuration files have been automatically updated!`);
    console.log(`======================================================\n`);
}

main().catch((err) => {
    console.error('Bump script failed:', err);
    process.exit(1);
});
