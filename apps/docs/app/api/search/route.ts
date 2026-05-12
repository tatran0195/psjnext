import { stopwords as japaneseStopwords } from '@orama/stopwords/japanese';
import { createTokenizer } from '@orama/tokenizers/japanese';
import { StructuredData } from 'fumadocs-core/mdx-plugins';
import { findPath } from 'fumadocs-core/page-tree';
import { createFromSource } from 'fumadocs-core/search/server';
import { LoaderConfig, LoaderOutput } from 'fumadocs-core/source';
import { basename, extname } from 'node:path';

import { env } from '@/env';
import { source } from '@/lib/source';

export const { GET } = createFromSource(source, {
    localeMap: {
        ja: {
            tokenizer: createTokenizer({ language: 'japanese', stopWords: japaneseStopwords }),
            search: { similarity: 0.1, exact: false, threshold: 2, tolerance: 1 },
        },
        en: {
            search: { similarity: 0.1, exact: false, tolerance: 2, threshold: 1 },
        },
    },
    async buildIndex(page) {
        if (!page) throw new Error('Cannot find page');

        const versionRegex = /^\d+\.\d+\.\d+$/;
        const version: string =
            (page.data._version as string | undefined) ??
            page.slugs.find((s) => versionRegex.test(s)) ??
            env.API_VERSIONS[0];

        let structuredData: StructuredData | undefined;
        if ('structuredData' in page.data) {
            structuredData =
                typeof page.data.structuredData === 'function'
                    ? await page.data.structuredData()
                    : page.data.structuredData;
        } else if ('load' in page.data) {
            structuredData = (await page.data.load()).structuredData;
        }

        if (!structuredData) throw new Error('Cannot find structured data for ' + page.path);

        const breadcrumbs = buildBreadcrumbs(source, page);

        return {
            title: page.data.title ?? basename(page.path, extname(page.path)),
            description: page.data.description,
            url: page.url,
            id: page.url,
            structuredData,
            breadcrumbs,
            tag: version || '',
        };
    },
});

function isBreadcrumbItem(item: unknown): item is string {
    return typeof item === 'string' && item.length > 0;
}

function buildBreadcrumbs<C extends LoaderConfig>(source: LoaderOutput<C>, page: C['page']): string[] | undefined {
    const pageTree = source.getPageTree(page.locale);
    const path = findPath(pageTree.children, (node) => node.type === 'page' && node.url === page.url);

    if (path) {
        const breadcrumbs: string[] = [];
        path.pop();

        if (isBreadcrumbItem(pageTree.name)) {
            breadcrumbs.push(pageTree.name);
        }

        for (const segment of path) {
            if (!isBreadcrumbItem(segment.name)) continue;
            breadcrumbs.push(segment.name);
        }

        return breadcrumbs;
    }
}
