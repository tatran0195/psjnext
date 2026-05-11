import React from 'react';

import { type LoaderPlugin } from 'fumadocs-core/source';

import { getSection } from '@/lib/source/navigation';

import type { Folder, Node } from 'fumadocs-core/page-tree';

type FolderWithGroup = Folder & { group?: boolean };

export function pageTreeFoldersPlugin(): LoaderPlugin {
    return {
        transformPageTree: {
            folder(node, _dir, metaFile) {
                let isRoot = false;
                let isGroup = (node as FolderWithGroup).group === true;

                if (metaFile) {
                    const meta = this.storage.read(metaFile);
                    const data = meta?.data as {
                        group?: boolean;
                        root?: boolean;
                    };

                    if (data?.root === true) isRoot = true;
                    if (data?.group === true) {
                        isGroup = true;
                        (node as FolderWithGroup).group = true;
                    }
                }

                if ((node as unknown as Record<string, unknown>).root === true) isRoot = true;

                if (isRoot || isGroup) {
                    // Apply styles
                    applyFolderStyles(node, metaFile);
                }

                return node;
            },
        },
    };
}

function applyFolderStyles(node: Folder, metaFile: string | undefined) {
    const isGroup = (node as FolderWithGroup).group === true;
    const isRoot = (node as unknown as Record<string, unknown>).root === true;

    if (!isGroup && !isRoot) return;

    // Derive color from metaFile if available, fallback to extracting from url
    let pathForColor = metaFile ? metaFile : undefined;
    const folderUrl =
        (node as unknown as Record<string, unknown>).url || (node.index as unknown as Record<string, unknown>)?.url;

    if (!pathForColor && typeof folderUrl === 'string') {
        const segments = folderUrl.split('/').filter(Boolean);
        const section = segments.find((s: string) => ['api', 'guides', 'data-type', 'sdk'].includes(s));
        if (section) pathForColor = section;
    }

    const color = `var(--${getSection(pathForColor)}-color, var(--color-fd-foreground))`;

    const Box = ({ children }: { children: React.ReactNode }) => (
        <div
            className="flex items-center justify-center [&_svg]:size-[18px] rounded-none size-8 shrink-0 text-(--tab-color) bg-(--tab-color)/10 border border-(--tab-color)/20 p-1.5"
            style={{ '--tab-color': color } as object}
        >
            {children}
        </div>
    );

    if (node.icon) {
        node.icon = <Box key={node.name?.toString()}>{node.icon}</Box>;
    }

    if (isGroup) {
        const styleChildren = (nodes: Node[]) => {
            for (const child of nodes) {
                if (child.type === 'folder') {
                    if (child.icon) {
                        child.icon = <Box key={child.name?.toString()}>{child.icon}</Box>;
                    }
                    styleChildren(child.children);
                }
            }
        };
        styleChildren(node.children);
    }
}
