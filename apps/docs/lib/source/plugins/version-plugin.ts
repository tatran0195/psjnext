// lib/source/plugins/version-plugin.ts
import { API_VERSIONS, getVersionStatus } from '@/lib/api-versions';

import type * as PageTree from 'fumadocs-core/page-tree';
import type { LoaderPlugin } from 'fumadocs-core/source';

// ─── Public types ─────────────────────────────────────────────────────────────

export interface VersionedPageFrontmatter {
    title: string;
    description?: string;
    /** Version the page / param was introduced in, e.g. "5.1.0" */
    introduced?: string;
    /** Version the page / param was deprecated in */
    deprecated?: string;
    /** Version the page / param was removed in */
    removed?: string;
    ribbon?: string;
}

// ─── Internal helpers ─────────────────────────────────────────────────────────

type VersionStatus = 'available' | 'deprecated' | 'removed' | 'unavailable';

/**
 * A page is visible for a given version when its status is NOT 'unavailable'
 * (not yet introduced) AND NOT 'removed' (past removal point).
 *
 * Note: 'deprecated' pages ARE still visible — they are rendered with a
 * deprecation indicator but are not hidden.
 */
function isPageVisible(status: VersionStatus): boolean {
    return status !== 'unavailable' && status !== 'removed';
}

// ─── Plugin ───────────────────────────────────────────────────────────────────

/**
 * Versioned API docs plugin.
 *
 * ## Strategy
 *
 * ### `transformStorage`
 * For every file under `app/`, the plugin:
 *  1. Checks the page-level frontmatter (`introduced`, `deprecated`, `removed`)
 *     against every known API version.
 *  2. For each version where the page is visible, writes a cloned virtual file
 *     at `app/<version>/…` with `_version` and `_status` baked into its data.
 *  3. Deletes the original unversioned file to prevent it from appearing in the
 *     tree or search index.
 *
 * Input-parameter filtering (params annotated with `@since`/`@removed`) is
 * handled at the MDX level by `remarkParamGaterV11`; the version plugin does
 * not need to replicate that logic.
 *
 * ### `transformPageTree`
 * After the builder resolves the full page tree the plugin:
 *  1. Locates the top-level `app` folder.
 *  2. Strips any page whose `_status === 'removed'` from the tree (belt-and-
 *     suspenders guard — storage deletion should already prevent these).
 *  3. Returns the cleaned folder structure.
 */
export function versionPlugin(): LoaderPlugin {
    return {
        name: 'fumadocs:api-versions',

        // ── Storage transformation ─────────────────────────────────────────────
        transformStorage({ storage }) {
            const apiFiles = storage.getFiles().filter((f) => f.startsWith('app/'));

            for (const filePath of apiFiles) {
                const file = storage.read(filePath);
                if (!file || file.format !== 'page') continue;

                // Skip virtual files that already carry a version tag (idempotency).
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

                    // Only materialise the page for versions where it is visible.
                    if (!isPageVisible(status)) continue;

                    // e.g. "app/foo.mdx" → "app/5.2.0/foo.mdx"
                    const suffix = filePath.replace(/^app\//, '');
                    const versionedPath = `app/${version}/${suffix}`;
                    const versionedSlugs = versionedPath.replace(/\.mdx?$/, '').split('/');

                    const cloned: typeof file = {
                        ...file,
                        path: versionedPath,
                        slugs: versionedSlugs,
                        data: {
                            ...(file.data as Record<string, unknown>),
                            // Attach version context so page.tsx / remark plugins can read it.
                            _version: version,
                            _status: status,
                        } as typeof file.data,
                    };

                    storage.write(versionedPath, cloned);
                }

                // Remove the original unversioned file so it won't appear in the
                // page tree or be indexed by the search engine.
                storage.delete(filePath);
            }
        },

        // ── Page tree transformation ───────────────────────────────────────────
        transformPageTree: {
            /**
             * The `root` hook fires after the builder has resolved the full tree.
             * At this point `app/<version>/…` sub-folders are already built by the
             * normal builder.  We clean up any stray removed pages and ensure each
             * version sub-folder is properly configured.
             */
            root(node) {
                // Locate the top-level "app" folder.
                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder =>
                        n.type === 'folder' &&
                        typeof n.name === 'string' &&
                        n.name.toLowerCase() === 'app',
                );
                if (apiFolderIdx === -1) return node;

                const apiFolder = node.children[apiFolderIdx] as PageTree.Folder;

                // Access storage to double-check page status at tree-build time.
                const storage = (this as { storage?: unknown }).storage as
                    | { read: (path: string) => { format: string; data: Record<string, unknown> } | null }
                    | undefined;

                /**
                 * Recursively filter a tree node:
                 *  - Folders: filter children recursively.
                 *  - Pages: exclude removed pages (belt-and-suspenders).
                 *  - Separators: pass through.
                 */
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
                            // Strip locale prefix like "en:" from the id.
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

                // Each direct child of the api folder should be a version sub-folder.
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
