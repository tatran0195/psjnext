import { Activity, Cog, Cpu, FileText, Layers, TrendingUp, Zap } from 'lucide-react';

export interface Solution {
    id: string;
    code: string;
    category: 'Fatigue' | 'AI' | 'Automation' | 'Reporting' | 'CFD' | 'Optimization';
    industry: string[];
    title: string;
    shortDesc: string;
    fullDesc: string;
    image: string;
    capabilities: string[];
    deliverables: string[];
    software: string[];
    duration: string;
    complexity: 'Standard' | 'Advanced' | 'Enterprise';
}

export const categoryConfig = {
    All: { color: '#0047AB', icon: Layers },
    Fatigue: { color: '#D4570D', icon: Activity },
    AI: { color: '#5B3BB8', icon: Cpu },
    Automation: { color: '#0047AB', icon: Cog },
    Reporting: { color: '#00875A', icon: FileText },
    CFD: { color: '#0099CC', icon: Zap },
    Optimization: { color: '#B86E00', icon: TrendingUp },
};

export const industriesByLang = {
    en: [
        'All Industries',
        'Automotive',
        'Aerospace',
        'Marine',
        'Energy',
        'Materials',
        'Heavy Machinery',
        'Manufacturing',
        'Research',
    ],
    ja: [
        'すべての業界',
        '自動車',
        '航空宇宙',
        '海洋',
        'エネルギー',
        '材料',
        '重機',
        '製造',
        '研究',
    ],
};

