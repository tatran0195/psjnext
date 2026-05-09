import type { Metadata } from 'next/types';

import type { Page } from './source';

import { toAbsoluteUrl } from './site-url';

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

export function buildCollectionPageJsonLd({
    title,
    description,
    path,
}: {
    title: string;
    description: string;
    path: string;
}) {
    return {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        name: title,
        description,
        url: toAbsoluteUrl(path),
    };
}
