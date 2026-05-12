'use client';

import type { ComponentProps } from 'react';

import { cn } from '@/lib/cn';

import { useDocsPage } from '..';

export function Container(props: ComponentProps<'article'>) {
    const {
        props: { full },
    } = useDocsPage();

    return (
        <article
            id="nd-page"
            data-full={full}
            {...props}
            className={cn(
                'flex flex-col [grid-area:main] px-4 py-6 gap-4 md:px-6 md:pt-8 xl:px-8 xl:pt-10 mx-auto w-full max-w-[1040px] min-w-0',
                full && 'max-w-[1440px]',
                props.className,
            )}
        >
            {props.children}
        </article>
    );
}
