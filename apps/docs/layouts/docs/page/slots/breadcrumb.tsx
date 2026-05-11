'use client';

import { type ComponentProps, Fragment, useMemo } from 'react';

import { type BreadcrumbOptions, getBreadcrumbItemsFromPath } from 'fumadocs-core/breadcrumb';
import Link from 'fumadocs-core/link';
import { useTreeContext, useTreePath } from 'fumadocs-ui/contexts/tree';
import { ChevronRight } from 'lucide-react';

import { cn } from '@/lib/cn';

export type BreadcrumbProps = BreadcrumbOptions & ComponentProps<'div'>;

export function Breadcrumb({ includeRoot, includeSeparator, includePage, ...props }: BreadcrumbProps) {
    const path = useTreePath();
    const { root } = useTreeContext();
    const items = useMemo(() => {
        return getBreadcrumbItemsFromPath(root, path, {
            includePage,
            includeSeparator,
            includeRoot,
        });
    }, [includePage, includeRoot, includeSeparator, path, root]);

    if (items.length === 0) return null;

    return (
        <div
            {...props}
            className={cn('flex items-center gap-2 text-xs', props.className)}
            style={{ color: 'var(--psj-text-3)', ...props.style }}
        >
            {items.map((item, i) => {
                const isLast = i === items.length - 1;
                const className = cn('truncate', isLast && 'font-medium');

                return (
                    <Fragment key={i}>
                        {i !== 0 && <ChevronRight size={11} className="shrink-0" />}
                        {item.url ? (
                            <Link
                                href={item.url}
                                className={cn(className, 'transition-colors hover:opacity-80')}
                                style={{
                                    color: isLast ? 'var(--psj-text-1)' : 'var(--psj-text-3)',
                                }}
                            >
                                {item.name}
                            </Link>
                        ) : (
                            <span
                                className={className}
                                style={{
                                    color: isLast ? 'var(--psj-text-1)' : 'var(--psj-text-3)',
                                }}
                            >
                                {item.name}
                            </span>
                        )}
                    </Fragment>
                );
            })}
        </div>
    );
}
