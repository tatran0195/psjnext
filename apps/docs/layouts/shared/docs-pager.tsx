'use client';

import Link from 'next/link';

import { ChevronLeft, ChevronRight, FoldHorizontal, UnfoldHorizontal } from 'lucide-react';

import { useDocsPage } from '@/layouts/docs/page';
import { MarkdownCopyButton } from '@/layouts/shared/page-actions';

type PagerItem = {
    url: string;
};

type DocsPagerProps = {
    previous?: PagerItem;
    next?: PagerItem;
    markdownUrl?: string;
};

export function DocsPager({ previous, next, markdownUrl }: DocsPagerProps) {
    const {
        props: { full, setFull },
    } = useDocsPage();

    const buttonClass =
        'flex size-7 items-center justify-center rounded-none bg-muted/50 text-muted-foreground transition-colors hover:bg-muted hover:text-foreground sm:size-8';
    const disabledClass =
        'flex size-7 items-center justify-center rounded-none bg-muted/30 text-muted-foreground/40 cursor-not-allowed sm:size-8';

    return (
        <div className="flex items-center gap-1">
            <button
                type="button"
                className={buttonClass}
                onClick={() => setFull(!full)}
                title={full ? 'Collapse' : 'Expand'}
            >
                {full ? <FoldHorizontal className="size-4" /> : <UnfoldHorizontal className="size-4" />}
            </button>
            {previous ? (
                <Link href={previous.url} className={buttonClass}>
                    <ChevronLeft className="size-4" />
                </Link>
            ) : (
                <div className={disabledClass}>
                    <ChevronLeft className="size-4" />
                </div>
            )}
            {next ? (
                <Link href={next.url} className={buttonClass}>
                    <ChevronRight className="size-4" />
                </Link>
            ) : (
                <div className={disabledClass}>
                    <ChevronRight className="size-4" />
                </div>
            )}
            {markdownUrl && (
                <MarkdownCopyButton markdownUrl={markdownUrl} title="Copy markdown" className={buttonClass} />
            )}
        </div>
    );
}
