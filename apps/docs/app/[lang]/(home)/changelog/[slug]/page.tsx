import type { Metadata } from 'next';
import Image from 'next/image';
import Link from 'next/link';
import { notFound } from 'next/navigation';

import { ArrowLeftIcon } from 'lucide-react';
import Markdown from 'markdown-to-jsx';

import { changelog } from '@/lib/source';
import { getMarkdownOptions } from '@/lib/utils/markdown';

interface ChangelogEntryPageProps {
    params: Promise<{ slug: string }>;
}

export default async function ChangelogEntryPage({ params }: ChangelogEntryPageProps) {
    const { slug } = await params;

    const entry = changelog.getPages().find((entry) => entry.data.slug === slug)?.data;

    if (!entry) {
        notFound();
    }

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
            url: 'https://psj.ai',
            logo: {
                '@type': 'ImageObject',
                url: 'https://psj.ai/favicon/android-chrome-512x512.png',
            },
        },
        mainEntityOfPage: {
            '@type': 'WebPage',
            '@id': `https://psj.ai/changelog/${slug}`,
        },
        ...(entry.image && {
            image: {
                '@type': 'ImageObject',
                url: entry.image.src.startsWith('http')
                    ? entry.image.src
                    : `https://psj.ai${entry.image.src}`,
                width: entry.image.width,
                height: entry.image.height,
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
                name: 'Home',
                item: 'https://psj.ai',
            },
            {
                '@type': 'ListItem',
                position: 2,
                name: 'Changelog',
                item: 'https://psj.ai/changelog',
            },
            {
                '@type': 'ListItem',
                position: 3,
                name: entry.title,
                item: `https://psj.ai/changelog/${slug}`,
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

            <div 
                className="min-h-screen"
                style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)' }}
            >
                <main className="psj-container psj-section">
                    <div className="max-w-4xl mx-auto">
                        <div className="mb-12 flex items-center justify-between">
                            <Link
                                href="/changelog"
                                className="inline-flex items-center text-sm font-bold transition-colors"
                                style={{ color: 'var(--psj-blue)' }}
                            >
                                <ArrowLeftIcon className="mr-2 h-4 w-4" />
                                Back to changelog
                            </Link>
                        </div>

                        <article className="prose prose-sm sm:prose-base dark:prose-invert max-w-none">
                            <header className="mb-10">
                                <div className="psj-label mb-3">Changelog Update</div>
                                <h1 className="psj-h1 mb-6" style={{ color: 'var(--psj-text-1)' }}>{entry.title}</h1>
                                <div style={{ color: 'var(--psj-text-2)' }}>
                                    {entry.summary && (
                                        <p className="text-lg leading-relaxed mb-4">{entry.summary}</p>
                                    )}
                                    <time dateTime={entry.date} className="text-sm font-mono uppercase tracking-wider">
                                        {new Date(entry.date).toLocaleDateString('en-US', {
                                            year: 'numeric',
                                            month: 'long',
                                            day: 'numeric',
                                        })}
                                    </time>
                                </div>
                            </header>

                            {entry.image && (
                                <div className="mb-12">
                                    <Image
                                        src={entry.image.src}
                                        alt={entry.image.alt ?? entry.title}
                                        width={entry.image.width}
                                        height={entry.image.height}
                                        className="w-full rounded-none object-cover border"
                                        style={{ borderColor: 'var(--psj-border)' }}
                                    />
                                </div>
                            )}

                            <div className="prose prose-sm sm:prose-base dark:prose-invert max-w-none">
                                <Markdown options={getMarkdownOptions()}>
                                    {entry.id}
                                </Markdown>
                            </div>
                        </article>
                    </div>
                </main>
            </div>
        </>
    );
}

export async function generateStaticParams() {
    return changelog.getPages().map((page) => ({ slug: page.data.slug }));
}

export async function generateMetadata({ params }: ChangelogEntryPageProps): Promise<Metadata> {
    const { slug } = await params;

    const entry = changelog.getPage([slug])?.data;

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
                          url: entry.image.src,
                          width: entry.image.width ?? 800,
                          height: entry.image.height ?? 400,
                          alt: entry.image.alt ?? entry.title,
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
