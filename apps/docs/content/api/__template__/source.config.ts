/**
 * source.config.ts TEMPLATE for API version workspaces.
 * Copied into content/api/<version>/ by scripts/sync-versions.ts.
 *
 * IMPORTANT: Keep self-contained — no relative cross-directory imports.
 * fumadocs-mdx uses esbuild to bundle workspace configs from the root context;
 * relative paths like '../../lib/...' are resolved relative to this file and
 * esbuild cannot reach outside the content dir reliably.
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
