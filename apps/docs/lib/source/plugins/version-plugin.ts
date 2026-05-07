import type { StructuredData } from 'fumadocs-core/mdx-plugins';
import type * as PageTree from 'fumadocs-core/page-tree';
import type { LoaderPlugin } from 'fumadocs-core/source';

// lib/source/plugins/version-plugin.ts
import { API_VERSIONS, getVersionStatus } from '@/lib/api-versions';

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

// Extract the raw folder path segment from a node's $id.
// generateId() produces: "[locale:]folderPath" — strip the locale prefix if present.
// e.g. "en:app/v1" → "app/v1",  "app/v1" → "app/v1"
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
                if (!file || file.format !== 'page') continue;

                const data = file.data as Record<string, unknown>;
                if (data._version) continue;

                const fm = file.data as VersionedPageFrontmatter;
                const originalData = file.data as Record<string, unknown>;
                const loadFn = originalData.load as
                    | (() => Promise<Record<string, unknown>>)
                    | undefined;

                // One getter on the prototype shared by all versioned entries.
                // `this` at call time is the versioned data object, so
                // `this._version` resolves to the correct version without
                // any per-version closure.
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
                            const versionedMap = (
                                exports?.versionedStructuredData ?? mod.versionedStructuredData
                            ) as Record<string, StructuredData> | undefined;
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

                    // Storage key is versioned so each version gets a distinct
                    // entry in the FileSystem map and appears as a separate node
                    // in the page tree under its version folder.
                    const storageKey = `app/${version}/${filePath.replace(/^app\//, '')}`;

                    // Slugs drive url() — encode the version segment so the
                    // loader produces the correct versioned href.
                    const slugs = storageKey.replace(/\.mdx?$/, '').split('/');

                    storage.write(storageKey, {
                        ...file,
                        // file.path stays as the original MDX path.
                        // getPageByHref() uses path.dirname(page.path) for
                        // relative link resolution — must not be the storage key.
                        path: file.path,
                        slugs,
                        // Versioned data shell: only _version and _status are
                        // own properties. Everything else — title, description,
                        // load, structuredData (getter), icon — resolves through
                        // the prototype chain to originalData. Zero data copying.
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
                // Locate the "app" folder by its raw storage path in $id,
                // not by node.name. The builder runs pathToName() on the folder
                // segment ("app" → "App"), so name-based matching is unreliable.
                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder =>
                        n.type === 'folder' && nodeStoragePath(n).toLowerCase() === 'app',
                );
                if (apiFolderIdx === -1) return node;

                const apiFolder = node.children[apiFolderIdx] as PageTree.Folder;

                // Pick version sub-folders by their raw storage path segment.
                // e.g. $id "app/v1" → last segment "v1" → matches API_VERSIONS.
                // node.name would be "V1" after pathToName() — never matches.
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

                // Removed pages are never written to storage, so no filterNode
                // pass is needed — they simply don't appear in the tree.

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
