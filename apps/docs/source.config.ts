import { mdxOptions } from '@/lib/mdx-options';
import { DocsSchema, MetaSchema } from '@/lib/source/schema';
import { defineConfig, defineDocs } from 'fumadocs-mdx/config';
import jsonSchema from 'fumadocs-mdx/plugins/json-schema';
import lastModified from 'fumadocs-mdx/plugins/last-modified';

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

export const apiDocs = defineDocs({
    dir: 'content/api',
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
});
