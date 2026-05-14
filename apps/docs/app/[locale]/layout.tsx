import type { Metadata, Viewport } from 'next';

import { NextProvider } from 'fumadocs-core/framework/next';
import { TreeContextProvider } from 'fumadocs-ui/contexts/tree';
import { Locale, NextIntlClientProvider } from 'next-intl';
import { getMessages } from 'next-intl/server';
import { Geist_Mono, Inter, Noto_Sans_JP } from 'next/font/google';

import { GlobalFooter } from '@/components/layout/global-footer';
import { LinkSidebar } from '@/components/mdx/link-sidebar';
import { createMetadata } from '@/lib/metadata';
import { getSiteUrl } from '@/lib/site-url';
import { source } from '@/lib/source';
import '@/styles/global.css';

import { Provider } from '../provider';
import { Body } from './layout.client';

export const metadata: Metadata = createMetadata({
    title: {
        template: '%s | PSJ Docs',
        default: 'PSJ Docs',
    },
    description: 'PSJ Command Documentation',
    metadataBase: getSiteUrl(),
});

/**
 * Inter Variable — primary UI/body font
 * Industry standard for technical documentation (Stripe, Vercel, Linear, Figma)
 * Superior Latin/numeric rendering at all sizes. Variable weight = single file.
 */
const inter = Inter({
    variable: '--font-inter',
    subsets: ['latin', 'latin-ext'],
    display: 'swap',
    axes: ['opsz'], // optical sizing axis — sharpens small text
});

/**
 * Noto Sans JP — Japanese CJK fallback only
 * Loaded via unicode-range in CSS so it only activates for Japanese characters.
 * Latin text always uses Inter; Japanese glyphs use Noto Sans JP.
 */
const notoSansJP = Noto_Sans_JP({
    variable: '--font-noto-jp',
    subsets: ['latin'],
    weight: ['400', '500', '700'],
    display: 'swap',
    preload: false, // deferred — only needed when CJK chars appear
});

/**
 * Geist Mono — code blocks and inline code
 * Clean, modern monospace with great developer tooling aesthetics.
 */
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

export default async function RootLayout({ children, params }: LayoutProps<'/[locale]'>) {
    const { locale } = await params;
    const messages = await getMessages({ locale: locale as Locale });

    return (
        <html
            lang={locale}
            className={`${inter.variable} ${notoSansJP.variable} ${mono.variable}`}
            suppressHydrationWarning
            data-scroll-behavior="smooth"
        >
            <Body>
                <NextProvider>
                    <TreeContextProvider tree={source.getPageTree(locale)}>
                        <Provider lang={locale}>
                            <NextIntlClientProvider messages={messages} locale={locale as Locale}>
                                {children}
                                <LinkSidebar />
                            </NextIntlClientProvider>
                        </Provider>
                    </TreeContextProvider>
                </NextProvider>
                <GlobalFooter />
            </Body>
        </html>
    );
}

export function generateStaticParams() {
    return source.generateParams('slug', 'lang');
}
