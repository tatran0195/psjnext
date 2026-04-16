import defaultMdxComponents from 'fumadocs-ui/mdx';
import * as FilesComponents from 'fumadocs-ui/components/files';
import * as TabsComponents from 'fumadocs-ui/components/tabs';
import type { MDXComponents } from 'mdx/types';
import { Accordion, Accordions } from 'fumadocs-ui/components/accordion';
import { ImageZoom } from 'fumadocs-ui/components/image-zoom';
import { SymbolLink } from '@/components/mdx/symbol-link';
import { RibbonPath } from '@/components/mdx/ribbon-path';

export function getMDXComponents(components?: MDXComponents) {
    return {
        ...defaultMdxComponents,
        ...TabsComponents,
        ...FilesComponents,
        Accordion,
        Accordions,
        SymbolLink,
        RibbonPath,
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
