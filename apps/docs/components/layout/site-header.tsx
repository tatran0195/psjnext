'use client';

import { TechnoStarLogo } from '@/components/icons/logo';
import { Link, usePathname } from '@/i18n/navigation';
import { LanguageSelect } from '@/layouts/shared/slots/language-select';
import { FullSearchTrigger, SearchTrigger } from '@/layouts/shared/slots/search-trigger';
import { navLinks } from '@/lib/nav-links';
import { useTheme } from '@teispace/next-themes';
import { AnimatePresence, motion } from 'framer-motion';
import {
    ArrowRight,
    BookOpen,
    ChevronDown,
    Compass,
    Diamond,
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
import { Fragment, ReactNode, useEffect, useState } from 'react';
interface SiteHeaderProps {
    /** When true, header starts transparent and gains background on scroll.
     *  When false (docs pages), header is always opaque. */
    transparent?: boolean;
}

// --- Helper Components ---

interface MegaMenuItemProps {
    href: string;
    icon: React.ElementType;
    title: string;
    description: string;
}

function MegaMenuItem({ href, icon: Icon, title, description }: MegaMenuItemProps) {
    return (
        <li>
            <Link
                href={href}
                className="group/item flex items-center gap-4 p-3 -mx-3 hover:bg-psj-surface-1 transition-all duration-300"
            >
                <div className="w-11 h-11 shrink-0 flex items-center justify-center bg-psj-surface-1 border border-psj-border text-psj-blue group-hover/item:bg-psj-blue/10 group-hover/item:border-psj-blue/30 transition-all duration-300">
                    <Icon size={18} strokeWidth={2.5} />
                </div>
                <div>
                    <div className="text-[13px] font-bold text-psj-text-1">{title}</div>
                    <div className="text-[11px] text-psj-text-3 leading-tight mt-0.5">{description}</div>
                </div>
            </Link>
        </li>
    );
}

interface MobileSubNavItemProps {
    href: string;
    title: string;
    onClick: () => void;
}

function MobileSubNavItem({ href, title, onClick }: MobileSubNavItemProps) {
    return (
        <Link onClick={onClick} href={href} className="hover:text-psj-blue transition-colors">
            {title}
        </Link>
    );
}

interface FeaturedCalloutProps {
    version?: string;
}

function FeaturedCallout({ version }: FeaturedCalloutProps) {
    return (
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
                    <span className="text-psj-blue">Jupiter {version || '5.x'}</span>
                </h5>
                <p className="text-[13px] text-psj-text-3 leading-relaxed opacity-80 mb-6">
                    Explore the latest PSJ advancements, featuring optimized Pythonic commands and the new native GUI
                    builder.
                </p>

                <div className="space-y-3">
                    <div className="flex items-center gap-3 text-[11px] text-psj-text-2">
                        <Zap size={12} className="text-psj-blue" />
                        <span className="whitespace-nowrap">New GUI Command Builder</span>
                    </div>
                    <div className="flex items-center gap-3 text-[11px] text-psj-text-2">
                        <Zap size={12} className="text-psj-blue" />
                        <span className="whitespace-nowrap">Enhanced PSJ-Utility API</span>
                    </div>
                </div>
            </div>

            <Link
                href="/changelog"
                className="psj-btn-primary w-full justify-center !text-[12px] !px-6 !py-4 !rounded-none mt-10 group/btn transition-all duration-300 hover:shadow-xl hover:shadow-psj-blue/20 relative overflow-hidden"
            >
                <div className="absolute inset-0 bg-white/10 translate-x-[-100%] group-hover/btn:translate-x-[100%] transition-transform duration-700" />
                <span className="relative z-10 whitespace-nowrap">Explore Changelog</span>
                <ArrowRight
                    size={14}
                    className="ml-2 relative z-10 group-hover/btn:translate-x-1 transition-transform"
                />
            </Link>
        </div>
    );
}

interface MainNavLinkProps {
    href: string;
    text: ReactNode;
    isActive: boolean;
}

function MainNavLink({ href, text, isActive }: MainNavLinkProps) {
    return (
        <Link
            href={href}
            className="relative px-4 py-2 text-[13px] font-semibold transition-all duration-300 group"
            style={{
                color: isActive ? 'var(--psj-blue)' : 'var(--psj-text-2)',
            }}
        >
            <span className="relative z-10 transition-colors group-hover:text-psj-text-1">{text}</span>
            {isActive && (
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
}

function MenuSectionHeader({ title, className = '' }: { title: string; className?: string }) {
    return (
        <h3 className={`psj-label text-psj-blue/60 tracking-[0.2em] uppercase text-[10px] font-bold ${className}`}>
            {title}
        </h3>
    );
}

function ThemeToggle() {
    const { resolvedTheme, setTheme } = useTheme();
    const isDark = resolvedTheme === 'dark';

    return (
        <button
            onClick={() => setTheme(isDark ? 'light' : 'dark')}
            aria-label="Toggle theme"
            className="w-9 h-9 flex items-center justify-center border-none bg-transparent text-psj-text-2 rounded-none cursor-pointer transition-colors hover:border-psj-border-hover hover:bg-psj-surface-1"
        >
            {isDark ? <Sun size={15} className="text-[#FBC94A]" /> : <Moon size={15} className="text-psj-text-1" />}
        </button>
    );
}

export function SiteHeader({ transparent = false }: SiteHeaderProps) {
    const [scrolled, setScrolled] = useState(false);
    const [mobileOpen, setMobileOpen] = useState(false);
    const pathname = usePathname();

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

    const DOCS_NAVIGATION = [
        {
            title: 'Framework',
            items: [
                { title: 'Introduction', description: 'Core concepts', href: '/docs', icon: Home },
                { title: 'Quick Start', description: 'Setup in minutes', href: '/docs/quick-start', icon: Zap },
                { title: 'Structure', description: 'Architecture overview', href: '/docs/psj-structure', icon: Layers },
                {
                    title: 'Data Types',
                    description: 'Type definitions',
                    href: '/docs/data-type',
                    icon: Diamond,
                },
            ],
        },
        {
            title: 'Guides',
            items: [
                { title: 'Basic', description: 'Essential features', href: '/docs/guides/basic', icon: BookOpen },
                {
                    title: 'Intermediate',
                    description: 'Advanced patterns',
                    href: '/docs/guides/intermediate',
                    icon: Compass,
                },
                {
                    title: 'Advanced',
                    description: 'Optimization & tuning',
                    href: '/docs/guides/advanced',
                    icon: GraduationCap,
                },
            ],
        },
        {
            title: 'API Reference',
            items: [
                {
                    title: 'Macro',
                    description: 'Built-in Jupiter API',
                    href: getVersionedLink('/docs/api/macro'),
                    icon: Play,
                },
                {
                    title: 'PSJ Command',
                    description: 'Pythonic Command System',
                    href: getVersionedLink('/docs/api/psj-command'),
                    icon: Terminal,
                },
                {
                    title: 'PSJ-Utility',
                    description: 'Model Querying & Helpers',
                    href: getVersionedLink('/docs/api/psj-utility'),
                    icon: Package,
                },
                {
                    title: 'PSJ-GUI',
                    description: 'GUI Creation Library',
                    href: getVersionedLink('/docs/api/psj-gui'),
                    icon: Layout,
                },
            ],
        },
    ];

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
                                <MainNavLink key={link.url} href={link.url} text={link.text} isActive={active} />
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
                                                    <div className="absolute -top-1.5 left-1/2 -translate-x-1/2 w-3 h-3 bg-psj-blue rotate-45" />

                                                    <div className="h-1 bg-psj-blue w-full relative z-10" />
                                                    <div className="grid grid-cols-12">
                                                        <div className="col-span-8 py-8 px-10 grid grid-cols-3 gap-x-12 gap-y-10">
                                                            {DOCS_NAVIGATION.map((section) => (
                                                                <div key={section.title}>
                                                                    <MenuSectionHeader
                                                                        title={section.title}
                                                                        className="mb-8"
                                                                    />
                                                                    <ul className="space-y-1">
                                                                        {section.items.map((item) => (
                                                                            <MegaMenuItem key={item.title} {...item} />
                                                                        ))}
                                                                    </ul>
                                                                </div>
                                                            ))}
                                                        </div>

                                                        {/* Right Side Callout (The "Cover" Area) */}
                                                        <FeaturedCallout version={latestVersion} />
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
                        <FullSearchTrigger className="hidden sm:inline-flex h-9 w-48 bg-transparent hover:bg-psj-surface-1 border-psj-border text-psj-text-2 hover:text-psj-text-1 transition-colors" />
                        <SearchTrigger className="sm:hidden" color="ghost" />

                        <LanguageSelect
                            className="h-9 w-9 border-none p-0 flex items-center justify-center rounded-none"
                            style={{ color: 'var(--psj-text-2)' }}
                        >
                            <Globe size={15} />
                        </LanguageSelect>

                        <ThemeToggle />
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
                                                <div className="pt-4 pb-2 border-b border-psj-border">
                                                    <div className="px-4 pb-4 psj-label">Documentation</div>
                                                    <div className="pl-6 space-y-6 pt-2 pb-4">
                                                        {DOCS_NAVIGATION.map((section) => (
                                                            <div key={section.title}>
                                                                <MenuSectionHeader
                                                                    title={section.title}
                                                                    className="mb-3 !text-psj-text-1"
                                                                />
                                                                <div className="flex flex-col gap-3.5 pl-2 text-[13px] text-psj-text-2">
                                                                    {section.items.map((item) => (
                                                                        <MobileSubNavItem
                                                                            key={item.title}
                                                                            href={item.href}
                                                                            title={item.title}
                                                                            onClick={() => setMobileOpen(false)}
                                                                        />
                                                                    ))}
                                                                </div>
                                                            </div>
                                                        ))}
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
