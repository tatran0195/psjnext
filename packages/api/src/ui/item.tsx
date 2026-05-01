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

function EnumChips({ values }: { values: EnumValue[] }) {
    return (
        <div className="not-prose mt-2.5">
            <p className="text-[0.65rem] font-semibold uppercase tracking-wider text-fd-muted-foreground mb-1.5">
                Allowed values
            </p>
            <div className="flex flex-wrap gap-1.5">
                {values.map((ev) => (
                    <span
                        key={String(ev.id)}
                        className="inline-flex items-center gap-1.5 rounded-md border border-fd-border bg-fd-secondary/50 px-2 py-0.5 font-mono text-[0.75rem] text-fd-foreground"
                        title={ev.description}
                    >
                        <span className="text-fd-primary font-bold">{ev.id}</span>
                        <span className="text-fd-muted-foreground/50">—</span>
                        <span className="text-fd-foreground/80">{ev.label}</span>
                    </span>
                ))}
            </div>
        </div>
    );
}

// ─── Property — Stripe-style param row ────────────────────────────────────────

function Property({
    name,
    type,
    required,
    deprecated,
    removed,
    className,
    children,
}: {
    name: ReactNode;
    type: ReactNode;
    required?: boolean;
    deprecated?: boolean;
    removed?: boolean;
    className?: string;
    children?: ReactNode;
}) {
    return (
        <div className={cn('px-4 py-3.5 text-sm', removed && 'opacity-40', className)}>
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
        >
            {descriptionNode}

            {/* Inline meta tags */}
            <div className="flex flex-wrap gap-2 mt-2 not-prose empty:hidden">
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
            <div className="rounded-lg border border-fd-border bg-fd-card overflow-hidden">
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
            <div className="rounded-lg border border-fd-border bg-fd-card overflow-hidden divide-y divide-fd-border/50">
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
        <div className="not-prose grid grid-cols-1 sm:grid-cols-2 gap-3">
            {refs.map((ref) => {
                const href = resolveRef(ref.$ref);
                const label = ref.label ?? ref.$ref.split('/').pop() ?? ref.$ref;
                const domain = ref.$ref.split('/')[0];
                return (
                    <a
                        key={ref.$ref}
                        href={href}
                        className="group flex flex-col gap-1 rounded-lg border border-fd-border bg-fd-card p-4 hover:bg-fd-muted hover:border-fd-primary/50 transition-colors"
                    >
                        <span className="text-xs font-mono text-fd-muted-foreground">{domain}</span>
                        <span className="text-sm font-semibold text-fd-foreground group-hover:text-fd-primary transition-colors flex items-center gap-1.5">
                            {label}
                            <svg
                                className="size-3.5 opacity-0 group-hover:opacity-100 transition-opacity translate-x-[-4px] group-hover:translate-x-0 transition-transform"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                                strokeWidth={2}
                            >
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    d="M9 5l7 7-7 7"
                                />
                            </svg>
                        </span>
                    </a>
                );
            })}
        </div>
    );
}

// ─── Syntax block ─────────────────────────────────────────────────────────────

function SyntaxBlock({ syntaxNode }: { syntaxNode: ReactNode }) {
    return <div className="prose-no-margin mb-6">{syntaxNode}</div>;
}

// ─── Item meta (domain badge + ribbon + namespace + links) ────────────────────

