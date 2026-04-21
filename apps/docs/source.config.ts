import { defineConfig, defineDocs } from 'fumadocs-mdx/config';
import jsonSchema from 'fumadocs-mdx/plugins/json-schema';
import lastModified from 'fumadocs-mdx/plugins/last-modified';

import { mdxOptions } from '@/lib/mdx-options';
import { DocsSchema, MetaSchema } from '@/lib/source/schema';

export const docs = defineDocs({
    docs: {
        schema: DocsSchema,
        postprocess: {
            includeProcessedMarkdown: true,
            extractLinkReferences: true,
            valueToExport: ['elementIds'],
        },
        async: true,
        mdxOptions,
    },
    meta: {
        schema: MetaSchema,
    },
});

export default defineConfig({
    plugins: [
        jsonSchema({
            insert: true,
        }),
        lastModified(),
    ],
    mdxOptions: {
        remarkPlugins: [],
        rehypePlugins: [],
    },
    // SYNC-VERSIONS:START
    workspaces: {
        '5.2.0': { dir: 'content/api/5.2.0', config: await import('./content/api/5.2.0/source.config.ts') },
        '5.1.0': { dir: 'content/api/5.1.0', config: await import('./content/api/5.1.0/source.config.ts') },
    },
    // SYNC-VERSIONS:END
});
