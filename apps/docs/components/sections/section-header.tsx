'use client';

import Link from 'fumadocs-core/link';
import { ArrowRight } from 'lucide-react';

import { FadeUp } from './fade-up';

interface SectionHeaderProps {
    label: string;
    title: string;
    subtitle?: string;
    link?: string;
    linkLabel?: string;
}

export function SectionHeader({ label, title, subtitle, link, linkLabel }: SectionHeaderProps) {
    return (
        <FadeUp className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
            <div>
                <div className="psj-label mb-3">{label}</div>
                <h2 className="psj-h2 text-balance" style={{ color: 'var(--psj-text-1)' }}>
                    {title}
                </h2>
                {subtitle && (
                    <p className="mt-3 text-base leading-relaxed max-w-xl" style={{ color: 'var(--psj-text-2)' }}>
                        {subtitle}
                    </p>
                )}
            </div>
            {link && linkLabel && (
                <Link
                    href={link}
                    className="group inline-flex items-center gap-2 text-sm font-bold shrink-0 transition-colors"
                    style={{ color: 'var(--psj-blue)' }}
                >
                    {linkLabel}
                    <ArrowRight size={15} className="group-hover:translate-x-1 transition-transform" />
                </Link>
            )}
        </FadeUp>
    );
}
