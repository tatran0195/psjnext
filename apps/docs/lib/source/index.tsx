import { apiDocs as _, docs } from 'collections/server';
import {
    type InferMetaType,
    type InferPageType,
    type LoaderPlugin,
    MetaData,
    loader,
} from 'fumadocs-core/source';
import { lucideIconsPlugin } from 'fumadocs-core/source/lucide-icons';
// import { openapi } from '@/lib/openapi';

import { i18n } from '@/lib/i18n';
import { getSection } from '@/lib/source/navigation';
import { Folder } from 'fumadocs-core/page-tree';

export const source = loader({
    source: docs.toFumadocsSource(),
    i18n,
    baseUrl: '/',
    plugins: [lucideIconsPlugin(), pageTreeCodeTitles(), pageTreeFolders()],
});

function pageTreeFolders(): LoaderPlugin {
    return {
        transformPageTree: {
            folder(node, _dir, metaFile) {
                if (metaFile) {
                    const meta = this.storage.read(metaFile);
                    const data = meta?.data as MetaData & { group?: boolean };

                    if (data?.group === true) {
                        (node as Folder & { group?: boolean }).group = true;
                    }

                    if (node.icon) {
                        const color = `var(--${getSection(meta?.path)}-color, var(--color-fd-foreground))`;
                        node.icon = (
                            <div
                                key={node.name?.toString()}
                                className="[&_svg]:size-[18px] rounded-lg size-xs text-(--tab-color) max-md:bg-(--tab-color)/10 max-md:border max-md:p-1.5"
                                style={
                                    {
                                        '--tab-color': color,
                                    } as object
                                }
                            >
                                {node.icon}
                            </div>
                        );
                    }
                }
                return node;
            },
        },
    };
}

function pageTreeCodeTitles(): LoaderPlugin {
    return {
        transformPageTree: {
            file(node) {
                if (
                    typeof node.name === 'string' &&
                    (node.name.endsWith('()') || node.name.match(/^<\w+ \/>$/))
                ) {
                    return {
                        ...node,
                        name: (
                            <code key="0" className="text-[0.8125rem]">
                                {node.name}
                            </code>
                        ),
                    };
                }
                return node;
            },
        },
    };
}

export type Page = InferPageType<typeof source>;
export type Meta = InferMetaType<typeof source>;