function ItemMeta({
    item,
    showDomainBadge,
    showRibbon,
    resolveRef,
}: {
    item: ResolvedItem;
    showDomainBadge: boolean;
    showRibbon: boolean;
    resolveRef: (ref: string) => string;
}) {
    return (
        <div className="not-prose flex flex-col gap-3">
            {/* Badges Row */}
            <div className="flex flex-wrap items-center gap-2">
                {showDomainBadge && <DomainBadge domain={item.domain} />}

                {item.namespace && (
                    <code className="text-fd-muted-foreground text-xs font-semibold bg-fd-muted rounded-md px-2 py-0.5 border border-fd-border">
                        {item.namespace}
                    </code>
                )}

                {showRibbon && item.ribbon && (
                    <span className="rounded-full border border-fd-border bg-fd-secondary px-2.5 py-0.5 text-[0.65rem] uppercase tracking-wider font-semibold text-fd-muted-foreground">
                        {item.ribbon}
                    </span>
                )}

                {item.version_introduced && (
                    <span className="text-fd-muted-foreground text-xs ml-1">
                        Added in <code>{item.version_introduced}</code>
                    </span>
                )}

                {item.deprecated && (
                    <span className="rounded-full border border-red-400/50 bg-red-50/50 dark:bg-red-900/10 px-2.5 py-0.5 text-[0.65rem] uppercase tracking-wider font-semibold text-red-700 dark:text-red-300">
                        Deprecated
                    </span>
                )}
            </div>

            {/* Reference Links Row (Macro <-> Command) */}
            {(item.macro_link || item.command_link) && (
                <div className="flex flex-wrap items-center gap-2 text-xs border border-fd-border bg-fd-card rounded-md px-3 py-2 mt-1 shadow-sm w-fit">
                    {item.macro_link && (
                        <>
                            <span className="text-fd-muted-foreground">Wraps macro:</span>
                            <a
                                href={resolveRef(`macro/${item.macro_link}`)}
                                className="font-mono text-fd-primary hover:underline hover:text-fd-accent-foreground transition-colors"
                            >
                                {item.macro_link}
                            </a>
                        </>
                    )}
                    {item.command_link && (
                        <>
                            <span className="text-fd-muted-foreground">Wrapped by command:</span>
                            <a
                                href={resolveRef(`psj-command/${item.command_link}`)}
                                className="font-mono text-fd-primary hover:underline hover:text-fd-accent-foreground transition-colors"
                            >
                                {item.command_link}
                            </a>
                        </>
                    )}
                </div>
            )}
        </div>
    );
}

// ─── Section heading helper ────────────────────────────────────────────────────

function SectionDivider() {
    return <div className="border-t border-fd-border/60 -mx-0 mb-5" />;
}

// ─── Examples panel (fumadocs-aligned, native codeblocks) ─────────────────────

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
                <div className="flex items-center justify-between gap-3 border-b border-fd-border bg-fd-secondary/30 px-4 py-2.5">
                    <span className="text-xs font-semibold text-fd-foreground truncate">
                        {ex.title ?? 'Example'}
                    </span>
                </div>
                <div className="p-1">
                    {/* Native Fumadocs CodeBlock rendering handles the copy button and rounded corners naturally here! */}
                    {renderedNodes[0]}
                </div>
            </div>
        );
    }

    return (
        <CodeBlockTabs groupId="@psj/api_examples" defaultValue="0">
            <CodeBlockTabsList className="w-full">
                {examples.map((ex, i) => (
                    <CodeBlockTabsTrigger key={i} value={String(i)}>
                        {ex.title ?? `Example ${i + 1}`}
                    </CodeBlockTabsTrigger>
                ))}

                <div className="sticky right-0 z-10 ml-auto flex shrink-0 items-center bg-gradient-to-l from-fd-card via-fd-card/90 to-transparent pl-0 pr-0 py-1.5 self-stretch">
                    <button className="flex items-center gap-1.5 rounded-full bg-fd-primary px-3 py-1.5 text-[11px] font-medium text-fd-primary-foreground shadow-lg transition-all hover:bg-fd-primary/90 active:scale-95 cursor-pointer">
                        <svg className="size-3" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z" />
                        </svg>
                        Try it
                    </button>
                </div>
            </CodeBlockTabsList>
            {examples.map((_ex, i) => (
                <CodeBlockTab key={i} value={String(i)}>
                    {renderedNodes[i]}
                </CodeBlockTab>
            ))}
        </CodeBlockTabs>
    );
}

// ─── Default two-column layout — Stripe-style ─────────────────────────────────

