// ─────────────────────────────────────────────────────────────────────────────
// i18n-translations.ts
//
// Production-grade translation dictionary following a nested-namespace pattern.
// Keys are grouped by page section, with arrays used for repeated content items
// (stats, philosophy cards, modules) to avoid flat `_1`, `_2`, etc. suffixes.
// ─────────────────────────────────────────────────────────────────────────────

export const translations = {
    en: {
        // ── Home / Enterprise landing page ────────────────────────────────────
        enterprise: {
            hero: {
                badge: 'PSJ v5.1 — Production Release',
                title: ['Python Scripting', 'for Jupiter'] as [string, string],
                desc: 'The industry-standard CAE automation platform. Build production-grade simulation workflows with the full power of Python 3.',
                cta: {
                    primary: 'Get Started',
                    secondary: 'View Tutorials',
                },
                code: {
                    filename: 'automate.py — PSJ v5.1',
                    language: 'Python 3.x',
                    statusBar: ['Connected to Jupiter', 'PSJ v5.1.1 Stable'] as [string, string],
                },
            },
            phi: {
                label: 'Core Philosophy',
                title: 'The 4F Design Principle',
                desc: 'PSJ is built around four core engineering principles — designed to solve every CAE automation challenge across organizations of all sizes.',
                readDocs: 'Read the documentation',
                cards: [
                    {
                        label: 'Friendly',
                        sub: 'Even non-programmers',
                        desc: 'Macro recording means anyone can automate workflows without writing code.',
                    },
                    {
                        label: 'Fast',
                        sub: 'Through automation',
                        desc: 'Eliminate repetitive operations. Hours of work become seconds of script.',
                    },
                    {
                        label: 'Functional',
                        sub: 'IDE & GUI Builder',
                        desc: 'Built-in development tools with full predictive tips and dialog builder.',
                    },
                    {
                        label: 'Flexible',
                        sub: 'Advanced simulation',
                        desc: 'Full Python 3 ecosystem — NumPy, Pandas, scikit-learn, pptx and more.',
                    },
                ] as { label: string; sub: string; desc: string }[],
            },
            modules: {
                header: {
                    label: 'System Architecture',
                    title: 'Six Integrated Modules',
                    linkLabel: 'View architecture docs',
                },
                exploreLabel: 'Explore module',
                items: [
                    { label: 'Macro', desc: 'Auto-recorded script equivalents of Jupiter GUI operations.' },
                    { label: 'PSJ-Command', desc: 'Command-language replay of any Jupiter dialog function.' },
                    { label: 'PSJ-Utility', desc: 'Query model database: IDs, names, colors, geometry.' },
                    { label: 'PSJ-GUI', desc: 'Visual GUI Command Builder — no code required.' },
                    { label: 'Custom Shell', desc: 'Interactive debug shell with real-time error output.' },
                    { label: 'Custom IDE', desc: 'Smart IDE with auto-complete and predictive tips.' },
                ] as { label: string; desc: string }[],
            },
            industries: {
                header: {
                    label: 'Industries Served',
                    title: 'Powering CAE teams across sectors',
                    desc: 'From automotive crash to marine hydrodynamics, PSJ adapts to industry-specific simulation pipelines.',
                },
            },
        },

        // ── Showcase page ─────────────────────────────────────────────────────
        showcase: {
            header: {
                label: 'Technical Showcase',
                title: 'Showcase Catalog',
                desc: 'Explore our production-grade CAE automation solutions and specialized engineering services developed for industry-leading organizations.',
            },
            search: {
                byCode: 'Search by code or title...',
                updates: 'Search updates',
            },
            filters: {
                industryPrefix: 'Industry:',
                sortPrefix: 'Sort:',
                sortByRelevant: 'Most relevant',
                sortByCode: 'Solution code',
                sortByComplexity: 'Complexity',
                filterSolutions: 'Filter Solutions',
            },
            results: {
                showing: 'Showing {count} of {total} Results',
                clearFilters: 'Clear all filters',
                noSolutions: 'No solutions match your criteria',
                resetFilters: 'Reset filters',
            },
            card: {
                details: 'Details',
                requestConsultation: 'Request Consultation',
                capabilities: 'Capabilities',
                deliverables: 'Deliverables',
                duration: 'Duration',
                complexity: 'Complexity',
                industry: 'Industry',
                software: 'Software:',
            },
            cta: {
                subtitle: 'Custom Engineering',
                title: "Don't see what you need?",
                desc: 'Our team specializes in custom CAE automation pipelines tailored to your specific engineering challenges.',
                primaryLabel: 'Request a quote',
                secondaryLabel: 'Schedule a call',
            },
        },

        // ── Changelog page ────────────────────────────────────────────────────
        changelog: {
            nav: {
                home: 'Home',
                backToChangelog: 'Back to changelog',
            },
            header: {
                label: 'Platform Updates',
                title: 'Changelog',
                desc: 'Product updates and release notes for PSJ CAE automation platform.',
            },
            sidebar: {
                allVersions: 'All versions',
            },
            search: {
                placeholder: 'Search changelog...',
                searchUpdates: 'Search updates',
                find: 'Search...',
            },
            filters: {
                filterByVersion: 'Filter by version',
                filterByTag: 'Filter by tag',
                filterByDate: 'Filter by date',
                sortBy: 'Sort by',
                sortByDate: 'Date',
                sortByVersion: 'Version',
                allTags: 'All tags',
                categories: 'Categories',
                all: 'All',
                clearFilters: 'Clear all filters',
            },
            results: {
                showing: 'Showing {count} of {total} results',
                noUpdates: 'No updates matched your criteria',
                noResults: 'No results found',
            },
            badges: {
                feature: 'Feature',
                fix: 'Fix',
                breaking: 'Breaking',
                maintenance: 'Maintenance',
                deprecated: 'Deprecated',
                preview: 'Preview',
                legacy: 'Legacy',
                release: 'Release',
            },
            entry: {
                moreUpdates: 'more updates',
                releaseNote: 'Release Note',
                defaultTitle: 'Update',
                copyLink: 'Copy Link',
                readDetails: 'Read details',
                highlights: 'Highlights',
                releaseDetails: 'Release Details',
                missingVersion: 'No Version',
            },
        },
    },

    ja: {
        // ── Home / Enterprise landing page ────────────────────────────────────
        enterprise: {
            hero: {
                badge: 'PSJ v5.1 — プロダクションリリース',
                title: ['Python スクリプティング', 'Jupiter のために'] as [string, string],
                desc: '業界標準の CAE 自動化プラットフォーム。Python 3 のパワーを最大限に活用し、プロダクションレベルのシミュレーションワークフローを構築。',
                cta: {
                    primary: '今すぐ始める',
                    secondary: 'チュートリアルを見る',
                },
                code: {
                    filename: 'automate.py — PSJ v5.1',
                    language: 'Python 3.x',
                    statusBar: ['Jupiter に接続中', 'PSJ v5.1.1 安定版'] as [string, string],
                },
            },
            phi: {
                label: 'コア・フィロソフィー',
                title: '4F デザイン原則',
                desc: 'PSJは、あらゆる規模の組織におけるCAE自動化の課題を解決するために設計された、4つのコア・エンジニアリング原則に基づいて構築されています。',
                readDocs: 'ドキュメントを読む',
                cards: [
                    {
                        label: 'Friendly',
                        sub: 'プログラマーでなくても',
                        desc: 'マクロ記録機能により、コードを書かずに誰でもワークフローを自動化できます。',
                    },
                    {
                        label: 'Fast',
                        sub: '自動化による高速化',
                        desc: '反復作業を排除。数時間の作業が数秒のスクリプトになります。',
                    },
                    {
                        label: 'Functional',
                        sub: 'IDE & GUI ビルダー',
                        desc: '予測チップやダイアログビルダーを備えた開発ツールを内蔵。',
                    },
                    {
                        label: 'Flexible',
                        sub: '高度なシミュレーション',
                        desc: 'Python 3 エコシステム（NumPy、Pandas、scikit-learn、pptxなど）をフル活用。',
                    },
                ] as { label: string; sub: string; desc: string }[],
            },
            modules: {
                header: {
                    label: 'システムアーキテクチャ',
                    title: '6つの統合モジュール',
                    linkLabel: 'アーキテクチャ資料を見る',
                },
                exploreLabel: 'モジュールを見る',
                items: [
                    { label: 'Macro', desc: 'Jupiter の GUI 操作を自動記録し、スクリプト化します。' },
                    { label: 'PSJ-Command', desc: 'Jupiter のあらゆるダイアログ機能をコマンド言語で再現します。' },
                    { label: 'PSJ-Utility', desc: 'モデルデータベース（ID、名前、色、ジオメトリ）を照会します。' },
                    { label: 'PSJ-GUI', desc: 'コード不要のビジュアル GUI コマンドビルダー。' },
                    { label: 'Custom Shell', desc: 'リアルタイムのエラー出力を備えた対話型デバッグシェル。' },
                    { label: 'Custom IDE', desc: 'オートコンプリートと予測チップを備えたスマート IDE。' },
                ] as { label: string; desc: string }[],
            },
            industries: {
                header: {
                    label: '対象業界',
                    title: 'さまざまな分野のCAEチームを支援',
                    desc: '自動車の衝突解析から海洋流体力学まで、PSJは業界ごとのシミュレーションパイプラインに柔軟に対応します。',
                },
            },
        },

        // ── Showcase page ─────────────────────────────────────────────────────
        showcase: {
            header: {
                label: 'テクニカルショーケース',
                title: 'ショーケースカタログ',
                desc: '業界をリードする組織のために開発された、プロダクションレベルの CAE 自動化ソリューションと専門的なエンジニアリングサービスをご覧ください。',
            },
            search: {
                byCode: 'コードまたはタイトルで検索...',
                updates: '更新履歴を検索',
            },
            filters: {
                industryPrefix: '業界:',
                sortPrefix: '並べ替え:',
                sortByRelevant: '関連度順',
                sortByCode: 'ソリューションコード',
                sortByComplexity: '難易度順',
                filterSolutions: 'ソリューションを絞り込む',
            },
            results: {
                showing: '{count} / {total} 件の結果を表示中',
                clearFilters: 'すべてのフィルターを解除',
                noSolutions: '条件に一致する解決策が見つかりませんでした',
                resetFilters: 'フィルターをリセット',
            },
            card: {
                details: '詳細を見る',
                requestConsultation: '相談を依頼する',
                capabilities: '機能・特徴',
                deliverables: '成果物',
                duration: '期間',
                complexity: '難易度',
                industry: '業界',
                software: '使用ソフトウェア:',
            },
            cta: {
                subtitle: 'カスタムエンジニアリング',
                title: 'お探しのものが見つかりませんか？',
                desc: '当社のチームは、お客様固有のエンジニアリング課題に合わせたカスタム CAE 自動化パイプラインの構築を専門としています。',
                primaryLabel: '見積もりを依頼する',
                secondaryLabel: '相談を予約する',
            },
        },

        // ── Changelog page ────────────────────────────────────────────────────
        changelog: {
            nav: {
                home: 'ホーム',
                backToChangelog: '更新履歴一覧に戻る',
            },
            header: {
                label: 'プラットフォームの更新',
                title: 'プロダクト更新履歴',
                desc: 'PSJエンジニアリング自動化プラットフォームの最新機能、パフォーマンス向上、技術的なアップデートをご確認いただけます。',
            },
            sidebar: {
                allVersions: '全バージョン',
            },
            search: {
                placeholder: '更新履歴を検索...',
                searchUpdates: '更新履歴を検索',
                find: '検索...',
            },
            filters: {
                filterByVersion: 'バージョンで絞り込む',
                filterByTag: 'タグで絞り込む',
                filterByDate: '日付で絞り込む',
                sortBy: '並べ替え',
                sortByDate: '日付順',
                sortByVersion: 'バージョン順',
                allTags: 'すべてのタグ',
                categories: 'カテゴリー',
                all: 'すべて',
                clearFilters: 'すべてのフィルターをクリア',
            },
            results: {
                showing: '{count} / {total} 件の更新を表示中',
                noUpdates: '条件に一致する更新履歴が見つかりませんでした',
                noResults: '結果が見つかりませんでした',
            },
            badges: {
                feature: '機能追加',
                fix: 'バグ修正',
                breaking: '破壊的変更',
                maintenance: 'メンテナンス',
                deprecated: '非推奨',
                preview: 'プレビュー',
                legacy: 'レガシー',
                release: 'リリース',
            },
            entry: {
                moreUpdates: '件の追加更新',
                releaseNote: 'リリースノート',
                defaultTitle: 'アップデート',
                copyLink: 'リンクをコピー',
                readDetails: '詳細を見る',
                highlights: '主要なアップデート',
                releaseDetails: '更新内容の詳細',
                missingVersion: 'バージョン情報なし',
            },
        },
    },
} as const;

/**
 * Utility type to recursively widen literal string types to `string`
 * while preserving structure (objects and arrays/tuples).
 */
type DeepString<T> = T extends string
    ? string
    : T extends (infer U)[]
      ? T extends [infer _A, infer _B] // Handle [string, string] specifically
          ? [string, string]
          : DeepString<U>[]
      : T extends object
        ? { [K in keyof T]: DeepString<T[K]> }
        : T;

export type TranslationDict = DeepString<typeof translations.en>;
export type SupportedLanguage = keyof typeof translations;
