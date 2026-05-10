'use client';

import type { ReactNode } from 'react';

import { GlobalHeader } from '@/components/layout/global-header';

export default function HomeLayout({ children }: { children: ReactNode }) {
    return (
        <div
            style={{
                background: 'var(--psj-surface-0)',
                color: 'var(--psj-text-1)',
                minHeight: '100vh',
            }}
        >
            {/* Shared global header (includes TopBar & Breadcrumbs logic) */}
            <GlobalHeader transparent />

            {/* Page content */}
            {children}
        </div>
    );
}