function DefaultItemLayout({ slots }: { slots: ItemLayoutSlots }) {
    return (
        <div className="container mx-auto flex flex-col gap-x-8 gap-y-6 lg:flex-row lg:items-start py-12">
            {/* ── LEFT: documentation content ── */}
            <div className="min-w-0 flex-1 flex flex-col gap-6">
                {/* Header Sequence */}
                <div className="flex flex-col gap-4">
                    {slots.header}
                    {slots.meta}
                </div>

                {/* Pull Syntax up prominently under header! */}
                {slots.syntax && <section className="mb-2">{slots.syntax}</section>}

                {slots.description && (
                    <div className="text-fd-foreground/90 leading-relaxed text-sm lg:text-base">
                        {slots.description}
                    </div>
                )}

                {slots.callouts}

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
            <div className="lg:sticky lg:top-[calc(var(--fd-docs-row-1,2rem)+3rem)] lg:w-[420px] xl:w-[480px] lg:shrink-0 pt-2 lg:pt-0">
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
            <CodeBlock>
                <Pre>{code}</Pre>
            </CodeBlock>
        );
    }

    async function renderMarkdown(md: string): Promise<ReactNode> {
        if (options.renderMarkdown) return await options.renderMarkdown(md);
        return <div className="text-sm text-fd-muted-foreground">{md}</div>;
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

    function generateSyntax(item: ResolvedItem): string {
        if (item.syntax) return item.syntax.trim();

        const title = item.title.replace('()', '');

        if (item.domain === 'macro') {
            const args = [`"${title}"`];
            item.params.forEach((p) => {
                args.push(p.required ? `<${p.name}>` : `[${p.name}]`);
            });
            return `JPT.Exec(${args.join(', ')})`;
        }

        if (item.domain === 'psj-command') {
            const args = item.params.map((p) => `${p.name}=<value>`);
            return `${title}(${args.join(', ')})`;
        }

        return `${title}(...)`;
    }

    const autoSyntax = generateSyntax(item);

    // ── Build all async content in parallel ───────────────────────────────────

    const [descriptionNode, syntaxCodeNode, ...calloutNodes] = await Promise.all([
        item.description ? renderMarkdown(item.description) : Promise.resolve(null),
        autoSyntax ? renderCodeBlock(psjLanguage, autoSyntax) : Promise.resolve(null),
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
        <ItemMeta
            item={item}
            showDomainBadge={showDomainBadge}
            showRibbon={showRibbon}
            resolveRef={resolveRef}
        />
    );

    const descriptionSlot = descriptionNode ? (
        <div className="prose-no-margin">{descriptionNode}</div>
    ) : null;

    const calloutsSlot =
        item.callouts.length > 0 ? (
            <div className="flex flex-col gap-2">
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
            </div>
        ) : null;

    // Syntax is now elevated!
    const syntaxSlot = syntaxCodeNode ? <SyntaxBlock syntaxNode={syntaxCodeNode} /> : null;

    const paramsSlot =
        item.params.length > 0 ? (
            <div className="flex flex-col gap-4">
                {renderHeading(headingLevel + 1, 'Parameters', {
                    id: `${item.id}-params`,
                    className: 'mb-0',
                })}
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
            </div>
        ) : null;

    const returnsSlot = (
        <div className="flex flex-col gap-4">
            {renderHeading(headingLevel + 1, 'Returns', {
                id: `${item.id}-returns`,
                className: 'mb-0',
            })}
            {renderReturns ? (
                renderReturns(item, ctx)
            ) : (
                <ReturnsSection returns={item.returns} resolveRef={resolveRef} />
            )}
        </div>
    );

    const seeAlsoSlot =
        item.see_also.length > 0 ? (
            <div className="flex flex-col gap-4">
                {renderHeading(headingLevel + 1, 'See Also', {
                    id: `${item.id}-see-also`,
                    className: 'mb-0',
                })}
                <SeeAlsoSection refs={item.see_also} resolveRef={resolveRef} />
            </div>
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
