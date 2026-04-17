import { transformerTwoslash } from 'fumadocs-twoslash';
import {
    remarkAutoTypeTable,
    createGenerator,
    createFileSystemGeneratorCache,
    type RemarkAutoTypeTableOptions,
} from 'fumadocs-typescript';

import { rehypeCodeDefaultOptions } from 'fumadocs-core/mdx-plugins/rehype-code';
import { remarkSteps } from 'fumadocs-core/mdx-plugins/remark-steps';
import { applyMdxPreset, DocCollection } from 'fumadocs-mdx/config';
import { createFileSystemTypesCache } from 'fumadocs-twoslash/cache-fs';
import remarkMath from 'remark-math';
import { visit } from 'unist-util-visit';

import { remarkElementIds } from '@/lib/mdx-plugins/remark-element-ids';
import { remarkLinkPreview } from '@/lib/mdx-plugins/remark-link-preview';
import { defaultShikiOptions } from '@/lib/shiki';
import { psjGrammar } from '@/lib/shiki/psj';

import type { ElementContent } from 'hast';
import type { Root } from 'mdast';
import type { ShikiTransformer } from 'shiki';
import type { Transformer } from 'unified';

const isLint = process.env.LINT === '1';
const isDev = process.env.NODE_ENV !== 'production';

// ── Singletons: created once at module load, reused across all MDX files ──
const _generatorCache = createFileSystemGeneratorCache('.next/fumadocs-typescript');
const _generator = createGenerator({ cache: _generatorCache });

const typeTableOptions: RemarkAutoTypeTableOptions = {
    generator: _generator,
    shiki: defaultShikiOptions,
};

// Twoslash is expensive (full TS language server). Only load in production.
// In dev, code blocks render without hover types — fine for authoring.
const twoslashTransformer = !isDev
    ? (() => {
          return transformerTwoslash({
              typesCache: createFileSystemTypesCache(),
              twoslashOptions: {
                  compilerOptions: { types: ['@types/node'] },
              },
          });
      })()
    : null;

export const mdxOptions: DocCollection['mdxOptions'] = (environment) => {
    return applyMdxPreset({
        rehypeCodeOptions: isLint
            ? false
            : {
                  langs: ['ts', 'js', 'html', 'tsx', 'mdx', 'py', 'python', psjGrammar],
                  inline: 'tailing-curly-colon',
                  themes: {
                      light: 'catppuccin-latte',
                      dark: 'catppuccin-mocha',
                  },
                  transformers: [
                      ...(rehypeCodeDefaultOptions.transformers ?? []),
                      // Twoslash only in prod — skipped in dev for faster compilation.
                      ...(twoslashTransformer ? [twoslashTransformer] : []),
                      transformerEscape(),
                  ],
              },
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
        remarkPlugins: (plugins) =>
            isLint
                ? [...plugins, remarkElementIds]
                : [
                      ...plugins,
                      //   remarkIncludeCode,
                      remarkSteps,
                      remarkMath,
                      [remarkLinkPreview, {}],
                      [remarkAutoTypeTable, typeTableOptions],
                  ],
        rehypePlugins: (v) => [...v],
    })(environment);
};

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
