'use client';

import { usePathname } from 'next/navigation';
import { Fragment, useEffect, useState } from 'react';

import { useTheme } from '@teispace/next-themes';
import { AnimatePresence, motion } from 'framer-motion';
import Link from 'fumadocs-core/link';
import { ChevronDown, Globe, Moon, Sun, X } from 'lucide-react';

import { TechnoStarLogo } from '@/components/icons/logo';
import { LanguageSelect } from '@/layouts/shared/slots/language-select';
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

        // 1. Home / Enterpise Section
        // Matches root, /en, /ja, or /enterpise
        if (href === '/enterpise') {
            return normalizedPath === '/' || normalizedPath === '/enterpise';
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
            return normalizedPath.startsWith('/tutorials') || normalizedPath.includes('/docs/tutorials');
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
                    transition: 'background 0.3s ease, border-color 0.3s ease, backdrop-filter 0.3s ease',
                }}
            >
                <div className="psj-container w-full flex items-center justify-between">
                    {/* Logo */}
                    <Link href="/enterpise" aria-label="e-TechnoStar Home">
                        <TechnoStarLogo variant="inline" className="h-6 sm:h-7 w-auto" />
                    </Link>

                    {/* Desktop Nav */}
                    <nav className="hidden lg:flex items-center gap-1" aria-label="Main navigation">
                        {navLinks.map((link) => {
                            if (link.type !== 'main') return null;
                            const active = isActive(link.url);
                            const linkElement = (
                                <Link
                                    key={link.url}
                                    href={link.url}
                                    className="relative px-3 py-2 text-sm font-semibold transition-colors duration-200"
                                    style={{
                                        color: active ? 'var(--psj-blue)' : 'var(--psj-text-2)',
                                        letterSpacing: 'var(--tracking-snug)',
                                    }}
                                    onMouseEnter={(e) => {
                                        if (!active) (e.currentTarget as HTMLElement).style.color = 'var(--psj-text-1)';
                                    }}
                                    onMouseLeave={(e) => {
                                        if (!active) (e.currentTarget as HTMLElement).style.color = 'var(--psj-text-2)';
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

                            if (link.text === 'Home') {
                                const isDocsActive = isActive('/docs') || isActive('/api') || isActive('/tutorials');
                                return (
                                    <Fragment key={link.url}>
                                        {linkElement}
                                        {/* Documentation Mega Menu */}
                                        <div className="group relative">
                                            <button
                                                className="relative px-3 py-2 text-sm font-semibold transition-colors duration-200 flex items-center gap-1"
                                                style={{
                                                    color: isDocsActive ? 'var(--psj-blue)' : 'var(--psj-text-2)',
                                                    letterSpacing: 'var(--tracking-snug)',
                                                }}
                                                onMouseEnter={(e) => {
                                                    if (!isDocsActive) (e.currentTarget as HTMLElement).style.color = 'var(--psj-text-1)';
                                                }}
                                                onMouseLeave={(e) => {
                                                    if (!isDocsActive) (e.currentTarget as HTMLElement).style.color = 'var(--psj-text-2)';
                                                }}
                                            >
                                                Documentation
                                                <ChevronDown size={14} className="opacity-70 group-hover:rotate-180 transition-transform duration-200" />
                                                {isDocsActive && (
                                                    <motion.div
                                                        layoutId="psj-nav-indicator"
                                                        style={{ background: 'var(--psj-blue)' }}
                                                        className="absolute bottom-0 left-3 right-3 h-0.5"
                                                        transition={{ type: 'spring', stiffness: 400, damping: 30 }}
                                                    />
                                                )}
                                            </button>

                                            {/* Dropdown Container */}
                                            <div className="absolute top-full left-0 pt-4 invisible opacity-0 group-hover:visible group-hover:opacity-100 transition-all duration-200 z-50">
                                                <div
                                                    className="w-[600px] p-6 grid grid-cols-3 gap-6 rounded-xl shadow-xl border relative"
                                                    style={{ background: 'var(--psj-surface-0)', borderColor: 'var(--psj-border)' }}
                                                >
                                                    {/* Triangle pointer */}
                                                    <div 
                                                        className="absolute -top-2 left-10 w-4 h-4 rotate-45 border-t border-l"
                                                        style={{ background: 'var(--psj-surface-0)', borderColor: 'var(--psj-border)' }}
                                                    />
                                                    
                                                    {/* Column 1: Framework */}
                                                    <div>
                                                        <h3 className="text-sm font-bold mb-3 uppercase tracking-wider" style={{ color: 'var(--psj-text-1)' }}>Framework</h3>
                                                        <ul className="space-y-3 text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                                            <li><Link href="/docs" className="hover:text-psj-blue transition-colors">Introduction</Link></li>
                                                            <li><Link href="/docs/quick-start" className="hover:text-psj-blue transition-colors">Quick Start</Link></li>
                                                            <li><Link href="/docs/psj-structure" className="hover:text-psj-blue transition-colors">Structure</Link></li>
                                                        </ul>
                                                    </div>

                                                    {/* Column 2: Guides */}
                                                    <div>
                                                        <h3 className="text-sm font-bold mb-3 uppercase tracking-wider" style={{ color: 'var(--psj-text-1)' }}>Guides</h3>
                                                        <ul className="space-y-3 text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                                            <li><Link href="/docs/guides/basic" className="hover:text-psj-blue transition-colors">Basic</Link></li>
                                                            <li><Link href="/docs/guides/intermediate" className="hover:text-psj-blue transition-colors">Intermediate</Link></li>
                                                            <li><Link href="/docs/guides/advanced" className="hover:text-psj-blue transition-colors">Advanced</Link></li>
                                                        </ul>
                                                    </div>

                                                    {/* Column 3: API Reference */}
                                                    <div>
                                                        <h3 className="text-sm font-bold mb-3 uppercase tracking-wider" style={{ color: 'var(--psj-text-1)' }}>API Reference</h3>
                                                        <ul className="space-y-3 text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                                            <li><Link href="/docs/api/data-types" className="hover:text-psj-blue transition-colors">Data Types</Link></li>
                                                            <li><Link href="/docs/api/macro" className="hover:text-psj-blue transition-colors">Macro</Link></li>
                                                            <li><Link href="/docs/api/psj-command" className="hover:text-psj-blue transition-colors">PSJ Command</Link></li>
                                                            <li><Link href="/docs/api/psj-gui" className="hover:text-psj-blue transition-colors">PSJ-GUI</Link></li>
                                                            <li><Link href="/docs/api/psj-utility" className="hover:text-psj-blue transition-colors">PSJ-Utility</Link></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </Fragment>
                                );
                            }
                            return linkElement;
                        })}
                    </nav>

                    {/* Actions */}
                    <div className="flex items-center gap-2">
                        {/* Search Triggers */}
                        <FullSearchTrigger className="hidden sm:inline-flex h-9 w-48 bg-transparent hover:bg-psj-surface-1 border-psj-border text-psj-text-2 hover:text-psj-text-1 transition-colors" />
                        <SearchTrigger className="sm:hidden" color="ghost" />

                        {/* Language Switch */}
                        <LanguageSelect className="h-9 w-9 border-none p-0 flex items-center justify-center rounded-none" style={{ color: 'var(--psj-text-2)' }}>
                            <Globe size={15} />
                        </LanguageSelect>

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
                                (e.currentTarget as HTMLElement).style.borderColor = 'var(--psj-border-hover)';
                                (e.currentTarget as HTMLElement).style.background = 'var(--psj-surface-1)';
                            }}
                            onMouseLeave={(e) => {
                                (e.currentTarget as HTMLElement).style.borderColor = 'var(--psj-border)';
                                (e.currentTarget as HTMLElement).style.background = 'transparent';
                            }}
                        >
                            {isDark ? (
                                <Sun size={15} style={{ color: '#FBC94A' }} />
                            ) : (
                                <Moon size={15} style={{ color: 'var(--psj-text-1)' }} />
                            )}
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
                                <button onClick={() => setMobileOpen(false)} style={{ color: 'var(--psj-text-2)' }}>
                                    <X size={20} />
                                </button>
                            </div>
                            <div className="flex-1 overflow-y-auto px-4 py-6 space-y-2">
                                {navLinks.map((link) => {
                                    if (link.type !== 'main') return null;
                                    const active = isActive(link.url);
                                    
                                    const linkElement = (
                                        <Link
                                            key={link.url}
                                            href={link.url}
                                            className="flex items-center px-3 py-3 text-sm font-semibold transition-colors"
                                            style={{
                                                color: active ? 'var(--psj-blue)' : 'var(--psj-text-2)',
                                                background: active ? 'var(--psj-blue-subtle)' : 'transparent',
                                                borderLeft: active
                                                    ? '2px solid var(--psj-blue)'
                                                    : '2px solid transparent',
                                            }}
                                        >
                                            {link.text}
                                        </Link>
                                    );

                                    if (link.text === 'Home') {
                                        return (
                                            <Fragment key={link.url}>
                                                {linkElement}
                                                {/* Mobile Documentation Nav */}
                                                <div className="pt-2 pb-1 border-b" style={{ borderColor: 'var(--psj-border)' }}>
                                                    <div className="px-3 pb-2 text-xs font-bold uppercase tracking-widest opacity-60" style={{ color: 'var(--psj-text-2)' }}>Documentation</div>
                                                    <div className="pl-4 space-y-4 pt-2">
                                                        <div>
                                                            <div className="text-xs font-bold mb-2 uppercase" style={{ color: 'var(--psj-text-1)' }}>Framework</div>
                                                            <div className="flex flex-col gap-3 pl-2 text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs">Introduction</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/quick-start">Quick Start</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/psj-structure">Structure</Link>
                                                            </div>
                                                        </div>
                                                        <div>
                                                            <div className="text-xs font-bold mb-2 uppercase" style={{ color: 'var(--psj-text-1)' }}>Guides</div>
                                                            <div className="flex flex-col gap-3 pl-2 text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/guides/basic">Basic</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/guides/intermediate">Intermediate</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/guides/advanced">Advanced</Link>
                                                            </div>
                                                        </div>
                                                        <div>
                                                            <div className="text-xs font-bold mb-2 uppercase" style={{ color: 'var(--psj-text-1)' }}>API Reference</div>
                                                            <div className="flex flex-col gap-3 pl-2 text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/api/data-types">Data Types</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/api/macro">Macro</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/api/psj-command">PSJ Command</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/api/psj-gui">PSJ-GUI</Link>
                                                                <Link onClick={() => setMobileOpen(false)} href="/docs/api/psj-utility">PSJ-Utility</Link>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </Fragment>
                                        );
                                    }
                                    
                                    return linkElement;
                                })}
                            </div>
                            <div className="px-4 pb-8 pt-4 border-t" style={{ borderColor: 'var(--psj-border)' }}>
                                <FullSearchTrigger className="w-full bg-transparent" />
                            </div>
                        </motion.nav>
                    </>
                )}
            </AnimatePresence>
        </>
    );
}
