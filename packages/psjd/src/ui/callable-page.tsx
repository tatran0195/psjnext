'use client';

import { useMemo, useState } from 'react';
import { semverCompare } from '../resolve.js';
import type { ResolvedItem, ResolvedParam, Returns } from '../types.js';
import { CodeSamplePanel } from './code-sample.js';
import { en, type PsjdLocale } from './i18n.js';
import { HighlightMatch, ParamSearchInput, useParamSearch } from './param-search.js';

// ─── CallablePage ─────────────────────────────────────────────────────────────

export interface CallablePageProps {
  item: ResolvedItem;
  versionItems?: Record<string, ResolvedItem>;
  typeBaseUrl?: string;
  /** UI locale. Defaults to `en`. Import `ja` from 'psjd/ui'. */
  locale?: PsjdLocale;
}

export function CallablePage({
  item: initialItem,
  versionItems,
  typeBaseUrl = '/docs/data-types',
  locale = en,
}: CallablePageProps) {
  const versions = versionItems ? Object.keys(versionItems).sort(semverCompare) : [];
  const [version, setVersion] = useState(initialItem.resolvedVersion);

  const item: ResolvedItem = useMemo(() => {
    if (versionItems && versionItems[version]) return versionItems[version]!;
    return initialItem;
  }, [initialItem, versionItems, version]);

  const search = useParamSearch(item.resolvedParams);

  return (
    <div className="psjd-page">
      <div className="psjd-docs-col">

        <header className="psjd-header">
          {item.namespace && (
            <p className="psjd-breadcrumb">
              <span className="psjd-breadcrumb-domain">{item.domain}</span>
              <ChevronRight />
              <span>{item.namespace}</span>
            </p>
          )}
          <h1 className="psjd-title">{item.title}</h1>
          {item.ribbon && (
            <p className="psjd-ribbon">
              <span className="psjd-ribbon-label">{locale.ribbon}</span>
              {item.ribbon}
            </p>
          )}
          {item.deprecated && (
            <div className="psjd-deprecated-badge" role="alert">
              {item.deprecated_in ? locale.deprecatedIn(item.deprecated_in) : locale.deprecated}
            </div>
          )}
        </header>

        {versions.length > 1 && (
          <VersionPicker
            versions={versions}
            current={version}
            introduced={item.version_introduced}
            onChange={setVersion}
            locale={locale}
          />
        )}

        {item.callouts?.map((c, i) => (
          <Callout key={i} level={c.level} text={c.text} />
        ))}

        {item.description && <p className="psjd-description">{item.description}</p>}
        {item.versionNotes && (
          <p className="psjd-version-notes">
            <strong>v{item.resolvedVersion}:</strong> {item.versionNotes}
          </p>
        )}

        {item.syntax && (
          <section className="psjd-section">
            <h2 className="psjd-section-title">{locale.syntax}</h2>
            <pre className="psjd-syntax-block"><code>{item.syntax.trim()}</code></pre>
          </section>
        )}

        <section className="psjd-section">
          <div className="psjd-section-header">
            <h2 className="psjd-section-title">
              {locale.parameters}
              {item.resolvedParams.length > 0 && (
                <span className="psjd-param-count">{item.resolvedParams.length}</span>
              )}
            </h2>
            {item.resolvedParams.length > 3 && (
              <ParamSearchInput
                query={search.query}
                setQuery={search.setQuery}
                matchCount={search.matchCount}
                totalCount={search.totalCount}
                locale={locale}
              />
            )}
          </div>
          {item.resolvedParams.length === 0 ? (
            <p className="psjd-no-params">{locale.noParams}</p>
          ) : (
            <ParamTable
              params={search.filteredParams}
              style={item.paramStyle}
              query={search.query}
              typeBaseUrl={typeBaseUrl}
              locale={locale}
            />
          )}
        </section>

        <section className="psjd-section">
          <h2 className="psjd-section-title">{locale.returns}</h2>
          <ReturnsSection returns={item.returns} typeBaseUrl={typeBaseUrl} locale={locale} />
        </section>

        {item.see_also && item.see_also.length > 0 && (
          <section className="psjd-section">
            <h2 className="psjd-section-title">{locale.seeAlso}</h2>
            <ul className="psjd-see-also-list">
              {item.see_also.map((ref, i) => (
                <li key={i}>
                  <a href={`/docs/api-reference/${ref.$ref}`} className="psjd-see-also-link">
                    {ref.label ?? ref.$ref}
                  </a>
                </li>
              ))}
            </ul>
          </section>
        )}

        <p className="psjd-version-meta">
          {locale.introducedIn(item.version_introduced)}
          {item.removed_in && locale.removedIn(item.removed_in)}.
        </p>
      </div>

      <aside className="psjd-sample-col">
        <CodeSamplePanel item={item} locale={locale} />
      </aside>
    </div>
  );
}

