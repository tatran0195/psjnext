# psjd — Integration Guide (Fumadocs v16)

Complete wiring for a **Next.js 15 + Fumadocs v16** app with multiple sources
and automatic i18n (English + Japanese).

Mirrors the `createOpenAPI` / `openapiSource` pattern from `fumadocs-openapi`.

---

## Prerequisites

```
Node 18+  |  Next.js 16+  |  React 19.2+  |  Fumadocs v16
```

```bash
pnpm add psjd fumadocs-core fumadocs-ui
```

---

## File structure

```
your-docs/
├── content/
│   └── psjd/
│       ├── sdk.psjd.yaml           ← root manifest
│       ├── _groups/
│       │   ├── nastran-base.yaml
│       │   ├── nastran-base.ja.yaml        ← Japanese sidecar
│       │   └── …
│       ├── psj-command/
│       │   ├── Analysis-Nastran-LinearStatic.yaml
│       │   ├── Analysis-Nastran-LinearStatic.ja.yaml  ← Japanese sidecar
│       │   └── …
│       └── psj-utility/
│           └── …
├── lib/
│   ├── i18n.ts          ← defineI18n config
│   ├── psjd.ts         ← createPsjd instance
│   └── source.ts        ← loader() with multiple sources
├── middleware.ts
└── app/
    └── [lang]/
        └── docs/
            └── [[...slug]]/
                └── page.tsx
```

---

## 1. i18n config

```ts
// lib/i18n.ts
import { defineI18n } from 'fumadocs-core/i18n';

export const i18n = defineI18n({
  defaultLanguage: 'en',
  languages: ['en', 'ja'],
  // fallback to English when a Japanese sidecar is missing
  fallbackLanguage: 'en',
});
```

---

## 2. psjd instance

Mirrors `createOpenAPI()`. Create once, import everywhere.

```ts
// lib/psjd.ts
import { createPsjd } from 'psjd/server';

export const psjd = createPsjd({
  /** Path to sdk.psjd.yaml */
  input: './content/psjd/sdk.psjd.yaml',
  /**
   * Supported locales. Must match lib/i18n.ts languages.
   * For each locale, sidecar files (<id>.<locale>.yaml) are auto-discovered
   * and merged at load time.
   */
  locales: ['en', 'ja'],
  /**
   * Throw on sidecar validation errors (recommended for CI).
   * Default: false (logs warnings).
   */
  strict: process.env.NODE_ENV === 'production',
});
```

---

## 3. Source loader (multiple sources)

```ts
// lib/source.ts
import { loader, multiple } from 'fumadocs-core/source';
import { psjdSource, psjdPlugin } from 'psjd/server';
import { docs } from 'collections/server';       // your MDX collection
import { i18n } from '@/lib/i18n';
import { psjd } from '@/lib/psjd';

export const source = loader(
  multiple({
    // Regular MDX docs
    docs: docs.toFumadocsSource(),
    // psjd API reference — async, loads all locales at once
    psjd: await psjdSource(psjd, {
      /**
       * Virtual path prefix for generated pages.
       * Pages will be at /docs/api/<namespace>/<item>
       */
      baseDir: 'api',
      /** Sidebar grouping strategy */
      groupBy: 'namespace',
    }),
  }),
  {
    baseUrl: '/docs',
    i18n,                      // enables per-locale page trees
    plugins: [psjdPlugin()],  // optional: for future badge/icon transforms
  },
);
```

---

## 4. Middleware

```ts
// middleware.ts
import { createI18nMiddleware } from 'fumadocs-core/i18n/middleware';
import { i18n } from '@/lib/i18n';

export default createI18nMiddleware(i18n);

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```

---

## 5. Page component

