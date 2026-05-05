import { getBreadcrumbItems } from 'fumadocs-core/breadcrumb';

import { source } from '@/lib/source';
import { getSection } from '@/lib/source/navigation';

import type { OramaDocument } from 'fumadocs-core/search/orama-cloud';

export const revalidate = false;

export async function GET(): Promise<Response> {
    const pages = source.getPages();
    const promises = pages.map(async (page) => {
        // if (page.data.type === 'openapi') return;

        const items = getBreadcrumbItems(page.url, source.getPageTree(), {
            includePage: false,
            includeRoot: true,
        });

        const data = await page.data.load();
        
        let structuredData = data.structuredData;
        const versionRegex = /(\d+\.\d+\.\d+)/;
        const match = page.slugs.find((slug) => slug.match(versionRegex));
        const version = match ? match : null;

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
                const validHeadings = structuredData.headings.filter(
                    (h: any) => !hiddenParamNames.has(h.content),
                );
                const hiddenHeadingIds = new Set(
                    structuredData.headings
                        .filter((h: any) => hiddenParamNames.has(h.content))
                        .map((h: any) => h.id),
                );
                const validContents = structuredData.contents.filter(
                    (c: any) => !c.heading || !hiddenHeadingIds.has(c.heading),
                );
                structuredData = { headings: validHeadings, contents: validContents };
            }
        }

        return {
            id: page.url,
            structured: structuredData,
            tag: getSection(page.slugs[0]),
            url: page.url,
            title: page.data.title,
            description: page.data.description,
            breadcrumbs: items.flatMap<string>((item, i) =>
                i > 0 && typeof item.name === 'string' ? item.name : [],
            ),
        } as OramaDocument;
    });

    return Response.json(
        (await Promise.all(promises)).filter((v) => v !== undefined) as OramaDocument[],
    );
}
