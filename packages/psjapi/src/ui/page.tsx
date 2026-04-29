import type { HTMLAttributes, ReactNode } from 'react';

import { highlightHast } from 'fumadocs-core/highlight/shiki';
import { defaultShikiFactory } from 'fumadocs-core/highlight/shiki/full';
import { createRehypeCode } from 'fumadocs-core/mdx-plugins/rehype-code.core';
import { remarkGfm } from 'fumadocs-core/mdx-plugins/remark-gfm';
import { CodeBlock, Pre } from 'fumadocs-ui/components/codeblock';
import { Heading } from 'fumadocs-ui/components/heading';
import defaultMdxComponents from 'fumadocs-ui/mdx';
import Slugger from 'github-slugger';
import { toJsxRuntime } from 'hast-util-to-jsx-runtime';
import * as JsxRuntime from 'react/jsx-runtime';
import { remark } from 'remark';
import remarkRehype from 'remark-rehype';

import type { PSJAPIServer } from '../types';
import type { CreatePSJAPIPageOptions, ResolvedPSJAPIPageOptions } from './context';

import { DEFAULT_SHIKI_OPTIONS } from './context';
import { PSJAPIItemRenderer } from './item';

import type { Root } from 'hast';
import type { Processor } from 'unified';
import type { VFile } from 'vfile';

// ─── Server-side page factory ─────────────────────────────────────────────────

export interface PSJAPIItemProps {
    /** "<domain>/<id>" */
    itemKey: string;
    /** SDK version (falls back to current_version) */
    version?: string;
    /** Locale (falls back to defaultLocale) */
    locale?: string;
    headingLevel?: number;
}

/**
 * Creates the <PSJAPIItem /> server component for a given PSJAPIServer.
 *
 * Usage in app/docs/[[...slug]]/page.tsx:
 * ```tsx
 * import { createPSJAPIPage } from 'fumadocs-psjapi/ui';
 * import { server } from '@/lib/psj-server';
 *
 * const PSJAPIItem = createPSJAPIPage(server, {
 *   shiki,
 *   shikiOptions: { themes: { light: 'github-light', dark: 'github-dark' } },
 * });
 *
 * export default function Page() {
 *   return <PSJAPIItem schemaId="..." itemKey="macro/AdvcStaticProcess" />;
 * }
 * ```
 */
export function createPSJAPIPage(
    server: PSJAPIServer,
    options: CreatePSJAPIPageOptions,
): (props: PSJAPIItemProps) => Promise<ReactNode> {
    // Build markdown processor once
    let processor: ReturnType<typeof createMarkdownProcessor> | undefined;

    function createMarkdownProcessor() {
        function rehypeReact(this: Processor) {
            // @ts-expect-error — attaches a custom compiler to the unified processor
            this.compiler = (tree: Root, file: VFile): ReactNode => {
                return toJsxRuntime(tree, {
                    development: false,
                    filePath: file.path as string,
                    ...JsxRuntime,
                    components: defaultMdxComponents,
                });
            };
        }

        return remark()
            .use(remarkGfm)
            .use(remarkRehype)
            .use(createRehypeCode(shiki), {
                langs: [],
                lazy: true,
                defaultColor: false,
                ...shikiOptions,
            })
            .use(rehypeReact);
    }

    // Resolve shiki + theme — fall back to Fumadocs' built-in singleton
    const shiki = options.shiki ?? defaultShikiFactory;
    const shikiOptions = options.shikiOptions ?? DEFAULT_SHIKI_OPTIONS;

    // Build the enriched options with default renderMarkdown / renderCodeBlock
    async function buildOptions(slugger: Slugger): Promise<ResolvedPSJAPIPageOptions> {
        return {
            ...options,
            shiki,
            shikiOptions,
            renderMarkdown: options.renderMarkdown
                ? options.renderMarkdown
                : async (text: string) => {
                      processor ??= createMarkdownProcessor();
                      const out = await processor.process({ value: text });
                      return out.result as ReactNode;
                  },
            renderCodeBlock: options.renderCodeBlock
                ? options.renderCodeBlock
                : async ({ lang, code }: { lang: string; code: string }) => {
                      const hast = await highlightHast(await shiki.getOrInit(), code, {
                          lang,
                          defaultColor: false,
                          ...shikiOptions,
                      });
                      const rendered = toJsxRuntime(hast, {
                          ...JsxRuntime,
                          components: { pre: Pre },
                      });
                      return <CodeBlock className="my-0">{rendered}</CodeBlock>;
                  },
            renderHeading: options.renderHeading
                ? options.renderHeading
                : (props: HTMLAttributes<HTMLHeadingElement>, depth: number) => {
                      const id =
                          props.id ??
                          (typeof props.children === 'string'
                              ? slugger.slug(props.children)
                              : undefined);
                      return (
                          <Heading id={id} key={id} as={`h${depth}` as 'h1'} {...props}>
                              {props.children}
                          </Heading>
                      );
                  },
        };
    }

    return async function PSJAPIItem({
        itemKey,
        version,
        locale,
        headingLevel = 1,
    }: PSJAPIItemProps) {
        const item = await server.resolveItem(itemKey, version, locale);

        if (!item) {
            return (
                <div className="rounded-lg border border-red-400/50 bg-red-50/50 p-4 text-sm text-red-800 dark:text-red-200">
                    Item not found: <code>{itemKey}</code>
                </div>
            );
        }

        const slugger = new Slugger();
        const resolvedOptions = await buildOptions(slugger);

        // Determine active version / locale
        const sdk = await server.getProcessedSdk();
        const activeVersion =
            version ?? sdk.manifest.current_version ?? sdk.manifest.versions.at(-1)?.id ?? '0';
        const activeLocale = locale ?? server.options.defaultLocale ?? 'en';

        return (
            <PSJAPIItemRenderer
                item={item}
                version={activeVersion}
                locale={activeLocale}
                options={resolvedOptions}
                headingLevel={headingLevel}
            />
        );
    };
}
