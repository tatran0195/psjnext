/**
 * fumadocs-mdx workspace config for API version 5.2.0 (latest).
 * Auto-managed by scripts/sync-versions.ts
 *
 * Self-contained: no relative imports outside this package.
 * fumadocs-mdx bundles workspace configs with esbuild; relative cross-dir
 * imports won't resolve, so schemas and options are inlined here.
 */
import { metaSchema, pageSchema } from 'fumadocs-core/source/schema';
import { applyMdxPreset, defineConfig, defineDocs, DocCollection } from 'fumadocs-mdx/config';
import lastModified from 'fumadocs-mdx/plugins/last-modified';

const mdxOptions: DocCollection['mdxOptions'] = (environment) =>
    applyMdxPreset({
        rehypeCodeOptions: {
            langs: ['ts', 'js', 'html', 'tsx', 'mdx', 'python'],
            inline: 'tailing-curly-colon',
            themes: { light: 'catppuccin-latte', dark: 'catppuccin-mocha' },
        },
        remarkCodeTabOptions: { parseMdx: true },
    })(environment);

export const docs = defineDocs({
    dir: '.',
    docs: {
        schema: pageSchema,
        mdxOptions,
        async: true,
        postprocess: {
            includeProcessedMarkdown: true,
            extractLinkReferences: true,
            valueToExport: ['elementIds'],
        },
    },
    meta: {
        schema: metaSchema,
    },
});

export default defineConfig({
    plugins: [lastModified()],
});
