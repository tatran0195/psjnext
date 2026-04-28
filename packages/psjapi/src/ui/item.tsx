import { type HTMLAttributes, type ReactNode, Fragment } from 'react';

import {
    CodeBlock,
    CodeBlockTab,
    CodeBlockTabs,
    CodeBlockTabsList,
    CodeBlockTabsTrigger,
    Pre,
} from 'fumadocs-ui/components/codeblock';
import { Heading } from 'fumadocs-ui/components/heading';

import type {
    CalloutLevel,
    Domain,
    Example,
    ResolvedItem,
    ResolvedParam,
    Returns,
    SeeAlsoRef,
} from '../types';
import type { ItemLayoutSlots, PsjRenderContext, ResolvedPSJAPIPageOptions } from './context';

import { cn } from '../utils/cn';
import { ParamsPanel } from './params-panel';

// ─── Domain badge ─────────────────────────────────────────────────────────────

const DOMAIN_COLORS: Record<Domain, string> = {
    macro: 'bg-purple-500/10 text-purple-700 dark:text-purple-300 border-purple-400/40',
    'psj-command': 'bg-blue-500/10 text-blue-700 dark:text-blue-300 border-blue-400/40',
    'psj-utility': 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 border-emerald-400/40',
    'psj-gui': 'bg-orange-500/10 text-orange-700 dark:text-orange-300 border-orange-400/40',
};

const DOMAIN_LABELS: Record<Domain, string> = {
    macro: 'Macro',
    'psj-command': 'PSJ Command',
    'psj-utility': 'PSJ Utility',
    'psj-gui': 'PSJ GUI',
};

function DomainBadge({ domain }: { domain: Domain }) {
    return (
        <span
            className={cn(
                'inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold font-mono',
                DOMAIN_COLORS[domain],
            )}
        >
            {DOMAIN_LABELS[domain]}
        </span>
    );
}

// ─── $ref type link ───────────────────────────────────────────────────────────
//
// psjapi type strings may contain $ref: e.g.
//   "List[$ref:data-type/JPT_ADVC_LOAD_NODE]"
//   "$ref:data-type/JPT_ADVC_STRUCT_TIME_STEP"
//
// Render them as clickable anchor links. The href is /<baseUrl>/<refPath>
// resolved by the page-level `resolveTypeRef` option (defaults to /sdk/<ref>).

function TypeWithRefs({ type, resolveRef }: { type: string; resolveRef: (ref: string) => string }) {
    // Split on $ref:... tokens, preserving surrounding text
    const parts = type.split(/(\$ref:[^\]\s,)]+)/g);
    if (parts.length === 1) {
        return <span className="text-sm font-mono text-fd-muted-foreground">{type}</span>;
    }
    return (
        <span className="text-sm font-mono text-fd-muted-foreground">
            {parts.map((part, i) => {
                if (part.startsWith('$ref:')) {
                    const ref = part.slice(5); // strip "$ref:"
                    return (
                        <a
                            key={i}
                            href={resolveRef(ref)}
                            className="underline hover:text-fd-accent-foreground transition-colors"
                        >
                            {ref.split('/').pop()} {/* show last segment as label */}
                        </a>
                    );
                }
                return <Fragment key={i}>{part}</Fragment>;
            })}
        </span>
    );
}

// ─── Callout ──────────────────────────────────────────────────────────────────

const CALLOUT_STYLES: Record<CalloutLevel, string> = {
    warn: 'border-yellow-400/50 bg-yellow-50/50 dark:bg-yellow-900/10 text-yellow-900 dark:text-yellow-200',
    info: 'border-blue-400/50 bg-blue-50/50 dark:bg-blue-900/10 text-blue-900 dark:text-blue-200',
    danger: 'border-red-400/50 bg-red-50/50 dark:bg-red-900/10 text-red-900 dark:text-red-200',
};

const CALLOUT_ICONS: Record<CalloutLevel, string> = {
    warn: '⚠',
    info: 'ℹ',
    danger: '✕',
};

