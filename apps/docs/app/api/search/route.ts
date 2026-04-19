// app/api/search/route.ts
//
// createSearchAPI('advanced') chỉ nhận `language` (top-level) — không có localeMap.
// localeMap là option của createFromSource(), không phải createSearchAPI().
//
// Với multi-source (nhiều versions) + i18n (en + ja), approach đúng:
//   - Một createFromSource() per source với localeMap
//   - Custom GET handler merge kết quả từ tất cả sources
//   - staticGET: mỗi source export riêng, client fetch tất cả và merge
//
// Japanese tokenizer:
//   - @orama/tokenizers/japanese — server-side only (WASM)
//   - createTokenizer() là sync trong v3

import { type NextRequest } from 'next/server';

import { stopwords as japaneseStopwords } from '@orama/stopwords/japanese';
import { createTokenizer } from '@orama/tokenizers/japanese';
import { createFromSource } from 'fumadocs-core/search/server';

import type { ApiVersion } from '@/lib/source';

import { apiSources, docsSource } from '@/lib/source';
import { getActiveCanonicalVersions } from '@/lib/versions';

export const revalidate = false;

// ── Shared locale config ──────────────────────────────────────────────────────

const japaneseTokenizer = createTokenizer({
    language: 'japanese',
    stopWords: japaneseStopwords,
});

const localeMap = {
    en: { language: 'english' as const },
    ja: {
        components: { tokenizer: japaneseTokenizer },
        search: { threshold: 0, tolerance: 0 },
    },
};

// ── One search server per source ──────────────────────────────────────────────
//
// createFromSource() tự handle:
//   - i18n locale filtering (page.locale)
//   - structuredData indexing
//   - tag support
//
// Mỗi source cần instance riêng vì localeMap và index config per-source.

const docsServer = createFromSource(docsSource, { localeMap });

const apiServers = Object.fromEntries(
    getActiveCanonicalVersions().map((version) => {
        const source = apiSources[version as ApiVersion];
        return [
            version,
            createFromSource(source, {
                localeMap,
                // tag = version key — client filter theo version
                buildIndex: async (page) => {
                    const data = await page.data.load();
                    return {
                        id: page.url,
                        title: page.data.title,
                        description: page.data.description,
                        url: page.url,
                        structuredData: data.structuredData,
                        tag: version,
                    };
                },
            }),
        ];
    }),
) as Record<string, ReturnType<typeof createFromSource>>;

// ── Merge GET handler ─────────────────────────────────────────────────────────
//
// Nhận request, forward đến tất cả servers, merge kết quả.
// Query params được giữ nguyên (locale, tag, query).

export async function GET(request: NextRequest) {
    const { searchParams } = request.nextUrl;
    const tag = searchParams.get('tag') ?? undefined;

    // Nếu có tag và tag là version key → chỉ query server đó
    if (tag && tag in apiServers) {
        return apiServers[tag]!.GET(request);
    }

    if (tag === 'docs') {
        return docsServer.GET(request);
    }

    // Không có tag → merge tất cả
    const [docsRes, ...apiResponses] = await Promise.all([
        docsServer.GET(request).then((r) => r.json()),
        ...Object.values(apiServers).map((s) => s.GET(request).then((r) => r.json())),
    ]);

    // Fumadocs search response shape: { results: SortedResult[] }
    const merged = [
        ...(docsRes?.results ?? []),
        ...apiResponses.flatMap((r: { results?: unknown[] }) => r?.results ?? []),
    ];

    return Response.json({ results: merged });
}

// ── Static GET ────────────────────────────────────────────────────────────────
//
// Client dùng type: 'static' → download index JSON một lần.
// Với multi-source, static mode phức tạp hơn — dùng fetch mode thay thế.
// Nếu vẫn muốn static: implement một endpoint per source.
//
// export const { staticGET: GET } = docsServer  ← chỉ dùng nếu single source
