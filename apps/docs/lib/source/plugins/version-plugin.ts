import { StructuredData } from 'fumadocs-core/mdx-plugins';

// lib/source/plugins/version-plugin.ts
import { API_VERSIONS, getVersionStatus } from '@/lib/api-versions';

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

export function versionPlugin(): LoaderPlugin {
    return {
        name: 'fumadocs:api-versions',
        enforce: 'pre',

        transformStorage({ storage }) {
            const apiFiles = storage.getFiles().filter((f) => f.startsWith('app/'));

            for (const filePath of apiFiles) {
                const file = storage.read(filePath);
                if (!file || file.format !== 'page') continue;

                const data = file.data as Record<string, unknown>;
                if (data._version) continue;

                const fm = file.data as VersionedPageFrontmatter;

                for (const version of API_VERSIONS) {
                    const status = getVersionStatus(
                        version,
                        fm.introduced,
                        fm.deprecated,
                        fm.removed,
                    );

                    if (!isPageVisible(status)) continue;

                    const suffix = filePath.replace(/^app\//, '');
                    const versionedPath = `app/${version}/${suffix}`;
                    const versionedSlugs = versionedPath.replace(/\.mdx?$/, '').split('/');

                    const capturedVersion = version;
                    const originalData = file.data as Record<string, unknown>;

                    const cloned: typeof file = {
                        ...file,
                        path: versionedPath,
                        slugs: versionedSlugs,
                        data: {
                            ...originalData,
                            _version: capturedVersion,
                            _status: status,

                            structuredData: async (): Promise<StructuredData> => {
                                const mod = await (
                                    originalData.load as
                                        | (() => Promise<Record<string, unknown>>)
                                        | undefined
                                )?.();
                                const versionedMap = ((
                                    mod?._exports as Record<string, unknown> | undefined
                                )?.versionedStructuredData ?? mod?.versionedStructuredData) as
                                    | Record<string, StructuredData>
                                    | undefined;

                                return (
                                    versionedMap?.[capturedVersion] ??
                                    (mod?.structuredData as StructuredData | undefined) ?? {
                                        headings: [],
                                        contents: [],
                                    }
                                );
                            },
                        } as typeof file.data,
                    };

                    storage.write(versionedPath, cloned);
                }

                storage.delete(filePath);
            }
        },

        transformPageTree: {
            root(node) {
                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder =>
                        n.type === 'folder' &&
                        typeof n.name === 'string' &&
                        n.name.toLowerCase() === 'app',
                );
                if (apiFolderIdx === -1) return node;

                const apiFolder = node.children[apiFolderIdx] as PageTree.Folder;

                const storage = (this as { storage?: unknown }).storage as
                    | {
                          read: (
                              path: string,
                          ) => { format: string; data: Record<string, unknown> } | null;
                      }
                    | undefined;

                const filterNode = (n: PageTree.Node): PageTree.Node | undefined => {
                    if (n.type === 'folder') {
                        const filtered = n.children
                            .map(filterNode)
                            .filter((child): child is PageTree.Node => child !== undefined);
                        return { ...n, children: filtered };
                    }

                    if (n.type === 'page' && storage) {
                        const id = (n as { $id?: string }).$id;
                        if (id) {
                            const filePath = id.replace(/^[a-z]{2}:/, '');
                            const file = storage.read(filePath);
                            if (file?.format === 'page') {
                                const status = file.data._status as string | undefined;
                                if (status === 'removed') return undefined;
                            }
                        }
                    }

                    return n;
                };

                const versionedChildren: PageTree.Node[] = apiFolder.children
                    .filter(
                        (child): child is PageTree.Folder =>
                            child.type === 'folder' &&
                            typeof child.name === 'string' &&
                            (API_VERSIONS as readonly string[]).includes(child.name),
                    )
                    .map((child) => {
                        const filtered = filterNode(child);
                        if (!filtered || filtered.type !== 'folder') return child;
                        return {
                            ...filtered,
                            name: child.name,
                            defaultOpen: false,
                        } satisfies PageTree.Folder;
                    });

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
