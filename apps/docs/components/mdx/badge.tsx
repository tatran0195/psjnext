// components/ui/badge.tsx
'use client';

import { Braces, Bug, Code2, Database, Sparkles, Tag, Wrench, Zap, type LucideIcon } from 'lucide-react';

import { cn } from '@/lib/cn';

export type BadgeVariant = 'feature' | 'fix' | 'api' | 'utility' | 'macro' | 'data' | 'highlight' | 'default';

interface BadgeProps {
    label: string;
    variant?: BadgeVariant;
    icon?: string;
    className?: string;
}

const variants: Record<BadgeVariant, string> = {
    feature: 'bg-blue-500/10    text-blue-600    border-blue-200    dark:text-blue-400    dark:border-blue-500/30',
    fix: 'bg-red-500/10     text-red-600     border-red-200     dark:text-red-400     dark:border-red-500/30',
    api: 'bg-emerald-500/10 text-emerald-600 border-emerald-200 dark:text-emerald-400 dark:border-emerald-500/30',
    utility: 'bg-amber-500/10   text-amber-600   border-amber-200   dark:text-amber-400   dark:border-amber-500/30',
    macro: 'bg-purple-500/10  text-purple-600  border-purple-200  dark:text-purple-400  dark:border-purple-500/30',
    data: 'bg-slate-500/10   text-slate-600   border-slate-200   dark:text-slate-400   dark:border-slate-500/30',
    highlight: 'bg-indigo-500/10  text-indigo-600  border-indigo-200  dark:text-indigo-400  dark:border-indigo-500/30',
    default: 'bg-gray-500/10    text-gray-600    border-gray-200    dark:text-gray-400    dark:border-gray-500/30',
};

const defaultIcons: Record<BadgeVariant, LucideIcon> = {
    feature: Zap,
    fix: Bug,
    api: Code2,
    utility: Wrench,
    macro: Braces,
    data: Database,
    highlight: Sparkles,
    default: Tag,
};

// Lucide icon map for custom icon override via string
const iconMap: Record<string, LucideIcon> = {
    zap: Zap,
    bug: Bug,
    code2: Code2,
    wrench: Wrench,
    braces: Braces,
    database: Database,
    sparkles: Sparkles,
    tag: Tag,
};

export function Badge({ label, variant = 'default', icon, className }: BadgeProps) {
    const IconComponent = icon ? (iconMap[icon] ?? defaultIcons[variant]) : defaultIcons[variant];

    return (
        <span
            className={cn(
                'inline-flex items-center gap-1.5 px-1.5 py-0.5 rounded-sm text-[10px] font-bold uppercase tracking-widest border align-baseline leading-none',
                variants[variant],
                className,
            )}
        >
            <IconComponent className="size-2.5 shrink-0" aria-hidden />
            {label}
        </span>
    );
}
