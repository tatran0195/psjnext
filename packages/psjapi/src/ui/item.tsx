/**
 * psjapi — PSJAPIItem React component (React Server Component)
 *
 * Renders a single resolved SDK item.
 *
 * KEY DIFFERENCE FROM OPENAPI:
 *   In fumadocs-openapi, the right panel shows an API playground / curl
 *   generator.  In psjapi, the right panel shows the item's EXAMPLE CODES —
 *   there is no network call to make.  The left column holds description,
 *   params, and returns; examples are placed in the right column.
 *
 * This is a React Server Component — async render functions (Shiki, remark)
 * are awaited here. Interactive sub-components (CodeBlockTabs etc.) are
 * already client components supplied by fumadocs-ui.
 */

import {
  type ReactNode,
  type HTMLAttributes,
  Fragment,
} from 'react';
import {
  CodeBlock,
  Pre,
  CodeBlockTab,
  CodeBlockTabs,
  CodeBlockTabsList,
  CodeBlockTabsTrigger,
} from 'fumadocs-ui/components/codeblock';
import { Heading } from 'fumadocs-ui/components/heading';
import { cn } from '../utils/cn';
import type {
  CalloutLevel,
  Domain,
  Example,
  ResolvedItem,
  ResolvedParam,
  Returns,
  SeeAlsoRef,
  EnumValue,
} from '../types';
import type { ResolvedPSJAPIPageOptions, ItemLayoutSlots, PsjRenderContext } from './context';

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

function CalloutBox({
  level,
  children,
}: {
  level: CalloutLevel;
  children: ReactNode;
}) {
  return (
    <div
      className={cn(
        'not-prose flex gap-3 rounded-lg border p-4 text-sm my-4',
        CALLOUT_STYLES[level],
      )}
    >
      <span className="shrink-0 text-base leading-5">{CALLOUT_ICONS[level]}</span>
      <div>{children}</div>
    </div>
  );
}

// ─── Params table ─────────────────────────────────────────────────────────────

function TypeChip({ type }: { type: string }) {
  return (
    <code className="rounded bg-fd-muted px-1.5 py-0.5 text-xs text-fd-muted-foreground font-mono">
      {type}
    </code>
  );
}

function EnumValues({ values }: { values: EnumValue[] }) {
  return (
    <div className="mt-1 flex flex-wrap gap-1">
      {values.map((ev) => (
        <span
          key={String(ev.id)}
          className="inline-flex items-center gap-1 rounded border border-fd-border bg-fd-muted/50 px-1.5 py-0.5 text-xs font-mono"
        >
          <span className="text-fd-muted-foreground">{ev.id}</span>
          <span>—</span>
          <span>{ev.label}</span>
        </span>
      ))}
    </div>
  );
}

function ParamRow({
  param,
  isMacro,
}: {
  param: ResolvedParam;
  isMacro: boolean;
}) {
  return (
    <div className="grid gap-x-4 border-b border-fd-border py-3 last:border-0 text-sm"
      style={{ gridTemplateColumns: isMacro ? '2.5rem 1fr auto' : '1fr auto' }}
    >
      {isMacro && (
        <div className="text-fd-muted-foreground text-xs font-mono pt-0.5">
          {param.position}
        </div>
      )}
      <div className="min-w-0">
        <div className="flex items-baseline gap-2 flex-wrap">
          <code className="font-semibold text-sm text-fd-foreground">
            {param.display_name ?? param.name}
          </code>
          {param.required && (
            <span className="text-xs text-red-500 font-medium">required</span>
          )}
          {param.deprecated && (
            <span className="text-xs text-fd-muted-foreground line-through">deprecated</span>
          )}
        </div>
        <p className="mt-0.5 text-fd-muted-foreground text-xs leading-relaxed">
          {param.description}
        </p>
        {param.default !== undefined && (
          <p className="mt-0.5 text-xs text-fd-muted-foreground">
            Default: <code className="text-fd-foreground">{param.default}</code>
          </p>
        )}
        {param.enum_values && param.enum_values.length > 0 && (
          <EnumValues values={param.enum_values} />
        )}
      </div>
      <div className="shrink-0">
        <TypeChip type={param.type} />
      </div>
    </div>
  );
}

