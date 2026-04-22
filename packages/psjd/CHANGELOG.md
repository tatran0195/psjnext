# fumadocs-psjd Changelog

## 1.0.0 (initial release)

### Core
- `createSDK()` — parse full psjd v2 file tree (sdk.psjd.yaml + _groups/ + domain folders)
- `resolveItem()` — fully correct spec Section 5 implementation: group expansion → delta application
- `resolveAll()` — resolve every item at a given SDK version
- `semverCompare/Lte/Gte` — numeric semver comparison (fixes lexicographic `5.10.0 < 5.9.0` bug)

### Fixes vs prior draft
- **[Critical]** `callable-page.tsx`: was `'use client'` while accepting `ParsedSDK` (Map objects) as a prop — Maps are not serializable across the RSC/client boundary. Fixed: RSC layer passes `ResolvedItem` (plain POJO); client component holds version state only.
- **[Bug]** `VersionPicker` filtered `versions.filter(v => v >= introduced)` using string comparison — broke for `5.10.0 < 5.9.0`. Fixed with `semverCompare`.
- **[Bug]** `resolveItem` spread `...item` (which includes raw `params: ParamOrGroupRef[]`) into `ResolvedItem`. Fixed: explicit field-by-field construction, zero raw fields leak.
- **[Bug]** `psjdSource` embedded `ParsedSDK` (Map) in page data — not JSON-serializable. Fixed: page data contains only `psjdId` + `version` strings.
- **[Bug]** `hasVersions` in `CallablePage` was computed but never used.
- **[Bug]** `sdk.manifest.items ?? sdk.items.size` — `items` is not on `manifest`. Dead code removed.
- **[Missing]** `tsconfig.json`, `tsup.config.ts`, `vitest.config.ts`, `turbo.json` — all added.
- **[Missing]** `src/ui/index.ts` barrel — added.
- **[Missing]** `src/ui/styles.css` — full CSS for all `psjd-*` classes, dark mode, OpenAPI-style two-column layout.
- **[Missing]** `src/ui/code-sample.tsx` — right-side code panel (PSJ / Python / Exec tabs, copy button, syntax highlighting, auto-generated samples).
- **[Missing]** `src/ui/param-search.tsx` — live param filter with `useParamSearch` hook, `<ParamSearchInput>`, `<HighlightMatch>`.
- **[Missing]** All test files and fixture YAML files — 58 tests, 3 test files.
- **[Missing]** Fixture YAML files covering: group-only items, exclude/insert_after, group extends, version delta add/remove/modify, positional macros, void returns, callouts.

### New features
- **Param search** — `useParamSearch` hook filters across name, display_name, type, description, enum labels. `<HighlightMatch>` wraps matches in `<mark>`.
- **Code sample panel** — auto-generates PSJ / Python / Exec samples from resolved params. Prefers explicit `examples:` if available for the active tab.
- **Slug deduplication** — `psjdSource` guarantees unique page paths even if two items slugify identically.
- **Item-level version overrides** — `description`, `ribbon`, `deprecated`, `notes` from `VersionDelta.item` applied to `ResolvedItem`.
- **`versionNotes`** on `ResolvedItem` — surfaces `VersionDelta.notes` for the resolved version in the UI.
