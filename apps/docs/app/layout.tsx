import type { Metadata, Viewport } from 'next';
import type { ReactNode } from 'react';

import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';
import { Geist, Geist_Mono } from 'next/font/google';

import { baseUrl, createMetadata } from '@/lib/metadata';
import { source } from '@/lib/source';
import '@/styles/global.css';
import { NextProvider } from 'fumadocs-core/framework/next';
import { Body } from './layout.client';
import { Provider } from './provider';

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
    params: Promise<{ lang: string }>;
}) {
    const params = await props.params;

    return (
        <html
            lang={params.lang}
            className={`${geist.variable} ${mono.variable}`}
            suppressHydrationWarning
            data-scroll-behavior="smooth"
        >
            <Body>
                <NextProvider>
                    <TreeContextProvider tree={source.getPageTree(params.lang)}>
                        <Provider locale={params.lang}>
                            {props.children}
                        </Provider>
                    </TreeContextProvider>
                </NextProvider>
            </Body>
        </html>
    );
}

export function generateStaticParams() {
    // return i18n.languages.map((lang) => ({ lang }));
    return source.generateParams('slug', 'locale');
}
