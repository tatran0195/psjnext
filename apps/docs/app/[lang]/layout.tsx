import type { Metadata, Viewport } from 'next';
import type { ReactNode } from 'react';

import { NextProvider } from 'fumadocs-core/framework/next';
import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';

import '@/styles/global.css';
import { Geist, Geist_Mono } from 'next/font/google';
import 'psjd/ui/styles.css';

import { baseUrl, createMetadata } from '@/lib/metadata';
import { docsSource } from '@/lib/source';

import { Provider } from '../provider';
import { Body } from './layout.client';

export const metadata: Metadata = createMetadata({
    title: {
        template: '%s | PSJ Docs',
        default: 'PSJ Docs',
    },
    description: 'PSJ Command Documentation',
    metadataBase: baseUrl,
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
    params: Promise<{ lang: string; version?: string }>;
}) {
    const { lang } = await props.params;

    const tree = docsSource.getPageTree(lang);

    return (
        <html
            lang={lang}
            className={`${geist.variable} ${mono.variable}`}
            suppressHydrationWarning
            data-scroll-behavior="smooth"
        >
            <Body>
                <NextProvider>
                    <TreeContextProvider tree={tree}>
                        <Provider>{props.children}</Provider>
                    </TreeContextProvider>
                </NextProvider>
            </Body>
        </html>
    );
}

export function generateStaticParams() {
    return docsSource.generateParams('slug', 'locale');
}
