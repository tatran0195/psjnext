'use client';

import { useTheme } from '@teispace/next-themes';
import { AnimatePresence, motion } from 'framer-motion';
import {
    ArrowRight,
    BookOpen,
    ChevronDown,
    Compass,
    Globe,
    GraduationCap,
    Home,
    Layers,
    Layout,
    Moon,
    Package,
    Play,
    Sparkles,
    Sun,
    Terminal,
    X,
    Zap,
} from 'lucide-react';
import { Fragment, useEffect, useState } from 'react';

import { TechnoStarLogo } from '@/components/icons/logo';
import { Link, usePathname } from '@/i18n/navigation';
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
    const pathname = usePathname();
    const { resolvedTheme, setTheme } = useTheme();
    const isDark = resolvedTheme === 'dark';

    const versions = (process.env.API_VERSIONS || '').split(',').filter(Boolean);
    const latestVersion = versions[0];
    const isMultiVersion = versions.length > 1;

    const getVersionedLink = (href: string) => {
        if (!isMultiVersion || !latestVersion) return href;
        if (href.startsWith('/docs/api/')) {
            const product = href.replace('/docs/api/', '');
            if (!/^\d+\.\d+\.\d+\//.test(product)) {
                return `/docs/api/${latestVersion}/${product}`;
            }
        }
        if (href.startsWith('/docs/data-types')) {
            const product = href.replace('/docs/data-types', '');
            if (!/^\d+\.\d+\.\d+\//.test(product)) {
                return `/docs/api/${latestVersion}/data-types${product}`;
            }
        }
        return href;
    };

    useEffect(() => {
        const onScroll = () => setScrolled(window.scrollY > 30);
        window.addEventListener('scroll', onScroll, { passive: true });
        return () => window.removeEventListener('scroll', onScroll);
    }, []);

    useEffect(() => {
        setMobileOpen(false);
    }, [pathname]);

    const isActive = (href: string) => {
        // usePathname() from @/i18n/navigation already returns the normalized pathname
        // without the locale prefix (e.g., '/docs' instead of '/en/docs').
        const normalizedPath = pathname || '/';
        const normalizedHref = href.replace(/^\/(en|ja)/, '');

        // 0. Root / Home
        if (href === '/') {
            return normalizedPath === '/';
        }

        // 1. Enterprise Section
        if (href === '/landing') {
            return normalizedPath === '/landing';
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
                className={`sticky top-0 z-50 w-full transition-all duration-300 ${
                    transparent && !scrolled
                        ? 'bg-transparent border-transparent'
                        : 'bg-white/80 dark:bg-[#0c1220]/80 backdrop-blur-xl border-b border-psj-border'
                }`}
                style={{
                    height: '64px',
                    display: 'flex',
                    alignItems: 'center',
                }}
            >
                <div className="psj-container w-full flex items-center justify-between">
                    {/* Logo */}
                    <Link href="/" aria-label="e-TechnoStar Home" className="flex items-center">
                        <TechnoStarLogo variant="inline" className="h-8 sm:h-9 w-auto" />
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
                                    className="relative px-4 py-2 text-[13px] font-semibold transition-colors duration-200"
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
                                            className="absolute bottom-0 left-4 right-4 h-0.5 bg-psj-blue"
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
                                const isDocsActive = isActive('/docs') || isActive('/api');
                                return (
                                    <Fragment key={link.url}>
                                        {linkElement}
                                        {/* Documentation Mega Menu */}
                                        <div className="group relative">
                                            <button
                                                className={`relative px-4 py-2 text-[13px] font-semibold transition-all duration-300 flex items-center gap-1.5 group/link ${
                                                    isDocsActive
                                                        ? 'text-psj-blue'
                                                        : 'text-psj-text-2 hover:text-psj-text-1'
                                                }`}
                                            >
                                                <span>Documentation</span>
                                                <ChevronDown
                                                    size={14}
                                                    className={`transition-transform duration-300 group-hover:rotate-180 ${
                                                        isDocsActive ? 'text-psj-blue' : 'text-psj-text-3'
                                                    }`}
                                                />
                                                {/* Hover Indicator Bridge */}
                                                <div className="absolute bottom-0 left-4 right-4 h-0.5 bg-psj-blue scale-x-0 group-hover:scale-x-100 transition-transform duration-300" />
                                                {isDocsActive && (
                                                    <motion.div
                                                        layoutId="psj-nav-indicator"
                                                        className="absolute bottom-0 left-4 right-4 h-0.5 bg-psj-blue"
                                                        transition={{ type: 'spring', stiffness: 400, damping: 30 }}
                                                    />
                                                )}
                                            </button>

                                            {/* Dropdown Container */}
                                            <div className="absolute top-[calc(100%-8px)] left-1/2 -translate-x-1/2 pt-4 invisible opacity-0 group-hover:visible group-hover:opacity-100 transition-all duration-300 z-50">
                                                <div
                                                    className="w-[1000px] p-0 rounded-none border border-psj-border shadow-2xl shadow-psj-navy/10 overflow-hidden relative"
                                                    style={{ background: 'var(--psj-surface-0)' }}
                                                >
                                                    {/* Navigation Caret */}
                                                    <div className="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-psj-blue rotate-45" />

                                                    <div className="h-1 bg-psj-blue w-full relative z-10" />
                                                    <div className="grid grid-cols-12">
                                                        {/* Left Content Area */}
                                                        <div className="col-span-8 py-8 px-10 grid grid-cols-3 gap-x-12 gap-y-10">
                                                            {/* Column 1: Framework */}
                                                            <div>
                                                                <h3 className="psj-label mb-8 text-psj-blue/60 tracking-[0.2em] uppercase text-[10px] font-bold">
                                                                    Framework
                                                                </h3>
                                                                <ul className="space-y-1">
                                                                    <li>
                                                                        <Link
                                                                            href="/docs"
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Home size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Introduction
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Core concepts
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href="/docs/quick-start"
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Zap size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Quick Start
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Setup in minutes
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href="/docs/psj-structure"
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Layers size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Structure
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Architecture overview
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                </ul>
                                                            </div>

                                                            {/* Column 2: Guides */}
                                                            <div>
                                                                <h3 className="psj-label mb-8 text-psj-blue/60 tracking-[0.2em] uppercase text-[10px] font-bold">
                                                                    Guides
                                                                </h3>
                                                                <ul className="space-y-1">
                                                                    <li>
                                                                        <Link
                                                                            href="/docs/guides/basic"
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <BookOpen size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Basic
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Essential features
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href="/docs/guides/intermediate"
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Compass size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Intermediate
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Advanced patterns
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href="/docs/guides/advanced"
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <GraduationCap
                                                                                    size={18}
                                                                                    strokeWidth={2.5}
                                                                                />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Advanced
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Optimization & tuning
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                </ul>
                                                            </div>

                                                            {/* Column 3: API Reference */}
                                                            <div>
                                                                <h3 className="psj-label mb-6 text-psj-blue/80 tracking-[0.1em] uppercase text-[11px]">
                                                                    API Reference
                                                                </h3>
                                                                <ul className="space-y-1">
                                                                    <li>
                                                                        <Link
                                                                            href={getVersionedLink('/docs/api/macro')}
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Play size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    Macro
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Built-in Jupiter API
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href={getVersionedLink(
                                                                                '/docs/api/psj-command'
                                                                            )}
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Terminal size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    PSJ Command
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Pythonic Command System
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href={getVersionedLink('/docs/data-types')}
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Package size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    PSJ-Utility
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    Model Querying & Helpers
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                    <li>
                                                                        <Link
                                                                            href={getVersionedLink('/docs/api/psj-gui')}
                                                                            className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
                                                                        >
                                                                            <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                                                                                <Layout size={18} strokeWidth={2.5} />
                                                                            </div>
                                                                            <div>
                                                                                <div className="text-[13px] font-bold text-psj-text-1">
                                                                                    PSJ-GUI
                                                                                </div>
                                                                                <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">
                                                                                    GUI Creation Library
                                                                                </div>
                                                                            </div>
                                                                        </Link>
                                                                    </li>
                                                                </ul>
                                                            </div>
                                                        </div>

                                                        {/* Right Side Callout (The "Cover" Area) */}
                                                        <div className="col-span-4 bg-psj-surface-1/40 py-8 px-10 border-l border-psj-border flex flex-col justify-between relative overflow-hidden group/callout">
                                                            {/* Background Glows */}
                                                            <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-psj-blue/10 rounded-full blur-[80px] group-hover/callout:bg-psj-blue/20 transition-colors duration-700" />
                                                            <div className="absolute bottom-0 left-0 -ml-8 -mb-8 w-32 h-32 bg-psj-blue/5 rounded-full blur-[40px]" />

                                                            <div className="relative z-10">
                                                                <div className="inline-flex items-center gap-2 px-2.5 py-1 bg-psj-blue/10 border border-psj-blue/20 text-psj-blue text-[10px] font-bold mb-6 tracking-widest uppercase">
                                                                    <Sparkles size={12} className="fill-psj-blue/20" />
                                                                    Latest Release
                                                                </div>
                                                                <h5 className="text-[20px] font-extrabold text-psj-text-1 leading-tight mb-3 tracking-tight">
                                                                    What&apos;s New in <br />
                                                                    <span className="text-psj-blue">Jupiter {latestVersion || '5.x'}</span>
                                                                </h5>
                                                                <p className="text-[13px] text-psj-text-3 leading-relaxed opacity-80 mb-6">
                                                                    Explore the latest PSJ advancements, featuring
                                                                    optimized Pythonic commands and the new native GUI
                                                                    builder.
                                                                </p>

                                                                <div className="space-y-3">
                                                                    <div className="flex items-center gap-3 text-[11px] text-psj-text-2">
                                                                        <Zap size={12} className="text-psj-blue" />
                                                                        <span className="whitespace-nowrap">
                                                                            New GUI Command Builder
                                                                        </span>
                                                                    </div>
                                                                    <div className="flex items-center gap-3 text-[11px] text-psj-text-2">
                                                                        <Zap size={12} className="text-psj-blue" />
                                                                        <span className="whitespace-nowrap">
                                                                            Enhanced PSJ-Utility API
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>

                                                            <Link
                                                                href="/changelog"
                                                                className="psj-btn-primary w-full justify-center !text-[12px] !px-6 !py-4 !rounded-none mt-10 group/btn transition-all duration-300 hover:shadow-xl hover:shadow-psj-blue/20 relative overflow-hidden"
                                                            >
                                                                <div className="absolute inset-0 bg-white/10 translate-x-[-100%] group-hover/btn:translate-x-[100%] transition-transform duration-700" />
                                                                <span className="relative z-10 whitespace-nowrap">
                                                                    Explore Changelog
                                                                </span>
                                                                <ArrowRight
                                                                    size={14}
                                                                    className="ml-2 relative z-10 group-hover/btn:translate-x-1 transition-transform"
                                                                />
                                                            </Link>
                                                        </div>
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
                        <LanguageSelect
                            className="h-9 w-9 border-none p-0 flex items-center justify-center rounded-none"
                            style={{ color: 'var(--psj-text-2)' }}
                        >
                            <Globe size={15} />
                        </LanguageSelect>

                        {/* Theme toggle */}
                        <button
                            onClick={() => setTheme(isDark ? 'light' : 'dark')}
                            aria-label="Toggle theme"
                            className="w-9 h-9 flex items-center justify-center border-none bg-transparent text-psj-text-2 rounded-none cursor-pointer transition-colors hover:border-psj-border-hover hover:bg-psj-surface-1"
                        >
                            {isDark ? (
                                <Sun size={15} className="text-[#FBC94A]" />
                            ) : (
                                <Moon size={15} className="text-psj-text-1" />
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
                            <div className="flex items-center justify-between px-6 h-16 border-b border-psj-border">
                                <TechnoStarLogo variant="inline" className="h-6 w-auto" />
                                <button
                                    onClick={() => setMobileOpen(false)}
                                    className="text-psj-text-2 hover:text-psj-text-1 transition-colors"
                                >
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
                                            className="flex items-center px-4 py-3.5 text-[13px] font-bold transition-colors"
                                            style={{
                                                color: active ? 'var(--psj-blue)' : 'var(--psj-text-2)',
                                                background: active ? 'var(--psj-blue-subtle)' : 'transparent',
                                                borderLeft: active
                                                    ? '3px solid var(--psj-blue)'
                                                    : '3px solid transparent',
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
                                                <div className="pt-4 pb-2 border-b border-psj-border">
                                                    <div className="px-4 pb-4 psj-label">Documentation</div>
                                                    <div className="pl-6 space-y-6 pt-2 pb-4">
                                                        <div>
                                                            <div className="text-[11px] font-bold mb-3 uppercase tracking-wider text-psj-text-1">
                                                                Framework
                                                            </div>
                                                            <div className="flex flex-col gap-3.5 pl-2 text-[13px] text-psj-text-2">
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Introduction
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/quick-start"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Quick Start
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/psj-structure"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Structure
                                                                </Link>
                                                            </div>
                                                        </div>
                                                        <div>
                                                            <div className="text-[11px] font-bold mb-3 uppercase tracking-wider text-psj-text-1">
                                                                Guides
                                                            </div>
                                                            <div className="flex flex-col gap-3.5 pl-2 text-[13px] text-psj-text-2">
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/guides/basic"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Basic
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/guides/intermediate"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Intermediate
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/guides/advanced"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Advanced
                                                                </Link>
                                                            </div>
                                                        </div>
                                                        <div>
                                                            <div className="text-[11px] font-bold mb-3 uppercase tracking-wider text-psj-text-1">
                                                                API Reference
                                                            </div>
                                                            <div className="flex flex-col gap-3.5 pl-2 text-[13px] text-psj-text-2">
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/api/data-types"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Data Types
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/api/macro"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    Macro
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/api/psj-command"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    PSJ Command
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/api/psj-gui"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    PSJ-GUI
                                                                </Link>
                                                                <Link
                                                                    onClick={() => setMobileOpen(false)}
                                                                    href="/docs/api/psj-utility"
                                                                    className="hover:text-psj-blue transition-colors"
                                                                >
                                                                    PSJ-Utility
                                                                </Link>
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
