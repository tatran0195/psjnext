import { load } from 'js-yaml';
import * as fs from 'node:fs/promises';
import * as path from 'node:path';

import type { ItemFile, JCallManifest, LoadedSDK, ParamGroupFile } from './types';

// ─── Individual file loaders ─────────────────────────────────────────────────

async function parseYaml<T>(filePath: string): Promise<T> {
    const content = await fs.readFile(filePath, 'utf-8');
    return load(content) as T;
}

export async function loadManifest(manifestPath: string): Promise<JCallManifest> {
    return parseYaml<JCallManifest>(manifestPath);
}

export async function loadGroup(filePath: string): Promise<ParamGroupFile> {
    return parseYaml<ParamGroupFile>(filePath);
}

export async function loadItem(filePath: string): Promise<ItemFile> {
    return parseYaml<ItemFile>(filePath);
}

// ─── Full SDK loader ──────────────────────────────────────────────────────────

/**
 * Loads the full SDK from a root manifest file.
 * Discovers groups in `_groups/*.yaml` and items in `<domain>/*.yaml`
 * relative to the manifest directory.
 */
export async function loadSDK(manifestPath: string): Promise<LoadedSDK> {
    const manifest = await loadManifest(manifestPath);
    const root = path.dirname(manifestPath);

    const groups = new Map<string, ParamGroupFile>();
    const items = new Map<string, ItemFile>();

    // Load param groups
    const groupsDir = path.join(root, '_groups');
    const groupFiles = await safeReadDir(groupsDir);
    await Promise.all(
        groupFiles
            .filter((f) => f.endsWith('.yaml') || f.endsWith('.yml'))
            .map(async (f) => {
                const group = await loadGroup(path.join(groupsDir, f));
                groups.set(group.id, group);
            }),
    );

    // Load items from each known domain directory
    const domainIds = manifest.domains.map((d) => d.id);
    await Promise.all(
        domainIds.map(async (domainId) => {
            const domainDir = path.join(root, domainId);
            const itemFiles = await safeReadDir(domainDir);
            await Promise.all(
                itemFiles
                    .filter((f) => f.endsWith('.yaml') || f.endsWith('.yml'))
                    .map(async (f) => {
                        const item = await loadItem(path.join(domainDir, f));
                        items.set(item.id, item);
                    }),
            );
        }),
    );

    return { manifest, groups, items, rootDir: root };
}

/**
 * Loads a fully-supplied raw SDK (no file I/O).
 * Useful for programmatic / in-memory usage.
 */
export function loadSDKFromRaw(
    manifest: JCallManifest,
    groupList: ParamGroupFile[],
    itemList: ItemFile[],
): LoadedSDK {
    const groups = new Map(groupList.map((g) => [g.id, g]));
    const items = new Map(itemList.map((i) => [i.id, i]));
    return { manifest, groups, items };
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

async function safeReadDir(dir: string): Promise<string[]> {
    try {
        return await fs.readdir(dir);
    } catch {
        return [];
    }
}
