import type { HTMLAttributes, ReactNode } from 'react';

import type { CalloutLevel, Example, ResolvedItem, ResolvedParam } from '../types';

import type { ShikiFactory } from 'fumadocs-core/highlight/shiki';
import type { BundledTheme, CodeOptionsThemes, CodeToHastOptionsCommon } from 'shiki';

// ─── Awaitable helper ─────────────────────────────────────────────────────────

export type Awaitable<T> = T | Promise<T>;

// ─── Render context ───────────────────────────────────────────────────────────

export interface PsjRenderContext {
    /** The resolved item being rendered */
    item: ResolvedItem;

    /** Active SDK version */
    version: string;

    /** Active locale */
    locale: string;

    shiki: ShikiFactory;
    shikiOptions: Omit<CodeToHastOptionsCommon, 'lang'> & CodeOptionsThemes<BundledTheme>;

    renderMarkdown: (md: string) => Awaitable<ReactNode>;
    renderCodeBlock: (lang: string, code: string) => Awaitable<ReactNode>;
    renderHeading: (
        depth: number,
        text: string | ReactNode,
        props?: HTMLAttributes<HTMLHeadingElement> & { id?: string },
    ) => ReactNode;
}

// ─── Default Shiki theme ──────────────────────────────────────────────────────

export const DEFAULT_SHIKI_OPTIONS: Omit<CodeToHastOptionsCommon, 'lang'> &
    CodeOptionsThemes<BundledTheme> = {
    themes: { light: 'github-light', dark: 'github-dark' },
};

// ─── Layout slot types ────────────────────────────────────────────────────────

export interface ItemLayoutSlots {
    /** Title (h1) of the item */
    header: ReactNode;
    /** Description markdown block */
    description: ReactNode;
    /** Domain badge + ribbon/namespace info */
    meta: ReactNode;
    /** Callout boxes (warnings, info) */
    callouts: ReactNode;
    /** Syntax string block */
    syntax: ReactNode;
    /** Parameters table */
    params: ReactNode;
    /** Returns section */
    returns: ReactNode;
    /** See-also links */
    seeAlso: ReactNode;
    /**
     * Examples panel — rendered on the RIGHT side in split-panel layouts,
     * NOT in the left content column.  This is the key difference from OpenAPI.
     */
    examplesPanel: ReactNode;
}

// ─── Page-level options ───────────────────────────────────────────────────────

export interface CreatePSJAPIPageOptions {
    /**
     * Shiki factory to use for syntax highlighting.
     * Defaults to `defaultShikiFactory` from `fumadocs-core/highlight/shiki/full`.
     * You do NOT need to pass this unless you want a custom Shiki instance.
     */
    shiki?: ShikiFactory;

    /**
     * Shiki theme options.
     * Defaults to `{ themes: { light: 'github-light', dark: 'github-dark' } }`.
     */
    shikiOptions?: Omit<CodeToHastOptionsCommon, 'lang'> & CodeOptionsThemes<BundledTheme>;

    renderMarkdown?: (md: string) => Awaitable<ReactNode>;
    renderCodeBlock?: (props: { lang: string; code: string }) => Awaitable<ReactNode>;
    renderHeading?: (props: HTMLAttributes<HTMLHeadingElement>, depth: number) => ReactNode;

    /**
     * Customize the overall item layout.
     *
     * The default is a two-column layout:
     *   left  — header + description + callouts + syntax + params + returns + see-also
     *   right — examples panel
     *
     * Override to change the split, add a sticky panel, etc.
     */
    renderItemLayout?: (slots: ItemLayoutSlots, ctx: PsjRenderContext) => ReactNode;

    /**
     * Customize how a single example code block is rendered inside the right panel.
     */
    renderExample?: (example: Example, ctx: PsjRenderContext) => ReactNode;

    /**
     * Customize the callout renderer.
     */
    renderCallout?: (level: CalloutLevel, text: ReactNode, ctx: PsjRenderContext) => ReactNode;

    /**
     * Customize the param table row.
     */
    renderParam?: (param: ResolvedParam, ctx: PsjRenderContext) => ReactNode;

    /**
     * Customize the returns section.
     */
    renderReturns?: (item: ResolvedItem, ctx: PsjRenderContext) => ReactNode;

    /**
     * Resolve a $ref string or "domain/id" key to a page URL.
     *
     * Used for:
     *   - type strings containing $ref: e.g. "List[$ref:data-type/JPT_FOO]"
     *   - see_also refs: e.g. { $ref: "macro/AdvcStaticProcess" }
     *
     * The second argument is the active locale (e.g. `'en'`, `'ja'`), so you
     * can generate locale-prefixed URLs:
     *
     *   resolveRef: (ref, locale) => `/${locale}/sdk/${ref}`
     */
    resolveRef?: (ref: string, locale: string) => string;

    /**
     * Show/hide the domain badge in the header.
     * @defaultValue true
     */
    showDomainBadge?: boolean;

    /**
     * Show/hide the ribbon path for psj-command items.
     * @defaultValue true
     */
    showRibbon?: boolean;

    /**
     * Show/hide the macro_link / command_link cross-reference card.
     * @defaultValue true
     */
    showLinkCard?: boolean;

    /**
     * Shiki language alias for PSJ macro syntax highlighting.
     * Falls back to 'python' if the alias is not registered.
     * @defaultValue 'python'
     */
    psjLanguage?: string;
}

// ─── Resolved options (internal) ──────────────────────────────────────────────
//
// After createPSJAPIPage() applies defaults, shiki and shikiOptions are always
// present. Components that receive options downstream use this type so the
// compiler knows they are non-nullable.

export interface ResolvedPSJAPIPageOptions extends Omit<
    CreatePSJAPIPageOptions,
    'shiki' | 'shikiOptions'
> {
    shiki: ShikiFactory;
    shikiOptions: Omit<CodeToHastOptionsCommon, 'lang'> & CodeOptionsThemes<BundledTheme>;
}
