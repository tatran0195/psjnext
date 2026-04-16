import type { Metadata } from 'next/types';
import type { Page } from './source';

export function createMetadata(override: Metadata): Metadata {
    return {
        ...override,
        openGraph: {
            title: override.title ?? undefined,
            description: override.description ?? undefined,
            url: 'https://psjdoc.e-technostar.com',
            images: '/banner.png',
            siteName: 'PSJ-Docs',
            ...override.openGraph,
        },
        twitter: {
            card: 'summary_large_image',
            creator: '@waka',
            title: override.title ?? undefined,
            description: override.description ?? undefined,
            images: '/banner.png',
            ...override.twitter,
        },
        alternates: {
            ...override.alternates,
        },
    };
}

export function getPageImage(page: Page) {
    const lang = page.locale || 'en';
    const segments = [lang, ...page.slugs, 'image.webp'];

    return {
        segments,
        url: `/og/${segments.join('/')}`,
    };
}

export const baseUrl =
    process.env.NODE_ENV === 'development' || !process.env.PRODUCTION_URL
        ? new URL('http://localhost:3000')
        : new URL(`https://${process.env.PRODUCTION_URL}`);
