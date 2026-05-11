'use client';

import { ChevronRight } from 'lucide-react';

import { TechnoStarLogo } from '@/components/icons/logo';

export function GlobalFooter() {
    return (
        <footer
            className="w-full flex flex-col relative transition-colors"
            style={{ background: 'var(--psj-surface-1)', borderTop: '1px solid var(--psj-border)' }}
        >
            {/* Top Info Section */}
            <div className="relative" style={{ padding: '4rem 0' }}>
                <div className="psj-container">
                    <div className="flex flex-col md:flex-row items-center md:justify-start justify-center gap-8 md:gap-12">
                        <a
                            href="https://www.e-technostar.com/"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            <TechnoStarLogo variant="inline" className="h-9 w-auto" />
                        </a>
                        <address
                            className="text-sm leading-relaxed not-italic text-left"
                            style={{ color: 'var(--psj-text-2)' }}
                        >
                            <strong
                                className="text-base font-bold mb-1 block"
                                style={{ color: 'var(--psj-text-1)' }}
                            >
                                株式会社テクノスター
                            </strong>
                            東京都港区赤坂7-1-1 青山安田ビル 6F
                        </address>
                    </div>
                </div>
            </div>

            {/* Bottom Copyright & Links Section */}
            <div
                style={{
                    background: 'var(--psj-surface-3)',
                    padding: '0.75rem 0',
                    borderTop: '1px solid var(--psj-border)',
                }}
            >
                <div className="psj-container flex flex-col md:flex-row items-center justify-between gap-4 text-xs font-medium">
                    <div style={{ color: 'var(--psj-text-3)' }}>© 2026 TechnoStar Co., Ltd.</div>
                    <div
                        className="flex flex-wrap items-center gap-6"
                        style={{ color: 'var(--psj-text-2)' }}
                    >
                        {[
                            {
                                label: '採用情報',
                                to: 'https://www.e-technostar.com/company/careers/',
                            },
                            {
                                label: '個人情報保護方針',
                                to: 'https://www.e-technostar.com/company/privacy/',
                            },
                            {
                                label: '品質管理方針',
                                to: 'https://www.e-technostar.com/company/quality/',
                            },
                        ].map((link) => (
                            <a
                                key={link.label}
                                href={link.to}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="flex items-center gap-1.5 transition-colors hover:underline"
                                onMouseEnter={(e) =>
                                    (e.currentTarget.style.color = 'var(--psj-text-1)')
                                }
                                onMouseLeave={(e) =>
                                    (e.currentTarget.style.color = 'var(--psj-text-2)')
                                }
                            >
                                <ChevronRight size={12} strokeWidth={3} />
                                {link.label}
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        </footer>
    );
}
