import { useMemo } from 'react';

import { cn } from '@/lib/cn';

import { buildMetas, DockRailRow, peekMarginLeft } from './internals';
import { DEFAULT_ITEMS, DockRailProps } from './types';

export * from './icons';
export { DEFAULT_ITEMS } from './types';
export type { AsidePostItem, DockRailProps } from './types';

export function DockRail({
    items = DEFAULT_ITEMS,
    activeHref,
    collapsedCount: rawCollapsedCount = 3,
    collapsedLabel = 'Our goodies!',
    className,
    onItemClick,
}: DockRailProps) {
    const collapsedCount = Math.min(Math.max(rawCollapsedCount, 0), items.length);
    const lastSlot = collapsedCount - 1;

    const resolvedItems = useMemo(
        () =>
            items.map((item) => ({
                ...item,
                active:
                    activeHref !== undefined ? item.href === activeHref : (item.active ?? false),
            })),
        [items, activeHref],
    );

    const activeItem = useMemo(
        () => resolvedItems.find((item) => item.active) ?? null,
        [resolvedItems],
    );

    const metas = useMemo(
        () => buildMetas(resolvedItems, collapsedCount),
        [resolvedItems, collapsedCount],
    );

    const overlayText: string | null =
        activeItem?.text ?? (collapsedLabel !== false ? (collapsedLabel as string) : null);

    return (
        <div
            className={cn(
                'group/container',
                'relative flex flex-col gap-px w-full min-h-10',
                'rounded-none overflow-hidden',
                className,
            )}
        >
            {resolvedItems.map((item, index) => (
                <DockRailRow
                    key={item.href + item.text}
                    item={item}
                    meta={metas[index]}
                    index={index}
                    onItemClick={onItemClick}
                />
            ))}

            {overlayText !== null && (
                <div
                    className={cn(
                        'absolute top-0 z-1 h-10 w-full pointer-events-none',
                        'flex items-center overflow-hidden pr-3',
                        'bg-[#f6f6f7] dark:bg-[#1c1c1c]',
                        'transition-opacity duration-250',
                        'opacity-100 group-hover/container:opacity-0 group-hover/container:z-[-1]',
                    )}
                    style={{ paddingLeft: peekMarginLeft(lastSlot) + 40 }}
                >
                    <span
                        className={cn(
                            'text-sm font-normal text-[#909090] truncate',
                            // activeItem && 'text-black! dark:text-white! font-medium!',
                        )}
                    >
                        {overlayText}
                    </span>
                </div>
            )}
        </div>
    );
}
