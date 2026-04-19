// components/SearchDialog.tsx
//
// Search dialog dùng type: 'fetch' — mỗi keystroke query server.
// Phù hợp với multi-source vì server merge kết quả từ tất cả versions.
//
// Static mode (type: 'static') không dùng ở đây vì:
//   - Multi-source cần một endpoint per source để export index JSON
//   - Merge nhiều static JSON files phức tạp và không cần thiết với docs site
//   - fetch mode đơn giản hơn và vẫn đủ nhanh với revalidate: false (cached)
//
// Tag filter:
//   Detect version từ URL → tự động filter kết quả theo version đang xem.
//   User vẫn có thể clear filter để search toàn bộ.

'use client'

import { useDocsSearch } from 'fumadocs-core/search/client'
import {
    SearchDialog as BaseSearchDialog,
    SearchDialogClose,
    SearchDialogContent,
    SearchDialogFooter,
    SearchDialogHeader,
    SearchDialogIcon,
    SearchDialogInput,
    SearchDialogList,
    SearchDialogOverlay,
    type SharedProps,
} from 'fumadocs-ui/components/dialog/search'
import { useI18n } from 'fumadocs-ui/contexts/i18n'
import { useParams } from 'next/navigation'
import { useState } from 'react'

export default function SearchDialog(props: SharedProps) {
    const params = useParams()
    const { locale } = useI18n()

    // Version từ URL — dùng làm tag filter mặc định
    const urlVersion = params['version'] as string | undefined
    const [tag, setTag] = useState<string | undefined>(urlVersion)

    const { search, setSearch, query } = useDocsSearch({
        type: 'fetch',
        locale,
        tag,
    })

    const placeholder =
        locale === 'ja' ? 'ドキュメントを検索...' : 'Search documentation...'

    const results =
        query.data !== 'empty' ? (query.data ?? []) : []

    return (
        <BaseSearchDialog
            search={search}
            onSearchChange={setSearch}
            isLoading={query.isLoading}
            {...props}
        >
            <SearchDialogOverlay />
            <SearchDialogContent>
                <SearchDialogHeader>
                    <SearchDialogIcon />
                    <SearchDialogInput placeholder={placeholder} />
                    <SearchDialogClose />
                </SearchDialogHeader>

                <SearchDialogList items={results} />

                <SearchDialogFooter>
                    {/* Tag toggle: filter theo version hiện tại hoặc search all */}
                    {urlVersion && (
                        <button
                            className="text-xs text-fd-muted-foreground underline"
                            onClick={() => setTag(tag ? undefined : urlVersion)}
                        >
                            {tag
                                ? locale === 'ja' ? 'すべてのバージョンを検索' : 'Search all versions'
                                : locale === 'ja' ? `${urlVersion} のみ検索` : `Search only ${urlVersion}`}
                        </button>
                    )}
                </SearchDialogFooter>
            </SearchDialogContent>
        </BaseSearchDialog>
    )
}
