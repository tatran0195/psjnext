import React from 'react';

import { BenchmarksIcon, ExtensionIcon, PackageIcon, PlayIcon, StudioIcon } from './icons';

// ─── Types ────────────────────────────────────────────────────────────────────

export interface AsidePostItem {
    href: string;
    text: string;
    icon: React.ReactNode;
    external?: boolean;
    active?: boolean;
    disabled?: boolean;
}

export interface DockRailProps {
    options?: AsidePostItem[];
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

export const DEFAULT_OPTIONS: AsidePostItem[] = [
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