const solutionsEn: Solution[] = [
    {
        id: '01',
        code: 'PSJ-FAT-001',
        category: 'Fatigue',
        industry: ['Automotive', 'Heavy Machinery'],
        title: 'Shaft Fatigue Modeling Service',
        shortDesc: 'Excel-driven shaft parameter automation with full fatigue analysis pipeline.',
        fullDesc:
            'Custom Excel-based input system that automatically collects shaft geometry parameters and operating conditions. The system integrates with Jupiter and SunShine solvers to perform comprehensive fatigue lifecycle analysis with automated reporting.',
        image: '/showcase/fatigue.jpg',
        capabilities: [
            'Parametric geometry generation',
            'Multi-axial fatigue analysis',
            'S-N curve evaluation',
            'Damage accumulation',
        ],
        deliverables: [
            'Excel workbook',
            'Python automation scripts',
            'PDF/PPT reports',
            'Training materials',
        ],
        software: ['Jupiter', 'SunShine', 'MS Excel'],
        duration: '4-6 weeks',
        complexity: 'Standard',
    },
    {
        id: '02',
        code: 'PSJ-MBD-002',
        category: 'Fatigue',
        industry: ['Automotive'],
        title: 'Exhaust System MBD Automation',
        shortDesc: 'End-to-end multi-body dynamics fatigue analysis for exhaust systems.',
        fullDesc:
            'Complete automation pipeline from thermal stress analysis through modal decomposition and RFI (Random Frequency Input) analysis for exhaust system durability assessment.',
        image: '/images/workflow-dark.jpg',
        capabilities: [
            'Thermal stress mapping',
            'Modal analysis',
            'RFI evaluation',
            'Lifecycle prediction',
        ],
        deliverables: ['Automation framework', 'Analysis templates', 'Validation reports'],
        software: ['Jupiter', 'PSJ', 'SunShine'],
        duration: '6-8 weeks',
        complexity: 'Advanced',
    },
    {
        id: '03',
        code: 'PSJ-RPT-003',
        category: 'Reporting',
        industry: ['All Industries'],
        title: 'Automated PowerPoint Reporting',
        shortDesc: 'One-click export of analysis results to professional PowerPoint reports.',
        fullDesc:
            'Custom reporting system that automatically generates branded PowerPoint presentations including 3D visualizations, stress contour plots, animations, and quantitative result tables.',
        image: '/images/product-ui.jpg',
        capabilities: [
            'Template-driven reports',
            '3D visualization export',
            'Chart generation',
            'Multi-language support',
        ],
        deliverables: ['PPT templates', 'Python report engine', 'Documentation'],
        software: ['PSJ', 'MS PowerPoint'],
        duration: '3-4 weeks',
        complexity: 'Standard',
    },
    {
        id: '04',
        code: 'PSJ-AI-004',
        category: 'AI',
        industry: ['Marine', 'Aerospace'],
        title: 'AI-Powered Smart Dialog System',
        shortDesc: 'Machine learning system that predicts and pre-fills analysis parameters.',
        fullDesc:
            'Intelligent dialog system that learns from user operations and automatically populates parameters based on historical workflows. Reduces operation time by up to 60% for repetitive analysis tasks.',
        image: '/images/gui-builder.jpg',
        capabilities: [
            'Pattern recognition',
            'Parameter prediction',
            'User behavior learning',
            'Adaptive UI',
        ],
        deliverables: ['ML model', 'Integration plugin', 'Training dataset'],
        software: ['PSJ', 'Python ML stack'],
        duration: '8-12 weeks',
        complexity: 'Enterprise',
    },
    {
        id: '05',
        code: 'PSJ-AI-005',
        category: 'AI',
        industry: ['Marine'],
        title: 'Generative Ship Hull Design',
        shortDesc: 'Parametric morphing engine for AI training dataset generation.',
        fullDesc:
            'Automated ship hull variant generator that produces thousands of geometric variations for training neural networks in hydrodynamic prediction and design optimization.',
        image: '/showcase/ai-ship.jpg',
        capabilities: [
            'Parametric morphing',
            'Batch generation',
            'Quality validation',
            'Dataset curation',
        ],
        deliverables: ['Generation pipeline', 'Validated dataset', 'Quality metrics'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-10 weeks',
        complexity: 'Advanced',
    },
    {
        id: '06',
        code: 'PSJ-AUT-006',
        category: 'Automation',
        industry: ['Materials', 'Research'],
        title: 'Voronoi Microstructure Generation',
        shortDesc: 'Automated polycrystalline microstructure modeling for metal analysis.',
        fullDesc:
            'Production-grade Voronoi tessellation engine for generating realistic metal microstructures. Used for crystal plasticity simulations and grain-level material behavior studies.',
        image: '/images/cae-model.jpg',
        capabilities: [
            'Voronoi tessellation',
            'Grain boundary modeling',
            'Crystal orientation',
            'Multi-scale coupling',
        ],
        deliverables: ['Generation tools', 'Mesh templates', 'Validation cases'],
        software: ['PSJ', 'Jupiter'],
        duration: '5-7 weeks',
        complexity: 'Advanced',
    },
    {
        id: '07',
        code: 'PSJ-CFD-007',
        category: 'CFD',
        industry: ['Energy', 'Manufacturing'],
        title: 'SunShine + OpenFOAM Coupling',
        shortDesc: 'Multi-physics coupling between thermal solver and CFD analysis.',
        fullDesc:
            'Bidirectional coupling system between OpenFOAM CFD solver and SunShine for iterative heat-flow and structural analysis until convergence. Enables true multi-physics simulations.',
        image: '/images/cae-analysis.jpg',
        capabilities: [
            'Solver coupling',
            'Iterative convergence',
            'Data interpolation',
            'Convergence monitoring',
        ],
        deliverables: ['Coupling interface', 'Workflow templates', 'Convergence tools'],
        software: ['OpenFOAM', 'SunShine', 'PSJ'],
        duration: '10-14 weeks',
        complexity: 'Enterprise',
    },
    {
        id: '08',
        code: 'PSJ-CFD-008',
        category: 'CFD',
        industry: ['Energy'],
        title: 'OpenFOAM Block Mesh Generation',
        shortDesc: 'Specialized structured mesh generation for high-fidelity CFD.',
        fullDesc:
            'Custom block mesh generator using OpenFOAM utilities for creating high-quality structured meshes optimized for specific CFD analysis requirements.',
        image: '/images/hero-mesh.jpg',
        capabilities: [
            'Structured meshing',
            'Quality control',
            'Boundary layer refinement',
            'Domain decomposition',
            'Mesh quality metrics',
        ],
        deliverables: ['Mesh generation scripts', 'Quality reports', 'Simulation templates'],
        software: ['OpenFOAM', 'PSJ'],
        duration: '4-6 weeks',
        complexity: 'Standard',
    },
    {
        id: '09',
        code: 'PSJ-AUT-009',
        category: 'Automation',
        industry: ['All Industries'],
        title: 'Automatic FE Model Generation',
        shortDesc: 'End-to-end FE model setup including mesh, BC, and materials.',
        fullDesc:
            'Complete automation of finite element model preparation including geometry meshing, boundary condition application, material assignment, and load case definition.',
        image: '/images/psj-workspace.jpg',
        capabilities: ['Auto-meshing', 'BC application', 'Material library', 'Quality validation'],
        deliverables: ['Automation scripts', 'Material library', 'Project templates'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-8 weeks',
        complexity: 'Advanced',
    },
];

const solutionsJa: Solution[] = [
    {
        id: '01',
        code: 'PSJ-FAT-001',
        category: 'Fatigue',
        industry: ['自動車', '重機'],
        title: 'シャフト疲労モデリングサービス',
        shortDesc: 'Excel駆動のシャフトパラメータ自動化と完全な疲労解析パイプライン。',
        fullDesc:
            'シャフトのジオメトリパラメータと動作条件を自動的に収集するカスタムExcelベースの入力システム。システムはJupiterおよびSunShineソルバーと統合され、自動レポート機能を備えた包括的な疲労ライフサイクル解析を実行します。',
        image: '/showcase/fatigue.jpg',
        capabilities: [
            'パラメータ化されたジオメトリ生成',
            '多軸疲労解析',
            'S-N曲線評価',
            '損傷蓄積解析',
        ],
        deliverables: [
            'Excel ワークブック',
            'Python 自動化スクリプト',
            'PDF/PPT レポート',
            'トレーニング資料',
        ],
        software: ['Jupiter', 'SunShine', 'MS Excel'],
        duration: '4-6 週間',
        complexity: 'Standard',
    },
    {
        id: '02',
        code: 'PSJ-MBD-002',
        category: 'Fatigue',
        industry: ['自動車'],
        title: '排気システム MBD 自動化',
        shortDesc: '排気システムのエンドツーエンドのマルチボディダイナミクス疲労解析。',
        fullDesc:
            '熱応力解析から固有概念分解、排気システムの耐久性評価のためのRFI（ランダム周波数入力）解析までの完全な自動化パイプライン。',
        image: '/images/workflow-dark.jpg',
        capabilities: ['熱応力マッピング', '固有値解析', 'RFI 評価', 'ライフサイクル予測'],
        deliverables: ['自動化フレームワーク', '解析テンプレート', '検証レポート'],
        software: ['Jupiter', 'PSJ', 'SunShine'],
        duration: '6-8 週間',
        complexity: 'Advanced',
    },
    {
        id: '03',
        code: 'PSJ-RPT-003',
        category: 'Reporting',
        industry: ['すべての業界'],
        title: 'PowerPoint レポート自動生成',
        shortDesc:
            '解析結果をプロフェッショナルな PowerPoint レポートにワンクリックでエクスポート。',
        fullDesc:
            '3Dビジュアライゼーション、応力コンター図、アニメーション、および定量的な結果テーブルを含む、ブランド化されたPowerPointプレゼンテーションを自動的に生成するカスタムレポートシステム。',
        image: '/images/product-ui.jpg',
        capabilities: [
            'テンプレート駆動のレポート',
            '3D ビジュアライゼーション・エクスポート',
            'チャート生成',
            '多言語サポート',
        ],
        deliverables: ['PPT テンプレート', 'Python レポートエンジン', 'ドキュメント'],
        software: ['PSJ', 'MS PowerPoint'],
        duration: '3-4 週間',
        complexity: 'Standard',
    },
    {
        id: '04',
        code: 'PSJ-AI-004',
        category: 'AI',
        industry: ['海洋', '航空宇宙'],
        title: 'AI 搭載スマートダイアログシステム',
        shortDesc: '解析パラメータを予測して事前入力する機械学習システム。',
        fullDesc:
            'ユーザーの操作から学習し、履歴ワークフローに基づいてパラメータを自動的に入力するインテリジェントなダイアログシステム。繰り返しの解析タスクの操作時間を最大 60% 短縮します。',
        image: '/images/gui-builder.jpg',
        capabilities: ['パターン認識', 'パラメータ予測', 'ユーザー行動学習', 'アダプティブ UI'],
        deliverables: ['ML モデル', '統合プラグイン', 'トレーニングデータセット'],
        software: ['PSJ', 'Python ML スタック'],
        duration: '8-12 週間',
        complexity: 'Enterprise',
    },
    {
        id: '05',
        code: 'PSJ-AI-005',
        category: 'AI',
        industry: ['海洋'],
        title: '生成的な船体設計',
        shortDesc: 'AI トレーニングデータセット生成用のパラメトリックモーフィングエンジン。',
        fullDesc:
            '流体予測や設計最適化におけるニューラルネットワークのトレーニングのために、数千の幾何学的バリエーションを生成する自動船体バリアントジェネレーター。',
        image: '/showcase/ai-ship.jpg',
        capabilities: [
            'パラメトリックモーフィング',
            'バッチ生成',
            '品質検証',
            'データセットキュレーション',
        ],
        deliverables: ['生成パイプライン', '検証済みデータセット', '品質メトリクス'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-10 週間',
        complexity: 'Advanced',
    },
    {
        id: '06',
        code: 'PSJ-AUT-006',
        category: 'Automation',
        industry: ['材料', '研究'],
        title: 'ボロノイ微細構造生成',
        shortDesc: '金属解析のための多結晶微細構造モデリングの自動化。',
        fullDesc:
            '現実的な金属の微細構造を生成するためのプロダクションレベルのボロノイ分割エンジン。結晶塑性シミュレーションや粒レベルの材料挙動の研究に使用されます。',
        image: '/images/cae-model.jpg',
        capabilities: [
            'ボロノイ分割',
            '粒界モデリング',
            '結晶方位設定',
            'マルチスケールカップリング',
        ],
        deliverables: ['生成ツール', 'メッシュテンプレート', '検証ケース'],
        software: ['PSJ', 'Jupiter'],
        duration: '5-7 週間',
        complexity: 'Advanced',
    },
    {
        id: '07',
        code: 'PSJ-CFD-007',
        category: 'CFD',
        industry: ['エネルギー', '製造'],
        title: 'SunShine + OpenFOAM カップリング',
        shortDesc: '熱ソルバーと CFD 解析の間のマルチフィジックスカップリング。',
        fullDesc:
            '収束するまで熱流と構造解析を繰り返すための、OpenFOAM CFD ソルバーと SunShine の間の双方向カップリングシステム。真のマルチフィジックスシミュレーションを可能にします。',
        image: '/images/cae-analysis.jpg',
        capabilities: ['ソルバーカップリング', '反復収束制御', 'データ補間', '収束モニタリング'],
        deliverables: ['カップリングインターフェース', 'ワークフローテンプレート', '収束ツール'],
        software: ['OpenFOAM', 'SunShine', 'PSJ'],
        duration: '10-14 週間',
        complexity: 'Enterprise',
    },
    {
        id: '08',
        code: 'PSJ-CFD-008',
        category: 'CFD',
        industry: ['エネルギー'],
        title: 'OpenFOAM ブロックメッシュ生成',
        shortDesc: '高忠実度 CFD 用の特殊な構造化メッシュ生成。',
        fullDesc:
            '特定の CFD 解析要件に最適化された高品質の構造化メッシュを作成するための、OpenFOAM ユーティリティを使用したカスタムブロックメッシュジェネレーター。',
        image: '/images/hero-mesh.jpg',
        capabilities: [
            '構造化メッシング',
            '品質管理',
            '境界層リファインメント',
            '領域分割',
            'メッシュ品質メトリクス',
        ],
        deliverables: ['メッシュ生成スクリプト', '品質レポート', 'シミュレーションテンプレート'],
        software: ['OpenFOAM', 'PSJ'],
        duration: '4-6 週間',
        complexity: 'Standard',
    },
    {
        id: '09',
        code: 'PSJ-AUT-009',
        category: 'Automation',
        industry: ['すべての業界'],
        title: '自動 FE モデル生成',
        shortDesc: 'メッシュ、境界条件、材料を含むエンドツーエンドの FE モデル設定。',
        fullDesc:
            'ジオメトリメッシング、境界条件の適用、材料の割り当て、およびロードケース定義を含む、有限要素モデル準備の完全な自動化。',
        image: '/images/psj-workspace.jpg',
        capabilities: ['自動メッシング', '境界条件適用', '材料ライブラリ', '品質検証'],
        deliverables: ['自動化スクリプト', '材料ライブラリ', 'プロジェクトテンプレート'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-8 週間',
        complexity: 'Advanced',
    },
];

export function getSolutions(lang: string): Solution[] {
    return lang === 'ja' ? solutionsJa : solutionsEn;
}

export function getIndustries(lang: string): string[] {
    return industriesByLang[lang as keyof typeof industriesByLang] || industriesByLang.en;
}
