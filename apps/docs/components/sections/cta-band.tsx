'use client';

import Link from 'fumadocs-core/link';
import { ArrowRight, Play } from 'lucide-react';

interface CtaBandProps {
    title?: string;
    subtitle?: string;
    description?: string;
    primaryLink?: { href: string; label: string };
    secondaryLink?: { href: string; label: string };
}

export function CtaBand({
    title = 'Start automating your CAE workflow today',
    subtitle = 'Ready to Start?',
    description = 'Explore the documentation, run through tutorials, or speak with our team to find the right solution.',
    primaryLink = { href: '/docs', label: 'Read Documentation' },
    secondaryLink = { href: '/tutorials', label: 'Start Tutorials' },
}: CtaBandProps) {
    return (
        <section style={{ background: 'var(--psj-blue)' }}>
            <div className="psj-container psj-section">
                <div className="grid md:grid-cols-2 gap-10 items-center">
                    <div>
                        <div
                            className="text-[10px] uppercase tracking-[0.25em] font-bold mb-4"
                            style={{ color: 'rgba(255,255,255,0.6)' }}
                        >
                            {subtitle}
                        </div>
                        <h2 className="psj-h2 text-balance mb-4 text-white">{title}</h2>
                        <p
                            className="text-sm leading-relaxed max-w-md"
                            style={{ color: 'rgba(255,255,255,0.7)' }}
                        >
                            {description}
                        </p>
                    </div>
                    <div className="flex flex-col sm:flex-row gap-3 md:justify-end">
                        <Link
                            href={primaryLink.href}
                            className="inline-flex items-center justify-center gap-2 px-7 py-4 text-sm font-bold transition-colors bg-white hover:bg-white/90"
                            style={{ color: 'var(--psj-blue)' }}
                        >
                            {primaryLink.label} <ArrowRight size={15} />
                        </Link>
                        <Link
                            href={secondaryLink.href}
                            className="inline-flex items-center justify-center gap-2 px-7 py-4 text-sm font-bold transition-colors text-white border border-white/35 hover:bg-white/10"
                        >
                            <Play size={15} /> {secondaryLink.label}
                        </Link>
                    </div>
                </div>
            </div>
        </section>
    );
}
