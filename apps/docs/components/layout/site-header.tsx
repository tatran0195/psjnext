'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useState } from 'react';

import { useTheme } from '@teispace/next-themes';
import { AnimatePresence, motion } from 'framer-motion';
import { ArrowRight, Menu, Moon, Sun, X } from 'lucide-react';

import { PsjLogo } from '@/components/icons/psj-logo';
import { navLinks } from '@/lib/nav-links';

interface SiteHeaderProps {
    /** When true, header starts transparent and gains background on scroll.
     *  When false (docs pages), header is always opaque. */
    transparent?: boolean;
}

export function SiteHeader({ transparent = false }: SiteHeaderProps) {
    const [scrolled, setScrolled] = useState(false);
    const [mobileOpen, setMobileOpen] = useState(false);
    const pathname = usePathname() || '';
    const { resolvedTheme, setTheme } = useTheme();
    const isDark = resolvedTheme === 'dark';

    useEffect(() => {
        const onScroll = () => setScrolled(window.scrollY > 30);
        window.addEventListener('scroll', onScroll, { passive: true });
        return () => window.removeEventListener('scroll', onScroll);
    }, []);

    useEffect(() => {
        setMobileOpen(false);
    }, [pathname]);

    const isActive = (href: string) => {
        if (href === '/landing') {
            return pathname.endsWith('/landing') || pathname === '/' || pathname === '/en' || pathname === '/ja';
        }
        if (href === '/docs') {
            return pathname.includes('/docs') && !pathname.includes('/docs/tutorials') && !pathname.includes('/docs/api');
        }
        return pathname.includes(href);
    };

    return (
        <>
            {/* ── Main Header ── */}
            <header
                style={{
                    position: 'sticky',
                    top: 0,
                    zIndex: 50,
                    height: '64px',
                    display: 'flex',
                    alignItems: 'center',
                    borderBottom: 'none',
                    background:
                        transparent && !scrolled
                            ? 'transparent'
                            : 'color-mix(in oklch, var(--psj-surface-0) 92%, transparent)',
                    backdropFilter: scrolled || !transparent ? 'blur(16px)' : 'none',
                    WebkitBackdropFilter: scrolled || !transparent ? 'blur(16px)' : 'none',
                    transition:
                        'background 0.3s ease, border-color 0.3s ease, backdrop-filter 0.3s ease',
                }}
            >
                <div className="w-full max-w-[1280px] mx-auto px-6 lg:px-10 flex items-center justify-between">
                    {/* Logo */}
                    <Link href="/landing" aria-label="PSJ Home">
                        <PsjLogo />
                    </Link>

                    {/* Desktop Nav */}
                    <nav className="hidden lg:flex items-center gap-1" aria-label="Main navigation">
                        {navLinks.map((link) => {
                            if (link.type !== 'main') return null;
                            const active = isActive(link.url);
                            return (
                                <Link
                                    key={link.url}
                                    href={link.url}
                                    className="relative px-3 py-2 text-sm font-semibold transition-colors duration-200"
                                    style={{
                                        color: active ? 'var(--psj-blue)' : 'var(--psj-text-2)',
                                        letterSpacing: 'var(--tracking-snug)',
                                    }}
                                    onMouseEnter={(e) => {
                                        if (!active)
                                            (e.currentTarget as HTMLElement).style.color =
                                                'var(--psj-text-1)';
                                    }}
                                    onMouseLeave={(e) => {
                                        if (!active)
                                            (e.currentTarget as HTMLElement).style.color =
                                                'var(--psj-text-2)';
                                    }}
                                >
                                    {link.text}
                                    {active && (
                                        <motion.div
                                            layoutId="psj-nav-indicator"
                                            style={{ background: 'var(--psj-blue)' }}
                                            className="absolute bottom-0 left-3 right-3 h-0.5"
                                            transition={{
                                                type: 'spring',
                                                stiffness: 400,
                                                damping: 30,
                                            }}
                                        />
                                    )}
                                </Link>
                            );
                        })}
                    </nav>

                    {/* Actions */}
                    <div className="flex items-center gap-2">
                        {/* Theme toggle */}
                        <button
                            onClick={() => setTheme(isDark ? 'light' : 'dark')}
                            aria-label="Toggle theme"
                            style={{
                                width: '36px',
                                height: '36px',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                border: '1px solid var(--psj-border)',
                                background: 'transparent',
                                color: 'var(--psj-text-2)',
                                cursor: 'pointer',
                                transition: 'border-color 0.15s, background 0.15s',
                            }}
                            onMouseEnter={(e) => {
                                (e.currentTarget as HTMLElement).style.borderColor =
                                    'var(--psj-border-hover)';
                                (e.currentTarget as HTMLElement).style.background =
                                    'var(--psj-surface-1)';
                            }}
                            onMouseLeave={(e) => {
                                (e.currentTarget as HTMLElement).style.borderColor =
                                    'var(--psj-border)';
                                (e.currentTarget as HTMLElement).style.background = 'transparent';
                            }}
                        >
                            {isDark ? (
                                <Sun size={15} style={{ color: '#FBC94A' }} />
                            ) : (
                                <Moon size={15} style={{ color: 'var(--psj-blue)' }} />
                            )}
                        </button>

                        {/* Get Started CTA */}
                        <Link
                            href="/docs"
                            className="hidden sm:inline-flex items-center gap-1.5 psj-btn-primary"
                            style={{ padding: '0 1.25rem', height: '36px', fontSize: '0.8125rem' }}
                        >
                            Get Started <ArrowRight size={14} />
                        </Link>

                        {/* Mobile hamburger */}
                        <button
                            onClick={() => setMobileOpen((v) => !v)}
                            aria-label="Menu"
                            className="lg:hidden"
                            style={{
                                width: '36px',
                                height: '36px',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                color: 'var(--psj-text-2)',
                            }}
                        >
                            {mobileOpen ? <X size={20} /> : <Menu size={20} />}
                        </button>
                    </div>
                </div>
            </header>

            {/* ── Mobile Menu Overlay ── */}
            <AnimatePresence>
                {mobileOpen && (
                    <>
                        <motion.div
                            key="overlay"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            transition={{ duration: 0.2 }}
                            className="lg:hidden fixed inset-0 z-40"
                            style={{ background: 'rgba(0,0,0,0.4)' }}
                            onClick={() => setMobileOpen(false)}
                        />
                        <motion.nav
                            key="menu"
                            initial={{ x: '100%' }}
                            animate={{ x: 0 }}
                            exit={{ x: '100%' }}
                            transition={{ type: 'spring', stiffness: 320, damping: 30 }}
                            className="lg:hidden fixed top-0 right-0 h-full w-72 z-50 flex flex-col"
                            style={{
                                background: 'var(--psj-surface-0)',
                                borderLeft: '1px solid var(--psj-border)',
                            }}
                        >
                            <div
                                className="flex items-center justify-between px-6 h-16 border-b"
                                style={{ borderColor: 'var(--psj-border)' }}
                            >
                                <PsjLogo />
                                <button
                                    onClick={() => setMobileOpen(false)}
                                    style={{ color: 'var(--psj-text-2)' }}
                                >
                                    <X size={20} />
                                </button>
                            </div>
                            <div className="flex-1 overflow-y-auto px-4 py-6 space-y-1">
                                {navLinks.map((link) => {
                                    if (link.type !== 'main') return null;
                                    const active = isActive(link.url);
                                    return (
                                        <Link
                                            key={link.url}
                                            href={link.url}
                                            className="flex items-center px-3 py-3 text-sm font-semibold transition-colors"
                                            style={{
                                                color: active
                                                    ? 'var(--psj-blue)'
                                                    : 'var(--psj-text-2)',
                                                background: active
                                                    ? 'var(--psj-blue-subtle)'
                                                    : 'transparent',
                                                borderLeft: active
                                                    ? '2px solid var(--psj-blue)'
                                                    : '2px solid transparent',
                                            }}
                                        >
                                            {link.text}
                                        </Link>
                                    );
                                })}
                            </div>
                            <div
                                className="px-4 pb-8 pt-4 border-t"
                                style={{ borderColor: 'var(--psj-border)' }}
                            >
                                <Link
                                    href="/docs"
                                    className="psj-btn-primary w-full justify-center"
                                >
                                    Get Started <ArrowRight size={14} />
                                </Link>
                            </div>
                        </motion.nav>
                    </>
                )}
            </AnimatePresence>
        </>
    );
}
