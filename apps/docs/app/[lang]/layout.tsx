import type { Metadata, Viewport } from 'next';
import { notFound } from 'next/navigation';
import type { ReactNode } from 'react';

import { NextProvider } from 'fumadocs-core/framework/next';
import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';
import { Geist, Geist_Mono } from 'next/font/google';

import { i18n } from '@/lib/i18n';
import { baseUrl, createMetadata } from '@/lib/metadata';
import { docsSource } from '@/lib/source';
import '@/styles/global.css';

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

const geist = Geist({ variable: '--font-sans', subsets: ['latin'] });
const mono = Geist_Mono({ variable: '--font-mono', subsets: ['latin'] });

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
    const { lang } = await props.params;
    if (!i18n.languages.includes(lang as (typeof i18n.languages)[number])) notFound();

    // Provide the docs tree at the top level so global components (e.g. search)
    // that call useTreeContext() always have a valid context.
    // Each sub-layout (docs / api) wraps its own TreeContextProvider which
    // shadows this one for the sidebar via React's nearest-provider rule.
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
    return i18n.languages.map((lang) => ({ lang }));
}
