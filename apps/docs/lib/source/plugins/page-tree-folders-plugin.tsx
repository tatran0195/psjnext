import { type LoaderPlugin } from 'fumadocs-core/source';

import { getSection } from '@/lib/source/navigation';

import type { Folder } from 'fumadocs-core/page-tree';

type FolderWithGroup = Folder & { group?: boolean };

export function pageTreeFoldersPlugin(): LoaderPlugin {
    return {
        transformPageTree: {
            folder(node, _dir, metaFile) {
                let isGroup = false;
                let isRoot = false;

                if (metaFile) {
                    const meta = this.storage.read(metaFile);
                    const data = meta?.data as { group?: boolean; root?: boolean };
                    if (data?.group === true) isGroup = true;
                    if (data?.root === true) isRoot = true;
                }

                if ((node as FolderWithGroup).group === true) isGroup = true;
                if ((node as unknown as Record<string, unknown>).root === true) isRoot = true;

                if (isGroup || isRoot) {
                    if (isGroup) {
                        (node as FolderWithGroup).group = true;
                    }

                    // Derive color from metaFile if available, fallback to extracting from url
                    let pathForColor = metaFile ? metaFile : undefined;
                    const folderUrl =
                        ((node as unknown as Record<string, unknown>).url as string | undefined) ||
                        node.index?.url;
                    if (!pathForColor && folderUrl) {
                        const segments = folderUrl.split('/').filter(Boolean);
                        const section = segments.find((s: string) =>
                            ['api', 'guides', 'data-type'].includes(s),
                        );
                        if (section) pathForColor = section;
                    }

                    const color = `var(--${getSection(pathForColor)}-color, var(--color-fd-foreground))`;

                    const Box = ({ children }: { children: React.ReactNode }) => (
                        <div
                            className="flex items-center justify-center [&_svg]:size-[18px] rounded-lg size-8 shrink-0 text-(--tab-color) bg-(--tab-color)/10 border border-(--tab-color)/20 p-1.5"
                            style={{ '--tab-color': color } as object}
                        >
                            {children}
                        </div>
                    );

                    if (node.icon) {
                        node.icon = <Box key={node.name?.toString()}>{node.icon}</Box>;
                    }

                    // Apply the same themed box to immediate children ONLY if it's a grouped node (populates nestedTabs)
                    if (isGroup) {
                        for (const child of node.children) {
                            if (child.type === 'folder' && child.icon) {
                                child.icon = <Box key={child.name?.toString()}>{child.icon}</Box>;
                            }
                        }
                    }
                }
                return node;
            },
        },
    };
}
