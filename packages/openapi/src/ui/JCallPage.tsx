/**
 * JCallPage — server component that renders a fully-resolved JCALL item.
 *
 * Props:
 *   item  — a ResolvedItem (pass directly when using source API)
 *
 * Sections rendered:
 *   1. Header (title, domain badge, version)
 *   2. Description (markdown)
 *   3. Callouts
 *   4. Syntax block
 *   5. Parameters table (positional or named)
 *   6. Returns
 *   7. Examples
 *   8. See Also
 */
import * as fa from 'fumadocs-ui/components/accordion';
import { getSingletonHighlighter } from 'shiki';
import type { EnumValue, ResolvedItem, ResolvedParam } from '../types';

let highlighter: any;
async function getCachedHighlighter() {
    if (!highlighter) {
        highlighter = await getSingletonHighlighter({
            themes: ['github-light', 'github-dark'],
            langs: ['python', 'typescript', 'javascript', 'json', 'yaml', 'csharp', 'vb', 'text'],
        });
    }
    return highlighter;
}

interface JCallPageProps {
    item: ResolvedItem;
}

export function JCallPage({ item }: JCallPageProps) {
    return (
        <div className="flex flex-col lg:flex-row lg:items-start gap-12 jcall-page">
            <div className="flex-1 min-w-0 space-y-8">
                <Header item={item} />
                {item.description && <Description text={item.description} />}
                {item.callouts?.map((c, i) => <Callout key={i} level={c.level} text={c.text} />)}

                {item.params.length > 0 && (
                    <ParamsSection params={item.params} paramStyle={item.param_style} />
                )}
                <ReturnsSection returns={item.returns} />
                {item.see_also && item.see_also.length > 0 && (
                    <SeeAlsoSection refs={item.see_also} />
                )}
            </div>

            <div className="w-full lg:w-[400px] xl:w-[450px] shrink-0 lg:sticky lg:top-24 space-y-6">
                {item.syntax && <SyntaxBlock syntax={item.syntax} />}
                {item.examples && item.examples.length > 0 && (
                    <ExamplesSection examples={item.examples} />
                )}
            </div>
        </div>
    );
}

function Header({ item }: { item: ResolvedItem }) {
    const domainColors: Record<string, string> = {
        macro: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400',
        'psj-command': 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400',
        'psj-utility': 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-400',
        'psj-gui': 'bg-orange-100 text-orange-700 dark:bg-orange-900/30 dark:text-orange-400',
    };
    const colorClass = domainColors[item.domain] || 'bg-fd-muted text-fd-foreground';
    const domainShort: Record<string, string> = {
        macro: 'MCR',
        'psj-command': 'CMD',
        'psj-utility': 'UTL',
        'psj-gui': 'GUI',
    };
    const shortName = domainShort[item.domain] || item.domain;

    return (
        <div className="flex flex-col gap-4 mb-6">
            <div className="flex items-center gap-3">
                <span className={`rounded-lg px-2 text-sm font-bold tracking-wider ${colorClass}`}>
                    {shortName}
                </span>
                <h1 className="text-3xl font-bold tracking-tight text-fd-foreground">
                    {item.title}
                </h1>
            </div>

            <div className="flex flex-wrap items-center gap-2 text-sm text-fd-muted-foreground">
                {item.deprecated && (
                    <span className="rounded bg-yellow-100 px-2 py-0.5 text-xs font-medium text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400">
                        Deprecated
                    </span>
                )}
                <span>Since {item.version_introduced}</span>
                {item.ribbon && (
                    <span className="flex items-center gap-1 before:content-['•'] before:mx-2">
                        Ribbon: {item.ribbon}
                    </span>
                )}
            </div>
        </div>
    );
}

function Description({ text }: { text: string }) {
    return (
        <p className="text-fd-foreground leading-relaxed whitespace-pre-wrap">
            {text}
        </p>
    );
}

const calloutStyles = {
    warn: 'border-yellow-400 bg-yellow-50 text-yellow-900 dark:bg-yellow-900/20 dark:text-yellow-300',
    info: 'border-blue-400 bg-blue-50 text-blue-900 dark:bg-blue-900/20 dark:text-blue-300',
    danger: 'border-red-400 bg-red-50 text-red-900 dark:bg-red-900/20 dark:text-red-300',
} as const;

