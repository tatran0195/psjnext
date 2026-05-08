import React from 'react';

// ─── Icons ────────────────────────────────────────────────────────────────────

const ArrowRight = () => (
    <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
    >
        <line x1="5" y1="12" x2="19" y2="12" />
        <polyline points="12 5 19 12 12 19" />
    </svg>
);

export const BenchmarksIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
        <path
            fill="currentColor"
            fillRule="evenodd"
            clipRule="evenodd"
            d="M8.732 5.771L5.67 9.914c-1.285 1.739-1.928 2.608-1.574 3.291l.018.034c.375.673 1.485.673 3.704.673c1.233 0 1.85 0 2.236.363l.02.02l3.872-4.57l-.02-.02c-.379-.371-.379-.963-.379-2.148v-.31c0-3.285 0-4.927-.923-5.21c-.923-.283-1.913 1.056-3.892 3.734"
        />
        <path
            fill="currentColor"
            opacity=".5"
            d="M10.453 16.443v.31c0 3.284 0 4.927.923 5.21c.923.283 1.913-1.056 3.893-3.734l3.062-4.143c1.284-1.739 1.927-2.608 1.573-3.291a1.353 1.353 0 0 0-.018-.034c-.375-.673-1.485-.673-3.704-.673c-1.233 0-1.85 0-2.236-.363l-3.872 4.57c.379.371.379.963.379 2.148"
        />
    </svg>
);

export const ExtensionIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
        <path
            fill="currentColor"
            fillRule="evenodd"
            clipRule="evenodd"
            d="m20.83 10.715l-.518 1.932c-.605 2.255-.907 3.383-1.592 4.114a4 4 0 0 1-2.01 1.161c-.097.023-.195.04-.295.052c-.915.113-2.032-.186-4.064-.73c-2.255-.605-3.383-.907-4.114-1.592a4 4 0 0 1-1.161-2.011c-.228-.976.074-2.103.679-4.358l.517-1.932l.244-.905c.455-1.666.761-2.583 1.348-3.21a4 4 0 0 1 2.01-1.16c.976-.228 2.104.074 4.36.679c2.254.604 3.382.906 4.113 1.59a4 4 0 0 1 1.161 2.012c.228.976-.075 2.103-.679 4.358m-9.778-.91a.75.75 0 0 1 .919-.53l4.83 1.295a.75.75 0 1 1-.389 1.448l-4.83-1.294a.75.75 0 0 1-.53-.918m-.776 2.898a.75.75 0 0 1 .918-.53l2.898.777a.75.75 0 1 1-.388 1.448l-2.898-.776a.75.75 0 0 1-.53-.919"
        />
        <path
            fill="currentColor"
            opacity="0.5"
            d="M16.415 17.975a4 4 0 0 1-1.068 1.677c-.731.685-1.859.987-4.114 1.591s-3.383.907-4.358.679a4 4 0 0 1-2.011-1.161c-.685-.731-.988-1.859-1.592-4.114l-.517-1.932c-.605-2.255-.907-3.383-.68-4.358a4 4 0 0 1 1.162-2.011c.731-.685 1.859-.987 4.114-1.592c.426-.114.813-.218 1.165-.309l-.244.906l-.517 1.932c-.605 2.255-.907 3.382-.68 4.358a4 4 0 0 0 1.162 2.011c.731.685 1.859.987 4.114 1.592c2.032.544 3.149.843 4.064.73"
        />
    </svg>
);