function ParamsSection({
  params,
  isMacro,
}: {
  params: ResolvedParam[];
  isMacro: boolean;
}) {
  if (params.length === 0) return null;

  return (
    <div className="not-prose">
      {isMacro && (
        <div
          className="grid gap-x-4 border-b border-fd-border pb-1.5 mb-1 text-xs font-medium text-fd-muted-foreground"
          style={{ gridTemplateColumns: '2.5rem 1fr auto' }}
        >
          <div>Pos</div>
          <div>Parameter</div>
          <div>Type</div>
        </div>
      )}
      {params.map((p) => (
        <ParamRow key={`${p.name}-${p.position}`} param={p} isMacro={isMacro} />
      ))}
    </div>
  );
}

// ─── Returns section ──────────────────────────────────────────────────────────

function ReturnsSection({ returns }: { returns: Returns }) {
  if (returns.kind === 'void') {
    return (
      <p className="text-sm text-fd-muted-foreground italic">No return value.</p>
    );
  }

  if (returns.kind === 'typed') {
    return (
      <div className="not-prose text-sm">
        <div className="flex items-center gap-2">
          <TypeChip type={returns.type ?? 'unknown'} />
          {returns.description && (
            <span className="text-fd-muted-foreground">{returns.description}</span>
          )}
        </div>
      </div>
    );
  }

  // macro_code
  if (returns.kind === 'macro_code' && returns.codes && returns.codes.length > 0) {
    return (
      <div className="not-prose text-sm space-y-1">
        {returns.codes.map((code) => (
          <div key={code.value} className="flex items-start gap-3">
            <code className="shrink-0 rounded border border-fd-border bg-fd-muted px-1.5 py-0.5 text-xs font-mono">
              {code.value}
            </code>
            <span className="text-fd-muted-foreground">{code.meaning}</span>
          </div>
        ))}
      </div>
    );
  }

  return null;
}

// ─── Right panel — examples (pre-rendered) ───────────────────────────────────
//
// ExamplesPanelPre receives code blocks that have already been rendered
// server-side (Shiki-highlighted ReactNodes).  This avoids calling async
// functions inside a synchronous render.

function ExamplesPanelPre({
  examples,
  renderedNodes,
}: {
  examples: Example[];
  renderedNodes: ReactNode[];
}) {
  if (examples.length === 0) {
    return (
      <div className="rounded-xl border border-fd-border bg-fd-card p-6 text-sm text-fd-muted-foreground italic">
        No examples available.
      </div>
    );
  }

  if (examples.length === 1) {
    const ex = examples[0];
    return (
      <div className="rounded-xl border border-fd-border bg-fd-card overflow-hidden">
        {ex.title && (
          <p className="border-b border-fd-border px-4 py-2 text-xs font-medium text-fd-muted-foreground">
            {ex.title}
          </p>
        )}
        <div className="prose-no-margin p-0">{renderedNodes[0]}</div>
      </div>
    );
  }

  return (
    <CodeBlockTabs groupId="psjapi_examples" defaultValue="0">
      <CodeBlockTabsList>
        {examples.map((ex, i) => (
          <CodeBlockTabsTrigger key={i} value={String(i)}>
            {ex.title ?? `Example ${i + 1}`}
          </CodeBlockTabsTrigger>
        ))}
      </CodeBlockTabsList>
      {examples.map((ex, i) => (
        <CodeBlockTab key={i} value={String(i)}>
          <div className="prose-no-margin">
            {renderedNodes[i]}
          </div>
        </CodeBlockTab>
      ))}
    </CodeBlockTabs>
  );
}

// ─── Meta block (namespace / ribbon / macro link) ─────────────────────────────

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
    <div className="not-prose flex flex-wrap items-center gap-2 text-sm">
      {showDomainBadge && <DomainBadge domain={item.domain} />}
      {item.namespace && (
        <code className="text-fd-muted-foreground text-xs">
          namespace: {item.namespace}
        </code>
      )}
      {showRibbon && item.ribbon && (
        <span className="text-fd-muted-foreground text-xs">
          Ribbon: <span className="text-fd-foreground">{item.ribbon}</span>
        </span>
      )}
      {item.deprecated && (
        <span className="rounded-full border border-red-400/50 bg-red-50/50 px-2 py-0.5 text-xs text-red-700 dark:text-red-300">
          Deprecated
        </span>
      )}
    </div>
  );
}

// ─── See also ─────────────────────────────────────────────────────────────────

