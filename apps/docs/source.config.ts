import nextEnv from '@next/env';
const { loadEnvConfig } = nextEnv;
loadEnvConfig(process.cwd());

import type { RemarkAutoTypeTableOptions } from 'fumadocs-typescript';

import { transformerMetaHighlight, transformerRemoveNotationEscape } from '@shikijs/transformers';
import { RehypeCodeOptions, remarkMdxFiles, remarkMdxMermaid } from 'fumadocs-core/mdx-plugins';
import { pageSchema } from 'fumadocs-core/source/schema';
import {
    applyMdxPreset,
    defineCollections,
    defineConfig,
    defineDocs,
    DocCollection,
    metaSchema,
} from 'fumadocs-mdx/config';
import jsonSchema from 'fumadocs-mdx/plugins/json-schema';
import lastModified from 'fumadocs-mdx/plugins/last-modified';
import remarkDirective from 'remark-directive';
import { z } from 'zod';

import { remarkBadge } from './lib/mdx-plugins/remark-badge';
import { remarkDirectiveAdmonition } from './lib/mdx-plugins/remark-directive-admonition';
import { remarkDirectiveFixer } from './lib/mdx-plugins/remark-directive-fixer';
import { remarkElementIds } from './lib/mdx-plugins/remark-element-ids';
import { remarkLinkPreview } from './lib/mdx-plugins/remark-link-preview';
import { remarkVersionGateParams } from './lib/mdx-plugins/remark-version-gate-params';
import { defaultShikiOptions } from './lib/shiki';

const { rehypeCodeDefaultOptions } = await import('fumadocs-core/mdx-plugins/rehype-code');
const { remarkSteps } = await import('fumadocs-core/mdx-plugins/remark-steps');
const { transformerTwoslash } = await import('fumadocs-twoslash');
const { createFileSystemTypesCache } = await import('fumadocs-twoslash/cache-fs');
const { default: remarkMath } = await import('remark-math');
const { remarkTypeScriptToJavaScript } = await import('fumadocs-docgen/remark-ts2js');
const { default: rehypeKatex } = await import('rehype-katex');
const { remarkAutoTypeTable, createGenerator, createFileSystemGeneratorCache } = await import('fumadocs-typescript');

const isLint = process.env.LINT === '1';

const mdxOptions: DocCollection['mdxOptions'] = async (environment) => {
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
                      transformerRemoveNotationEscape(),
                      transformerMetaHighlight(),
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
                  remarkDirectiveFixer,
                  remarkDirective,
                  [remarkDirectiveAdmonition, { types: { tip: 'idea' } }],
                  remarkBadge,
                  remarkMdxFiles,
                  remarkVersionGateParams,
                  remarkSteps,
                  remarkMath,
                  remarkMdxMermaid,
                  remarkLinkPreview,
                  [remarkAutoTypeTable, typeTableOptions],
                  remarkTypeScriptToJavaScript,
              ],
        rehypePlugins: (v) => [rehypeKatex, ...v],
    })(environment);
};

export const docs = defineDocs({
    docs: {
        schema: pageSchema.extend({
            index: z.boolean().default(false),
            ribbon: z.string().optional(),
            shortcut: z.string().optional(),
            since: z.string().optional(),
            deprecated: z.string().optional(),
            removed: z.string().optional(),
            _version: z.string().optional(),
            _status: z.string().optional(),
        }),
        postprocess: {
            includeProcessedMarkdown: true,
            extractLinkReferences: true,
            valueToExport: ['elementIds', 'paramMeta'],
        },
        async: true,
        mdxOptions,
    },
    meta: {
        schema: metaSchema.extend({
            group: z.boolean().optional(),
            groupType: z.enum(['stacked', 'tabs']).default('tabs').optional(),
            groupOrder: z.number().default(0).optional(),
        }),
    },
});

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
        highlights: z.array(z.string()).optional(),
        tags: z.array(z.string()).optional(),
        draft: z.boolean().optional(),
        image: z
            .string()
            .refine((s) => !s.startsWith('http'), {
                message: 'Image source must be a relative link',
            })
            .optional(),
    }),
    async: true,
    mdxOptions,
});

export default defineConfig({
    plugins: [
        jsonSchema({
            insert: true,
        }),
        lastModified(),
    ],
});