export const StudioIcon = () => (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
            className="togglelib-icon-primary"
            d="M12 2C16.714 2 19.071 2 20.535 3.464C21.615 4.544 21.899 6.111 21.974 8.75L22 9.5H2.026V8.75C2.101 6.11 2.384 4.545 3.464 3.464C4.93 2 7.286 2 12 2Z"
        />
        <path
            className="togglelib-icon-tertiary"
            d="M13 6C13 6.26522 12.8946 6.51957 12.7071 6.70711C12.5196 6.89464 12.2652 7 12 7C11.7348 7 11.4804 6.89464 11.2929 6.70711C11.1054 6.51957 11 6.26522 11 6C11 5.73478 11.1054 5.48043 11.2929 5.29289C11.4804 5.10136 11.7348 5 12 5C12.2652 5 12.5196 5.10536 12.7071 5.29289C12.8946 5.48043 13 5.73478 13 6ZM10 6C10 6.26522 9.89464 6.51957 9.70711 6.70711C9.51957 6.89464 9.26522 7 9 7C8.73478 7 8.48043 6.89464 8.29289 6.70711C8.10536 6.51957 8 6.26522 8 6C8 5.73478 8.10536 5.48043 8.29289 5.29289C8.48043 5.10136 8.73478 5 9 5C9.26522 5 9.51957 5.10536 9.70711 5.29289C9.89464 5.48043 10 5.73478 10 6ZM7 6C7 6.26522 6.89464 6.51957 6.70711 6.70711C6.51957 6.89464 6.26522 7 6 7C5.73478 7 5.48043 6.89464 5.29289 6.70711C5.10536 6.51957 5 6.26522 5 6C5 5.73478 5.10536 5.48043 5.29289 5.29289C5.48043 5.10136 5.73478 5 6 5C6.26522 5 6.51957 5.10536 6.70711 5.29289C6.89464 5.48043 7 5.73478 7 6Z"
        />
        <path
            className="togglelib-icon-secondary"
            d="M2 12C2 16.714 2 19.071 3.464 20.535C4.474 21.545 5.91 21.859 8.25 21.956L9 22V9.5H2.026L2.003 10.25C2 10.794 2 11.377 2 12Z"
        />
        <path
            className="togglelib-icon-tertiary"
            d="M22 12C22 16.714 22 19.071 20.535 20.535C19.072 22 16.714 22 12 22C11.181 22 9.684 22 9 21.992V9.5H22L21.997 10.25C22 10.794 22 11.377 22 12Z"
        />
    </svg>
);

export const PackageIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
        <path
            fill="currentColor"
            d="M8.422 20.618C10.178 21.54 11.056 22 12 22V12L2.638 7.073a3.196 3.196 0 0 0-.04.067C2 8.154 2 9.417 2 11.942v.117c0 2.524 0 3.787.597 4.801c.598 1.015 1.674 1.58 3.825 2.709z"
        />
        <path
            fill="currentColor"
            opacity="0.7"
            d="m17.577 4.432l-2-1.05C13.822 2.461 12.944 2 12 2c-.945 0-1.822.46-3.578 1.382l-2 1.05C4.318 5.536 3.242 6.1 2.638 7.072L12 12l9.362-4.927c-.606-.973-1.68-1.537-3.785-2.641"
        />
        <path
            fill="currentColor"
            opacity="0.5"
            d="M21.403 7.14a3.153 3.153 0 0 0-.041-.067L12 12v10c.944 0 1.822-.46 3.578-1.382l2-1.05c2.151-1.129 3.227-1.693 3.825-2.708c.597-1.014.597-2.277.597-4.8v-.117c0-2.525 0-3.788-.597-4.802"
        />
        <path
            fill="currentColor"
            d="m6.323 4.484l.1-.052l1.493-.784l9.1 5.005l4.025-2.011c.137.155.257.32.362.498c.15.254.262.524.346.825L17.75 9.964V13a.75.75 0 0 1-1.5 0v-2.286l-3.5 1.75v9.44A3.062 3.062 0 0 1 12 22c-.248 0-.493-.032-.75-.096v-9.44l-8.998-4.5c.084-.3.196-.57.346-.824a3.15 3.15 0 0 1 .362-.498l9.04 4.52l3.387-1.693z"
        />
    </svg>
);

export const PlayIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
        <path
            className="play-path"
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="1.5"
            d="M6.906 4.537A.6.6 0 0 0 6 5.053v13.894a.6.6 0 0 0 .906.516l11.723-6.947a.6.6 0 0 0 0-1.032L6.906 4.537Z"
        />
    </svg>
);

// ─── Types ────────────────────────────────────────────────────────────────────

export interface AsidePostItem {
    href: string;
    text: string;
    icon: React.ReactNode;
    external?: boolean;
    active?: boolean;
    disabled?: boolean;
}

