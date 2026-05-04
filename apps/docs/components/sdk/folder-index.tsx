import { Card, Cards } from 'fumadocs-ui/components/card';
import { Box } from 'lucide-react';

import { getFirstUrl } from '@/layouts/shared';

import type * as PageTree from 'fumadocs-core/page-tree';

interface SdkFolderNode extends PageTree.Folder {
    title?: string;
    description?: string;
    icon?: React.ReactNode;
}

export function FolderIndex({ folder, resolveUrl = (u) => u }: { folder: PageTree.Folder; resolveUrl?: (url: string) => string }) {
    const parentFolder = folder as SdkFolderNode;

    return (
        <div className="space-y-8">
            <Cards>
                {parentFolder.children.map((child) => {
                    if (child.type === 'page' && child.url === parentFolder.index?.url) return null;

                    const childFolder = child as SdkFolderNode;
                    const title = childFolder.title || child.name;
                    const description = childFolder.description;
                    const icon =
                        child.type === 'folder'
                            ? childFolder.icon || <Box className="size-4" />
                            : child.icon;
                    const url =
                        child.type === 'page' ? child.url : getFirstUrl(child as PageTree.Folder);

                    if (!url) return null;

                    return (
                        <Card
                            key={child.name?.toString()}
                            title={title}
                            description={
                                description ||
                                (child.type === 'folder' ? `Browse ${title} items` : undefined)
                            }
                            href={resolveUrl(url)}
                            icon={
                                <div className="p-2 rounded-lg bg-fd-primary/10 text-fd-primary">
                                    {icon}
                                </div>
                            }
                        />
                    );
                })}
            </Cards>
        </div>
    );
}
