'use client';

import * as React from 'react';
import { X, ExternalLink } from 'lucide-react';
import { cn } from '@/lib/cn';
import { Presence } from '@radix-ui/react-presence';

import { getPreviewData, type PreviewData } from '@/app/api/preview/actions';
import { usePathname } from 'next/navigation';
import { LinkPreviewProvider } from '@/components/mdx/link-preview';

interface SidebarContextType {
    open: (href: string) => void;
    close: () => void;
    isOpen: boolean;
    currentHref: string | null;
}

const LinkSidebarContext = React.createContext<SidebarContextType | null>(null);

export function useLinkSidebar() {
    const context = React.useContext(LinkSidebarContext);
    if (!context) {
        throw new Error('useLinkSidebar must be used within a LinkSidebarProvider');
    }
    return context;
}

export function LinkSidebarProvider({ children }: { children: React.ReactNode }) {
    const [isOpen, setIsOpen] = React.useState(false);
    const [currentHref, setCurrentHref] = React.useState<string | null>(null);
    const pathname = usePathname();

    // Close sidebar on navigation
    React.useEffect(() => {
        setIsOpen(false);
    }, [pathname]);

    const open = React.useCallback((href: string) => {
        setCurrentHref(href);
        setIsOpen(true);
    }, []);

    const close = React.useCallback(() => {
        setIsOpen(false);
    }, []);

    return (
        <LinkSidebarContext.Provider value={{ open, close, isOpen, currentHref }}>
            {children}
        </LinkSidebarContext.Provider>
    );
}

