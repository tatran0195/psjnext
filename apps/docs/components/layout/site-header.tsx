'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useState } from 'react';

import { useTheme } from '@teispace/next-themes';
import { AnimatePresence, motion } from 'framer-motion';
import { Menu, Moon, Sun, X } from 'lucide-react';

import { TechnoStarLogo } from '@/components/icons/logo';
import { FullSearchTrigger, SearchTrigger } from '@/layouts/shared/slots/search-trigger';
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
        // Normalize pathname and href by removing locale prefix (e.g., /en, /ja)
        // This ensures the active state logic is locale-agnostic.
        const normalizedPath = pathname.replace(/^\/(en|ja)/, '') || '/';
        const normalizedHref = href.replace(/^\/(en|ja)/, '');

        // 1. Home / Landing Section
        // Matches root, /en, /ja, or /landing
        if (href === '/landing') {
            return normalizedPath === '/' || normalizedPath === '/landing';
        }

        // 2. Fundamentals Section
        // Matches /docs, but excludes tutorials and api reference
        if (href === '/docs' || href === '') {
            return (
                normalizedPath.startsWith('/docs') &&
                !normalizedPath.includes('/docs/tutorials') &&
                !normalizedPath.includes('/docs/api')
            );
        }

        // 3. Tutorials Section
        // Matches anything under tutorials or docs/tutorials
        if (href.includes('/tutorials')) {
            return (
                normalizedPath.startsWith('/tutorials') || normalizedPath.includes('/docs/tutorials')
            );
        }

        // 4. API Reference Section
        // Matches anything under api or docs/api
        if (href.includes('/api')) {
            return normalizedPath.startsWith('/api') || normalizedPath.includes('/docs/api');
        }

        // 5. Default: Nested URL matching
        // Ensures /changelog matches /changelog/v1 but not unrelated paths
        return normalizedHref !== '' && normalizedPath.startsWith(normalizedHref);
    };

    return (
        <>
            {/* ── Main Header ── */}
            <header
                style={{
                    position: 'relative',
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
                <div className="psj-container w-full flex items-center justify-between">
                    {/* Logo */}
                    <Link href="/landing" aria-label="e-TechnoStar Home">
                        <TechnoStarLogo variant="inline" className="h-6 sm:h-7 w-auto" />
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
                        {/* Search Triggers */}
                        <FullSearchTrigger className="hidden sm:inline-flex h-9 w-48 bg-transparent hover:bg-psj-surface-1 border-psj-border text-psj-text-2 hover:text-psj-text-1 transition-colors" />
                        <SearchTrigger className="sm:hidden" color="ghost" />

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
                                borderRadius: '0',
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
                                <Moon size={15} style={{ color: 'var(--psj-text-1)' }} />
                            )}
                        </button>

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
                                <TechnoStarLogo variant="inline" className="h-6 w-auto" />
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
                                <FullSearchTrigger className="w-full bg-transparent" />
                            </div>
                        </motion.nav>
                    </>
                )}
            </AnimatePresence>
        </>
    );
}