function Callout({ level, text }: { level: 'warn' | 'info' | 'danger'; text: string }) {
    return (
        <div className={`rounded-lg border-l-4 px-4 py-3 text-sm ${calloutStyles[level]}`}>
            {text}
        </div>
    );
}

async function SyntaxBlock({ syntax }: { syntax: string }) {
    const hl = await getCachedHighlighter();
    const html = hl.codeToHtml(syntax, {
        lang: 'typescript',
        themes: { light: 'github-light', dark: 'github-dark' }
    });

    return (
        <div className="space-y-2">
            <h3 className="text-sm font-semibold uppercase tracking-wide text-fd-muted-foreground">
                Syntax
            </h3>
            <div
                className="overflow-x-auto rounded-lg border border-fd-border bg-fd-muted p-4 font-mono text-xs max-h-[400px] [&_pre]:!bg-transparent [&_pre]:!m-0 [&_pre]:!p-0"
                dangerouslySetInnerHTML={{ __html: html }}
            />
        </div>
    );
}

function ParamsSection({
    params,
    paramStyle,
}: {
    params: ResolvedParam[];
    paramStyle: 'positional' | 'named';
}) {
    return (
        <div className="space-y-4">
            <h3 className="text-lg font-semibold tracking-tight text-fd-foreground border-b border-fd-border pb-2">
                Parameters
            </h3>
            <fa.Accordions type="multiple">
                {params.map((param, i) => (
                    <ParamAccordion key={param.name ?? i} param={param} paramStyle={paramStyle} index={i} />
                ))}
            </fa.Accordions>
        </div>
    );
}

function ParamAccordion({ param, paramStyle, index }: { param: ResolvedParam; paramStyle: 'positional' | 'named', index: number }) {
    const displayName = param.display_name ?? param.name ?? '—';
    const id = param.name ?? String(index);
    const title = (
        <div className="flex flex-row items-center gap-3 w-full pr-4 text-sm">
            {paramStyle === 'positional' && (
                <span className="font-mono text-xs text-fd-muted-foreground w-4 opacity-50">{param.position}</span>
            )}
            <span className="font-mono text-fd-foreground font-semibold">{displayName}</span>
            {param.required ? (
                <span className="text-red-600 dark:text-red-400 text-xs font-medium border border-red-600/30 px-1 rounded bg-red-500/10">required</span>
            ) : null}
            <span className="font-mono text-xs text-fd-muted-foreground ml-auto truncate opacity-70">
                {param.type}
            </span>
        </div>
    );

    return (
        <fa.Accordion title={title} id={id} value={id}>
            <div className="flex flex-col gap-3 pt-2 pb-4 text-sm">
                <p className="text-fd-muted-foreground">{param.description}</p>
                {param.default != null && (
                    <p className="text-fd-muted-foreground">
                        Default: <code className="font-mono text-fd-primary bg-fd-muted px-1.5 py-0.5 rounded">{param.default}</code>
                    </p>
                )}
                {param.deprecated && (
                    <p className="text-yellow-600 dark:text-yellow-400 font-medium">Deprecated</p>
                )}
                {param.enum_values && param.enum_values.length > 0 && (
                    <div className="mt-2 border border-fd-border rounded-lg overflow-hidden">
                        <div className="bg-fd-muted px-3 py-1.5 text-xs font-medium text-fd-muted-foreground border-b border-fd-border">
                            Enum Values
                        </div>
                        <EnumTable values={param.enum_values} />
                    </div>
                )}
            </div>
        </fa.Accordion>
    );
}

