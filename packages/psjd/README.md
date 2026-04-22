# fumadocs-psjd

Fumadocs plugin for **psjd v2** — the PSJ/Jupiter SDK documentation format.

Same pattern as `fumadocs-openapi`: static MDX generation **or** virtual Loader API source, with a two-column OpenAPI-style page layout, live param search, and tabbed code samples.

---

## Package layout

```
fumadocs-psjd/
├── src/
│   ├── types.ts              ← Full TypeScript mirror of psjd v2 spec
│   ├── resolve.ts            ← Core resolver: group expansion + delta reconstruction
│   ├── server.ts             ← createSDK(), psjdSource(), psjdPlugin()
│   ├── index.ts              ← generateFiles() + re-exports
│   ├── ui/
│   │   ├── callable-page.tsx ← <CallablePage> — two-column page component
│   │   ├── code-sample.tsx   ← <CodeSamplePanel> — right-side tabbed code panel
│   │   ├── param-search.tsx  ← useParamSearch hook + <ParamSearchInput>
│   │   ├── styles.css        ← All psjd-* CSS, dark mode, responsive
│   │   └── index.ts          ← Barrel export
│   └── __tests__/
│       ├── resolve.test.ts   ← 31 unit tests (semver, expandGroups, resolveItem)
│       ├── server.test.ts    ← 20 integration tests (real fixture YAMLs)
│       └── generate.test.ts  ← 7 integration tests (generateFiles)
├── fixtures/                 ← Test YAML files (mirrors spec examples)
├── turbo.json
├── tsup.config.ts
├── vitest.config.ts
└── tsconfig.json
```

---

## Three exports

| Import path | Content | Node? |
|---|---|---|
| `fumadocs-psjd` | `generateFiles()`, `createSDK()`, `resolveItem()` | ✅ server/build only |
| `fumadocs-psjd/server` | `createSDK()`, `psjdSource()`, `psjdPlugin()` | ✅ server/build only |
| `fumadocs-psjd/ui` | `<CallablePage>`, `<ParamTable>`, `<CodeSamplePanel>`, `useParamSearch` | 🌐 browser-safe |

---

## Quick start

### Mode A — Static MDX generation

```ts
// scripts/generate-psjd-docs.ts
import { generateFiles } from 'fumadocs-psjd';
import { rimraf } from 'rimraf';

const OUT = './content/docs/api-reference/(generated)';
await rimraf(OUT, { filter: (v) => !v.endsWith('meta.json') });

await generateFiles({
  input: './content/psjd/sdk.psjd.yaml',
  output: OUT,
  per: 'item',              // 'item' | 'namespace' | 'domain'
  includeDescription: true,
  version: '5.1.0',         // defaults to current_version
});
```

Add `<CallablePage>` to your MDX component map:

```ts
// mdx-components.ts
import { CallablePage } from 'fumadocs-psjd/ui';
export function getMDXComponents(components?) {
  return { ...defaultComponents, CallablePage, ...components };
}
```

### Mode B — Virtual source (no generated files)

```ts
// lib/source.ts
import { loader } from 'fumadocs-core/source';
import { psjdSource, psjdPlugin } from 'fumadocs-psjd/server';
import { sdk } from './psjd';  // your createSDK() singleton

export const source = loader({
  source: psjdSource(sdk, { groupBy: 'namespace' }),
  baseUrl: '/docs/api-reference',
  plugins: [psjdPlugin()],
});
```

```tsx
// app/docs/api-reference/[...slug]/page.tsx
import { source } from '@/lib/source';
import { sdk } from '@/lib/psjd';
import { resolveItem } from 'fumadocs-psjd';
import { CallablePage } from 'fumadocs-psjd/ui';
import 'fumadocs-psjd/ui/styles.css';

export default async function Page({ params }) {
  const { slug } = await params;
  const page = source.getPage(slug);
  if (!page || page.data.type !== 'psjd') notFound();

  // Resolve all versions for client-side switching
  const versionItems = Object.fromEntries(
    sdk.versionIds.map((v) => [v, resolveItem(sdk, page.data.psjdId, v)])
  );
  const item = versionItems[page.data.version]!;

  return (
    <DocsPage>
      <DocsBody>
        <CallablePage item={item} versionItems={versionItems} />
      </DocsBody>
    </DocsPage>
  );
}
```

---

## SDK singleton

```ts
// lib/psjd.ts
import { createSDK } from 'fumadocs-psjd/server';
export const sdk = await createSDK('./content/psjd/sdk.psjd.yaml');
```

---

## Tests

```bash
pnpm test           # vitest run (58 tests)
pnpm test:coverage  # with V8 coverage
```