function CalloutBox({ level, children }: { level: CalloutLevel; children: ReactNode }) {
    return (
        <div
            className={cn(
                'not-prose flex gap-3 rounded-lg border p-4 text-sm my-3',
                CALLOUT_STYLES[level],
            )}
        >
            <span className="shrink-0 text-base leading-5">{CALLOUT_ICONS[level]}</span>
            <div className="min-w-0">{children}</div>
        </div>
    );
}

// ─── InfoTag — exact match of openapi InfoTag ─────────────────────────────────

function InfoTag({ label, value }: { label: string; value: string }) {
    return (
        <div className="flex flex-row items-start gap-2 bg-fd-secondary border rounded-lg text-xs p-1.5 shadow-md max-w-full">
            <span className="font-medium shrink-0">{label}</span>
            <code className="min-w-0 flex-1 text-fd-muted-foreground break-all">{value}</code>
        </div>
    );
}

// ─── Property — exact match of openapi Property ───────────────────────────────

function Property({
    name,
    type,
    required,
    deprecated,
    removed,
    nested = false,
    className,
    children,
}: {
    name: ReactNode;
    type: ReactNode;
    required?: boolean;
    deprecated?: boolean;
    removed?: boolean;
    nested?: boolean;
    className?: string;
    children?: ReactNode;
}) {
    return (
        <div
            className={cn(
                'text-sm border-t',
                nested
                    ? 'p-3 border-x bg-fd-card last:rounded-b-xl first:rounded-tr-xl last:border-b'
                    : 'py-4 first:border-t-0',
                removed && 'opacity-50',
                className,
            )}
        >
            <div className="flex flex-wrap items-center gap-3 not-prose">
                <span
                    className={cn(
                        'font-medium font-mono text-fd-primary',
                        removed && 'line-through',
                    )}
                >
                    {name}
                    {required ? (
                        <span className="text-red-400">*</span>
                    ) : (
                        <span className="text-fd-muted-foreground">?</span>
                    )}
                </span>
                {type}
                {deprecated && !removed && (
                    <span className="ms-auto font-mono font-medium text-xs text-yellow-600 dark:text-yellow-400">
                        deprecated
                    </span>
                )}
                {removed && (
                    <span className="ms-auto font-mono font-medium text-xs text-red-500 dark:text-red-400">
                        removed
                    </span>
                )}
            </div>
            <div className="prose-no-margin pt-2.5 empty:hidden">{children}</div>
        </div>
    );
}

// ─── Param property ───────────────────────────────────────────────────────────

function ParamProperty({
    param,
    isMacro,
    descriptionNode,
    resolveRef,
}: {
    param: ResolvedParam;
    isMacro: boolean;
    descriptionNode: ReactNode;
    resolveRef: (ref: string) => string;
}) {
    const displayName = param.display_name ?? param.name;
    const nameNode = (
        <>
            {isMacro && param.position !== undefined && (
                <span className="text-fd-muted-foreground me-1 text-[0.65rem]">
                    {param.position}.
                </span>
            )}
            {displayName}
        </>
    );

    const typeNode = <TypeWithRefs type={param.type} resolveRef={resolveRef} />;

    return (
        <Property
            name={nameNode}
            type={typeNode}
            required={param.required}
            deprecated={param.deprecated}
            removed={param.removed}
        >
            {descriptionNode}
            {param.default !== undefined && (
                <div className="flex flex-row gap-2 flex-wrap my-2 not-prose">
                    <InfoTag label="Default" value={param.default} />
                </div>
            )}
            {param.enum_values && param.enum_values.length > 0 && (
                <div className="flex flex-row gap-2 flex-wrap my-2 not-prose">
                    <InfoTag
                        label="Enum"
                        value={param.enum_values.map((ev) => `${ev.id} — ${ev.label}`).join(' | ')}
                    />
                </div>
            )}
            {param.deprecated_in && (
                <div className="flex flex-row gap-2 flex-wrap my-2 not-prose">
                    <InfoTag label="Deprecated in" value={param.deprecated_in} />
                </div>
            )}
            {param.removed_in && (
                <div className="flex flex-row gap-2 flex-wrap my-2 not-prose">
                    <InfoTag label="Removed in" value={param.removed_in} />
                </div>
            )}
        </Property>
    );
}

// ─── Returns section ──────────────────────────────────────────────────────────

