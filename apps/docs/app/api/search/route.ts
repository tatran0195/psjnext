import { stopwords as japaneseStopwords } from '@orama/stopwords/japanese';
import { createTokenizer } from '@orama/tokenizers/japanese';
import { createFromSource } from 'fumadocs-core/search/server';

import { source } from '@/lib/source';

const filteredSource = {
    ...source,
    getPages: () =>
        source
            .getPages()
            .filter((page) => (page.data as { _status?: string })._status !== 'removed'),
};
/* eslint-disable @typescript-eslint/no-explicit-any -- createFromSource expects a specific loader type */
export const { GET } = createFromSource(filteredSource as any, {
    localeMap: {
        ja: {
            tokenizer: createTokenizer({
                language: 'japanese',
                stopWords: japaneseStopwords,
            }),
            search: {
                similarity: 0.1,
                exact: false,
                threshold: 2,
                tolerance: 1,
            },
        },
        en: {
            search: {
                similarity: 0.1,
                exact: false,
                tolerance: 2,
                threshold: 1,
            },
        },
    },
    async buildIndex(page) {
        const data = await page.data.load();
        const versionRegex = /(\d+\.\d+\.\d+)/;
        const match = page.slugs.find((slug) => slug.match(versionRegex));
        const version = match ? match : null;

        return {
            title: page.data.title ?? '',
            description: page.data.description,
            url: page.url,
            id: page.url,
            structuredData: data.structuredData,
            breadcrumbs: page.slugs,
            tag: version || '',
        };
    },
});
