/**
 * fumadocs-mdx workspace config for API version 5.2.0 (latest).
 * Auto-managed by scripts/sync-versions.ts
 *
 * Self-contained: no relative imports outside this package.
 * fumadocs-mdx bundles workspace configs with esbuild; relative cross-dir
 * imports won't resolve, so schemas and options are inlined here.
 */
import { metaSchema, pageSchema } from 'fumadocs-core/source/schema';
import { applyMdxPreset, defineConfig, defineDocs, type DocCollection } from 'fumadocs-mdx/config';
import { z } from 'zod';

const RibbonItemSchema = z.object({
    label: z.string(),
    icon: z.string().optional(),
    shortcut: z.string().optional(),
    tooltip: z.string().optional(),
});

const DocsSchema = pageSchema.extend({
    preview: z.string().optional(),
    index: z.boolean().default(false),
    method: z.string().optional(),
    tag: z.string().optional(),
    ribbon: z
        .object({
            tab: z.string(),
            panel: z.object({
                label: z.string(),
                item: RibbonItemSchema.extend({ flyout: z.array(RibbonItemSchema).optional() }),
            }),
            note: z.string().optional(),
        })
        .optional(),
});

const MetaSchema = metaSchema.extend({
    description: z.string().optional(),
    group: z.boolean().optional(),
});

const mdxOptions: DocCollection['mdxOptions'] = (environment) =>
    applyMdxPreset({
        rehypeCodeOptions: {
            langs: ['ts', 'js', 'html', 'tsx', 'mdx', 'py'],
            inline: 'tailing-curly-colon',
            themes: { light: 'catppuccin-latte', dark: 'catppuccin-mocha' },
        },
        remarkCodeTabOptions: { parseMdx: true },
    })(environment);

export const docs = defineDocs({
    docs: {
        schema: DocsSchema,
        mdxOptions,
        async: true,
        postprocess: {
            includeProcessedMarkdown: true,
            extractLinkReferences: true,
            valueToExport: ['elementIds'],
        },
    },
    meta: { schema: MetaSchema },
});

export default defineConfig();
