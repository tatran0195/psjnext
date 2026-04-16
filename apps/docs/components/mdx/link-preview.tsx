'use client';

import * as React from 'react';
import Link from 'next/link';
import * as HoverCard from '@radix-ui/react-hover-card';
import { PanelRight, ArrowUpRight } from 'lucide-react';

import { getPreviewData, type PreviewData } from '@/app/api/preview/actions';

import { useLinkSidebar } from '@/components/mdx/link-sidebar';

interface LinkPreviewConfig {
    allowPreview: boolean;
}

const LinkPreviewContext = React.createContext<LinkPreviewConfig>({ allowPreview: true });

export function useLinkPreviewConfig() {
    return React.useContext(LinkPreviewContext);
}

export function LinkPreviewProvider({
    children,
    allowPreview,
}: {
    children: React.ReactNode;
    allowPreview: boolean;
}) {
    return (
        <LinkPreviewContext.Provider value={{ allowPreview }}>
            {children}
        </LinkPreviewContext.Provider>
    );
}

export interface LinkPreviewProps {
    href: string;
    title?: string;
    description?: string;
    children: React.ReactNode;
    allowPreview?: boolean;
}

const previewCache = new Map<string, PreviewData>();

export function LinkPreview({
    href,
    title: initialTitle,
    description: initialDescription,
    children,
    allowPreview: propAllowPreview,
}: LinkPreviewProps) {
    const { allowPreview: contextAllowPreview } = useLinkPreviewConfig();
    const allowPreview = propAllowPreview ?? contextAllowPreview;
    const { open: openSidebar } = useLinkSidebar();
    const [data, setData] = React.useState<PreviewData | null>(
        initialTitle
            ? { title: initialTitle, description: initialDescription, content: null }
            : null,
    );
    const [isLoading, setIsLoading] = React.useState(!initialTitle || !data?.content);
    const [error, setError] = React.useState(false);

    const isInternal = React.useMemo(() => {
        if (href.startsWith('/') || href.startsWith('#')) return true;
        try {
            const url = new URL(href);
            return url.hostname === (typeof window !== 'undefined' ? window.location.hostname : '');
        } catch (_) {
            return false;
        }
    }, [href]);

    const handleClick = (e: React.MouseEvent) => {
        // Allow standard navigation for modified clicks
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;

        if (isInternal && !href.startsWith('#')) {
            e.preventDefault();
            openSidebar(href);
        }
    };

    const fetchData = React.useCallback(async () => {
        if (data?.content || !isLoading) return;

        if (previewCache.has(href)) {
            const cached = previewCache.get(href)!;
            if (cached.content) {
                setData(cached);
                setIsLoading(false);
                return;
            }
        }

        try {
            const result = await getPreviewData(href);
            if (!result) {
                setError(true);
            } else {
                previewCache.set(href, result);
                setData(result);
            }
        } catch (err) {
            console.error('LinkPreview fetch error:', err);
            setError(true);
        } finally {
            setIsLoading(false);
        }
    }, [href, data, isLoading]);

    if (!allowPreview) {
        return (
            <Link
                href={href}
                onClick={handleClick}
                className="font-medium text-primary underline decoration-dotted underline-offset-4"
            >
                {children}
            </Link>
        );
    }

    return (
        <HoverCard.Root
            openDelay={200}
            closeDelay={100}
            onOpenChange={(open) => {
                if (open) fetchData();
            }}
        >
            <HoverCard.Trigger asChild>
                <Link
                    href={href}
                    onClick={handleClick}
                    className="font-medium text-primary underline decoration-dotted underline-offset-4"
                >
                    {children}
                </Link>
            </HoverCard.Trigger>

            <HoverCard.Portal>
                <HoverCard.Content
                    side="top"
                    align="center"
                    sideOffset={10}
                    collisionPadding={16}
                    sticky="always"
                    className="z-50 w-[min(450px,calc(100vw-2rem))] max-h-(--radix-hover-card-content-available-height) overflow-hidden rounded-xl border bg-fd-popover/95 p-0 shadow-2xl backdrop-blur-md animate-in fade-in zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2"
                >
                    <div className="flex flex-col max-h-[min(500px,var(--radix-hover-card-content-available-height))]">
                        <div className="border-b bg-muted/30 px-4 py-3">
                            {isLoading ? (
                                <div className="h-5 w-1/2 animate-pulse rounded bg-muted" />
                            ) : (
                                <p className="truncate text-sm font-semibold text-fd-foreground">
                                    {data?.title}
                                </p>
                            )}
                            {data?.description && !isLoading && (
                                <p className="truncate text-xs text-fd-muted-foreground mt-0.5">
                                    {data.description}
                                </p>
                            )}
                        </div>

                        <div className="flex-1 overflow-auto min-h-0 fd-scroll-container">
                            <div className="p-4">
                                {isLoading ? (
                                    <div className="flex flex-col gap-3 py-2">
                                        <div className="h-4 w-full animate-pulse rounded bg-muted" />
                                        <div className="h-4 w-[90%] animate-pulse rounded bg-muted" />
                                        <div className="h-4 w-[95%] animate-pulse rounded bg-muted" />
                                        <div className="h-4 w-[80%] animate-pulse rounded bg-muted" />
                                    </div>
                                ) : error ? (
                                    <div className="flex flex-col items-center justify-center py-8 text-center">
                                        <p className="text-sm font-medium text-fd-muted-foreground">
                                            Failed to load preview content
                                        </p>
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

                        <div className="flex border-t divide-x bg-muted/10">
                            <Link
                                href={href}
                                className="flex-1 flex items-center justify-center gap-2 px-3 py-2.5 text-[11px] font-medium text-fd-muted-foreground hover:bg-fd-accent hover:text-fd-accent-foreground transition-all active:bg-fd-accent/80 active:scale-[0.98]"
                            >
                                <ArrowUpRight className="size-3.5 opacity-70" />
                                <span>Open Page</span>
                            </Link>

                            {isInternal && (
                                <button
                                    type="button"
                                    onClick={(e) => {
                                        e.preventDefault();
                                        openSidebar(href);
                                    }}
                                    className="flex-1 flex items-center justify-center gap-2 px-3 py-2.5 text-[11px] font-medium text-fd-muted-foreground hover:bg-fd-accent hover:text-fd-accent-foreground transition-all active:bg-fd-accent/80 active:scale-[0.98]"
                                >
                                    <PanelRight className="size-3.5 opacity-70" />
                                    <span>In Sidebar</span>
                                </button>
                            )}
                        </div>
                    </div>
                </HoverCard.Content>
            </HoverCard.Portal>
        </HoverCard.Root>
    );
}
