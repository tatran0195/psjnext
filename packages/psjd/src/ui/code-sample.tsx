'use client';

import React, { useCallback, useState } from 'react';
import type { ExampleLanguage, ResolvedItem, ResolvedParam } from '../types.js';
import { en, type PsjdLocale } from './i18n.js';

// ─── Types ────────────────────────────────────────────────────────────────────

type SampleLanguage = ExampleLanguage | 'psj-exec';

export interface CodeSamplePanelProps {
  item: ResolvedItem;
  execPrefix?: string;
  locale?: PsjdLocale;
}

// ─── Auto-generate call signatures ───────────────────────────────────────────

function buildPspsjdSample(item: ResolvedItem): string {
  if (item.paramStyle === 'positional') {
    const args = item.resolvedParams.slice(0, 8).map(formatDefaultValue).join(', ');
    const ellipsis = item.resolvedParams.length > 8 ? ', ...' : '';
    return `JPT.Exec('${item.id}(${args}${ellipsis})')`;
  }
  const requiredParams = item.resolvedParams.filter((p) => p.required);
  const optionalParams = item.resolvedParams.filter((p) => !p.required).slice(0, 4);
  const shown = [...requiredParams, ...optionalParams];
  const lines = shown.map((p) => `    ${p.name}=${formatDefaultValue(p)}`);
  const hasMore = item.resolvedParams.length > shown.length;
  if (hasMore) lines.push(`    # … ${item.resolvedParams.length - shown.length} more optional params`);
  if (lines.length === 0) return `result = ${item.title.replace(/\(\)$/, '')}()`;
  return `result = ${item.title.replace(/\(\)$/, '')}(\n${lines.join(',\n')}\n)`;
}

function buildPythonSample(item: ResolvedItem, commentLine: string): string {
  const ns = item.namespace ?? item.domain;
  const args = item.resolvedParams
    .filter((p) => p.required)
    .map((p) => `${p.name}=${formatDefaultValue(p)}`)
    .join(', ');
  return [
    commentLine,
    `import jpt`,
    ``,
    `# ${(item.description.split('\n')[0] ?? '').slice(0, 80)}`,
    `result = jpt.${ns}.${item.id.split('-').pop()}(${args})`,
    `print(result)`,
  ].join('\n');
}

function formatDefaultValue(p: ResolvedParam): string {
  if (p.default != null && p.default !== '~') return p.default;
  switch (p.type.split('[')[0]) {
    case 'String': return '""';
    case 'Boolean': return 'False';
    case 'Integer': return '0';
    case 'Double': return '0.0';
    case 'Cursor': return 'None';
    default: return p.type.startsWith('List') ? '[]' : 'None';
  }
}

// ─── Copy button ──────────────────────────────────────────────────────────────

function CopyButton({ text, locale }: { text: string; locale: PsjdLocale }) {
  const [copied, setCopied] = useState(false);
  const handleCopy = useCallback(async () => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch { /* ignore */ }
  }, [text]);

  return (
    <button className="psjd-copy-btn" onClick={handleCopy}
      aria-label={copied ? locale.copied : locale.copyCode}
      title={copied ? locale.copied : locale.copyToClipboard}>
      {copied ? (
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
          <polyline points="20 6 9 17 4 12" />
        </svg>
      ) : (
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="9" y="9" width="13" height="13" rx="2" />
          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
        </svg>
      )}
    </button>
  );
}

// ─── Lightweight syntax tokeniser ─────────────────────────────────────────────

function tokenize(code: string, language: string): React.ReactNode[] {
  if (language === 'psj' || language === 'psj-exec' || language === 'python') {
    const lines = code.split('\n');
    return lines.map((line, li) => (
      <span key={li} className="psjd-code-line">
        {tokenizeLine(line)}
        {li < lines.length - 1 && '\n'}
      </span>
    ));
  }
  return [<span key="raw">{code}</span>];
}

function tokenizeLine(line: string): React.ReactNode[] {
  const tokens: React.ReactNode[] = [];
  const pattern =
    /("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')|(\b(?:import|from|print|result|True|False|None|return|def|class|if|else|for|in|not|and|or|is)\b)|(#.*)|([\w.]+(?=\s*[=(]))|(\b\d+(?:\.\d+)?\b)/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = pattern.exec(line)) !== null) {
    if (m.index > last) tokens.push(<span key={last}>{line.slice(last, m.index)}</span>);
    const [full, str, kw, comment, fname, num] = m;
    if (str) tokens.push(<span key={m.index} className="psjd-tok-str">{full}</span>);
    else if (kw) tokens.push(<span key={m.index} className="psjd-tok-kw">{full}</span>);
    else if (comment) tokens.push(<span key={m.index} className="psjd-tok-comment">{full}</span>);
    else if (fname) tokens.push(<span key={m.index} className="psjd-tok-fn">{full}</span>);
    else if (num) tokens.push(<span key={m.index} className="psjd-tok-num">{full}</span>);
    last = m.index + full.length;
  }
  if (last < line.length) tokens.push(<span key={last}>{line.slice(last)}</span>);
  return tokens;
}

// ─── Main panel ───────────────────────────────────────────────────────────────

const TABS: { id: SampleLanguage; label: string }[] = [
  { id: 'psj', label: 'PSJ' },
  { id: 'python', label: 'Python' },
  { id: 'psj-exec', label: 'Exec' },
];

export function CodeSamplePanel({ item, locale = en }: CodeSamplePanelProps) {
  const [activeTab, setActiveTab] = useState<SampleLanguage>('psj');

  const explicitExample = item.examples?.find(
    (e) => e.language === activeTab || (activeTab === 'psj-exec' && e.language === 'psj'),
  );

  const generatedSamples: Record<SampleLanguage, string> = {
    psj: buildPspsjdSample(item),
    python: buildPythonSample(item, locale.pythonCommentLine),
    'psj-exec': buildPspsjdSample(item),
  };

  const code = explicitExample?.code.trim() ?? generatedSamples[activeTab];

  return (
    <div className="psjd-sample-panel">
      <div className="psjd-sample-tabs" role="tablist">
        {TABS.map((tab) => (
          <button key={tab.id} role="tab"
            aria-selected={activeTab === tab.id}
            className={`psjd-sample-tab${activeTab === tab.id ? ' psjd-sample-tab--active' : ''}`}
            onClick={() => setActiveTab(tab.id)}>
            {tab.label}
          </button>
        ))}
        <div className="psjd-sample-tabs-spacer" />
        <CopyButton text={code} locale={locale} />
      </div>
      <div className="psjd-sample-body">
        <pre className={`psjd-sample-code language-${activeTab}`}>
          <code>{tokenize(code, activeTab)}</code>
        </pre>
      </div>
      {item.returns.kind !== 'void' && (
        <div className="psjd-sample-returns">
          <span className="psjd-sample-returns-label">{locale.returnsLabel}</span>
          <span className="psjd-sample-returns-type">{item.returns.type ?? 'macro_code'}</span>
          {item.returns.description && (
            <span className="psjd-sample-returns-desc">{item.returns.description}</span>
          )}
        </div>
      )}
    </div>
  );
}