// ─── ParamTable ───────────────────────────────────────────────────────────────

export interface ParamTableProps {
  params: ResolvedParam[];
  style: 'named' | 'positional';
  query: string;
  typeBaseUrl: string;
  locale?: PsjdLocale;
}

export function ParamTable({ params, style, query, typeBaseUrl, locale = en }: ParamTableProps) {
  if (params.length === 0) {
    return <p className="psjd-no-params psjd-no-params--filtered">{locale.noParamsFiltered}</p>;
  }

  if (style === 'positional') {
    return (
      <div className="psjd-table-wrapper">
        <table className="psjd-param-table psjd-param-table--positional">
          <thead>
            <tr>
              <th className="psjd-th psjd-th--pos">{locale.thPosition}</th>
              <th className="psjd-th">{locale.thName}</th>
              <th className="psjd-th">{locale.thType}</th>
              <th className="psjd-th">{locale.thDescription}</th>
            </tr>
          </thead>
          <tbody>
            {params.map((p, i) => (
              <tr key={p.name ?? i} className="psjd-param-row">
                <td className="psjd-td psjd-td--pos">{p.position ?? i + 1}</td>
                <td className="psjd-td">
                  <code className="psjd-param-name-code">
                    <HighlightMatch text={p.name} query={query} />
                  </code>
                  {p.deprecated && <span className="psjd-deprecated-tag">{locale.badgeDeprecated}</span>}
                </td>
                <td className="psjd-td"><TypeBadge type={p.type} baseUrl={typeBaseUrl} /></td>
                <td className="psjd-td psjd-td--desc">
                  {p.description && (
                    <span className="psjd-param-desc">
                      <HighlightMatch text={p.description} query={query} />
                    </span>
                  )}
                  {p.enum_values && p.enum_values.length > 0 && <EnumList values={p.enum_values} query={query} />}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }

  return (
    <div className="psjd-table-wrapper">
      <table className="psjd-param-table psjd-param-table--named">
        <thead>
          <tr>
            <th className="psjd-th">{locale.thName}</th>
            <th className="psjd-th">{locale.thType}</th>
            <th className="psjd-th psjd-th--center">{locale.thRequired}</th>
            <th className="psjd-th">{locale.thDefault}</th>
            <th className="psjd-th">{locale.thDescription}</th>
          </tr>
        </thead>
        <tbody>
          {params.map((p, i) => (
            <tr key={p.name ?? i} className={`psjd-param-row${p.required ? ' psjd-param-row--required' : ''}`}>
              <td className="psjd-td psjd-td--name">
                <code className="psjd-param-name-code">
                  <HighlightMatch text={p.display_name ?? p.name} query={query} />
                </code>
                {p.required && <span className="psjd-required-badge">{locale.badgeRequired}</span>}
                {p.deprecated && <span className="psjd-deprecated-tag">{locale.badgeDeprecated}</span>}
                {p.inferred && <span className="psjd-inferred-tag" title={locale.badgeInferred}>~</span>}
              </td>
              <td className="psjd-td"><TypeBadge type={p.type} baseUrl={typeBaseUrl} /></td>
              <td className="psjd-td psjd-td--center">
                <span
                  className={`psjd-bool-dot ${p.required ? 'psjd-bool-dot--yes' : 'psjd-bool-dot--no'}`}
                  title={p.required ? locale.dotRequired : locale.dotOptional}
                  aria-label={p.required ? locale.dotRequired : locale.dotOptional}
                />
              </td>
              <td className="psjd-td psjd-td--default">
                {p.default != null && p.default !== '~'
                  ? <code className="psjd-default-val">{p.default}</code>
                  : <span className="psjd-none" aria-label={locale.noneAriaLabel}>—</span>}
              </td>
              <td className="psjd-td psjd-td--desc">
                {p.description && (
                  <span className="psjd-param-desc">
                    <HighlightMatch text={p.description} query={query} />
                  </span>
                )}
                {p.enum_values && p.enum_values.length > 0 && <EnumList values={p.enum_values} query={query} />}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// ─── VersionPicker ────────────────────────────────────────────────────────────

export interface VersionPickerProps {
  versions: string[];
  current: string;
  introduced: string;
  onChange: (v: string) => void;
  locale?: PsjdLocale;
}

export function VersionPicker({ versions, current, introduced, onChange, locale = en }: VersionPickerProps) {
  const available = versions.filter((v) => semverCompare(v, introduced) >= 0);
  return (
    <div className="psjd-version-picker">
      <label className="psjd-version-label" htmlFor="psjd-version-sel">
        {locale.sdkVersion}
      </label>
      <select id="psjd-version-sel" className="psjd-version-select"
        value={current} onChange={(e) => onChange(e.target.value)}>
        {available.map((v) => <option key={v} value={v}>{v}</option>)}
      </select>
    </div>
  );
}

// ─── Internal sub-components ──────────────────────────────────────────────────

function TypeBadge({ type, baseUrl }: { type: string; baseUrl: string }) {
  if (type.startsWith('$ref:')) {
    const refPath = type.slice('$ref:'.length);
    const label = refPath.split('/').pop() ?? refPath;
    return <a href={`${baseUrl}/${label}`} className="psjd-type-ref" title={refPath}>{label}</a>;
  }
  const listMatch = type.match(/^List\[(.+)\]$/);
  if (listMatch && listMatch[1]) {
    return <span className="psjd-type-list">List[<TypeBadge type={listMatch[1]} baseUrl={baseUrl} />]</span>;
  }
  return <code className="psjd-type-prim">{type}</code>;
}

function EnumList({ values, query }: {
  values: Array<{ id: number | string; label: string; description?: string }>;
  query: string;
}) {
  return (
    <dl className="psjd-enum-list">
      {values.map((v) => (
        <div key={v.id} className="psjd-enum-row">
          <dt className="psjd-enum-id"><code>{v.id}</code></dt>
          <dd className="psjd-enum-label">
            <HighlightMatch text={v.label} query={query} />
            {v.description && <span className="psjd-enum-desc">{' — '}<HighlightMatch text={v.description} query={query} /></span>}
          </dd>
        </div>
      ))}
    </dl>
  );
}

function ReturnsSection({ returns, typeBaseUrl, locale }: { returns: Returns; typeBaseUrl: string; locale: PsjdLocale }) {
  if (returns.kind === 'void') return <p className="psjd-returns-void">{locale.returnsVoid}</p>;
  if (returns.kind === 'typed') {
    return (
      <div className="psjd-returns-typed">
        <TypeBadge type={returns.type ?? 'Unknown'} baseUrl={typeBaseUrl} />
        {returns.description && <span className="psjd-returns-desc"> — {returns.description}</span>}
      </div>
    );
  }
  return (
    <div className="psjd-returns-codes">
      {returns.description && <p>{returns.description}</p>}
      {returns.codes && returns.codes.length > 0 && (
        <dl className="psjd-return-code-list">
          {returns.codes.map((c) => (
            <div key={c.value} className="psjd-return-code-row">
              <dt><code className="psjd-return-code-val">{c.value}</code></dt>
              <dd className="psjd-return-code-meaning">{c.meaning}</dd>
            </div>
          ))}
        </dl>
      )}
    </div>
  );
}

function Callout({ level, text }: { level: string; text: string }) {
  const icons: Record<string, string> = { warn: '⚠', danger: '✕', info: 'ℹ' };
  return (
    <div className={`psjd-callout psjd-callout--${level}`} role="note">
      <span className="psjd-callout-icon" aria-hidden>{icons[level] ?? 'ℹ'}</span>
      <span className="psjd-callout-text">{text}</span>
    </div>
  );
}

function ChevronRight() {
  return (
    <svg className="psjd-breadcrumb-sep" width="12" height="12" viewBox="0 0 24 24"
      fill="none" stroke="currentColor" strokeWidth="2" aria-hidden>
      <polyline points="9 18 15 12 9 6" />
    </svg>
  );
}