function EnumTable({ values }: { values: EnumValue[] }) {
    return (
        <table className="w-full text-xs">
            <tbody className="divide-y divide-fd-border">
                {values.map((v) => (
                    <tr key={String(v.id)} className="align-top">
                        <td className="px-3 py-2 font-mono w-1/4">{v.id}</td>
                        <td className="px-3 py-2 font-medium">{v.label}</td>
                        {values.some((v) => v.description) && (
                            <td className="px-3 py-2 text-fd-muted-foreground">{v.description}</td>
                        )}
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

function ReturnsSection({ returns }: { returns: ResolvedItem['returns'] }) {
    return (
        <div className="space-y-4">
            <h3 className="text-lg font-semibold tracking-tight text-fd-foreground border-b border-fd-border pb-2">
                Responses
            </h3>
            {returns.kind === 'void' && (
                <div className="rounded-lg border border-fd-border bg-fd-card px-4 py-3 text-sm flex items-center gap-3">
                    <span className="font-mono text-fd-muted-foreground font-semibold">void</span>
                    {returns.description && <span className="text-fd-muted-foreground opacity-80">— {returns.description}</span>}
                </div>
            )}
            {returns.kind === 'typed' && (
                <div className="rounded-lg border border-fd-border bg-fd-card px-4 py-3 text-sm flex items-center gap-3">
                    <span className="font-mono text-fd-primary font-semibold">{returns.type}</span>
                    {returns.description && (
                        <span className="text-fd-muted-foreground opacity-80">— {returns.description}</span>
                    )}
                </div>
            )}
            {returns.kind === 'macro_code' && (
                <div className="overflow-x-auto rounded-lg border border-fd-border bg-fd-card">
                    <table className="w-full text-sm">
                        <thead>
                            <tr className="border-b border-fd-border bg-fd-muted text-left">
                                <th className="px-3 py-2 font-medium text-fd-muted-foreground">Code</th>
                                <th className="px-3 py-2 font-medium text-fd-muted-foreground">Meaning</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-fd-border">
                            {returns.codes.map((c) => (
                                <tr key={c.value} className="align-top">
                                    <td className="px-3 py-2 font-mono text-xs text-fd-primary">{c.value}</td>
                                    <td className="px-3 py-2 text-xs text-fd-muted-foreground">{c.meaning}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}

async function ExamplesSection({ examples }: { examples: NonNullable<ResolvedItem['examples']> }) {
    const hl = await getCachedHighlighter();
    return (
        <div className="space-y-4">
            <h3 className="text-sm font-semibold uppercase tracking-wide text-fd-muted-foreground">
                Examples
            </h3>
            <div className="space-y-4">
                {await Promise.all(examples.map(async (ex, i) => {
                    const mappedLang = ['python', 'typescript', 'javascript', 'json', 'yaml', 'csharp', 'vb'].includes(ex.language) ? ex.language : (ex.language === 'psj' ? 'typescript' : 'text');
                    const html = hl.codeToHtml(ex.code || '', {
                        lang: mappedLang,
                        themes: { light: 'github-light', dark: 'github-dark' }
                    });

                    return (
                        <div key={i} className="flex flex-col rounded-lg border border-fd-border overflow-hidden">
                            <div className="flex items-center justify-between bg-fd-muted px-4 py-2 border-b border-fd-border">
                                {ex.title ? (
                                    <span className="text-xs font-medium text-fd-foreground">{ex.title}</span>
                                ) : <div></div>}
                                <span className="font-mono text-[10px] text-fd-muted-foreground uppercase opacity-80 tracking-wider">
                                    {ex.language}
                                </span>
                            </div>
                            <div
                                className="overflow-x-auto bg-fd-background p-4 font-mono text-xs max-h-[300px] [&_pre]:!bg-transparent [&_pre]:!m-0 [&_pre]:!p-0"
                                dangerouslySetInnerHTML={{ __html: html }}
                            />
                        </div>
                    );
                }))}
            </div>
        </div>
    );
}

function SeeAlsoSection({ refs }: { refs: NonNullable<ResolvedItem['see_also']> }) {
    return (
        <div className="space-y-4 pt-4">
            <h3 className="text-lg font-semibold tracking-tight text-fd-foreground border-b border-fd-border pb-2">
                See Also
            </h3>
            <ul className="flex flex-col gap-2 text-sm">
                {refs.map((r, i) => (
                    <li key={i} className="flex items-center before:content-['↪'] before:text-fd-muted-foreground before:mr-2">
                        <span className="font-mono text-fd-primary hover:underline cursor-pointer">{r.label ?? r.$ref}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
}
