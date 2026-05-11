'use client';

/**
 * components/SymbolLink.tsx
 *
 * Renders a linked, hoverable symbol token.
 * The `category` prop drives visual styling so readers can immediately
 * distinguish parameter types, class names, enum constants, etc.
 */

import Link from 'next/link';
import { useId, useState } from 'react';

import { useI18n } from 'fumadocs-ui/contexts/i18n';

import type { SymbolEntry } from '@/lib/symbol-resolver';

// ── Category badge styles ─────────────────────────────────────────────────

const CATEGORY_STYLES: Record<SymbolEntry['category'], { link: string; badge: string; label: string }> = {
    'parameter-type': {
        link: 'text-blue-700 dark:text-blue-400',
        badge: 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300',
        label: 'param type',
    },
    class: {
        link: 'text-blue-600 dark:text-blue-400',
        badge: 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300',
        label: 'class',
    },
    'built-in': {
        link: 'text-green-700 dark:text-green-400',
        badge: 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300',
        label: 'built-in',
    },
    element: {
        link: 'text-orange-600 dark:text-orange-400',
        badge: 'bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300',
        label: 'element',
    },
    entity: {
        link: 'text-rose-600 dark:text-rose-400',
        badge: 'bg-rose-100 text-rose-700 dark:bg-rose-900 dark:text-rose-300',
        label: 'entity',
    },
    'material-key': {
        link: 'text-amber-700 dark:text-amber-400',
        badge: 'bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300',
        label: 'material key',
    },
    'unit-key': {
        link: 'text-teal-600 dark:text-teal-400',
        badge: 'bg-teal-100 text-teal-700 dark:bg-teal-900 dark:text-teal-300',
        label: 'unit',
    },
    enum: {
        link: 'text-sky-700 dark:text-sky-400',
        badge: 'bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300',
        label: 'enum',
    },
};

// ── Component ─────────────────────────────────────────────────────────────

interface Props {
    name: string;
    href: string;
    description: string;
    category: SymbolEntry['category'];
    children: React.ReactNode;
}

export function SymbolLink({ name, href, description, category, children }: Props) {
    const [open, setOpen] = useState(false);
    const tooltipId = useId();
    const { locale } = useI18n();

    const styles = CATEGORY_STYLES[category] ?? CATEGORY_STYLES['built-in'];

    return (
        <span className="relative inline-block cursor-pointer">
            <Link
                href={`${locale ?? ''}${href}`}
                aria-describedby={open ? tooltipId : undefined}
                onMouseEnter={() => setOpen(true)}
                onMouseLeave={() => setOpen(false)}
                onFocus={() => setOpen(true)}
                onBlur={() => setOpen(false)}
                className={`
          font-mono font-medium underline decoration-dotted
          underline-offset-2 transition-colors
          ${styles.link}
        `}
            >
                {children}
            </Link>

            {open && (
                <span
                    id={tooltipId}
                    role="tooltip"
                    className="
            pointer-events-none absolute bottom-full left-0 z-50 mb-1
            min-w-max max-w-xs rounded-md border border-neutral-200
            bg-white px-3 py-2 shadow-lg
            dark:border-neutral-700 dark:bg-neutral-900
          "
                >
                    {/* Header row: name + category badge */}
                    <span className="flex items-center gap-2">
                        <span className="font-mono text-sm font-semibold text-neutral-900 dark:text-neutral-100">
                            {name}
                        </span>
                        <span className={`rounded px-1.5 py-0.5 text-[10px] font-medium ${styles.badge}`}>
                            {styles.label}
                        </span>
                    </span>

                    {/* Description */}
                    {description && (
                        <span className="mt-1 block text-xs text-neutral-600 dark:text-neutral-400">{description}</span>
                    )}
                </span>
            )}
        </span>
    );
}
