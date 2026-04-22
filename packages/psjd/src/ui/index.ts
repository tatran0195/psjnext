'use client';

// psjd/src/ui/index.ts
// Browser-safe barrel. No Node.js builtins.

export { CallablePage } from './callable-page.js';
export type { CallablePageProps } from './callable-page.js';

export { ParamTable, VersionPicker } from './callable-page.js';
export type { ParamTableProps, VersionPickerProps } from './callable-page.js';

export { CodeSamplePanel } from './code-sample.js';
export type { CodeSamplePanelProps } from './code-sample.js';

export { HighlightMatch, ParamSearchInput, useParamSearch } from './param-search.js';
export type { ParamSearchProps, UseParamSearchResult } from './param-search.js';

// i18n — locale objects and type
export { en, ja, locales } from './i18n.js';
export type { LocaleKey, PsjdLocale } from './i18n.js';

// styles
export { default as styles } from './';
