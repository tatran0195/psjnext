import type { MetadataRoute } from 'next';

import { getSiteUrl } from '@/lib/site-url';
import { source } from '@/lib/source';

export const revalidate = false;

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
    const url = (path: string): string => new URL(path, getSiteUrl()).toString();
    const items = await Promise.all(
        source.getPages().map(async (page) => {
            // if (page.data.type === 'openapi') return;
            const { lastModified } = await page.data.load();

            return {
                url: url(page.url),
                lastModified: lastModified ? new Date(lastModified) : undefined,
                changeFrequency: 'weekly',
                priority: 0.5,
            } as MetadataRoute.Sitemap[number];
        }),
    );

    return [
        {
            url: url('/'),
            changeFrequency: 'monthly',
            priority: 1,
        },
        {
            url: url('/enterprise'),
            changeFrequency: 'monthly',
            priority: 0.8,
        },
        {
            url: url('/showcase'),
            changeFrequency: 'monthly',
            priority: 0.8,
        },
        {
            url: url('/changelog'),
            changeFrequency: 'monthly',
            priority: 0.8,
        },
        {
            url: url('/docs'),
            changeFrequency: 'monthly',
            priority: 0.8,
        },
        ...items.filter((v) => v !== undefined),
    ];
}
