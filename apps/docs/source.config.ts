import type { RemarkAutoTypeTableOptions } from 'fumadocs-typescript';

import {
    RehypeCodeOptions,
    remarkDirectiveAdmonition,
    remarkMdxMermaid,
} from 'fumadocs-core/mdx-plugins';
import { applyMdxPreset, defineCollections, defineConfig, defineDocs } from 'fumadocs-mdx/config';
import jsonSchema from 'fumadocs-mdx/plugins/json-schema';
import lastModified from 'fumadocs-mdx/plugins/last-modified';
import rehypePrettyCode from 'rehype-pretty-code';
import { z } from 'zod';

import { remarkVersionGateParams } from '@/lib/mdx-plugins/remark-version-gate-params';

import { transformers } from './lib/highlight-code';
import { remarkElementIds } from './lib/mdx-plugins/remark-element-ids';
import { remarkLinkPreview } from './lib/mdx-plugins/remark-link-preview';
import { defaultShikiOptions } from './lib/shiki';
import { docsSchema, metaSchemaWithGroup } from './lib/source/schema';

import type { ElementContent } from 'hast';
import type { ShikiTransformer } from 'shiki';
const { rehypeCodeDefaultOptions } = await import('fumadocs-core/mdx-plugins/rehype-code');
const { remarkSteps } = await import('fumadocs-core/mdx-plugins/remark-steps');
const { transformerTwoslash } = await import('fumadocs-twoslash');
const { createFileSystemTypesCache } = await import('fumadocs-twoslash/cache-fs');
const { default: remarkMath } = await import('remark-math');
const { remarkTypeScriptToJavaScript } = await import('fumadocs-docgen/remark-ts2js');
const { default: rehypeKatex } = await import('rehype-katex');
const { remarkAutoTypeTable, createGenerator, createFileSystemGeneratorCache } =
    await import('fumadocs-typescript');

const isLint = process.env.LINT === '1';

export const docs = defineDocs({
    docs: {
        schema: docsSchema,
        postprocess: {
            includeProcessedMarkdown: true,
            extractLinkReferences: true,
            valueToExport: ['elementIds', 'paramMeta'],
        },
        async: true,
        async mdxOptions(environment) {
            const typeTableOptions: RemarkAutoTypeTableOptions = {
                generator: createGenerator({
                    cache: createFileSystemGeneratorCache('.next/fumadocs-typescript'),
                }),
                shiki: defaultShikiOptions,
            };
            return applyMdxPreset({
                rehypeCodeOptions: isLint
                    ? false
                    : ({
                          inline: 'tailing-curly-colon',
                          themes: {
                              light: 'catppuccin-latte',
                              dark: 'catppuccin-mocha',
                          },
                          transformers: [
                              ...(rehypeCodeDefaultOptions.transformers ?? []),
                              transformerTwoslash({
                                  typesCache: createFileSystemTypesCache(),
                                  twoslashOptions: {
                                      compilerOptions: {
                                          types: ['@types/node'],
                                      },
                                  },
                              }),
                              transformerEscape(),
                          ],
                          lazy: false,
                          langs: ['js', 'jsx', 'ts', 'tsx', 'py', 'shell', 'bat', 'python'],
                          langAlias: {
                              psj: 'py',
                          },
                      } satisfies RehypeCodeOptions),
                remarkCodeTabOptions: {
                    parseMdx: true,
                },
                remarkStructureOptions: {
                    stringify: {
                        filterElement(node) {
                            switch (node.type) {
                                case 'mdxJsxFlowElement':
                                case 'mdxJsxTextElement':
                                    switch (node.name) {
                                        case 'File':
                                        case 'TypeTable':
                                        case 'Callout':
                                        case 'Card':
                                        case 'Custom':
                                        case 'ParamSection':
                                            return true;
                                    }
                                    return 'children-only';
                            }

                            return true;
                        },
                    },
                },
                remarkNpmOptions: {
                    persist: {
                        id: 'package-manager',
                    },
                },
                remarkPlugins: isLint
                    ? [remarkElementIds]
                    : [
                          remarkVersionGateParams,
                          remarkSteps,
                          remarkMath,
                          remarkMdxMermaid,
                          remarkLinkPreview,
                          remarkDirectiveAdmonition,
                          [remarkAutoTypeTable, typeTableOptions],
                          remarkTypeScriptToJavaScript,
                      ],
                rehypePlugins: (v) => [
                    rehypeKatex,
                    [
                        rehypePrettyCode,
                        {
                            theme: {
                                dark: 'github-dark',
                                light: 'github-light-default',
                            },
                            transformers,
                        },
                    ],
                    ...v,
                ],
            })(environment);
        },
    },
    meta: {
        schema: metaSchemaWithGroup,
    },
});

function transformerEscape(): ShikiTransformer {
    return {
        name: '@shikijs/transformers:remove-notation-escape',
        code(hast) {
            function replace(node: ElementContent) {
                if (node.type === 'text') {
                    node.value = node.value.replace('[\\!code', '[!code');
                } else if ('children' in node) {
                    for (const child of node.children) {
                        replace(child);
                    }
                }
            }

            replace(hast);
            return hast;
        },
    };
}

export const changelog = defineCollections({
    type: 'doc',
    dir: './content/changelog',
    schema: z.object({
        id: z.string(),
        slug: z.string(),
        date: z.string(),
        version: z.string(),
        title: z.string(),
        summary: z.string(),
        tags: z.array(z.string()).optional(),
        draft: z.boolean().optional(),
        image: z.object({
            src: z.string(),
            alt: z.string(),
            width: z.number(),
            height: z.number(),
        }),
    }),
});

export default defineConfig({
    plugins: [
        jsonSchema({
            insert: true,
        }),
        lastModified(),
    ],
});
