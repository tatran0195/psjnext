import React from 'react';

import { cn } from '@/lib/cn';

import { ArrowRight } from './icons';
import { AsidePostItem } from './types';

// ─── Peek layout helper ───────────────────────────────────────────────────────

/**
 * Margin-left (px) for an icon at the given collapsed peek slot.
 *
 * slot 0 → 12   (base ml-3, no override needed)
 * slot 1 → 32   (+20)
 * slot n ≥ 2 → 32 + (n-1)*24
 */
export function peekMarginLeft(slot: number): number {
    if (slot === 0) return 12;
    if (slot === 1) return 32;
    return 32 + (slot - 1) * 24;
}

// ─── ItemMeta ─────────────────────────────────────────────────────────────────

export type ItemMeta = {
    /** Visual left-offset slot in the collapsed stack; null = hidden. */
    peekSlot: number | null;
    /** True for the active item when it has been swapped into the last visible slot. */
    activeInPeek: boolean;
};

/**
 * Derive peek-slot metadata for every item.
 *
 * Rules:
 * 1. Items at natural index < collapsedCount occupy their own slot.
 * 2. Items at natural index >= collapsedCount are hidden in peek.
 * 3. If the active item is hidden, it is swapped into slot (collapsedCount-1),
 *    displacing the item that was naturally there.
 */
export function buildMetas(items: Array<{ active: boolean }>, collapsedCount: number): ItemMeta[] {
    const activeIndex = items.findIndex((item) => item.active);
    const activeIsHidden = activeIndex !== -1 && activeIndex >= collapsedCount;
    const lastSlot = collapsedCount - 1;

    return items.map((item, i) => {
        if (item.active && activeIsHidden) {
            return { peekSlot: lastSlot, activeInPeek: true };
        }
        if (!item.active && activeIsHidden && i === lastSlot) {
            return { peekSlot: null, activeInPeek: false };
        }
        if (i < collapsedCount) {
            return { peekSlot: i, activeInPeek: false };
        }
        return { peekSlot: null, activeInPeek: false };
    });
}

// ─── IconWrapper ──────────────────────────────────────────────────────────────

interface IconWrapperProps {
    peekMarginLeftPx: number | null;
    hiddenInPeek: boolean;
    active: boolean;
    activeInPeek: boolean;
    children: React.ReactNode;
}

// const BRIGHT_COLORS = cn('[&_svg]:text-black! dark:[&_svg]:text-white!');

export function IconWrapper({ peekMarginLeftPx, hiddenInPeek, active, activeInPeek: _, children }: IconWrapperProps) {
    const style: React.CSSProperties =
        peekMarginLeftPx !== null && peekMarginLeftPx !== 12 ? { marginLeft: peekMarginLeftPx } : {};

    return (
        <div
            className={cn(
                'relative z-6 shrink-0 flex items-center justify-center w-6 h-6',
                'mt-3 mr-2 mb-3 ml-3',
                'scale-80',
                'transition-[margin-left,transform,opacity] duration-150',

                hiddenInPeek ? 'opacity-0' : 'opacity-100',
                'group-hover/container:ml-3! group-hover/container:scale-100! group-hover/container:opacity-100!',

                // Active: only force opacity — margin-left is correct via inline style
                // (collapsed) and group-hover/container:ml-3! (expanded).
                active && 'opacity-100!',

                '[&_svg]:h-full [&_svg]:w-full',
                '[&_svg]:text-[#8e8e8e] dark:[&_svg]:text-[#4d4d4d]',
                '[&_svg]:transition-colors [&_svg]:duration-200 [&_svg]:ease-in-out',

                'group-hover/row:[&_svg]:text-black dark:group-hover/row:[&_svg]:text-white',

                // highlight active icon on hover-group
                // (active || activeInPeek) && BRIGHT_COLORS,
                active && 'group-hover/container:[&_svg]:text-black! dark:group-hover/container:[&_svg]:text-white!',
            )}
            style={style}
        >
            {children}
        </div>
    );
}

// ─── DockRailRow ──────────────────────────────────────────────────────────────

interface DockRailRowProps {
    item: AsidePostItem & { active: boolean };
    meta: ItemMeta;
    index: number;
    onItemClick?: (item: AsidePostItem) => void;
}

const ROW_BASE = cn(
    'h-10 w-full flex items-center',
    'bg-[#f6f6f7] dark:bg-[#1c1c1c]',
    'transition-[background-color,margin-top] duration-150 ease-in-out',
    'group-hover/container:mt-0!',
);

export function DockRailRow({ item, meta, index, onItemClick }: DockRailRowProps) {
    const stackStyle: React.CSSProperties = index > 0 ? { marginTop: -41 } : {};

    const iconMarginLeftPx = meta.peekSlot !== null ? peekMarginLeft(meta.peekSlot) : null;

    const inner = (
        <>
            <IconWrapper
                peekMarginLeftPx={iconMarginLeftPx}
                hiddenInPeek={meta.peekSlot === null}
                active={item.active}
                activeInPeek={meta.activeInPeek}
            >
                {item.icon}
            </IconWrapper>

            <div
                className={cn(
                    'text-sm font-normal text-[#909090]',
                    'transition-[color,opacity] duration-150 ease-in-out',
                    'opacity-0 group-hover/container:opacity-100',
                    'group-hover/row:text-black dark:group-hover/row:text-white',
                    item.active && 'opacity-100! text-black! font-medium! dark:text-white!',
                )}
            >
                {item.text}
            </div>

            {!item.disabled && (
                <div
                    className={cn(
                        'shrink-0 flex items-center justify-center w-8 h-8 ml-auto mr-2',
                        'opacity-0 -translate-x-1',
                        'transition-all duration-200 ease-in-out',
                        '[&_svg]:h-4 [&_svg]:w-4',
                        '[&_svg]:text-black dark:[&_svg]:text-white',
                        'group-hover/row:opacity-100 group-hover/row:translate-x-0',
                        item.active && 'opacity-100! translate-x-0!',
                    )}
                >
                    <ArrowRight />
                </div>
            )}
        </>
    );

    const rowCn = cn(ROW_BASE, item.active && 'bg-[#eff0f3]! dark:bg-[#282828]!');

    if (item.disabled) {
        return (
            <span
                key={item.href + item.text}
                className={cn(rowCn, 'cursor-default pointer-events-none opacity-45')}
                style={stackStyle}
            >
                {inner}
            </span>
        );
    }

    return (
        <a
            key={item.href + item.text}
            href={item.href}
            className={cn('group/row no-underline', rowCn, 'hover:bg-[#eff0f3] dark:hover:bg-[#282828]')}
            style={stackStyle}
            onClick={onItemClick ? () => onItemClick(item) : undefined}
            {...(item.external ? { target: '_blank', rel: 'nofollow noreferrer' } : {})}
        >
            {inner}
        </a>
    );
}
