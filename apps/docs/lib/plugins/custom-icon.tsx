import { Icons } from '@/components/icons';

import type { LoaderPlugin } from 'fumadocs-core/source';

export function customIconsPlugin(): LoaderPlugin {
    return {
        transformPageTree: {
            file(node) {
                if (!node.icon || typeof node.icon !== 'string') return node;

                const Icon = Icons[node.icon as keyof typeof Icons];
                if (!Icon) return node;

                return {
                    ...node,
                    icon: <Icon className="size-4" />,
                };
            },

            folder(node, _dir, metaFile) {
                let iconName = node.icon;

                if (!iconName && metaFile) {
                    const meta = this.storage.read(metaFile);
                    if (meta?.data?.icon) {
                        iconName = meta.data.icon;
                    }
                }

                if (!iconName || typeof iconName !== 'string') return node;

                const Icon = Icons[iconName as keyof typeof Icons];
                if (!Icon) return node;

                return {
                    ...node,
                    icon: <Icon className="size-4" />,
                };
            },
        },
    };
}
