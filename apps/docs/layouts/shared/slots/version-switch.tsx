'use client';

import { useEffect, useRef, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import { Check } from 'lucide-react';
import { usePathname, useRouter } from 'next/navigation';

import { useVersionContext, type VersionItem } from '@/contexts/versions';

function formatVersion(item: VersionItem, isLatest: boolean): { label: string; badge: string | undefined } {
    return {
        label: `v${item.value}`,
        badge: isLatest ? 'Latest' : undefined,
    };
}

export function VersionSwitcher() {
    const { versions, currentVersion, setCurrentVersion } = useVersionContext();
    const [open, setOpen] = useState(false);
    const containerRef = useRef<HTMLDivElement>(null);
    const pathname = usePathname();
    const router = useRouter();

    useEffect(() => {
        function onClickOutside(e: MouseEvent) {
            if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
                setOpen(false);
            }
        }
        if (open) {
            document.addEventListener('mousedown', onClickOutside);
        }
        return () => document.removeEventListener('mousedown', onClickOutside);
    }, [open]);

    function handleSelect(item: VersionItem) {
        setCurrentVersion(item.value);
        setOpen(false);

        // Pathname: /{lang}/api/{version}/...rest
        // segments: ['', lang, 'api', version, ...rest]
        const segments = pathname.split('/');
        const apiIdx = segments.indexOf('api');

        if (apiIdx !== -1 && segments[apiIdx + 1]) {
            // Swap the version segment and push to the equivalent page.
            segments[apiIdx + 1] = item.value;
            router.push(segments.join('/'));
        } else {
            // Not on an API page — go to the API root for the selected version.
            const lang = segments[1] ?? 'en';
            router.push(`/${lang}/api/${item.value}`);
        }
    }

    // Derive label/badge for the active button display.
    const activeItem = versions.find((v) => v.value === currentVersion) ?? versions[0];
    const activeFormatted = activeItem
        ? formatVersion(activeItem, activeItem === versions[0])
        : { label: 'Select version', badge: undefined };

    if (versions.length === 0) return null;

    return (
        <div ref={containerRef} className="relative border-y border-foreground/5">
            <button
                type="button"
                onClick={() => setOpen((v) => !v)}
                className="group/version flex w-full items-center gap-2 px-4 py-[9px] text-sm text-foreground/55 hover:text-foreground/80 hover:bg-foreground/3 transition-colors"
            >
                <svg
                    className="size-4 shrink-0 text-foreground opacity-55 group-hover/version:opacity-80 transition-opacity"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                >
                    <path d="M7 8.25a2.75 2.75 0 1 0 0-5.5a2.75 2.75 0 0 0 0 5.5m0 0V12m0 3.75a2.75 2.75 0 1 0 0 5.5a2.75 2.75 0 0 0 0-5.5m0 0V12m10-3.75a2.75 2.75 0 1 0 0-5.5a2.75 2.75 0 0 0 0 5.5m0 0V9a3 3 0 0 1-3 3H7" />
                </svg>
                <span className="truncate">{activeFormatted.label}</span>
                {activeFormatted.badge && (
                    <span className="font-mono text-[9px] uppercase tracking-wider px-1.5 py-0.5 border border-dashed border-foreground/20 text-foreground/45">
                        {activeFormatted.badge}
                    </span>
                )}
                {/* Up/down chevron */}
                <svg className="ml-auto size-4 shrink-0 text-foreground/40" viewBox="0 0 16 16" fill="none">
                    <path
                        d="M5 6.5L8 3.5L11 6.5"
                        stroke="currentColor"
                        strokeWidth="1.2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                    />
                    <path
                        d="M5 9.5L8 12.5L11 9.5"
                        stroke="currentColor"
                        strokeWidth="1.2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                    />
                </svg>
            </button>

            <AnimatePresence>
                {open && (
                    <motion.div
                        initial={{ opacity: 0, y: -4 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -4 }}
                        transition={{ duration: 0.12, ease: 'easeOut' }}
                        className="absolute left-0 right-0 top-full z-50 border-b border-foreground/[0.08] bg-background shadow-lg shadow-black/10 dark:shadow-black/40 py-1"
                    >
                        {versions.map((item, idx) => {
                            const isActive = item.value === currentVersion;
                            const { label, badge } = formatVersion(item, idx === 0);
                            return (
                                <button
                                    key={item.value}
                                    type="button"
                                    onClick={() => handleSelect(item)}
                                    className={`flex w-full items-center gap-2 px-4 py-2 text-sm transition-colors duration-150 ${
                                        isActive
                                            ? 'text-foreground bg-foreground/5'
                                            : 'text-foreground/55 hover:text-foreground/80 hover:bg-foreground/3'
                                    }`}
                                >
                                    <span className="size-4 shrink-0 flex items-center justify-center">
                                        {isActive && <Check className="size-3.5 text-foreground/70" />}
                                    </span>
                                    <span className="truncate">{label}</span>
                                    {badge && (
                                        <span className="font-mono text-[9px] uppercase tracking-wider px-1.5 py-0.5 border border-dashed border-foreground/20 text-foreground/45">
                                            {badge}
                                        </span>
                                    )}
                                </button>
                            );
                        })}
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
}
