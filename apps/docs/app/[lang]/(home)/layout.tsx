'use client';

import type { ReactNode } from 'react';
import Link from 'next/link';
import { ArrowRight } from 'lucide-react';
import { GlobalHeader } from '@/components/layout/global-header';

export default function HomeLayout({ children }: { children: ReactNode }) {
    return (
        <div style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-1)', minHeight: '100vh' }}>
            {/* Shared global header (includes TopBar & Breadcrumbs logic) */}
            <GlobalHeader transparent />

            {/* Page content */}
            {children}

            {/* ── Footer ── */}
            <footer style={{ background: 'var(--psj-surface-1)', borderTop: '1px solid var(--psj-border)' }}>
                <div className="max-w-[1280px] mx-auto px-6 lg:px-10 py-14">
                    {/* Columns */}
                    <div className="grid grid-cols-2 md:grid-cols-5 gap-10 mb-12">
                        {/* Brand */}
                        <div className="col-span-2">
                            <div className="flex items-center gap-3 mb-5">
                                <div style={{ background: 'var(--psj-blue)', width: '36px', height: '36px', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                                    <span className="text-white font-bold text-xs tracking-wider">PSJ</span>
                                </div>
                                <div>
                                    <div className="text-sm font-bold" style={{ color: 'var(--psj-text-1)' }}>e-TechnoStar</div>
                                    <div className="text-[10px] uppercase tracking-widest" style={{ color: 'var(--psj-text-3)' }}>CAE Engineering Services</div>
                                </div>
                            </div>
                            <p className="text-sm leading-relaxed max-w-xs mb-6" style={{ color: 'var(--psj-text-2)' }}>
                                Engineering automation specialists delivering production-grade
                                CAE solutions to manufacturers worldwide since 2010.
                            </p>
                            <div className="flex items-center gap-2">
                                <span className="text-[10px] uppercase tracking-widest font-bold" style={{ color: 'var(--psj-text-3)' }}>Certified:</span>
                                {['ISO 9001', 'ISO 27001'].map(cert => (
                                    <span key={cert}
                                        className="text-[11px] px-2 py-1 font-medium"
                                        style={{ border: '1px solid var(--psj-border)', color: 'var(--psj-text-2)' }}>
                                        {cert}
                                    </span>
                                ))}
                            </div>
                        </div>

                        {/* Link columns */}
                        {[
                            {
                                title: 'Product',
                                links: [
                                    { label: 'Overview',       to: '/landing' },
                                    { label: 'Fundamentals',  to: '/docs' },
                                    { label: 'Tutorials',      to: '/tutorials' },
                                    { label: 'Showcase',       to: '/showcase' },
                                ],
                            },
                            {
                                title: 'Modules',
                                links: [
                                    { label: 'Macro',          to: '/docs' },
                                    { label: 'PSJ-Command',    to: '/docs' },
                                    { label: 'PSJ-GUI',        to: '/docs' },
                                    { label: 'Custom IDE',     to: '/docs' },
                                ],
                            },
                            {
                                title: 'Company',
                                links: [
                                    { label: 'About us',           to: '#about' },
                                    { label: 'Careers',            to: '#careers' },
                                    { label: 'Contact',            to: '#contact' },
                                    { label: 'e-TechnoStar.com',   to: 'https://www.e-technostar.com' },
                                ],
                            },
                        ].map((col) => (
                            <div key={col.title}>
                                <h5
                                    className="text-[10px] uppercase tracking-widest font-bold mb-4"
                                    style={{ color: 'var(--psj-text-3)' }}
                                >
                                    {col.title}
                                </h5>
                                <ul className="space-y-3">
                                    {col.links.map((l) => (
                                        <li key={l.label}>
                                            <Link
                                                href={l.to}
                                                className="text-sm transition-colors"
                                                style={{ color: 'var(--psj-text-2)' }}
                                                onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')}
                                                onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-2)')}
                                            >
                                                {l.label}
                                            </Link>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        ))}
                    </div>

                    {/* Bottom bar */}
                    <div
                        className="pt-6 flex flex-wrap items-center justify-between gap-4 text-xs"
                        style={{ borderTop: '1px solid var(--psj-border)', color: 'var(--psj-text-3)' }}
                    >
                        <div>© 2026 e-TechnoStar Co., Ltd. Python Scripting for Jupiter. All rights reserved.</div>
                        <div className="flex items-center gap-5">
                            <a href="#" onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')} onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-3)')}>Privacy Policy</a>
                            <a href="#" onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')} onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-3)')}>Terms of Service</a>
                            <Link href="/docs" onMouseEnter={e => (e.currentTarget.style.color = 'var(--psj-text-1)')} onMouseLeave={e => (e.currentTarget.style.color = 'var(--psj-text-3)')}>Fundamentals</Link>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
}
