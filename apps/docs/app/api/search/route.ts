import { stopwords as japaneseStopwords } from '@orama/stopwords/japanese';
import { createTokenizer } from '@orama/tokenizers/japanese';
import { getBreadcrumbItems } from 'fumadocs-core/breadcrumb';
import { AdvancedIndex, createI18nSearchAPI } from 'fumadocs-core/search/server';

import type { ApiVersion, Page } from '@/lib/source';

import { i18n } from '@/lib/i18n';
import { apiSources, docsSource } from '@/lib/source';
import { ACTIVE_VERSIONS } from '@/lib/versions';

export const revalidate = false;

function getBreadcrumbs(page: Page) {
    const items = getBreadcrumbItems(page.url, docsSource.getPageTree(), {
        includePage: false,
        includeRoot: true,
    });
    const breadcrumbs = items.flatMap<string>((item, i) =>
        i > 0 && typeof item.name === 'string' ? item.name : [],
    );
    return breadcrumbs;
}

type IndexedPage = AdvancedIndex & { locale: string };
async function buildIndexes() {
    const indexes: IndexedPage[] = [];

    for (const page of docsSource.getPages()) {
        const { structuredData } = await page.data.load();
        const breadcrumbs = getBreadcrumbs(page);
        indexes.push({
            id: page.url,
            title: page.data.title,
            description: page.data.description,
            breadcrumbs,
            url: page.url,
            structuredData,
            tag: 'docs',
            locale: page.locale ?? 'en',
        });
    }

    for (const version of ACTIVE_VERSIONS) {
        const source = apiSources[version as ApiVersion];
        if (!source) continue;

        for (const page of source.getPages()) {
            const { structuredData } = await page.data.load();
            const breadcrumbs = getBreadcrumbs(page);
            indexes.push({
                id: page.url,
                title: page.data.title,
                description: page.data.description,
                breadcrumbs,
                url: page.url,
                structuredData,
                tag: version,
                locale: page.locale ?? 'en',
            });
        }
    }

    return indexes;
}

export const { GET } = createI18nSearchAPI('advanced', {
    i18n,
    localeMap: {
        en: { language: 'english' },
        ja: {
            tokenizer: createTokenizer({
                language: 'japanese',
                stopWords: japaneseStopwords,
            }),
            search: {
                tolerance: 1,
                exact: false,
            },
        },
    },
    indexes: await buildIndexes(),
});
