'use client';

import Link from 'next/link';
import { type ReactNode } from 'react';

// ─── Types ────────────────────────────────────────────────────────────────────

interface StackedNavItem {
    href: string;
    label: string;
    icon: ReactNode;
    external?: boolean;
    /** Icon left-margin class when nav is collapsed */
    collapsedIconMargin: string;
    /** Fully hide icon when collapsed (deeply stacked items) */
    collapsedIconHidden?: boolean;
}

// ─── Icons ────────────────────────────────────────────────────────────────────

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

const BenchmarksIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden>
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

const ExtensionIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden>
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

const StudioIcon = () => (
    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden>
        {(
            [
                {
                    d: 'M12 2C16.714 2 19.071 2 20.535 3.464C21.615 4.544 21.899 6.111 21.974 8.75L22 9.5H2.026V8.75C2.101 6.11 2.384 4.545 3.464 3.464C4.93 2 7.286 2 12 2Z',
                    className:
                        'fill-[#737373] dark:fill-[#424242] group-hover/item:fill-black dark:group-hover/item:fill-[#858586]',
                },
                {
                    d: 'M13 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm-3 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm-3 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z',
                    className:
                        'fill-[#b9b9b9] dark:fill-[#737373] group-hover/item:fill-[#cccccc] dark:group-hover/item:fill-[#f9fafb]',
                },
                {
                    d: 'M2 12C2 16.714 2 19.071 3.464 20.535C4.474 21.545 5.91 21.859 8.25 21.956L9 22V9.5H2.026L2.003 10.25C2 10.794 2 11.377 2 12Z',
                    className:
                        'fill-[#9d9d9d] dark:fill-[#565656] group-hover/item:fill-[#818283] dark:group-hover/item:fill-[#b3b4b5]',
                },
                {
                    d: 'M22 12C22 16.714 22 19.071 20.535 20.535C19.072 22 16.714 22 12 22C11.181 22 9.684 22 9 21.992V9.5H22L21.997 10.25C22 10.794 22 11.377 22 12Z',
                    className:
                        'fill-[#b9b9b9] dark:fill-[#737373] group-hover/item:fill-[#cccccc] dark:group-hover/item:fill-[#f9fafb]',
                },
            ] as const
        ).map(({ d, className }) => (
            <path
                key={d}
                d={d}
                className={`transition-[fill] duration-150 ease-[cubic-bezier(0.4,0,0.2,1)] ${className}`}
            />
        ))}
    </svg>
);

const PackageIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden>
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

const PlayIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden>
        <path
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="1.5"
            className="fill-[#c4c4c4] dark:fill-[#333333] group-hover/item:fill-current transition-[fill] duration-150"
            d="M6.906 4.537A.6.6 0 0 0 6 5.053v13.894a.6.6 0 0 0 .906.516l11.723-6.947a.6.6 0 0 0 0-1.032L6.906 4.537Z"
        />
    </svg>
);

// ─── Nav items config ──────────────────────────────────────────────────────────

const NAV_ITEMS: StackedNavItem[] = [
    {
        href: '/benchmarks',
        label: 'Benchmarks',
        icon: <BenchmarksIcon />,
        collapsedIconMargin: 'ml-3',
    },
    {
        href: 'https://driz.link/extension',
        label: 'Extension',
        icon: <ExtensionIcon />,
        external: true,
        collapsedIconMargin: 'ml-8',
    },
    {
        href: '/drizzle-studio/overview',
        label: 'Studio',
        icon: <StudioIcon />,
        collapsedIconMargin: 'ml-14',
    },
    {
        href: 'https://github.com/drizzle-team/drizzle-studio-npm',
        label: 'Studio Package',
        icon: <PackageIcon />,
        external: true,
        collapsedIconMargin: 'ml-20',
    },
    {
        href: 'https://gateway.drizzle.team',
        label: 'Gateway',
        icon: <PackageIcon />,
        external: true,
        collapsedIconMargin: 'ml-20',
        collapsedIconHidden: true,
    },
    {
        href: 'https://drizzle.run',
        label: 'Drizzle Run',
        icon: <PlayIcon />,
        collapsedIconMargin: 'ml-20',
        collapsedIconHidden: true,
    },
];