export interface AsidePostsProps {
    items?: AsidePostItem[];
    /**
     * Href to auto-mark as active. Takes precedence over per-item `active` flag.
     */
    activeHref?: string;
    /**
     * How many icons to show stacked in the collapsed peek state.
     * The active item's icon is always guaranteed to appear within this range,
     * replacing the last slot if it would otherwise be hidden.
     * @default 3
     */
    collapsedCount?: number;
    /**
     * Text shown in the collapsed overlay when no item is active.
     * Pass `false` to suppress the overlay entirely.
     * @default "Our goodies!"
     */
    collapsedLabel?: string | false;
    className?: string;
    onItemClick?: (item: AsidePostItem) => void;
}

// ─── Default items ────────────────────────────────────────────────────────────

export const DEFAULT_ITEMS: AsidePostItem[] = [
    { href: '/benchmarks', text: 'Benchmarks', icon: <BenchmarksIcon /> },
    {
        href: 'https://driz.link/extension',
        text: 'Extension',
        icon: <ExtensionIcon />,
        external: true,
    },
    { href: '/drizzle-studio/overview', text: 'Studio', icon: <StudioIcon /> },
    {
        href: 'https://github.com/drizzle-team/drizzle-studio-npm',
        text: 'Studio Package',
        icon: <PackageIcon />,
        external: true,
    },
    {
        href: 'https://gateway.drizzle.team',
        text: 'Gateway',
        icon: <PackageIcon />,
        external: true,
    },
    { href: 'https://drizzle.run', text: 'Drizzle Run', icon: <PlayIcon /> },
];

// ─── Helpers ──────────────────────────────────────────────────────────────────

function cn(...parts: Array<string | false | undefined | null>): string {
    return parts.filter(Boolean).join(' ');
}

/**
 * Compute the margin-left for each icon in the collapsed peek stack.
 *
 * Original CSS nth-child offsets (base margin-left is 12px / ml-3):
 *   peek slot 0 → 12 px  (no override — base ml-3)
 *   peek slot 1 → 32 px
 *   peek slot 2 → 56 px
 *   peek slot 3 → 80 px  (and so on, +24px per extra slot)
 *
 * The formula generalises to: 12 + slot * 20 px
 * Slot 0: 12 + 0*20 = 12 (no override needed)
 * Slot 1: 12 + 1*20 = 32 ✓
 * Slot 2: 12 + 2*20 = 52 — original uses 56, so it's actually +24 after slot 1.
 * Re-checking original: slot0=12, slot1=32 (+20), slot2=56 (+24), slot3=80 (+24).
 * Generalise: slot 0→12, slot 1→32, slot n≥2 → 32 + (n-1)*24
 */
function peekMarginLeft(slot: number): number {
    if (slot === 0) return 12;
    if (slot === 1) return 32;
    return 32 + (slot - 1) * 24;
}

// ─── Sub-components ───────────────────────────────────────────────────────────

interface IconWrapperProps {
    /**
     * Margin-left in the collapsed state (px). Applied as inline style so it can
     * be overridden by `group-hover/container:ml-3!` on expand.
     * Pass `null` for items that are not visible in the peek (they use default ml-3).
     */
    peekMarginLeftPx: number | null;
    /** True for items beyond the collapsedCount — hidden in peek, shown on expand. */
    hiddenInPeek: boolean;
    active: boolean;
    /** Highlight this icon in the peek overlay (active item swapped into last slot). */
    activeInPeek: boolean;
    children: React.ReactNode;
}

