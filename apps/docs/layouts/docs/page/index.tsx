'use client';
import { type ComponentProps, createContext, type FC, type ReactNode, use, useEffect, useState } from 'react';

import { I18nLabel, useI18n } from 'fumadocs-ui/contexts/i18n';
import { useCopyButton } from 'fumadocs-ui/utils/use-copy-button';
import { Check, Copy, Edit } from 'lucide-react';

import { buttonVariants } from '@/components/ui/button';
import { cn } from '@/lib/cn';

import { Breadcrumb, type BreadcrumbProps } from './slots/breadcrumb';
import { Container } from './slots/container';
import { Footer, type FooterProps } from './slots/footer';
import { TOC, TOCPopover, type TOCPopoverProps, type TOCProps, TOCProvider, type TOCProviderProps } from './slots/toc';

import type { TOCItemType } from 'fumadocs-core/toc';

export interface DocsPageProps extends ComponentProps<'article'> {
    toc?: TOCItemType[];
    /**
     * Extend the page to fill all available space
     *
     * @defaultValue false
     */
    full?: boolean;
    slots?: Partial<DocsPageSlots>;

    footer?: FooterOptions;
    breadcrumb?: BreadcrumbOptions;
    tableOfContent?: TableOfContentOptions;
    tableOfContentPopover?: TableOfContentPopoverOptions;
}

interface BreadcrumbOptions extends BreadcrumbProps {
    enabled?: boolean;
    /**
     * @deprecated use `slots.breadcrumb` instead.
     */
    component?: ReactNode;
}

interface FooterOptions extends FooterProps {
    enabled?: boolean;
    /**
     * @deprecated use `slots.footer` instead.
     */
    component?: ReactNode;
}

interface TableOfContentOptions extends Pick<TOCProviderProps, 'single'>, TOCProps {
    enabled?: boolean;
    /**
     * @deprecated use `slots.toc` instead.
     */
    component?: ReactNode;
}

interface TableOfContentPopoverOptions extends TOCPopoverProps {
    enabled?: boolean;
    /**
     * @deprecated use `slots.tocPopover` instead.
     */
    component?: ReactNode;
}

interface DocsPageSlots {
    toc: {
        provider: FC<TOCProviderProps>;
        main: FC<TOCProps>;
        popover: FC<TOCPopoverProps>;
    };
    container: FC<ComponentProps<'article'>>;
    footer: FC<FooterProps>;
    breadcrumb: FC<BreadcrumbProps>;
}

type PageSlotsProps = {
    full: boolean;
    setFull: (full: boolean) => void;
};

const PageContext = createContext<{
    props: PageSlotsProps;
    slots: DocsPageSlots;
} | null>(null);

export function useDocsPage() {
    const context = use(PageContext);
    if (!context)
        throw new Error('Please use page components under <DocsPage /> (`fumadocs-ui/layouts/notebook/page`).');
    return context;
}

export function DocsPage({
    tableOfContent: { enabled: tocEnabled, single, ...tocProps } = {},
    tableOfContentPopover: { enabled: tocPopoverEnabled, ...tocPopoverProps } = {},
    breadcrumb: { enabled: breadcrumbEnabled = true, ...breadcrumb } = {},
    footer: { enabled: footerEnabled = true, ...footer } = {},
    full = false,
    toc = [],
    slots: defaultSlots = {},
    children,
    ...containerProps
}: DocsPageProps) {
    const [isFull, setIsFull] = useState(full);

    useEffect(() => {
        setIsFull(full);
    }, [full]);

    tocEnabled ??= Boolean(!isFull && (toc.length > 0 || tocProps.footer || tocProps.header));
    tocPopoverEnabled ??= Boolean(toc.length > 0 || tocPopoverProps.header || tocPopoverProps.footer);

    const slots: DocsPageSlots = {
        breadcrumb: defaultSlots.breadcrumb ?? Breadcrumb,
        footer: defaultSlots.footer ?? Footer,
        toc: defaultSlots.toc ?? {
            provider: TOCProvider,
            main: TOC,
            popover: TOCPopover,
        },
        container: defaultSlots.container ?? Container,
    };

    return (
        <PageContext
            value={{
                props: { full: isFull, setFull: setIsFull },
                slots,
            }}
        >
            <slots.toc.provider single={single} toc={tocEnabled || tocPopoverEnabled ? toc : []}>
                {tocPopoverEnabled && (tocPopoverProps.component ?? <slots.toc.popover {...tocPopoverProps} />)}
                <slots.container {...containerProps}>
                    {breadcrumbEnabled && (breadcrumb.component ?? <slots.breadcrumb {...breadcrumb} />)}
                    {children}
                    {footerEnabled && (footer.component ?? <slots.footer {...footer} />)}
                </slots.container>
                {tocEnabled && (tocProps.component ?? <slots.toc.main {...tocProps} />)}
            </slots.toc.provider>
        </PageContext>
    );
}

export function EditOnGitHub(props: ComponentProps<'a'>) {
    return (
        <a
            target="_blank"
            rel="noreferrer noopener"
            {...props}
            className={cn(
                buttonVariants({
                    color: 'secondary',
                    size: 'sm',
                }),
                'gap-1.5 not-prose',
                props.className,
            )}
        >
            {props.children ?? (
                <>
                    <Edit className="size-3.5" />
                    <I18nLabel label="editOnGithub" />
                </>
            )}
        </a>
    );
}

/**
 * Add typography styles
 */
export function DocsBody({ children, className, ...props }: ComponentProps<'div'>) {
    return (
        <div {...props} className={cn('prose flex-1', className)}>
            {children}
        </div>
    );
}

export function DocsDescription({ children, className, ...props }: ComponentProps<'p'>) {
    // Don't render if no description provided
    if (children === undefined) return null;

    return (
        <p {...props} className={cn('mb-8 text-lg text-fd-muted-foreground', className)}>
            {children}
        </p>
    );
}

export function DocsTitle({ children, className, ...props }: ComponentProps<'h1'>) {
    const [checked, onClick] = useCopyButton(() => {
        if (typeof children === 'string') {
            navigator.clipboard.writeText(children);
        } else {
            const text = document.getElementById(props.id ?? '')?.innerText ?? '';
            if (text) navigator.clipboard.writeText(text);
        }
    });

    return (
        <h1
            {...props}
            className={cn(
                'group flex items-center gap-2 text-[1.75em] font-semibold wrap-break-word min-w-0',
                className,
            )}
        >
            <span className="flex-1 min-w-0">{children}</span>
            <button
                type="button"
                className="opacity-0 group-hover:opacity-100 transition-opacity p-2 rounded-none hover:bg-fd-muted text-fd-muted-foreground hover:text-fd-foreground shrink-0"
                onClick={onClick}
                aria-label="Copy title"
            >
                {checked ? <Check className="size-4" /> : <Copy className="size-4" />}
            </button>
        </h1>
    );
}

export function PageLastUpdate({ date: value, ...props }: Omit<ComponentProps<'p'>, 'children'> & { date: Date }) {
    const { text } = useI18n();
    const [date, setDate] = useState('');

    useEffect(() => {
        // to the timezone of client
        setDate(value.toLocaleDateString());
    }, [value]);

    return (
        <p {...props} className={cn('text-sm text-fd-muted-foreground', props.className)}>
            {text.lastUpdate} {date}
        </p>
    );
}

export { MarkdownCopyButton, ViewOptionsPopover } from '@/layouts/shared/page-actions';
export { Breadcrumb as PageBreadcrumb, type BreadcrumbProps } from './slots/breadcrumb';
export { Footer as PageFooter, type FooterProps } from './slots/footer';
