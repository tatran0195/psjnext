import { ReactNode } from 'react';

import { Archive, Tag } from 'lucide-react';

import { env } from '@/env';
import { getVersionStatus, semverGte } from '@/lib/api-versions';
import { getApiVersions } from '@/lib/source';

import type { StructuredData } from 'fumadocs-core/mdx-plugins';
import type * as PageTree from 'fumadocs-core/page-tree';
import type { LoaderPlugin } from 'fumadocs-core/source';

interface FolderNode extends PageTree.Folder {
    group?: boolean;
    groupType?: 'stacked' | 'tabs';
    groupOrder?: number;
}

export interface VersionedPageFrontmatter {
    title: string;
    description?: string;
    since?: string;
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

/**
 * Resolve sidebar icon and label for a version by its position in API_VERSIONS.
 * idx === 0  → latest  → Tag icon     + "Latest"
 * idx  > 0  → archive → Archive icon + "Version X.Y"
 */
function _resolveVersionMeta(idx: number): { icon: ReactNode | string; description: string } {
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
function installVersionedGetters(
    originalData: Record<string, unknown>,
    loadFn: (() => Promise<Record<string, unknown>>) | undefined,
    fixedVersion?: string
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
                const versionedMap = (exports?.versionedStructuredData ?? mod.versionedStructuredData) as
                    | Record<string, StructuredData>
                    | undefined;
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

    if (loadFn) {
        Object.defineProperty(originalData, 'load', {
            value: async function (this: Record<string, unknown>) {
                const result = await loadFn();
                const version = fixedVersion ?? (this._version as string);
                if (!version) return result;

                const exports = (result._exports ?? result) as Record<string, unknown>;
                const versionedMap = exports.versionedStructuredData as Record<string, StructuredData> | undefined;

                if (versionedMap?.[version] && Array.isArray(result.toc)) {
                    const validIds = new Set(versionedMap[version]!.headings.map((h) => h.id));
                    return {
                        ...result,
                        toc: (result.toc as { url: string }[]).filter((item) => {
                            const id = item.url.startsWith('#') ? item.url.slice(1) : item.url;
                            return validIds.has(id);
                        }),
                    };
                }
                return result;
            },
            configurable: true,
            enumerable: false,
            writable: true,
        });
    }
}

const API_VERSIONS = env.API_VERSIONS;

export function versionPlugin(): LoaderPlugin {
    const isMultiVersion = API_VERSIONS.length > 1;
    const SEMVER_SEGMENT_RE = /^api\/\d+\.\d+/;

    return {
        name: 'fumadocs:api-versions',
        enforce: 'post',

        transformStorage({ storage }) {
            const apiFiles = storage.getFiles().filter((f) => f.startsWith('api/'));
            // ── Pre-flight: already-versioned folder layout ──────────────────
            // If api/ already contains semver subfolders (api/5.2.0/…), the
            // content was authored pre-versioned. Skip fan-out entirely to
            // avoid double-nesting and redundant getter installation.
            if (apiFiles.some((f) => SEMVER_SEGMENT_RE.test(f))) return;

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

                    installVersionedGetters(
                        originalData,
                        originalData.load as (() => Promise<Record<string, unknown>>) | undefined,
                        API_VERSIONS[0] // fixed: single version, no shell prototype chain
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
                const loadFn = originalData.load as (() => Promise<Record<string, unknown>>) | undefined;

                for (const version of API_VERSIONS) {
                    const status = getVersionStatus(version, fm.since, fm.deprecated, fm.removed);

                    if (!isPageVisible(status)) continue;

                    const storageKey = `api/${version}/${filePath.replace(/^api\//, '')}`;
                    const slugs = storageKey.replace(/\.mdx?$/, '').split('/');

                    const versionedData = {
                        ...originalData,
                        _version: version,
                        _status: status,
                    } as typeof originalData;

                    installVersionedGetters(versionedData, loadFn, version);

                    storage.write(storageKey, {
                        ...file,
                        path: file.path,
                        slugs,
                        data: versionedData as typeof file.data,
                    });
                }

                storage.delete(filePath);
            }
        },

        transformPageTree: {
            root(node) {
                if (!isMultiVersion) return node;

                const apiFolderIdx = node.children.findIndex(
                    (n): n is PageTree.Folder => n.type === 'folder' && nodeStoragePath(n).toLowerCase() === 'api'
                );
                if (apiFolderIdx === -1) return node;

                const apiFolder = node.children[apiFolderIdx] as PageTree.Folder;
                const versions = getApiVersions();

                const versionedChildren: PageTree.Node[] = apiFolder.children
                    .filter((child): child is PageTree.Folder => {
                        if (child.type !== 'folder') return false;
                        const storagePath = nodeStoragePath(child);
                        const segment = storagePath.split('/').pop() ?? '';
                        return (API_VERSIONS as readonly string[]).includes(segment);
                    })
                    .sort((a, b) => {
                        const versionA = typeof a.name === 'string' ? a.name : '';
                        const versionB = typeof b.name === 'string' ? b.name : '';
                        return semverGte(versionA, versionB) ? -1 : 1;
                    })
                    .map((child, _idx) => {
                        const versionMeta = versions.find((v) => v.value === child.name);
                        return {
                            ...child,
                            defaultOpen: false,
                            description: versionMeta?.releasedAt ?? 'Unreleased',
                            group: true,
                            type: 'folder',
                            groupType: 'stacked',
                            groupOrder: 1,
                            icon: <Tag />,
                        };
                    });

                const newApiFolder: FolderNode & { root: true } = {
                    ...apiFolder,
                    children: versionedChildren,
                    root: true,
                    group: true,
                    groupType: 'tabs',
                    groupOrder: 0,
                };

                const newChildren = [...node.children];
                newChildren[apiFolderIdx] = newApiFolder;
                return { ...node, children: newChildren };
            },
        },
    };
}