export function LinkSidebar() {
    const { isOpen, close, currentHref } = useLinkSidebar();
    const [data, setData] = React.useState<PreviewData | null>(null);
    const [isLoading, setIsLoading] = React.useState(false);
    const [error, setError] = React.useState(false);

    // Resizing state
    const [width, setWidth] = React.useState(400);
    const [isResizing, setIsResizing] = React.useState(false);

    // Load persisted width
    React.useEffect(() => {
        const saved = localStorage.getItem('link-sidebar-width');
        if (saved) {
            const parsed = parseInt(saved, 10);
            if (!isNaN(parsed) && parsed >= 320) {
                setWidth(parsed);
            }
        }
    }, []);

    // Save width when it changes
    React.useEffect(() => {
        if (width !== 400) {
            localStorage.setItem('link-sidebar-width', width.toString());
        }
    }, [width]);

    // Use ref to store the starting width for calculation
    const isResizingRef = React.useRef(false);

    React.useEffect(() => {
        if (isOpen && currentHref) {
            void fetchData(currentHref);
        } else if (!isOpen) {
            // Delay clearing data for smooth exit animation
            const timer = setTimeout(() => setData(null), 300);
            return () => clearTimeout(timer);
        }
    }, [isOpen, currentHref]);

    // Resizing logic
    const startResizing = React.useCallback((e: React.MouseEvent) => {
        e.preventDefault();
        setIsResizing(true);
        isResizingRef.current = true;
    }, []);

    const stopResizing = React.useCallback(() => {
        setIsResizing(false);
        isResizingRef.current = false;
    }, []);

    const resize = React.useCallback((e: MouseEvent) => {
        if (!isResizingRef.current) return;

        // Calculate new width relative to the right edge of the window
        const newWidth = window.innerWidth - e.clientX;

        // Enforce bounds
        if (newWidth >= 320 && newWidth <= window.innerWidth * 0.8) {
            setWidth(newWidth);
        }
    }, []);

    React.useEffect(() => {
        if (isResizing) {
            window.addEventListener('mousemove', resize);
            window.addEventListener('mouseup', stopResizing);
            document.body.style.cursor = 'col-resize';
            document.body.style.userSelect = 'none'; // Prevent text selection
        } else {
            window.removeEventListener('mousemove', resize);
            window.removeEventListener('mouseup', stopResizing);
            document.body.style.cursor = '';
            document.body.style.userSelect = '';
        }

        return () => {
            window.removeEventListener('mousemove', resize);
            window.removeEventListener('mouseup', stopResizing);
            document.body.style.cursor = '';
            document.body.style.userSelect = '';
        };
    }, [isResizing, resize, stopResizing]);

    const fetchData = async (href: string) => {
        setIsLoading(true);
        setError(false);
        try {
            const result = await getPreviewData(href);
            if (result) {
                setData(result);
            } else {
                setError(true);
            }
        } catch (err) {
            console.error('[LinkSidebar] fetch error:', err);
            setError(true);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <style>
                {`
                @keyframes link-sidebar-open {
                  from { translate: 100% 0; }
                  to { translate: 0 0; }
                }
                @keyframes link-sidebar-close {
                  from { width: var(--link-sidebar-width); }
                  to { width: 0px; }
                }
                @keyframes link-sidebar-mobile-open {
                  from { transform: translateY(100%); }
                  to { transform: translateY(0); }
                }
                @keyframes link-sidebar-mobile-close {
                  from { transform: translateY(0); }
                  to { transform: translateY(100%); }
                }
                `}
            </style>

            {/* Backdrop */}
            <Presence present={isOpen}>
                <div
                    data-state={isOpen ? 'open' : 'closed'}
                    className="fixed inset-0 z-60 backdrop-blur-xs bg-fd-overlay data-[state=open]:animate-fd-fade-in data-[state=closed]:animate-fd-fade-out lg:hidden"
                    onClick={close}
                />
            </Presence>

            {/* Sidebar Panel */}
            <Presence present={isOpen}>
                <div
                    className={cn(
                        'overflow-hidden z-70 bg-fd-card text-fd-card-foreground',
                        'max-lg:fixed max-lg:inset-x-0 max-lg:bottom-0 max-lg:w-full max-lg:h-[85dvh] max-lg:flex max-lg:flex-col max-lg:border-t max-lg:rounded-t-2xl max-lg:shadow-2xl',
                        'lg:fixed lg:inset-y-0 lg:right-0 lg:h-screen lg:border-s lg:ms-auto lg:w-(--link-sidebar-width)',
                        isOpen
                            ? 'max-lg:animate-[link-sidebar-mobile-open_400ms_cubic-bezier(0.16,1,0.3,1)] lg:animate-[link-sidebar-open_400ms_cubic-bezier(0.16,1,0.3,1)]'
                            : 'max-lg:animate-[link-sidebar-mobile-close_400ms_cubic-bezier(0.16,1,0.3,1)] lg:animate-[link-sidebar-close_400ms_cubic-bezier(0.16,1,0.3,1)]',
                        // Disable transitions during drag for 1:1 response
                        isResizing && 'transition-none animate-none',
                    )}
                    style={
                        {
                            '--link-sidebar-width': `${width}px`,
                        } as React.CSSProperties
                    }
                >
                    {/* Resizer Handle (Left Edge) */}
                    <div
                        onMouseDown={startResizing}
                        className={cn(
                            'absolute left-0 top-0 bottom-0 w-1 z-50 cursor-col-resize hidden lg:block transition-colors shrink-0',
                            isResizing ? 'bg-fd-primary/40' : 'hover:bg-fd-primary/20',
                        )}
                    />

                    <div className="flex flex-col size-full bg-fd-background">
                        {/* Header */}
                        <div className="flex items-center justify-between sticky top-0 z-20 border-b border-fd-border/50 bg-fd-background px-4 py-3">
                            <div className="flex-1 min-w-0">
                                {isLoading ? (
                                    <div className="space-y-2">
                                        <div className="h-4 w-32 animate-pulse rounded bg-muted/50" />
                                        <div className="h-3 w-48 animate-pulse rounded bg-muted/30" />
                                    </div>
                                ) : (
                                    <div className="flex flex-col items-start gap-1">
                                        <h2 className="text-md font-semibold truncate text-fd-foreground tracking-tight leading-none">
                                            {data?.title || 'Preview'}
                                        </h2>
                                        {data?.description && (
                                            <span className="text-sm text-fd-muted-foreground line-clamp-1">
                                                {data?.description}
                                            </span>
                                        )}
                                    </div>
                                )}
                            </div>
                            <div className="flex items-center gap-1 ml-4">
                                {currentHref && (
                                    <a
                                        href={currentHref}
                                        className={cn(
                                            'p-2 hover:bg-fd-accent rounded-md transition-all group shrink-0',
                                            'text-fd-muted-foreground hover:text-fd-foreground active:scale-95',
                                        )}
                                        title="Open full page"
                                    >
                                        <ExternalLink className="size-4 opacity-70 group-hover:opacity-100 transition-opacity" />
                                    </a>
                                )}
                                <button
                                    onClick={close}
                                    className={cn(
                                        'p-2 hover:bg-fd-accent rounded-md transition-all group shrink-0',
                                        'text-fd-muted-foreground hover:text-fd-foreground active:scale-95',
                                    )}
                                    aria-label="Close sidebar"
                                >
                                    <X className="size-4 opacity-70 group-hover:opacity-100 transition-opacity" />
                                </button>
                            </div>
                        </div>

                        {/* Content Area */}
                        <div
                            className="flex-1 min-h-0 relative overflow-auto fd-scroll-container overscroll-contain"
                            style={{
                                maskImage:
                                    'linear-gradient(to bottom, transparent, white 2rem, white calc(100% - 2rem), transparent 100%)',
                                WebkitMaskImage:
                                    'linear-gradient(to bottom, transparent, white 2rem, white calc(100% - 2rem), transparent 100%)',
                            }}
                        >
                            <div className="p-4">
                                {isLoading ? (
                                    <div className="space-y-6 max-w-2xl mx-auto py-4">
                                        <div className="space-y-2">
                                            <div className="h-7 w-3/4 animate-pulse rounded bg-muted/60" />
                                            <div className="h-4 w-1/2 animate-pulse rounded bg-muted/40" />
                                        </div>
                                        <div className="space-y-3">
                                            <div className="h-4 w-full animate-pulse rounded bg-muted/40" />
                                            <div className="h-4 w-[95%] animate-pulse rounded bg-muted/40" />
                                            <div className="h-4 w-[90%] animate-pulse rounded bg-muted/40" />
                                        </div>
                                        <div className="h-40 w-full animate-pulse rounded bg-muted/20" />
                                    </div>
                                ) : error ? (
                                    <div className="flex flex-col items-center justify-center py-24 text-center space-y-4">
                                        <div className="size-14 rounded-2xl bg-red-500/5 border border-red-500/10 flex items-center justify-center">
                                            <X className="size-6 text-red-500/50" />
                                        </div>
                                        <div>
                                            <p className="font-semibold text-fd-foreground tracking-tight">
                                                Content Unavailable
                                            </p>
                                            <p className="text-sm text-fd-muted-foreground mt-1 max-w-[200px]">
                                                We couldn&apos;t retrieve the documentation for this
                                                link.
                                            </p>
                                        </div>
                                    </div>
                                ) : (
                                    <div
                                        className="
                                           prose prose-sm max-w-none text-sm

                                            **:text-inherit

                                            [&_h1]:hidden
                                            [&_h2]:text-base
                                            [&_h3]:text-sm

                                            [&_p]:text-sm [&_p]:leading-relaxed
                                        "
                                    >
                                        <LinkPreviewProvider allowPreview={false}>
                                            {data?.content}
                                        </LinkPreviewProvider>
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </Presence>
        </>
    );
}
