import { API_VERSIONS, getVersionStatus } from '@/lib/api-versions';

import type { StructuredData } from 'fumadocs-core/mdx-plugins';
import type * as PageTree from 'fumadocs-core/page-tree';
import type { LoaderPlugin } from 'fumadocs-core/source';

export interface VersionedPageFrontmatter {
    title: string;
    description?: string;
    introduced?: string;
    deprecated?: string;
    removed?: string;
    ribbon?: string;
}

type VersionStatus = 'available' | 'deprecated' | 'removed' | 'unavailable';

function isPageVisible(status: VersionStatus): boolean {
    return status !== 'unavailable' && status !== 'removed';
}

const EMPTY_STRUCTURED_DATA: StructuredData = { headings: [], contents: [] };

/**
 * Extract the raw storage path from a node's $id.
 * generateId() produces "[locale:]storagePath" — strip the locale prefix if present.
 * nodeStoragePath({ $id: 'en:app/v1' }) // 'app/v1'
 * nodeStoragePath({ $id: 'app/v1' }) // 'app/v1'
 */
function nodeStoragePath(node: { $id?: string }): string {
    const id = node.$id ?? '';
    const colonIdx = id.indexOf(':');
    return colonIdx !== -1 ? id.slice(colonIdx + 1) : id;
}

export function versionPlugin(): LoaderPlugin {
    return {
        name: 'fumadocs:api-versions',

        transformStorage({ storage }) {
            const apiFiles = storage.getFiles().filter((f) => f.startsWith('app/'));

            for (const filePath of apiFiles) {
                const file = storage.read(filePath);
                if (!file) continue;

                // ── Meta files (meta.json / meta.yaml) ──────────────────────────
                if (file.format === 'meta') {
                    const segments = filePath.split('/');
                    if (segments.length !== 3) continue; // skip app/meta.json

                    for (const version of API_VERSIONS) {
                        const versionedKey = `app/${version}/${segments[1]}/meta.json`;
                        storage.write(versionedKey, {
                            ...file,
                            path: file.path, // keep original path
                            absolutePath: undefined, // cleared, not real file
                        });
                    }

                    storage.delete(filePath);
                    continue;
                }

                // ── Page files (.mdx / .md) ──────────────────────────────────────
                if (file.format !== 'page') continue;

                const data = file.data as Record<string, unknown>;
                if (data._version) continue;

                const fm = file.data as VersionedPageFrontmatter;
                const originalData = file.data as Record<string, unknown>;
                const loadFn = originalData.load as
                    | (() => Promise<Record<string, unknown>>)
                    | undefined;

                Object.defineProperty(originalData, 'structuredData', {
                    get(this: Record<string, unknown>) {
                        const version = this._version as string | undefined;
                        return async (): Promise<StructuredData> => {
                            if (!loadFn) return EMPTY_STRUCTURED_DATA;
                            let mod: Record<string, unknown>;
                            try {
                                mod = await loadFn();
                            } catch {
                                return EMPTY_STRUCTURED_DATA;
                            }
                            const exports = mod._exports as Record<string, unknown> | undefined;
                            const versionedMap = (exports?.versionedStructuredData ??
                                mod.versionedStructuredData) as
                                | Record<string, StructuredData>
                                | undefined;
                            return (
                                versionedMap?.[version ?? ''] ??
                                (mod.structuredData as StructuredData | undefined) ??
                                EMPTY_STRUCTURED_DATA
                            );
                        };
                    },
                    configurable: true,
                    enumerable: false,
                });

                for (const version of API_VERSIONS) {
                    const status = getVersionStatus(
                        version,
                        fm.introduced,
                        fm.deprecated,
                        fm.removed,
                    );

                    if (!isPageVisible(status)) continue;

                    const storageKey = `app/${version}/${filePath.replace(/^app\//, '')}`;
                    const slugs = storageKey.replace(/\.mdx?$/, '').split('/');

                    storage.write(storageKey, {
                        ...file,
                        path: file.path,
                        slugs,
                        data: Object.assign(Object.create(originalData), {
                            _version: version,
                            _status: status,
                        }) as typeof file.data,
                    });
                }

                storage.delete(filePath);
            }
        },

        transformPageTree: {
            root(node) {
                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder =>
                        n.type === 'folder' && nodeStoragePath(n).toLowerCase() === 'app',
                );
                if (apiFolderIdx === -1) return node;

                const apiFolder = node.children[apiFolderIdx] as PageTree.Folder;

                const versionedChildren: PageTree.Node[] = apiFolder.children
                    .filter((child): child is PageTree.Folder => {
                        if (child.type !== 'folder') return false;
                        const storagePath = nodeStoragePath(child);
                        const segment = storagePath.split('/').pop() ?? '';
                        return (API_VERSIONS as readonly string[]).includes(segment);
                    })
                    .map((child) => ({
                        ...child,
                        defaultOpen: false,
                        group: true,
                    }));

                const newApiFolder: PageTree.Folder & { root: true; group: true } = {
                    ...apiFolder,
                    children: versionedChildren,
                    root: true,
                    group: true,
                };

                const newChildren = [...node.children];
                newChildren[apiFolderIdx] = newApiFolder;
                return { ...node, children: newChildren };
            },
        },
    };
}