// ─── Sub-components ───────────────────────────────────────────────────────────

function StackedNavLink({
    href,
    label,
    icon,
    external,
    collapsedIconMargin,
    collapsedIconHidden,
}: StackedNavItem) {
    return (
        <Link
            href={href}
            target={external ? '_blank' : undefined}
            rel={external ? 'nofollow noreferrer' : undefined}
            aria-label={label}
            className="
        stacked-nav-item group/item
        relative flex items-center h-10 w-full
        bg-[#f6f6f7] dark:bg-[#1c1c1c]
        hover:bg-[#eff0f3] dark:hover:bg-[#282828]
        no-underline [transition:background-color_0.2s_ease-in-out,margin-top_0.15s]
      "
        >
            <div
                className={[
                    // base
                    'relative z-[6] shrink-0 w-6 h-6 my-3 mr-2 flex items-center justify-center',
                    '[transition:margin-left_0.15s,transform_0.15s,opacity_0.15s]',
                    // collapsed
                    'scale-[0.8]',
                    collapsedIconMargin,
                    collapsedIconHidden ? 'opacity-0' : 'opacity-100',
                    // expanded (parent container hovered)
                    'group-hover/nav:ml-3 group-hover/nav:scale-100 group-hover/nav:opacity-100',
                    // svg sizing + color
                    '[&_svg]:w-full [&_svg]:h-full [&_svg]:transition-colors [&_svg]:duration-200',
                    '[&_svg]:text-[#8e8e8e] dark:[&_svg]:text-[#4d4d4d]',
                    'group-hover/item:[&_svg]:text-black dark:group-hover/item:[&_svg]:text-white',
                ].join(' ')}
            >
                {icon}
            </div>

            <span
                className="
          text-sm font-normal text-[#909090]
          opacity-0 group-hover/nav:opacity-100
          group-hover/item:text-black dark:group-hover/item:text-white
          [transition:color_0.2s_ease-in-out,opacity_0.15s]
        "
            >
                {label}
            </span>

            <div
                className="
          ml-auto mr-2 shrink-0 w-8 h-8 flex items-center justify-center
          text-black dark:text-white
          opacity-0 -translate-x-1
          group-hover/item:opacity-100 group-hover/item:translate-x-0
          transition-all duration-200 ease-in-out
          [&_svg]:w-4 [&_svg]:h-4
        "
            >
                <ArrowRightIcon />
            </div>
        </Link>
    );
}

// ─── Main component ───────────────────────────────────────────────────────────

interface StackedNavProps {
    items?: StackedNavItem[];
    collapsedLabel?: string;
}

export function StackedNav({
    items = NAV_ITEMS,
    collapsedLabel = 'Our goodies!',
}: StackedNavProps) {
    return (
        <>
            <style>{`
        .stacked-nav-item:not(:first-child) { margin-top: -41px; }
        .stacked-nav:hover .stacked-nav-item:not(:first-child) { margin-top: 0; }
      `}</style>

            <nav
                aria-label={collapsedLabel}
                className="stacked-nav group/nav relative flex flex-col gap-px mb-1 w-full min-h-10 rounded-sm overflow-hidden"
            >
                {items.map((item) => (
                    <StackedNavLink key={item.href} {...item} />
                ))}

                <div
                    aria-hidden
                    className="
            absolute inset-x-0 top-0 z-[1] h-10
            flex items-center pl-[111px]
            bg-[#f6f6f7] dark:bg-[#1c1c1c]
            pointer-events-none select-none
            transition-opacity duration-250
            group-hover/nav:opacity-0
          "
                >
                    <span className="text-sm text-[#909090] font-normal">{collapsedLabel}</span>
                </div>
            </nav>
        </>
    );
}
