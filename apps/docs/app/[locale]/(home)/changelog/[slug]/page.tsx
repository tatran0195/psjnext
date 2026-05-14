import type { Metadata } from 'next';
import Image from 'next/image';
import { notFound } from 'next/navigation';

import Link from 'fumadocs-core/link';
import { ArrowLeftIcon } from 'lucide-react';
import Markdown from 'markdown-to-jsx';

import { Grid } from '@/components/grid-pattern';
import { getMDXComponents } from '@/components/mdx';
import { i18n } from '@/lib/i18n';
import { changelog } from '@/lib/source';
import { getTranslations } from 'next-intl/server';

export default async function ChangelogEntryPage({ params }: { params: Promise<{ slug: string; locale: string }> }) {
    const { slug, locale } = await params;
    const t = await getTranslations('changelog');
    const dateLocale = locale === 'ja' ? 'ja-JP' : 'en-US';

    const page = changelog.getPages(locale).find((p) => p.data.slug === slug || p.slugs[0] === slug);

    if (!page) {
        notFound();
    }

    const entry = page.data;
    const { body: Mdx } = await page.data.load();

    const articleSchema = {
        '@context': 'https://schema.org',
        '@type': 'Article',
        headline: entry.title,
        description: entry.summary ?? 'PSJ changelog entry',
        datePublished: entry.date,
        dateModified: entry.date,
        author: {
            '@type': 'Organization',
            name: 'PSJ',
            url: 'https://psj.ai',
        },
        publisher: {
            '@type': 'Organization',
            name: 'PSJ',
            url: 'https://psjdoc.e-technostar.com',
            logo: {
                '@type': 'ImageObject',
                url: 'https://psjdoc.e-technostar.com/favicon/android-chrome-512x512.png',
            },
        },
        mainEntityOfPage: {
            '@type': 'WebPage',
            '@id': `https://psjdoc.e-technostar.com/${locale}/changelog/${slug}`,
        },
        ...(entry.image && {
            image: {
                '@type': 'ImageObject',
                url: `https://psjdoc.e-technostar.com/${locale}/${entry.image.startsWith('/') ? entry.image.slice(1) : entry.image}`,
                width: 1200,
                height: 630,
            },
        }),
    };

    const breadcrumbSchema = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        itemListElement: [
            {
                '@type': 'ListItem',
                position: 1,
                name: t('nav.home'),
                item: 'https://psjdoc.e-technostar.com',
            },
            {
                '@type': 'ListItem',
                position: 2,
                name: t('header.title'),
                item: `https://psjdoc.e-technostar.com/${locale}/changelog`,
            },
            {
                '@type': 'ListItem',
                position: 3,
                name: entry.title,
                item: `https://psjdoc.e-technostar.com/${locale}/changelog/${slug}`,
            },
        ],
    };

    return (
        <>
            <script
                type="application/ld+json"
                dangerouslySetInnerHTML={{
                    __html: JSON.stringify(articleSchema),
                }}
            />
            <script
                type="application/ld+json"
                dangerouslySetInnerHTML={{
                    __html: JSON.stringify(breadcrumbSchema),
                }}
            />

            <div className="min-h-screen" style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}>
                <main className="psj-container psj-section">
                    <div className="max-w-4xl mx-auto">
                        <div className="mb-12 flex items-center justify-between">
                            <Link
                                href="/changelog"
                                className="inline-flex items-center text-sm font-bold transition-colors"
                                style={{ color: 'var(--psj-blue)' }}
                            >
                                <ArrowLeftIcon className="mr-2 h-4 w-4" />
                                {t('nav.backToChangelog')}
                            </Link>
                        </div>

                        <article className="prose prose-sm sm:prose-base dark:prose-invert max-w-none">
                            <header className="mb-10">
                                <h1 className="psj-h1 mb-6" style={{ color: 'var(--psj-text-1)' }}>
                                    {entry.title}
                                </h1>
                                <div style={{ color: 'var(--psj-text-2)' }}>
                                    {entry.summary && (
                                        <div className="text-lg leading-relaxed mb-4 prose prose-sm sm:prose-base dark:prose-invert max-w-none psj-prose">
                                            <Markdown options={{ wrapper: 'div' }}>{entry.summary}</Markdown>
                                        </div>
                                    )}
                                    <time dateTime={entry.date} className="text-sm font-mono uppercase tracking-wider">
                                        {new Date(entry.date).toLocaleDateString(dateLocale, {
                                            year: 'numeric',
                                            month: 'long',
                                            day: 'numeric',
                                        })}
                                    </time>
                                </div>
                            </header>

                            {entry.image ? (
                                <div className="mb-12">
                                    <Image
                                        src={entry.image}
                                        alt={entry.title}
                                        width={1200}
                                        height={630}
                                        className="w-full rounded-none object-cover border"
                                        style={{ borderColor: 'var(--psj-border)' }}
                                    />
                                </div>
                            ) : (
                                <div
                                    className="mb-12 w-full aspect-[2.5/1] sm:aspect-[3.5/1] flex flex-col justify-center relative overflow-hidden border rounded-lg"
                                    style={{
                                        background:
                                            'linear-gradient(135deg, var(--psj-surface-0) 0%, var(--psj-surface-1) 100%)',
                                        borderColor: 'var(--psj-border)',
                                    }}
                                >
                                    <Grid size={32} />
                                    <div
                                        className="absolute inset-0 opacity-[0.03]"
                                        style={{
                                            backgroundImage:
                                                'radial-gradient(var(--psj-text-1) 1.5px, transparent 1.5px)',
                                            backgroundSize: '32px 32px',
                                        }}
                                    />
                                    <div
                                        className="absolute right-4 top-4 text-[100px] sm:text-[160px] font-black tracking-tighter opacity-[0.04] leading-none select-none max-w-[50%]"
                                        style={{ color: 'var(--psj-text-1)' }}
                                    >
                                        {entry.version || 'PSJ'}
                                    </div>
                                    <div className="absolute -bottom-24 -left-24 w-96 h-96 bg-(--psj-blue) rounded-full blur-[128px] opacity-10" />

                                    <div className="relative z-10 px-8 sm:px-16 flex flex-col gap-4">
                                        <div
                                            className="inline-flex items-center w-fit border rounded-full px-4 py-1.5 text-xs font-bold uppercase tracking-widest bg-background/50 backdrop-blur-sm"
                                            style={{
                                                borderColor: 'var(--psj-border)',
                                                color: 'var(--psj-blue)',
                                            }}
                                        >
                                            {t('entry.releaseDetails')}
                                        </div>
                                        <div
                                            className="text-5xl sm:text-7xl font-black tracking-tighter"
                                            style={{ color: 'var(--psj-text-1)' }}
                                        >
                                            {entry.version || t('entry.defaultTitle')}
                                        </div>
                                    </div>
                                </div>
                            )}

                            {entry.highlights && entry.highlights.length > 0 && (
                                <div
                                    className="mb-12 p-6 rounded-lg border bg-(--psj-surface-1)"
                                    style={{ borderColor: 'var(--psj-border)' }}
                                >
                                    <h3
                                        className="text-xs font-bold uppercase tracking-widest mb-4"
                                        style={{ color: 'var(--psj-blue)' }}
                                    >
                                        {t('entry.highlights')}
                                    </h3>
                                    <ul className="space-y-2 list-disc list-inside">
                                        {entry.highlights.map((h, i) => (
                                            <li
                                                key={i}
                                                className="text-base leading-relaxed prose prose-sm sm:prose-base dark:prose-invert max-w-none psj-prose"
                                                style={{ color: 'var(--psj-text-1)' }}
                                            >
                                                <Markdown>{h}</Markdown>
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            )}

                            <div className="prose prose-sm sm:prose-base dark:prose-invert max-w-none">
                                <Mdx components={getMDXComponents({})} />
                            </div>
                        </article>
                    </div>
                </main>
            </div>
        </>
    );
}

export async function generateStaticParams() {
    return i18n.languages.flatMap((lang) =>
        changelog.getPages(lang).map((page) => ({
            lang,
            slug: page.data.slug || page.slugs[0],
        })),
    );
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string; locale: string }> }): Promise<Metadata> {
    const { slug, locale } = await params;

    const page = changelog.getPages(locale).find((p) => p.data.slug === slug || p.slugs[0] === slug);
    const entry = page?.data;

    if (!entry) {
        return {};
    }

    return {
        title: `${entry.title} - Changelog`,
        description: entry.summary ?? 'PSJ changelog entry',
        openGraph: {
            title: `${entry.title} - Changelog - PSJ`,
            description: entry.summary ?? 'PSJ changelog entry',
            type: 'article',
            images: entry.image
                ? [
                      {
                          url: entry.image,
                          width: 1200,
                          height: 630,
                          alt: entry.title,
                      },
                  ]
                : ['/opengraph.png'],
        },
        twitter: {
            card: 'summary_large_image',
            title: `${entry.title} - Changelog - PSJ`,
            description: entry.summary ?? 'PSJ changelog entry',
        },
    };
}
