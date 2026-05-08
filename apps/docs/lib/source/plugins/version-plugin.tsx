import { ReactNode } from 'react';

import { Archive, Tag } from 'lucide-react';

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
 * nodeStoragePath({ $id: 'en:api/v1' }) // 'api/v1'
 * nodeStoragePath({ $id: 'api/v1' }) // 'api/v1'
 */
function nodeStoragePath(node: { $id?: string }): string {
    const id = node.$id ?? '';
    const colonIdx = id.indexOf(':');
    return colonIdx !== -1 ? id.slice(colonIdx + 1) : id;
}

// const Box = ({ children, color }: { children: React.ReactNode; color: string }) => (
//     <div
//         className="flex items-center justify-center [&_svg]:size-[18px] rounded-lg size-8 shrink-0 text-(--tab-color) bg-(--tab-color)/10 border border-(--tab-color)/20 p-1.5"
//         style={{ '--tab-color': color } as object}
//     >
//         {children}
//     </div>
// );

/**
 * Resolve sidebar icon and label for a version by its position in API_VERSIONS.
 * idx === 0  → latest  → Tag icon     + "Latest"
 * idx  > 0  → archive → Archive icon + "Version X.Y"
 */
function resolveVersionMeta(idx: number): { icon: ReactNode | string; description: string } {
    return idx === 0
        ? {
              icon: <Tag />,
              description: 'Latest',
          }
        : {
              icon: <Archive />,
              description: `Version ${API_VERSIONS[idx]?.split('.').slice(0, 2).join('.')}`,
          };
}

/**
 * Install a version-aware structuredData getter on a page data object.
 *
 * fumadocs' buildIndexDefault checks:
 *   typeof page.data.structuredData === 'function'
 *     ? await page.data.structuredData()
 *     : page.data.structuredData
 *
 * Multi-version: installed on `originalData` which is the prototype for every
 * versioned shell. `this._version` resolves to the shell's own property at
 * call time, giving each shell its own correct versionedStructuredData slice.
 *
 * Single-version: installed directly on the file's data object with a fixed
 * `version` captured in the closure (API_VERSIONS[0]). `this._version` is
 * never consulted. This ensures pages with @removed params (e.g. bIsMergePart
 * @removed:5.2.0) are excluded from search even when only one version exists.
 */
function installStructuredDataGetter(
    originalData: Record<string, unknown>,
    loadFn: (() => Promise<Record<string, unknown>>) | undefined,
    fixedVersion?: string,
): void {
    Object.defineProperty(originalData, 'structuredData', {
        get(this: Record<string, unknown>) {
            // Multi-version: read from the versioned shell's own property.
            // Single-version: use the fixed version captured in the closure.
            const version = fixedVersion ?? (this._version as string);
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
                    mod.versionedStructuredData) as Record<string, StructuredData> | undefined;
                // Fall back to the plain structuredData export for pages that
                // have no @since/@removed annotations and no versionedStructuredData.
                return (
                    versionedMap?.[version] ??
                    (mod.structuredData as StructuredData | undefined) ??
                    EMPTY_STRUCTURED_DATA
                );
            };
        },
        configurable: true,
        enumerable: false,
    });
}

export function versionPlugin(): LoaderPlugin {
    const isMultiVersion = API_VERSIONS.length > 1;

    return {
        name: 'fumadocs:api-versions',
        enforce: 'pre',

        transformStorage({ storage }) {
            const apiFiles = storage.getFiles().filter((f) => f.startsWith('api/'));

            // ── Single-version path ──────────────────────────────────────────────
            // No file fan-out, no deletions, no new storage keys. We only install
            // the structuredData getter with a fixed version so that
            // versionedStructuredData[API_VERSIONS[0]] is used for search indexing
            // rather than the version-blind plain structuredData export.
            if (!isMultiVersion) {
                for (const filePath of apiFiles) {
                    const file = storage.read(filePath);
                    if (!file || file.format !== 'page') continue;

                    const originalData = file.data as Record<string, unknown>;
                    if (originalData._version) continue;

                    installStructuredDataGetter(
                        originalData,
                        originalData.load as (() => Promise<Record<string, unknown>>) | undefined,
                        API_VERSIONS[0], // fixed: single version, no shell prototype chain
                    );
                }
                return;
            }

            // ── Multi-version path ───────────────────────────────────────────────
            for (const filePath of apiFiles) {
                const file = storage.read(filePath);
                if (!file) continue;

                // ── Meta files (meta.json / meta.yaml) ──────────────────────────
                if (file.format === 'meta') {
                    const segments = filePath.split('/');
                    if (segments.length !== 3) continue; // only api/<dir>/meta.json

                    for (const version of API_VERSIONS) {
                        const versionedKey = `api/${version}/${segments[1]}/meta.json`;
                        storage.write(versionedKey, {
                            ...file,
                            path: file.path,
                            absolutePath: undefined,
                        });
                    }

                    storage.delete(filePath);
                    continue;
                }

                // ── Page files (.mdx / .md) ──────────────────────────────────────
                if (file.format !== 'page') continue;

                const originalData = file.data as Record<string, unknown>;
                if (originalData._version) continue;

                const fm = file.data as VersionedPageFrontmatter;
                const loadFn = originalData.load as
                    | (() => Promise<Record<string, unknown>>)
                    | undefined;

                // No fixedVersion — getter reads this._version from the shell
                // at call time, giving each version its own structured data slice.
                installStructuredDataGetter(originalData, loadFn);

                for (const version of API_VERSIONS) {
                    const status = getVersionStatus(
                        version,
                        fm.introduced,
                        fm.deprecated,
                        fm.removed,
                    );

                    if (!isPageVisible(status)) continue;

                    const storageKey = `api/${version}/${filePath.replace(/^api\//, '')}`;
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
                if (!isMultiVersion) return node;

                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder =>
                        n.type === 'folder' && nodeStoragePath(n).toLowerCase() === 'api',
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
                    .map((child, idx) => ({
                        ...child,
                        defaultOpen: false,
                        group: true,
                        type: 'folder',
                        ...resolveVersionMeta(idx),
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
