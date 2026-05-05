// lib/version-plugin.ts
import { API_VERSIONS, getVersionStatus, isVisible } from '@/lib/api-versions';

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

/**
 * Versioned API docs plugin.
 *
 * Strategy:
 * 1. `transformStorage` — for every file under `api/`, write N cloned virtual
 *    files at `api/<version>/…` with the version baked into the slugs.
 *    The original `api/…` files are deleted so they don't appear in the tree.
 * 2. `transformPageTree.root` — after the builder runs, reorganise the top-level
 *    api folder children into per-version sub-folders.
 */
export function versionPlugin(): LoaderPlugin {
    return {
        name: 'fumadocs:api-versions',

        transformStorage({ storage }) {
            const apiFiles = storage.getFiles().filter((f) => f.startsWith('app/'));

            for (const filePath of apiFiles) {
                const file = storage.read(filePath);
                if (!file || file.format !== 'page') continue;

                // Do not re-process virtual files that already have a version attached
                const data = file.data as unknown as Record<string, unknown>;
                if (data._version) continue;

                const fm = file.data as VersionedPageFrontmatter;

                for (const version of API_VERSIONS) {
                    const status = getVersionStatus(
                        version,
                        fm.introduced,
                        fm.deprecated,
                        fm.removed,
                    );
                    if (!isVisible(status)) continue;

                    // e.g. api/foo.mdx → api/5.1.0/foo  (slugs: ['api','5.1.0','foo'])
                    const suffix = filePath.replace(/^app\//, ''); // e.g. "foo.mdx" or "group/bar.mdx"
                    const versionedPath = `app/${version}/${suffix}`;

                    // Derive slugs from versioned path instead of empty originalSlugs
                    const versionedSlugs = versionedPath.replace(/\.mdx?$/, '').split('/');

                    const cloned: typeof file = {
                        ...file,
                        path: versionedPath,
                        slugs: versionedSlugs,
                        data: {
                            ...(file.data as Record<string, unknown>),
                            // Attach version context so page.tsx can read it without parsing the URL
                            _version: version,
                            _status: status,
                        } as any,
                    };

                    storage.write(versionedPath, cloned);
                }

                // Remove the original unversioned file so it won't appear in the tree
                storage.delete(filePath);
            }
        },

        transformPageTree: {
            // The `root` hook fires after the builder has resolved the entire tree.
            // At this point `api/<version>/…` folders are already built correctly
            // by the normal builder — we just need to give each version folder a
            // clean label and mark removed pages inside them.
            root(node) {
                // Find the api folder in the tree children
                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder =>
                        n.type === 'folder' &&
                        typeof n.name === 'string' &&
                        n.name.toLowerCase() === 'app',
                );
                if (apiFolderIdx === -1) return node;

                const apiFolder = node.children[apiFolderIdx] as PageTree.Folder;

                // We need storage to check for page status
                const storage = (this as { storage?: any }).storage;

                const filterNode = (n: PageTree.Node): PageTree.Node | undefined => {
                    if (n.type === 'folder') {
                        return {
                            ...n,
                            children: n.children
                                .map(filterNode)
                                .filter((child): child is PageTree.Node => child !== undefined),
                        };
                    }

                    if (n.type === 'page' && storage) {
                        const id = (n as { $id?: string }).$id;
                        if (id && id.includes('app/')) {
                            const filePath = id.replace(/^[a-z]{2}:/, '');
                            const file = storage.read(filePath);

                            if (file && file.format === 'page') {
                                const status = (file.data as { _status?: string })._status;
                                if (status === 'removed') return undefined;
                            }
                        }
                    }

                    return n;
                };

                // Each direct child of the api folder is a version sub-folder
                // (the builder already named them from the directory name)
                const versionedChildren: PageTree.Node[] = apiFolder.children
                    .filter(
                        (child): child is PageTree.Folder =>
                            child.type === 'folder' &&
                            typeof child.name === 'string' &&
                            API_VERSIONS.includes(child.name as (typeof API_VERSIONS)[number]),
                    )
                    .map((child) => {
                        const filtered = filterNode(child);
                        if (!filtered || filtered.type !== 'folder') return child;

                        return {
                            ...filtered,
                            name: `${child.name}`,
                            // Mark the folder as a sidebar root so it collapses independently
                            defaultOpen: false,
                        } satisfies PageTree.Folder;
                    });

                const newApiFolder: PageTree.Folder = {
                    ...apiFolder,
                    children: versionedChildren,
                };

                const newChildren = [...node.children];
                newChildren[apiFolderIdx] = newApiFolder;
                return { ...node, children: newChildren };
            },
        },
    };
}
