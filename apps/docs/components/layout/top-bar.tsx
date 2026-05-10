'use client';

import { Globe2, Mail, Phone, ShieldCheck } from 'lucide-react';

/**
 * Global utility bar — shown above the main header on md+ screens.
 * Uses PSJ design tokens. Dark mode handled via CSS variables.
 */
export function TopBar() {
    return (
        <div className="hidden md:block border-b transition-colors"
            style={{
                background: 'var(--psj-surface-1)',
                borderColor: 'var(--psj-border)',
            }}
        >
            <div className="max-w-[1280px] mx-auto px-6 lg:px-10 py-1.5 flex items-center justify-between">
                <div className="flex items-center gap-6">
                    <a
                        href="tel:+81312345678"
                        className="flex items-center gap-2 text-xs font-medium transition-colors hover:opacity-80"
                        style={{ color: 'var(--psj-text-2)' }}
                        onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')}
                        onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-2)')}
                    >
                        <Phone size={12} strokeWidth={2.5} />
                        +81 3-1234-5678
                    </a>
                    <div className="w-[1px] h-3 bg-fd-border/60" />
                    <a
                        href="mailto:contact@e-technostar.com"
                        className="flex items-center gap-2 text-xs font-medium transition-colors hover:opacity-80"
                        style={{ color: 'var(--psj-text-2)' }}
                        onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')}
                        onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-2)')}
                    >
                        <Mail size={12} strokeWidth={2.5} />
                        contact@e-technostar.com
                    </a>
                </div>
                <div className="flex items-center gap-6">
                    <span className="flex items-center gap-2 text-xs font-medium cursor-pointer transition-colors"
                        style={{ color: 'var(--psj-text-2)' }}
                        onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')}
                        onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-2)')}>
                        <Globe2 size={12} strokeWidth={2.5} />
                        EN / JP
                    </span>
                    <div className="w-[1px] h-3 bg-fd-border/60" />
                    <span className="flex items-center gap-2 text-xs font-semibold"
                        style={{ color: 'var(--psj-text-2)' }}>
                        <ShieldCheck size={13} strokeWidth={2.5} className="text-emerald-500" />
                        ISO 9001:2015
                    </span>
                </div>
            </div>
        </div>
    );
}
