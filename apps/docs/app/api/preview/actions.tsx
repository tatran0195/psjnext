'use server';

import React from 'react';

import { getMDXComponents } from '@/components/mdx';
import { DocsCategory, DocsSectionOverview } from '@/components/mdx/docs-category';
import { LinkPreview } from '@/components/mdx/link-preview';
import { i18n } from '@/lib/i18n';
import { source } from '@/lib/source';

export interface PreviewData {
    title: string;
    description?: string;
    content: React.ReactNode;
}

export async function getPreviewData(url: string): Promise<PreviewData | null> {
    try {
        const pathname = new URL(url, 'http://localhost').pathname;
        const segments = pathname.split('/').filter(Boolean);

        // Detect language
        let lang = i18n.defaultLanguage;
        if (segments.length > 0 && i18n.languages.includes(segments[0] as 'en' | 'ja')) {
            lang = segments.shift()! as 'en' | 'ja';
        }

        // Remove 'docs' prefix if present
        if (segments[0] === 'docs') {
            segments.shift();
        }

        const page = source.getPage(segments, lang);

        if (!page) return null;

        // Handle OpenAPI separately
        // if (page.data.type === 'openapi') {
        //     return {
        //         title: page.data.title,
        //         description: page.data.description,
        //         content: React.createElement(
        //             'p',
        //             { className: 'text-sm text-fd-muted-foreground italic' },
        //             'API Documentation preview',
        //         ),
        //     };
        // }

        const { body: Mdx } = await page.data.load();

        return {
            title: page.data.title,
            description: page.data.description,
            content: React.createElement(Mdx, {
                components: getMDXComponents({
                    LinkPreview,
                    DocsCategory: ({ url }) => <DocsCategory url={url ?? page.url} lang={lang} />,
                    DocsSectionOverview: ({ url }) => (
                        <DocsSectionOverview url={url ?? page.url} lang={lang} />
                    ),
                }),
            }),
        };
    } catch (e) {
        console.error('[preview-action] Error rendering preview:', e);
        return null;
    }
}