```tsx
// app/[lang]/docs/[[...slug]]/page.tsx
import { notFound } from 'next/navigation';
import { DocsPage, DocsBody } from 'fumadocs-ui/page';
import { source } from '@/lib/source';
import { psjd } from '@/lib/psjd';
import { resolveItem } from 'psjd';
import { CallablePage } from 'psjd/ui';
import { ja, en, type PsjdLocale } from 'psjd/ui';
import 'psjd/ui/styles.css';

// Map Fumadocs locale strings to PsjdLocale UI dictionaries
const localeMap: Record<string, PsjdLocale> = { en, ja };

interface Props {
  params: Promise<{ lang: string; slug?: string[] }>;
}

export default async function Page({ params }: Props) {
  const { lang, slug = [] } = await params;
  const page = source.getPage(slug, lang);
  if (!page) notFound();

  // ── psjd API reference page ────────────────────────────────────────────
  if (page.data.type === 'psjd') {
    const { psjdId, version } = page.data;
    const locale = page.data.locale;

    // Load the SDK for this locale (cached by module-level psjd instance)
    const { createSDK } = await import('psjd/server');
    const sdk = await createSDK(
      psjd._options.input,
      psjd._options.baseDir,
      { locale, strict: psjd._options.strict },
    );

    // Pre-resolve all versions so the VersionPicker can switch client-side
    const versionItems = Object.fromEntries(
      sdk.versionIds.map((v) => [v, resolveItem(sdk, psjdId, v)])
    );
    const item = versionItems[version] ?? resolveItem(sdk, psjdId, version);

    return (
      <DocsPage full>
        <DocsBody>
          <CallablePage
            item={item}
            versionItems={versionItems}
            locale={localeMap[lang] ?? en}
          />
        </DocsBody>
      </DocsPage>
    );
  }

  // ── Regular MDX docs page ────────────────────────────────────────────────
  const MDX = page.data.body;
  return (
    <DocsPage>
      <DocsBody>
        <h1>{page.data.title}</h1>
        <MDX />
      </DocsBody>
    </DocsPage>
  );
}

export async function generateStaticParams() {
  return source.generateParams();
}

export async function generateMetadata({ params }: Props) {
  const { lang, slug = [] } = await params;
  const page = source.getPage(slug, lang);
  if (!page) return {};
  return { title: page.data.title, description: page.data.description };
}
```

---

## 6. Layout with I18nProvider

```tsx
// app/[lang]/layout.tsx
import { RootProvider } from 'fumadocs-ui/provider/next';
import { I18nProvider, type Translations } from 'fumadocs-ui/i18n';
import { i18n } from '@/lib/i18n';

// Fumadocs UI component translations (separate from psjd content)
const jaUI: Partial<Translations> = {
  search: '検索',
  toc: '目次',
  lastUpdate: '最終更新',
  chooseLanguage: '言語を選択',
  nextPage: '次のページ',
  previousPage: '前のページ',
  tocTitle: 'このページの内容',
};

const locales = [
  { name: 'English', locale: 'en' },
  { name: '日本語', locale: 'ja' },
];

export default async function Layout({
  params,
  children,
}: {
  params: Promise<{ lang: string }>;
  children: React.ReactNode;
}) {
  const { lang } = await params;

  return (
    <html lang={lang}>
      <body>
        <RootProvider>
          <I18nProvider
            locale={lang}
            locales={locales}
            translations={{ ja: jaUI }[lang]}
          >
            {children}
          </I18nProvider>
        </RootProvider>
      </body>
    </html>
  );
}
```

---

## How sidecar auto-loading works

`psjdSource(psjd)` internally calls `createSDK` once per locale in
`psjd._options.locales`. For locale `"ja"`, it looks for:

```
content/psjd/_groups/nastran-base.ja.yaml          ← group sidecar
content/psjd/psj-command/Analysis-Nastran-LinearStatic.ja.yaml  ← item sidecar
```

Missing sidecars are silently skipped — partial translation is fine.
The resulting items are stored in the `ParsedSDK` with translated strings
already merged in, so `resolveItem` produces translated `ResolvedItem`
objects with no additional work in the page component.

---

## Comparison with fumadocs-openapi

| Concern | fumadocs-openapi | psjd |
|---|---|---|
| Factory | `createOpenAPI({ input })` | `createPsjd({ input, locales })` |
| Source | `await openapiSource(openapi, { baseDir })` | `await psjdSource(psjd, { baseDir })` |
| Plugin | `openapiPlugin()` | `psjdPlugin()` |
| Page check | `page.data.type === 'openapi'` | `page.data.type === 'psjd'` |
| i18n | not built-in | `locales: ['en','ja']` + sidecar files |
| UI locale | — | `<CallablePage locale={localeMap[lang]}/>` |
| Version picker | — | built-in, client-side |
| Param search | — | built-in, client-side |
