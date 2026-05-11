'use client';

import React from 'react';

import { cn } from '@/lib/cn';

export type BadgeVariant = 'feature' | 'fix' | 'api' | 'utility' | 'macro' | 'data' | 'highlight' | 'default';

interface ChangelogBadgeProps {
    children: React.ReactNode;
    variant?: BadgeVariant;
    className?: string;
}

const variants: Record<BadgeVariant, string> = {
    feature: 'bg-blue-500/10 text-blue-600 border-blue-200 dark:text-blue-400 dark:border-blue-500/30',
    fix: 'bg-red-500/10 text-red-600 border-red-200 dark:text-red-400 dark:border-red-500/30',
    api: 'bg-emerald-500/10 text-emerald-600 border-emerald-200 dark:text-emerald-400 dark:border-emerald-500/30',
    utility: 'bg-amber-500/10 text-amber-600 border-amber-200 dark:text-amber-400 dark:border-amber-500/30',
    macro: 'bg-purple-500/10 text-purple-600 border-purple-200 dark:text-purple-400 dark:border-purple-500/30',
    data: 'bg-slate-500/10 text-slate-600 border-slate-200 dark:text-slate-400 dark:border-slate-500/30',
    highlight: 'bg-indigo-500/10 text-indigo-600 border-indigo-200 dark:text-indigo-400 dark:border-indigo-500/30',
    default: 'bg-gray-500/10 text-gray-600 border-gray-200 dark:text-gray-400 dark:border-gray-500/30',
};

export function ChangelogBadge({ children, variant = 'default', className }: ChangelogBadgeProps) {
    return (
        <span
            className={cn(
                'inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-[0.15em] border align-middle mr-2',
                variants[variant],
                className,
            )}
        >
            {children}
        </span>
    );
}