function SeeAlso({ refs }: { refs: SeeAlsoRef[] }) {
  if (refs.length === 0) return null;
  return (
    <div className="not-prose">
      <ul className="flex flex-col gap-1">
        {refs.map((ref) => (
          <li key={ref.$ref}>
            <a
              href={`#${ref.$ref.replace('/', '-')}`}
              className="text-sm text-fd-primary hover:underline"
            >
              {ref.label ?? ref.$ref}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

// ─── Default two-column layout ────────────────────────────────────────────────

function DefaultItemLayout({ slots }: { slots: ItemLayoutSlots }) {
  return (
    <div className="grid @container grid-cols-1 @3xl:grid-cols-[1fr_min(40%,28rem)] gap-8 items-start text-sm">
      {/* LEFT: content */}
      <div className="flex flex-col gap-6 min-w-0">
        {slots.header}
        {slots.meta}
        {slots.description}
        {slots.callouts}
        {slots.syntax}
        {slots.params}
        {slots.returns}
        {slots.seeAlso}
      </div>
      {/* RIGHT: examples */}
      <div className="flex flex-col gap-4 @3xl:sticky @3xl:top-20">
        {slots.examplesPanel}
      </div>
    </div>
  );
}

// ─── PSJAPIItemRenderer — main renderer ──────────────────────────────────────

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
  } = options;

  const isMacro = item.domain === 'macro';

  // renderCodeBlock wrapper — async-safe, awaited in RSC context
  async function renderCodeBlock(lang: string, code: string): Promise<ReactNode> {
    if (options.renderCodeBlock) {
      return await options.renderCodeBlock({ lang, code });
    }
    return (
      <CodeBlock className="my-0">
        <Pre>{code}</Pre>
      </CodeBlock>
    );
  }

  // renderMarkdown wrapper — async-safe
  async function renderMarkdown(md: string): Promise<ReactNode> {
    if (options.renderMarkdown) {
      return await options.renderMarkdown(md);
    }
    return <p className="text-sm text-fd-muted-foreground">{md}</p>;
  }

  function renderHeading(depth: number, text: string | ReactNode, props?: HTMLAttributes<HTMLHeadingElement> & { id?: string }) {
    if (options.renderHeading) return options.renderHeading({ children: text, ...props }, depth);
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

  // ── Build slots (async — this is an RSC) ────────────────────────────────

  const headerSlot = renderHeading(headingLevel, item.title);

  const metaSlot = (
    <ItemMeta item={item} showDomainBadge={showDomainBadge} showRibbon={showRibbon} />
  );

  const descriptionSlot = item.description ? await renderMarkdown(item.description) : null;

  // Callouts — await each text render in parallel
  const calloutTexts = await Promise.all(
    item.callouts.map((c) => renderMarkdown(c.text)),
  );
  const calloutsSlot =
    item.callouts.length > 0 ? (
      <>
        {item.callouts.map((c, i) => {
          const text = calloutTexts[i];
          if (renderCallout) return <Fragment key={i}>{renderCallout(c.level, text, ctx)}</Fragment>;
          return (
            <CalloutBox key={i} level={c.level}>
              {text}
            </CalloutBox>
          );
        })}
      </>
    ) : null;

  const syntaxCodeNode = item.syntax ? await renderCodeBlock(psjLanguage, item.syntax) : null;
  const syntaxSlot = item.syntax ? (
    <>
      {renderHeading(headingLevel + 1, 'Syntax', { id: `${item.id}-syntax` })}
      <div className="prose-no-margin">{syntaxCodeNode}</div>
    </>
  ) : null;

  const paramsSlot =
    item.params.length > 0 ? (
      <>
        {renderHeading(headingLevel + 1, 'Parameters', { id: `${item.id}-params` })}
        {renderParam ? (
          item.params.map((p, i) => <Fragment key={i}>{renderParam(p, ctx)}</Fragment>)
        ) : (
          <ParamsSection params={item.params} isMacro={isMacro} />
        )}
      </>
    ) : null;

  const returnsSlot = (
    <>
      {renderHeading(headingLevel + 1, 'Returns', { id: `${item.id}-returns` })}
      {renderReturns ? (
        renderReturns(item, ctx)
      ) : (
        <ReturnsSection returns={item.returns} />
      )}
    </>
  );

  const seeAlsoSlot =
    item.see_also.length > 0 ? (
      <>
        {renderHeading(headingLevel + 1, 'See Also', { id: `${item.id}-see-also` })}
        <SeeAlso refs={item.see_also} />
      </>
    ) : null;

  // Right panel — examples (pre-render all code blocks in parallel)
  const exampleNodes = await Promise.all(
    item.examples.map((ex) => renderCodeBlock(ex.language === 'psj' ? psjLanguage : ex.language, ex.code)),
  );
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