function ReturnsSection({
    returns,
    resolveRef,
}: {
    returns: Returns;
    resolveRef: (ref: string) => string;
}) {
    if (returns.kind === 'void') {
        return <p className="text-sm text-fd-muted-foreground italic">No return value.</p>;
    }

    if (returns.kind === 'typed') {
        return (
            <Property
                name="return"
                type={<TypeWithRefs type={returns.type ?? 'unknown'} resolveRef={resolveRef} />}
                required={false}
            >
                {returns.description && (
                    <p className="text-fd-muted-foreground text-sm">{returns.description}</p>
                )}
            </Property>
        );
    }

    // macro_code — each code value as its own Property row
    if (returns.kind === 'macro_code' && returns.codes && returns.codes.length > 0) {
        return (
            <div className="flex flex-col">
                {returns.codes.map((code) => (
                    <Property
                        key={code.value}
                        name={<code>{code.value}</code>}
                        type={null}
                        required={false}
                    >
                        <p className="text-fd-muted-foreground text-sm">{code.meaning}</p>
                    </Property>
                ))}
            </div>
        );
    }

    return null;
}

// ─── See Also — proper links ──────────────────────────────────────────────────
//
// $ref format: "<domain>/<id>"
// We resolve these to page URLs using the same resolveRef function.
// Labels come from the YAML see_also[].label field.

function SeeAlsoSection({
    refs,
    resolveRef,
}: {
    refs: SeeAlsoRef[];
    resolveRef: (ref: string) => string;
}) {
    if (refs.length === 0) return null;
    return (
        <div className="not-prose flex flex-col gap-1.5">
            {refs.map((ref) => {
                const href = resolveRef(ref.$ref);
                const label = ref.label ?? ref.$ref.split('/').pop() ?? ref.$ref;
                return (
                    <a
                        key={ref.$ref}
                        href={href}
                        className="inline-flex items-center gap-1.5 text-sm text-fd-primary underline-offset-2 hover:underline"
                    >
                        <span className="text-fd-muted-foreground text-xs font-mono">
                            {ref.$ref.split('/')[0]}
                        </span>
                        {label}
                    </a>
                );
            })}
        </div>
    );
}

// ─── Syntax block ─────────────────────────────────────────────────────────────

function SyntaxBlock({ syntaxNode }: { syntaxNode: ReactNode }) {
    return <div className="prose-no-margin">{syntaxNode}</div>;
}

// ─── Item meta (domain badge + ribbon + namespace + deprecated) ───────────────

function ItemMeta({
    item,
    showDomainBadge,
    showRibbon,
}: {
    item: ResolvedItem;
    showDomainBadge: boolean;
    showRibbon: boolean;
}) {
    return (
        <div className="not-prose flex flex-wrap items-center gap-2">
            {showDomainBadge && <DomainBadge domain={item.domain} />}
            {item.namespace && (
                <code className="text-fd-muted-foreground text-xs bg-fd-muted rounded px-1.5 py-0.5">
                    {item.namespace}
                </code>
            )}
            {showRibbon && item.ribbon && (
                <span className="text-fd-muted-foreground text-xs">
                    <span className="font-medium">Ribbon:</span> <code>{item.ribbon}</code>
                </span>
            )}
            {item.version_introduced && (
                <span className="text-fd-muted-foreground text-xs">
                    Since <code>{item.version_introduced}</code>
                </span>
            )}
            {item.deprecated && (
                <span className="rounded-full border border-red-400/50 bg-red-50/50 dark:bg-red-900/10 px-2 py-0.5 text-xs text-red-700 dark:text-red-300 font-medium">
                    Deprecated
                </span>
            )}
        </div>
    );
}

// ─── Examples right panel ─────────────────────────────────────────────────────

