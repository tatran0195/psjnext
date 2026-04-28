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
    EnumValue,
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

function TypeWithRefs({ type, resolveRef }: { type: string; resolveRef: (ref: string) => string }) {
    const parts = type.split(/(\$ref:[^\]\s,)]+)/g);
    if (parts.length === 1) {
        return <span className="text-xs font-mono text-fd-muted-foreground">{type}</span>;
    }
    return (
        <span className="text-xs font-mono text-fd-muted-foreground">
            {parts.map((part, i) => {
                if (part.startsWith('$ref:')) {
                    const ref = part.slice(5);
                    return (
                        <a
                            key={i}
                            href={resolveRef(ref)}
                            className="underline hover:text-fd-accent-foreground transition-colors"
                        >
                            {ref.split('/').pop()}
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
    warn: 'border-l-amber-400 bg-amber-50/60 dark:bg-amber-900/10 text-amber-900 dark:text-amber-200',
    info: 'border-l-blue-400 bg-blue-50/60 dark:bg-blue-900/10 text-blue-900 dark:text-blue-200',
    danger: 'border-l-red-400 bg-red-50/60 dark:bg-red-900/10 text-red-900 dark:text-red-200',
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
                'not-prose flex gap-3 rounded-md border-l-4 px-4 py-3 text-sm my-3',
                CALLOUT_STYLES[level],
            )}
        >
            <span className="shrink-0 text-base leading-5 mt-0.5">{CALLOUT_ICONS[level]}</span>
            <div className="min-w-0">{children}</div>
        </div>
    );
}

// ─── InfoTag ──────────────────────────────────────────────────────────────────

function InfoTag({ label, value }: { label: string; value: string }) {
    return (
        <div className="inline-flex items-baseline gap-1.5 rounded border border-fd-border bg-fd-secondary/60 px-2 py-1 text-xs max-w-full">
            <span className="font-semibold text-fd-foreground/70 shrink-0">{label}</span>
            <code className="min-w-0 flex-1 text-fd-muted-foreground break-all font-mono">
                {value}
            </code>
        </div>
    );
}

// ─── Enum chips ───────────────────────────────────────────────────────────────
// Renders each enum value as an individual chip: `id — label`

function EnumChips({ values }: { values: EnumValue[] }) {
    return (
        <div className="not-prose mt-2">
            <p className="text-[0.65rem] font-semibold uppercase tracking-wider text-fd-muted-foreground mb-1.5">
                Allowed values
            </p>
            <div className="flex flex-wrap gap-1.5">
                {values.map((ev) => (
                    <span
                        key={String(ev.id)}
                        className="inline-flex items-center gap-1 rounded-md border border-fd-border bg-fd-secondary/50 px-2 py-0.5 font-mono text-[0.7rem] text-fd-foreground"
                        title={ev.description}
                    >
                        <span className="text-fd-primary font-bold">{ev.id}</span>
                        <span className="text-fd-muted-foreground">—</span>
                        <span className="text-fd-foreground/80">{ev.label}</span>
                    </span>
                ))}
            </div>
        </div>
    );
}

// ─── Property — Stripe-style param row ────────────────────────────────────────
// Used inside the bordered ParamsPanel container — no outer border needed,
// dividers are handled by the container's divide-y.

function Property({
    name,
    type,
    required,
    deprecated,
    removed,
    groupId,
    className,
    children,
}: {
    name: ReactNode;
    type: ReactNode;
    required?: boolean;
    deprecated?: boolean;
    removed?: boolean;
    /** Which param group this property came from */
    groupId?: string;
    className?: string;
    children?: ReactNode;
}) {
    return (
        <div className={cn('px-4 py-3 text-sm', removed && 'opacity-40', className)}>
            {/* name + type + badges row */}
            <div className="flex flex-wrap items-baseline gap-x-2 gap-y-1 not-prose">
                <span
                    className={cn(
                        'font-mono font-semibold text-[0.8rem] text-fd-foreground',
                        removed && 'line-through',
                    )}
                >
                    {name}
                    {required ? (
                        <span className="text-red-500 ms-0.5">*</span>
                    ) : (
                        <span className="text-fd-muted-foreground/50 ms-0.5 font-normal">?</span>
                    )}
                </span>

                {type && <span className="text-xs">{type}</span>}

                {groupId && (
                    <span className="text-[0.6rem] font-mono text-fd-muted-foreground/60 border border-fd-border/50 rounded px-1 py-px">
                        {groupId}
                    </span>
                )}

                {deprecated && !removed && (
                    <span className="ms-auto rounded-sm bg-amber-100 dark:bg-amber-900/30 px-1.5 py-0.5 text-[0.65rem] font-semibold uppercase tracking-wide text-amber-700 dark:text-amber-300">
                        deprecated
                    </span>
                )}
                {removed && (
                    <span className="ms-auto rounded-sm bg-red-100 dark:bg-red-900/30 px-1.5 py-0.5 text-[0.65rem] font-semibold uppercase tracking-wide text-red-700 dark:text-red-400">
                        removed
                    </span>
                )}
            </div>

            {/* description + meta */}
            <div className="prose-no-margin pt-1.5 empty:hidden text-fd-muted-foreground/90 text-sm">
                {children}
            </div>
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
            groupId={param._fromGroup}
        >
            {descriptionNode}

            {/* Inline meta tags */}
            <div className="flex flex-wrap gap-2 mt-1.5 not-prose empty:hidden">
                {param.default !== undefined && <InfoTag label="Default" value={param.default} />}
                {param.deprecated_in && (
                    <InfoTag label="Deprecated in" value={param.deprecated_in} />
                )}
                {param.removed_in && <InfoTag label="Removed in" value={param.removed_in} />}
            </div>

            {/* Enum chips */}
            {param.enum_values && param.enum_values.length > 0 && (
                <EnumChips values={param.enum_values} />
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
            <div className="rounded-lg border border-fd-border overflow-hidden">
                <Property
                    name="return"
                    type={<TypeWithRefs type={returns.type ?? 'unknown'} resolveRef={resolveRef} />}
                    required={false}
                >
                    {returns.description && (
                        <p className="text-fd-muted-foreground text-sm">{returns.description}</p>
                    )}
                </Property>
            </div>
        );
    }

    // macro_code — each code value as its own row
    if (returns.kind === 'macro_code' && returns.codes && returns.codes.length > 0) {
        return (
            <div className="rounded-lg border border-fd-border overflow-hidden divide-y divide-fd-border/60">
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

// ─── See Also ─────────────────────────────────────────────────────────────────

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

// ─── Section heading helper ────────────────────────────────────────────────────
// A subtle section divider that matches fumadocs heading style but adds a rule.

function SectionDivider() {
    return <div className="border-t border-fd-border/50 -mx-0 mb-4" />;
}

// ─── Examples panel (fumadocs-aligned, theme-aware) ───────────────────────────

function ExamplesPanel({
    examples,
    renderedNodes,
}: {
    examples: Example[];
    renderedNodes: ReactNode[];
}) {
    if (examples.length === 0) {
        return (
            <div className="rounded-xl border border-fd-border bg-fd-card/50 px-4 py-8 text-sm text-fd-muted-foreground italic text-center">
                No examples available.
            </div>
        );
    }

    if (examples.length === 1) {
        const ex = examples[0];
        return (
            <div className="rounded-xl overflow-hidden border border-fd-border bg-fd-card shadow-sm">
                {/* header bar */}
                <div className="flex items-center justify-between gap-3 border-b border-fd-border bg-fd-secondary/50 px-4 py-2.5">
                    <span className="text-xs font-medium text-fd-foreground truncate">
                        {ex.title ?? 'Example'}
                    </span>
                    {ex.language && (
                        <span className="shrink-0 rounded-full border border-fd-border bg-fd-muted px-2 py-0.5 font-mono text-[0.6rem] uppercase tracking-wider text-fd-muted-foreground">
                            {ex.language}
                        </span>
                    )}
                </div>
                {/* code block — stripped of extra margin */}
                <div className="[&_.fd-codeblock]:my-0 [&_.fd-codeblock]:rounded-none [&_.fd-codeblock]:border-0 [&_.fd-codeblock]:shadow-none">
                    {renderedNodes[0]}
                </div>
            </div>
        );
    }

    return (
        <div className="rounded-xl overflow-hidden border border-fd-border bg-fd-card shadow-sm">
            <CodeBlockTabs groupId="psjapi_examples" defaultValue="0">
                {/* tab bar */}
                <div className="border-b border-fd-border bg-fd-secondary/50 px-3 pt-2">
                    <CodeBlockTabsList className="gap-0 bg-transparent p-0">
                        {examples.map((ex, i) => (
                            <CodeBlockTabsTrigger
                                key={i}
                                value={String(i)}
                                className="rounded-t-md rounded-b-none border-0 border-b-2 border-transparent px-3 py-2 text-xs font-medium text-fd-muted-foreground transition-colors data-[state=active]:border-fd-primary data-[state=active]:bg-transparent data-[state=active]:text-fd-foreground hover:text-fd-foreground"
                            >
                                {ex.title ?? `Example ${i + 1}`}
                            </CodeBlockTabsTrigger>
                        ))}
                    </CodeBlockTabsList>
                </div>
                {examples.map((_ex, i) => (
                    <CodeBlockTab key={i} value={String(i)}>
                        <div className="[&_.fd-codeblock]:my-0 [&_.fd-codeblock]:rounded-none [&_.fd-codeblock]:border-0 [&_.fd-codeblock]:shadow-none">
                            {renderedNodes[i]}
                        </div>
                    </CodeBlockTab>
                ))}
            </CodeBlockTabs>
        </div>
    );
}

// ─── Default two-column layout — Stripe-style ─────────────────────────────────

function DefaultItemLayout({ slots }: { slots: ItemLayoutSlots }) {
    return (
        <div className="flex flex-col gap-x-8 gap-y-6 xl:flex-row xl:items-start">
            {/* ── LEFT: documentation content ── */}
            <div className="min-w-0 flex-1 flex flex-col gap-5">
                {/* header + meta */}
                <div className="flex flex-col gap-2">
                    {slots.header}
                    {slots.meta}
                </div>

                {slots.description && (
                    <div className="text-fd-muted-foreground leading-relaxed">
                        {slots.description}
                    </div>
                )}

                {slots.callouts}

                {slots.syntax && (
                    <section>
                        <SectionDivider />
                        {slots.syntax}
                    </section>
                )}

                {slots.params && (
                    <section>
                        <SectionDivider />
                        {slots.params}
                    </section>
                )}

                {slots.returns && (
                    <section>
                        <SectionDivider />
                        {slots.returns}
                    </section>
                )}

                {slots.seeAlso && (
                    <section>
                        <SectionDivider />
                        {slots.seeAlso}
                    </section>
                )}
            </div>

            {/* ── RIGHT: sticky examples panel ── */}
            <div className="xl:sticky xl:top-[calc(var(--fd-docs-row-1,2rem)+4rem)] xl:w-[420px] xl:shrink-0">
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

    function resolveRef(ref: string): string {
        if (resolveRefOption) return resolveRefOption(ref);
        const normalized = ref
            .toLowerCase()
            .replace(/[^a-z0-9/]+/g, '-')
            .replace(/^-|-$/g, '');
        return `/docs/${normalized}`;
    }

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

    // ── Build all async content in parallel ───────────────────────────────────

    const [descriptionNode, syntaxCodeNode, ...calloutNodes] = await Promise.all([
        item.description ? renderMarkdown(item.description) : Promise.resolve(null),
        item.syntax ? renderCodeBlock(psjLanguage, item.syntax) : Promise.resolve(null),
        ...item.callouts.map((c) => renderMarkdown(c.text)),
    ]);

    const paramDescNodes = await Promise.all(
        item.params.map((p) =>
            p.description ? renderMarkdown(p.description) : Promise.resolve(null),
        ),
    );

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
                <ReturnsSection returns={item.returns} resolveRef={resolveRef} />
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
        <ExamplesPanel examples={item.examples} renderedNodes={exampleNodes} />
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