function IconWrapper({
    peekMarginLeftPx,
    hiddenInPeek,
    active,
    activeInPeek,
    children,
}: IconWrapperProps) {
    /**
     * Inline style carries only the margin-left stagger offset.
     * Opacity is kept as a class so group-hover can override it.
     */
    const style: React.CSSProperties =
        peekMarginLeftPx !== null && peekMarginLeftPx !== 12
            ? { marginLeft: peekMarginLeftPx }
            : {};

    return (
        <div
            className={cn(
                // size + base margin (12px 8px 12px 12px)
                'relative z-[6] flex items-center justify-center w-6 h-6',
                'mt-3 mr-2 mb-3 ml-3',
                // collapsed: scaled down
                'scale-80',
                'transition-[margin-left,transform,opacity] duration-150',

                // ── Opacity ──────────────────────────────────────────────────
                // Hidden-in-peek items start invisible; revealed on expand.
                hiddenInPeek ? 'opacity-0' : 'opacity-100',
                // Container hover: reset margin-left to 12px, full scale, fully visible.
                'group-hover/container:ml-3! group-hover/container:scale-100! group-hover/container:opacity-100!',
                // Active: force margin and opacity but NOT scale — scale stays
                // scale-80 in collapsed state, and is reset to scale-100 only
                // via group-hover/container (same as all other icons).
                active && 'ml-3! opacity-100!',

                // ── Default SVG colours ──────────────────────────────────────
                '[&_svg]:h-full [&_svg]:w-full',
                '[&_svg]:text-[#8e8e8e] dark:[&_svg]:text-[#4d4d4d]',
                '[&_svg]:transition-colors [&_svg]:duration-200 [&_svg]:ease-in-out',

                // togglelib fills — default
                '[&_.togglelib-icon-primary]:fill-[#737373]   dark:[&_.togglelib-icon-primary]:fill-[#424242]',
                '[&_.togglelib-icon-secondary]:fill-[#9d9d9d] dark:[&_.togglelib-icon-secondary]:fill-[#565656]',
                '[&_.togglelib-icon-tertiary]:fill-[#b9b9b9]  dark:[&_.togglelib-icon-tertiary]:fill-[#737373]',
                '[&_.togglelib-icon-primary]:transition-[fill]   [&_.togglelib-icon-primary]:duration-150',
                '[&_.togglelib-icon-secondary]:transition-[fill] [&_.togglelib-icon-secondary]:duration-150',
                '[&_.togglelib-icon-tertiary]:transition-[fill]  [&_.togglelib-icon-tertiary]:duration-150',
                '[&_.play-path]:fill-[#c4c4c4] dark:[&_.play-path]:fill-[#333333]',

                // ── Row hover (scoped via group/row on parent <a>) ───────────
                'group-hover/row:[&_svg]:text-black                           dark:group-hover/row:[&_svg]:text-white',
                'group-hover/row:[&_.togglelib-icon-primary]:fill-black       dark:group-hover/row:[&_.togglelib-icon-primary]:fill-[#858586]',
                'group-hover/row:[&_.togglelib-icon-secondary]:fill-[#818283] dark:group-hover/row:[&_.togglelib-icon-secondary]:fill-[#b3b4b5]',
                'group-hover/row:[&_.togglelib-icon-tertiary]:fill-[#cccccc]  dark:group-hover/row:[&_.togglelib-icon-tertiary]:fill-[#f9fafb]',

                // ── Active row: permanently bright ───────────────────────────
                active &&
                    cn(
                        '[&_svg]:text-black!                              dark:[&_svg]:text-white!',
                        '[&_.togglelib-icon-primary]:fill-black!          dark:[&_.togglelib-icon-primary]:fill-[#858586]!',
                        '[&_.togglelib-icon-secondary]:fill-[#818283]!    dark:[&_.togglelib-icon-secondary]:fill-[#b3b4b5]!',
                        '[&_.togglelib-icon-tertiary]:fill-[#cccccc]!     dark:[&_.togglelib-icon-tertiary]:fill-[#f9fafb]!',
                    ),

                // ── Active-in-peek: highlighted even when row is not active ──
                // (the active item's icon swapped into the last visible peek slot)
                !active &&
                    activeInPeek &&
                    cn(
                        '[&_svg]:text-black!                              dark:[&_svg]:text-white!',
                        '[&_.togglelib-icon-primary]:fill-black!          dark:[&_.togglelib-icon-primary]:fill-[#858586]!',
                        '[&_.togglelib-icon-secondary]:fill-[#818283]!    dark:[&_.togglelib-icon-secondary]:fill-[#b3b4b5]!',
                        '[&_.togglelib-icon-tertiary]:fill-[#cccccc]!     dark:[&_.togglelib-icon-tertiary]:fill-[#f9fafb]!',
                    ),
            )}
            style={style}
        >
            {children}
        </div>
    );
}