function ExamplesPanelPre({
    examples,
    renderedNodes,
}: {
    examples: Example[];
    renderedNodes: ReactNode[];
}) {
    if (examples.length === 0) {
        return (
            <div className="rounded-lg border border-fd-border bg-fd-card p-4 text-sm text-fd-muted-foreground italic">
                No examples available.
            </div>
        );
    }

    if (examples.length === 1) {
        const ex = examples[0];
        return (
            <div className="rounded-lg border border-fd-border bg-fd-card overflow-hidden">
                {ex.title && (
                    <p className="border-b border-fd-border px-4 py-2 text-xs font-medium text-fd-muted-foreground">
                        {ex.title}
                    </p>
                )}
                <div className="prose-no-margin">{renderedNodes[0]}</div>
            </div>
        );
    }

    return (
        <div className="rounded-lg border border-fd-border bg-fd-card overflow-hidden">
            <CodeBlockTabs groupId="psjapi_examples" defaultValue="0">
                <div className="border-b border-fd-border">
                    <CodeBlockTabsList>
                        {examples.map((ex, i) => (
                            <CodeBlockTabsTrigger key={i} value={String(i)}>
                                {ex.title ?? `Example ${i + 1}`}
                            </CodeBlockTabsTrigger>
                        ))}
                    </CodeBlockTabsList>
                </div>
                {examples.map((ex, i) => (
                    <CodeBlockTab key={i} value={String(i)}>
                        <div className="prose-no-margin">{renderedNodes[i]}</div>
                    </CodeBlockTab>
                ))}
            </CodeBlockTabs>
        </div>
    );
}

// ─── Default two-column layout — exact match of openapi Operation layout ──────

function DefaultItemLayout({ slots }: { slots: ItemLayoutSlots }) {
    return (
        <div className="flex flex-col gap-x-6 gap-y-4 @4xl:flex-row @4xl:items-start @container">
            {/* LEFT: content */}
            <div className="min-w-0 flex-1">
                {slots.header}
                {slots.meta}
                {slots.description}
                {slots.callouts}
                {slots.syntax}
                {slots.params}
                {slots.returns}
                {slots.seeAlso}
            </div>
            {/* RIGHT: sticky examples panel */}
            <div className="@4xl:sticky @4xl:top-[calc(var(--fd-docs-row-1,2rem)+1rem)] @4xl:w-[400px]">
                {slots.examplesPanel}
            </div>
        </div>
    );
}

// ─── PSJAPIItemRenderer ───────────────────────────────────────────────────────

export interface PSJAPIItemRendererProps {
    item: ResolvedItem;
    version: string;
    locale: string;
    options: ResolvedPSJAPIPageOptions;
    headingLevel?: number;
}

