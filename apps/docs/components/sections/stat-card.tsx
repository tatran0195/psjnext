'use client';

import React from 'react';
import { cn } from '@/lib/cn';

interface StatCardProps {
    icon: React.ReactNode;
    label: string;
    value: string;
    className?: string;
    /** Whether to use the border-right/bottom style from the landing page grid */
    bordered?: boolean;
}

export function StatCard({ icon, label, value, className, bordered = true }: StatCardProps) {
    return (
        <div
            className={cn(
                "flex flex-col gap-2 p-5 lg:p-6",
                bordered && "border-r border-b border-[var(--psj-border)]",
                className
            )}
            style={!bordered ? { 
                background: 'var(--psj-surface-0)',
                borderRight: '1px solid var(--psj-border)',
                borderBottom: '1px solid var(--psj-border)'
            } : undefined}
        >
            <div 
                className="flex items-center gap-2 text-[10px] uppercase tracking-widest font-bold"
                style={{ color: 'var(--psj-text-3)' }}
            >
                {icon} {label}
            </div>
            <div 
                className="text-2xl lg:text-3xl font-extrabold num-marker tracking-tighter"
                style={{ color: 'var(--psj-text-1)' }}
            >
                {value}
            </div>
        </div>
    );
}