// ─── Component ────────────────────────────────────────────────────────────────

export function AsidePosts({
    items = DEFAULT_ITEMS,
    activeHref,
    collapsedCount: rawCollapsedCount = 3,
    collapsedLabel = 'Our goodies!',
    className,
    onItemClick,
}: AsidePostsProps) {
    const collapsedCount = Math.min(Math.max(rawCollapsedCount, 0), items.length);

    // ── Resolve active flags ───────────────────────────────────────────────────
    const resolvedItems = items.map((item) => ({
        ...item,
        active: activeHref !== undefined ? item.href === activeHref : (item.active ?? false),
    }));

    const activeIndex = resolvedItems.findIndex((item) => item.active);
    const activeItem = activeIndex !== -1 ? resolvedItems[activeIndex] : null;

    /**
     * Peek slot assignment
     * ─────────────────────
     * collapsedCount determines how many icons are visible stacked in the
     * collapsed state (0-indexed slots 0…collapsedCount-1).
     *
     * Rules:
     * 1. Items at natural index < collapsedCount occupy their own slot.
     * 2. Items at natural index >= collapsedCount are hidden in peek.
     * 3. If the active item is hidden (its natural index >= collapsedCount),
     *    it is assigned to slot (collapsedCount - 1) — the last visible slot —
     *    replacing whatever was naturally there visually (via margin-left).
     *    The displaced item keeps its natural render position but becomes hidden.
     *
     * `peekSlot`: the visual slot index in the collapsed stack (null = hidden).
     * `activeInPeek`: true only for the active item when it is swapped into
     *                 the last slot so its icon gets the highlighted colour.
     */
    const activeIsHidden = activeIndex !== -1 && activeIndex >= collapsedCount;
    const lastSlot = collapsedCount - 1;

    type ItemMeta = {
        peekSlot: number | null; // visual left-offset slot; null = hidden
        activeInPeek: boolean; // swapped-in active icon highlight
    };

    const metas: ItemMeta[] = resolvedItems.map((item, i) => {
        if (item.active && activeIsHidden) {
            // Active item is beyond collapsedCount — swap into last slot
            return { peekSlot: lastSlot, activeInPeek: true };
        }
        if (!item.active && activeIsHidden && i === lastSlot) {
            // The item naturally at the last slot is displaced — hide it in peek
            return { peekSlot: null, activeInPeek: false };
        }
        if (i < collapsedCount) {
            return { peekSlot: i, activeInPeek: false };
        }
        return { peekSlot: null, activeInPeek: false };
    });

    // ── Overlay label ──────────────────────────────────────────────────────────
    // Priority: active item text > collapsedLabel > null (no overlay)
    const overlayText: string | null =
        activeItem?.text ?? (collapsedLabel !== false ? (collapsedLabel as string) : null);

    // ── Render ─────────────────────────────────────────────────────────────────
    return (
        <div
            className={cn(
                'group/container',
                // No gap — rows are stacked via negative margin-top.
                // overflow-hidden clips the stack in collapsed state.
                'relative flex flex-col w-full min-h-10',
                'rounded overflow-hidden',
                className,
            )}
        >
            {resolvedItems.map((item, index) => {
                const { peekSlot, activeInPeek } = metas[index];

                /**
                 * Stack offset
                 * ─────────────
                 * Row 0 has no offset. Rows 1…n are pulled up by 41px each
                 * so only the first row (40px + 1px border gap) is visible
                 * when the container is at min-height.
                 *
                 * On container hover, `group-hover/container:!mt-0` fires on
                 * each row and the `transition-[margin-top]` on the row makes
                 * it slide down smoothly — this is the key to the smooth expand.
                 *
                 * IMPORTANT: labels are opacity-0 by default and fade in via
                 * `group-hover/container:opacity-100` at the same time rows
                 * slide down, so everything animates together.
                 */
                const stackStyle: React.CSSProperties = index > 0 ? { marginTop: -41 } : {};

                /**
                 * Peek margin-left for the icon.
                 * When peekSlot is null, the icon is hidden (opacity-0) and sits
                 * at the default ml-3 position — it will slide in from there on expand.
                 * When peekSlot is assigned, the icon is offset by peekMarginLeft(slot).
                 */
                const iconMarginLeftPx: number | null =
                    peekSlot !== null ? peekMarginLeft(peekSlot) : null;

                const hiddenInPeek = peekSlot === null;

                const inner = (
                    <>
                        <IconWrapper
                            peekMarginLeftPx={iconMarginLeftPx}
                            hiddenInPeek={hiddenInPeek}
                            active={item.active}
                            activeInPeek={activeInPeek}
                        >
                            {item.icon}
                        </IconWrapper>

                        {/* Label — hidden in collapsed, fades in on expand */}
                        <div
                            className={cn(
                                'text-sm font-normal text-[#909090]',
                                'transition-[color,opacity] duration-150 ease-in-out',
                                'opacity-0 group-hover/container:opacity-100',
                                'group-hover/row:text-black dark:group-hover/row:text-white',
                                item.active &&
                                    'opacity-100! text-black! font-medium! dark:text-white!',
                            )}
                        >
                            {item.text}
                        </div>

                        {/* Arrow — hidden until row hover / active */}
                        {!item.disabled && (
                            <div
                                className={cn(
                                    'flex items-center justify-center w-8 h-8 ml-auto mr-2',
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

                const rowBase = cn(
                    'h-10 w-full flex items-center',
                    'bg-[#f6f6f7] dark:bg-[#1c1c1c]',
                    // margin-top transition drives the smooth expand/collapse
                    'transition-[background-color,margin-top] duration-150 ease-in-out',
                    // expand: reset the stacked negative margin
                    'group-hover/container:!mt-0',
                    item.active && 'bg-[#eff0f3]! dark:bg-[#282828]!',
                );

                if (item.disabled) {
                    return (
                        <span
                            key={item.href + item.text}
                            className={cn(rowBase, 'cursor-default pointer-events-none opacity-45')}
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
                        className={cn(
                            'group/row no-underline',
                            rowBase,
                            'hover:bg-[#eff0f3] dark:hover:bg-[#282828]',
                        )}
                        style={stackStyle}
                        onClick={onItemClick ? () => onItemClick(item) : undefined}
                        {...(item.external ? { target: '_blank', rel: 'nofollow noreferrer' } : {})}
                    >
                        {inner}
                    </a>
                );
            })}

            {/* ── Collapsed peek overlay ─────────────────────────────────────
                Floats above the stack in collapsed state; fades out on hover.
                Shows the active item's text (highlighted) when one exists,
                otherwise shows collapsedLabel.
            ──────────────────────────────────────────────────────────────── */}
            {overlayText !== null && (
                <div
                    className={cn(
                        'absolute top-0 z-[1] h-10 w-full pointer-events-none',
                        'flex items-center overflow-hidden pr-3',
                        'bg-[#f6f6f7] dark:bg-[#1c1c1c]',
                        'transition-opacity duration-150',
                        'opacity-100 group-hover/container:opacity-0 group-hover/container:-z-[1]',
                    )}
                    /**
                     * The overlay label starts at the same x-position as the
                     * text labels in the rows. In the original CSS this was
                     * pl-[111px] which is: ml-3(12) + icon-w(24) + mr-2(8) = 44px
                     * for collapsedCount=3: 44 + (56-12) = 88... original used 111px
                     * which corresponds to the 3rd slot icon right-edge:
                     * icon offset 56 + 24(icon-w) + 8(mr) + 12(ml) = ~100. The
                     * original hardcoded 111px for 3 icons. We derive it dynamically:
                     * last-peek-icon-ml + icon-width(24) + mr(8) + scale-factor-gap
                     * ≈ peekMarginLeft(lastSlot) + 44 rounded to nearest nice value.
                     */
                    style={{
                        // last-icon left-edge + icon-width(24) + mr-2(8) = text start
                        paddingLeft: peekMarginLeft(lastSlot) + 32,
                    }}
                >
                    <span
                        className={cn(
                            'text-sm font-normal text-[#909090] truncate',
                            activeItem && 'text-black! dark:text-white! font-medium!',
                        )}
                    >
                        {overlayText}
                    </span>
                </div>
            )}
        </div>
    );
}
