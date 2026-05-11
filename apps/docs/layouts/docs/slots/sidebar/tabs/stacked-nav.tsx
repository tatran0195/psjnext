'use client';

import Link from 'next/link';
import { type ReactNode } from 'react';

// ─── Types ────────────────────────────────────────────────────────────────────

export interface AccordionNavOption {
    id: string;
    href: string;
    label: string;
    icon: ReactNode;
    external?: boolean;
    /** Hide this icon in the collapsed peek overlay (for overflow/deeply nested items) */
    hiddenWhenCollapsed?: boolean;
}

export interface AccordionNavProps {
    options: AccordionNavOption[];
    activeId?: string;
    collapsedLabel?: string;
    /** Gap in px between stacked icons in collapsed state. Defaults to 20 */
    collapsedIconGap?: number;
    /** Left padding in px before the first collapsed icon. Defaults to 12 */
    collapsedIconStartX?: number;
}

// ─── Arrow icon ───────────────────────────────────────────────────────────────

const ArrowRightIcon = () => (
    <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden
    >
        <line x1="5" y1="12" x2="19" y2="12" />
        <polyline points="12 5 19 12 12 19" />
    </svg>
);

// ─── Single item ──────────────────────────────────────────────────────────────

function AccordionNavItem({ href, label, icon, external, isActive }: AccordionNavOption & { isActive: boolean }) {
    return (
        <Link
            href={href}
            target={external ? '_blank' : undefined}
            rel={external ? 'nofollow noreferrer' : undefined}
            aria-label={label}
            aria-current={isActive ? 'page' : undefined}
            className={[
                'accordion-nav-item group/item',
                'relative flex items-center h-10 w-full no-underline',
                'transition-colors duration-200',
                isActive
                    ? 'bg-[#ebebed] dark:bg-[#242424]'
                    : 'bg-[#f6f6f7] dark:bg-[#1c1c1c] hover:bg-[#eff0f3] dark:hover:bg-[#282828]',
            ].join(' ')}
        >
            <div
                className={[
                    'relative z-[6] my-3 ml-3 mr-2 flex shrink-0 items-center justify-center size-6',
                    '[&_svg]:size-full [&_svg]:transition-colors [&_svg]:duration-200',
                    isActive
                        ? '[&_svg]:text-black dark:[&_svg]:text-white'
                        : '[&_svg]:text-[#8e8e8e] dark:[&_svg]:text-[#4d4d4d] group-hover/item:[&_svg]:text-black dark:group-hover/item:[&_svg]:text-white',
                ].join(' ')}
            >
                {icon}
            </div>

            <span
                className={[
                    'text-sm font-normal',
                    'opacity-0 group-hover/nav:opacity-100',
                    'transition-[color,opacity] duration-200',
                    isActive
                        ? 'text-black dark:text-white'
                        : 'text-[#909090] group-hover/item:text-black dark:group-hover/item:text-white',
                ].join(' ')}
            >
                {label}
            </span>

            <div
                className={[
                    'ml-auto mr-2 flex shrink-0 items-center justify-center size-8',
                    'text-black dark:text-white',
                    'opacity-0 -translate-x-1 transition-all duration-200',
                    'group-hover/item:opacity-100 group-hover/item:translate-x-0',
                    '[&_svg]:size-4',
                ].join(' ')}
            >
                <ArrowRightIcon />
            </div>
        </Link>
    );
}

// ─── Main ─────────────────────────────────────────────────────────────────────

const ICON_SIZE = 24; // px, matches size-6

export function AccordionNav({
    options,
    activeId,
    collapsedLabel = 'More options',
    collapsedIconGap = 20,
    collapsedIconStartX = 12,
}: AccordionNavProps) {
    const activeOption = options.find((o) => o.id === activeId);
    const peekLabel = activeOption?.label ?? collapsedLabel;

    // Only visible icons participate in the stacking layout
    const visibleOptions = options.filter((o) => !o.hiddenWhenCollapsed);

    // Compute left offset per visible icon index
    const iconLeftPx = (index: number) => collapsedIconStartX + index * collapsedIconGap;

    // Label starts right after the last icon
    const labelLeftPx =
        visibleOptions.length > 0 ? iconLeftPx(visibleOptions.length - 1) + ICON_SIZE + 8 : collapsedIconStartX;

    return (
        <>
            <style>{`
        .accordion-nav-item:not(:first-child) { margin-top: -41px; }
        .accordion-nav:hover .accordion-nav-item:not(:first-child) { margin-top: 0; }
      `}</style>

            <nav
                aria-label={peekLabel}
                className="accordion-nav group/nav relative mb-1 flex w-full flex-col gap-px overflow-hidden rounded-sm min-h-10"
            >
                {options.map((option) => (
                    <AccordionNavItem key={option.id} {...option} isActive={option.id === activeId} />
                ))}

                {/* Collapsed peek overlay */}
                <div
                    aria-hidden
                    className="pointer-events-none absolute inset-x-0 top-0 z-10 h-10 flex items-center select-none bg-[#f6f6f7] dark:bg-[#1c1c1c] transition-opacity duration-150 group-hover/nav:opacity-0"
                >
                    {/* Auto-positioned stacked icons */}
                    <div className="relative h-full flex items-center">
                        {visibleOptions.map((option, index) => (
                            <div
                                key={option.id}
                                className={[
                                    'absolute flex items-center justify-center size-6',
                                    '[&_svg]:size-full',
                                    option.id === activeId
                                        ? '[&_svg]:text-black dark:[&_svg]:text-white'
                                        : '[&_svg]:text-[#8e8e8e] dark:[&_svg]:text-[#4d4d4d]',
                                ].join(' ')}
                                style={{ left: iconLeftPx(index) }}
                            >
                                {option.icon}
                            </div>
                        ))}
                    </div>

                    {/* Peek label, auto-positioned after last icon */}
                    <span
                        className="text-sm text-[#909090] font-normal whitespace-nowrap"
                        style={{ marginLeft: labelLeftPx }}
                    >
                        {peekLabel}
                    </span>
                </div>
            </nav>
        </>
    );
}