export async function PSJAPIItemRenderer({
    item,
    version,
    locale,
    options,
    headingLevel = 1,
}: PSJAPIItemRendererProps) {
    const {
        showDomainBadge = true,
        showRibbon = true,
        psjLanguage = 'python',
        renderItemLayout,
        renderCallout,
        renderParam,
        renderReturns,
        resolveRef: resolveRefOption,
    } = options;

    const isMacro = item.domain === 'macro';

    // ── resolveRef — converts "$ref:domain/Id" or "domain/Id" to a page URL ──
    function resolveRef(ref: string): string {
        if (resolveRefOption) return resolveRefOption(ref);
        // Default: convert "psj-command/Analysis-ADVC-MakeProcess-Static"
        // to "/docs/psj-command/analysis-advc-makeprocess-static"
        const normalized = ref
            .toLowerCase()
            .replace(/[^a-z0-9/]+/g, '-')
            .replace(/^-|-$/g, '');
        return `/docs/${normalized}`;
    }

    // ── async render helpers ───────────────────────────────────────────────────
    async function renderCodeBlock(lang: string, code: string): Promise<ReactNode> {
        if (options.renderCodeBlock) return await options.renderCodeBlock({ lang, code });
        return (
            <CodeBlock className="my-0">
                <Pre>{code}</Pre>
            </CodeBlock>
        );
    }

    async function renderMarkdown(md: string): Promise<ReactNode> {
        if (options.renderMarkdown) return await options.renderMarkdown(md);
        return <p className="text-sm text-fd-muted-foreground">{md}</p>;
    }

    function renderHeading(
        depth: number,
        text: string | ReactNode,
        props?: HTMLAttributes<HTMLHeadingElement> & { id?: string },
    ): ReactNode {
        if (options.renderHeading) return options.renderHeading(props ?? {}, depth);
        return (
            <Heading as={`h${depth}` as 'h1'} id={props?.id} {...props}>
                {text}
            </Heading>
        );
    }

    const ctx: PsjRenderContext = {
        item,
        version,
        locale,
        shiki: options.shiki,
        shikiOptions: options.shikiOptions,
        renderMarkdown,
        renderCodeBlock,
        renderHeading,
    };

    // ── Build all async content in parallel where possible ────────────────────

    const [descriptionNode, syntaxCodeNode, ...calloutNodes] = await Promise.all([
        item.description ? renderMarkdown(item.description) : Promise.resolve(null),
        item.syntax ? renderCodeBlock(psjLanguage, item.syntax) : Promise.resolve(null),
        ...item.callouts.map((c) => renderMarkdown(c.text)),
    ]);

    // Param descriptions — parallel
    const paramDescNodes = await Promise.all(
        item.params.map((p) =>
            p.description ? renderMarkdown(p.description) : Promise.resolve(null),
        ),
    );

    // Example code blocks — parallel
    const exampleNodes = await Promise.all(
        item.examples.map((ex) =>
            renderCodeBlock(ex.language === 'psj' ? psjLanguage : ex.language, ex.code),
        ),
    );

    // ── Slots ─────────────────────────────────────────────────────────────────

    const headerSlot = renderHeading(headingLevel, item.title, { id: item.id });

    const metaSlot = (
        <ItemMeta item={item} showDomainBadge={showDomainBadge} showRibbon={showRibbon} />
    );

    const descriptionSlot = descriptionNode ? (
        <div className="prose-no-margin">{descriptionNode}</div>
    ) : null;

    const calloutsSlot =
        item.callouts.length > 0 ? (
            <>
                {item.callouts.map((c, i) => {
                    const text = calloutNodes[i];
                    if (renderCallout)
                        return <Fragment key={i}>{renderCallout(c.level, text, ctx)}</Fragment>;
                    return (
                        <CalloutBox key={i} level={c.level}>
                            {text}
                        </CalloutBox>
                    );
                })}
            </>
        ) : null;

    const syntaxSlot = syntaxCodeNode ? (
        <>
            {renderHeading(headingLevel + 1, 'Syntax', { id: `${item.id}-syntax` })}
            <SyntaxBlock syntaxNode={syntaxCodeNode} />
        </>
    ) : null;

    const paramsSlot =
        item.params.length > 0 ? (
            <>
                {renderHeading(headingLevel + 1, 'Parameters', { id: `${item.id}-params` })}
                <ParamsPanel
                    entries={item.params.map((p, i) => ({
                        key: `${p.name}-${p.position ?? i}`,
                        param: p,
                        node: renderParam ? (
                            renderParam(p, ctx)
                        ) : (
                            <ParamProperty
                                param={p}
                                isMacro={isMacro}
                                descriptionNode={paramDescNodes[i]}
                                resolveRef={resolveRef}
                            />
                        ),
                    }))}
                />
            </>
        ) : null;

    const returnsSlot = (
        <>
            {renderHeading(headingLevel + 1, 'Returns', { id: `${item.id}-returns` })}
            {renderReturns ? (
                renderReturns(item, ctx)
            ) : (
                <div className="flex flex-col">
                    <ReturnsSection returns={item.returns} resolveRef={resolveRef} />
                </div>
            )}
        </>
    );

    const seeAlsoSlot =
        item.see_also.length > 0 ? (
            <>
                {renderHeading(headingLevel + 1, 'See Also', { id: `${item.id}-see-also` })}
                <SeeAlsoSection refs={item.see_also} resolveRef={resolveRef} />
            </>
        ) : null;

    const examplesPanelSlot = (
        <ExamplesPanelPre examples={item.examples} renderedNodes={exampleNodes} />
    );

    const slots: ItemLayoutSlots = {
        header: headerSlot,
        meta: metaSlot,
        description: descriptionSlot,
        callouts: calloutsSlot,
        syntax: syntaxSlot,
        params: paramsSlot,
        returns: returnsSlot,
        seeAlso: seeAlsoSlot,
        examplesPanel: examplesPanelSlot,
    };

    if (renderItemLayout) return <>{renderItemLayout(slots, ctx)}</>;
    return <DefaultItemLayout slots={slots} />;
}
