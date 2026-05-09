import type { Metadata, Viewport } from 'next';
import type { ReactNode } from 'react';

import { NextProvider } from 'fumadocs-core/framework/next';
import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';
import { Geist, Geist_Mono } from 'next/font/google';

import { createMetadata } from '@/lib/metadata';
import { getSiteUrl } from '@/lib/site-url';
import { source } from '@/lib/source';
import '@/styles/global.css';
import { Body } from './layout.client';
import { Provider } from './provider';

export const metadata: Metadata = createMetadata({
    title: {
        template: '%s | PSJ Docs',
        default: 'PSJ Docs',
    },
    description: 'PSJ Command Documentation',
    metadataBase: getSiteUrl(),
});

const geist = Geist({
    variable: '--font-sans',
    subsets: ['latin'],
});

const mono = Geist_Mono({
    variable: '--font-mono',
    subsets: ['latin'],
});

export const viewport: Viewport = {
    themeColor: [
        { media: '(prefers-color-scheme: dark)', color: '#0A0A0A' },
        { media: '(prefers-color-scheme: light)', color: '#fff' },
    ],
};

export default async function RootLayout(props: {
    children: ReactNode;
    params: Promise<{ lang?: string }>;
}) {
    const params = await props.params;

    const lang = params.lang ?? 'en';
    return (
        <html
            lang={lang}
            className={`${geist.variable} ${mono.variable}`}
            suppressHydrationWarning
            data-scroll-behavior="smooth"
        >
            <Body>
                <NextProvider>
                    <TreeContextProvider tree={source.getPageTree(lang)}>
                        <Provider lang={lang}>{props.children}</Provider>
                    </TreeContextProvider>
                </NextProvider>
            </Body>
        </html>
    );
}

export function generateStaticParams() {
    return source.generateParams('slug', 'lang');
}
