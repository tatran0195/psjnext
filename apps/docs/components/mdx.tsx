import * as Twoslash from 'fumadocs-twoslash/ui';
import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';
import { Banner } from 'fumadocs-ui/components/banner';
import * as FilesComponents from 'fumadocs-ui/components/files';
import { ImageZoom } from 'fumadocs-ui/components/image-zoom';
import * as TabsComponents from 'fumadocs-ui/components/tabs';
import { TypeTable } from 'fumadocs-ui/components/type-table';
import defaultMdxComponents from 'fumadocs-ui/mdx';

import { LinkPreview } from './mdx/link-preview';
import { Mermaid } from './mdx/mermaid';
import { RibbonPath } from './mdx/ribbon-path';
import { SymbolLink } from './mdx/symbol-link';
import { Video } from './mdx/video';

import type { MDXComponents } from 'mdx/types';

export function getMDXComponents(components?: MDXComponents) {
    return {
        ...defaultMdxComponents,
        ...TabsComponents,
        ...FilesComponents,
        ...Twoslash,
        Accordion,
        Accordions,
        RibbonPath,
        Banner,
        Mermaid,
        TypeTable,
        SymbolLink,
        LinkPreview,
        Video,
        // oxlint-disable-next-line typescript/no-explicit-any
        img: (props: any) => {
            const isGif =
                typeof props.src === 'string'
                    ? props.src.split('?')[0].endsWith('.gif')
                    : typeof props.src === 'object' &&
                      (props.src.src || props.src.default?.src)?.split('?')[0].endsWith('.gif');

            return <ImageZoom {...props} unoptimized={isGif || props.unoptimized} priority />;
        },
        ...components,
    } satisfies MDXComponents;
}

export const useMDXComponents = getMDXComponents;

declare global {
    type MDXProvidedComponents = ReturnType<typeof getMDXComponents>;
}
