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

        let structuredData = data.structuredData;
        const paramMeta = (data.paramMeta as { name: string; since?: string; removed?: string }[]) || [];

        if (version && paramMeta.length > 0) {
            const getVersionStatus = (
                current: string,
                introduced?: string,
                deprecated?: string,
                removed?: string,
            ) => {
                const parseSemver = (v: string): [number, number, number] => {
                    const [a = 0, b = 0, c = 0] = v.split('.').map(Number);
                    return [a, b, c];
                };
                const semverGte = (a: string, b: string): boolean => {
                    const pa = parseSemver(a);
                    const pb = parseSemver(b);
                    for (let i = 0; i < 3; i++) {
                        if (pa[i] > pb[i]) return true;
                        if (pa[i] < pb[i]) return false;
                    }
                    return true;
                };

                if (removed && semverGte(current, removed)) return 'removed';
                if (introduced && !semverGte(current, introduced)) return 'unavailable';
                return 'available';
            };

            const hiddenParamNames = new Set(
                paramMeta
                    .filter((pm) => {
                        const status = getVersionStatus(version, pm.since, undefined, pm.removed);
                        return status === 'removed' || status === 'unavailable';
                    })
                    .map((pm) => pm.name),
            );

            if (hiddenParamNames.size > 0 && structuredData) {
                // Remove hidden headings
                const validHeadings = structuredData.headings.filter(
                    (h: any) => !hiddenParamNames.has(h.content),
                );
                
                // Track IDs of hidden headings
                const hiddenHeadingIds = new Set(
                    structuredData.headings
                        .filter((h: any) => hiddenParamNames.has(h.content))
                        .map((h: any) => h.id),
                );

                // Remove contents that belong to hidden headings
                const validContents = structuredData.contents.filter(
                    (c: any) => !c.heading || !hiddenHeadingIds.has(c.heading),
                );

                structuredData = {
                    headings: validHeadings,
                    contents: validContents,
                };
            }
        }

        return {
            title: page.data.title ?? '',
            description: page.data.description,
            url: page.url,
            id: page.url,
            structuredData,
            breadcrumbs: page.slugs,
            tag: version || '',
        };
    },
});
