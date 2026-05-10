'use client';
import { useMemo, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import {
    Activity,
    ArrowRight,
    Atom,
    Award,
    Box,
    Briefcase,
    Building2,
    Car,
    CheckCircle2,
    Clock,
    Cog,
    Cpu,
    Download,
    ExternalLink,
    Factory,
    FileText,
    Layers,
    Phone,
    Plane,
    Search,
    Settings,
    Ship,
    TrendingUp,
    Users,
    X,
    Zap,
} from 'lucide-react';

interface Solution {
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

const solutions: Solution[] = [
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
        ],
        deliverables: ['Mesh generation scripts', 'Quality reports'],
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
        deliverables: ['Automation scripts', 'Material library', 'Templates'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-8 weeks',
        complexity: 'Advanced',
    },
];

const categoryConfig = {
    All: { color: '#0047AB', icon: Layers },
    Fatigue: { color: '#D4570D', icon: Activity },
    AI: { color: '#5B3BB8', icon: Cpu },
    Automation: { color: '#0047AB', icon: Cog },
    Reporting: { color: '#00875A', icon: FileText },
    CFD: { color: '#0099CC', icon: Zap },
    Optimization: { color: '#B86E00', icon: TrendingUp },
};

const industries = [
    'All Industries',
    'Automotive',
    'Aerospace',
    'Marine',
    'Energy',
    'Materials',
    'Heavy Machinery',
    'Manufacturing',
    'Research',
];

export default function CAEServices() {
    const [activeCategory, setActiveCategory] = useState<keyof typeof categoryConfig>('All');
    const [activeIndustry, setActiveIndustry] = useState('All Industries');
    const [search, setSearch] = useState('');
    const [selectedSolution, setSelectedSolution] = useState<Solution | null>(null);
    const [mobileFiltersOpen, setMobileFiltersOpen] = useState(false);

    const filtered = useMemo(() => {
        return solutions.filter((s) => {
            const matchCat = activeCategory === 'All' || s.category === activeCategory;
            const matchInd =
                activeIndustry === 'All Industries' ||
                s.industry.includes(activeIndustry) ||
                s.industry.includes('All Industries');
            const matchSearch =
                !search ||
                s.title.toLowerCase().includes(search.toLowerCase()) ||
                s.shortDesc.toLowerCase().includes(search.toLowerCase()) ||
                s.code.toLowerCase().includes(search.toLowerCase());
            return matchCat && matchInd && matchSearch;
        });
    }, [activeCategory, activeIndustry, search]);

    return (
        <div
            style={{
                background: 'var(--psj-surface-0)',
                color: 'var(--psj-text-1)',
                minHeight: '100vh',
            }}
        >
            {/* layout provides header */}
            <section style={{ borderBottom: '1px solid var(--psj-border)' }}>
                <div className="psj-container py-12 lg:py-16">
                    <div className="grid lg:grid-cols-12 gap-8 items-end">
                        <div className="lg:col-span-8">
                            <div className="psj-label mb-3">Engineering Services Catalog</div>
                            <h1 className="psj-h1 mb-5" style={{ color: 'var(--psj-text-1)' }}>
                                CAE Solutions &<br />
                                Engineering Services
                            </h1>
                            <p
                                className="text-base leading-relaxed max-w-2xl"
                                style={{ color: 'var(--psj-text-2)' }}
                            >
                                A comprehensive catalog of production-grade CAE automation services
                                delivered to leading manufacturers worldwide. Each solution is
                                engineered, validated, and supported by our team.
                            </p>
                            <div className="mt-8 flex flex-wrap gap-3">
                                <a href="#catalog" className="psj-btn-primary">
                                    Browse Catalog <ArrowRight size={14} />
                                </a>
                                <a href="#" className="psj-btn-secondary">
                                    <Download size={14} /> Download Brochure
                                </a>
                            </div>
                        </div>
                        <div className="lg:col-span-4">
                            <div
                                className="grid grid-cols-2"
                                style={{ border: '1px solid var(--psj-border)' }}
                            >
                                <Stat
                                    icon={<Briefcase size={14} />}
                                    label="Solutions"
                                    value={String(solutions.length)}
                                />
                                <Stat icon={<Building2 size={14} />} label="Clients" value="120+" />
                                <Stat icon={<Award size={14} />} label="Years" value="15+" />
                                <Stat icon={<Users size={14} />} label="Engineers" value="40+" />
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ─────── INDUSTRY BAR ─────── */}
            <section
                style={{
                    background: 'var(--psj-surface-1)',
                    borderBottom: '1px solid var(--psj-border)',
                }}
            >
                <div className="psj-container py-4">
                    <div className="flex items-center gap-8">
                        <span
                            className="text-[10px] uppercase tracking-widest font-bold whitespace-nowrap"
                            style={{ color: 'var(--psj-text-3)' }}
                        >
                            Trusted by
                        </span>
                        <div className="flex items-center gap-8 flex-wrap">
                            {[
                                { icon: Car, name: 'Automotive' },
                                { icon: Plane, name: 'Aerospace' },
                                { icon: Ship, name: 'Marine' },
                                { icon: Factory, name: 'Manufacturing' },
                                { icon: Atom, name: 'Energy' },
                            ].map((I) => (
                                <div
                                    key={I.name}
                                    className="flex items-center gap-2"
                                    style={{ color: 'var(--psj-text-3)' }}
                                >
                                    <I.icon size={16} />
                                    <span className="text-sm font-medium">{I.name}</span>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </section>

            {/* ─────── MAIN LAYOUT ─────── */}
            <main id="catalog" className="psj-container py-10">
                <div className="grid lg:grid-cols-12 gap-10">
                    {/* ── SIDEBAR ── */}
                    <aside
                        className="hidden lg:block lg:col-span-3 sticky self-start space-y-7"
                        style={{ top: '80px' }}
                    >
                        {/* Search */}
                        <div>
                            <label
                                className="text-[10px] uppercase tracking-widest font-bold mb-2 block"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                Search
                            </label>
                            <div
                                className="flex items-center gap-2 px-3 py-2.5"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                <Search size={13} style={{ color: 'var(--psj-text-3)' }} />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder="Solution code, name..."
                                    className="bg-transparent text-sm outline-none flex-1"
                                    style={{ color: 'var(--psj-text-1)' }}
                                />
                            </div>
                        </div>

                        {/* Categories */}
                        <div>
                            <label
                                className="text-[10px] uppercase tracking-widest font-bold mb-2 block"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                Service Category
                            </label>
                            <div className="space-y-0.5">
                                {(
                                    Object.keys(categoryConfig) as Array<
                                        keyof typeof categoryConfig
                                    >
                                ).map((cat) => {
                                    const config = categoryConfig[cat];
                                    const Icon = config.icon;
                                    const count =
                                        cat === 'All'
                                            ? solutions.length
                                            : solutions.filter((s) => s.category === cat).length;
                                    const active = activeCategory === cat;
                                    return (
                                        <button
                                            key={cat}
                                            onClick={() => setActiveCategory(cat)}
                                            className="w-full flex items-center justify-between px-3 py-2.5 text-sm transition-colors"
                                            style={{
                                                background: active
                                                    ? 'var(--psj-blue-subtle)'
                                                    : 'transparent',
                                                borderLeft: `2px solid ${active ? 'var(--psj-blue)' : 'transparent'}`,
                                                color: active
                                                    ? 'var(--psj-blue)'
                                                    : 'var(--psj-text-2)',
                                                fontWeight: active ? 600 : 400,
                                            }}
                                        >
                                            <span className="flex items-center gap-2.5">
                                                <Icon
                                                    size={13}
                                                    style={{
                                                        color: active
                                                            ? config.color
                                                            : 'var(--psj-text-3)',
                                                    }}
                                                />
                                                {cat}
                                            </span>
                                            <span
                                                className="text-xs num-marker"
                                                style={{ color: 'var(--psj-text-3)' }}
                                            >
                                                {count}
                                            </span>
                                        </button>
                                    );
                                })}
                            </div>
                        </div>

                        {/* Industries */}
                        <div>
                            <label
                                className="text-[10px] uppercase tracking-widest font-bold mb-2 block"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                Industry
                            </label>
                            <select
                                value={activeIndustry}
                                onChange={(e) => setActiveIndustry(e.target.value)}
                                className="w-full px-3 py-2.5 text-sm outline-none"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                    color: 'var(--psj-text-1)',
                                }}
                            >
                                {industries.map((i) => (
                                    <option key={i}>{i}</option>
                                ))}
                            </select>
                        </div>

                        {/* Help box */}
                        <div
                            className="p-5"
                            style={{
                                border: '1px solid var(--psj-border)',
                                background: 'var(--psj-surface-1)',
                            }}
                        >
                            <div className="psj-label mb-2">Need Help?</div>
                            <h4
                                className="text-sm font-bold mb-2"
                                style={{ color: 'var(--psj-text-1)' }}
                            >
                                Speak with a CAE specialist
                            </h4>
                            <p
                                className="text-xs leading-relaxed mb-4"
                                style={{ color: 'var(--psj-text-2)' }}
                            >
                                Our engineers can help you select the right solution.
                            </p>
                            <a
                                href="#"
                                className="text-xs font-bold flex items-center gap-1"
                                style={{ color: 'var(--psj-blue)' }}
                            >
                                Schedule a call <ArrowRight size={11} />
                            </a>
                        </div>
                        {/* Resources */}
                        <div>
                            <label
                                className="text-[10px] uppercase tracking-widest font-bold mb-2 block"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                Resources
                            </label>
                            <div className="space-y-2">
                                {[
                                    { icon: FileText, label: 'Capability statement' },
                                    { icon: Download, label: 'Service catalog (PDF)' },
                                    { icon: ExternalLink, label: 'Case studies' },
                                ].map((r) => (
                                    <a
                                        key={r.label}
                                        href="#"
                                        className="flex items-center gap-2 text-xs transition-colors"
                                        style={{ color: 'var(--psj-text-2)' }}
                                    >
                                        <r.icon size={12} /> {r.label}
                                    </a>
                                ))}
                            </div>
                        </div>
                    </aside>

                    {/* ── MAIN CONTENT ── */}
                    <div className="lg:col-span-9">
                        {/* Toolbar */}
                        <div
                            className="flex flex-wrap items-center justify-between gap-4 mb-6 pb-5"
                            style={{ borderBottom: '1px solid var(--psj-border)' }}
                        >
                            <div className="text-sm">
                                <span
                                    className="font-bold num-marker"
                                    style={{ color: 'var(--psj-text-1)' }}
                                >
                                    {filtered.length}
                                </span>
                                <span style={{ color: 'var(--psj-text-2)' }}>
                                    {' '}
                                    of {solutions.length} solutions
                                </span>
                                {activeCategory !== 'All' && (
                                    <span style={{ color: 'var(--psj-text-3)' }}>
                                        {' '}
                                        · {activeCategory}
                                    </span>
                                )}
                                {activeIndustry !== 'All Industries' && (
                                    <span style={{ color: 'var(--psj-text-3)' }}>
                                        {' '}
                                        · {activeIndustry}
                                    </span>
                                )}
                            </div>
                            <select
                                className="px-3 py-1.5 text-xs outline-none"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                    color: 'var(--psj-text-1)',
                                }}
                            >
                                <option>Most relevant</option>
                                <option>Latest released</option>
                                <option>Solution code</option>
                            </select>
                        </div>

                        {/* Solutions list */}
                        <AnimatePresence mode="popLayout">
                            {filtered.length === 0 ? (
                                <motion.div
                                    key="empty"
                                    initial={{ opacity: 0 }}
                                    animate={{ opacity: 1 }}
                                    exit={{ opacity: 0 }}
                                    className="py-32 text-center"
                                    style={{ border: '1px dashed var(--psj-border)' }}
                                >
                                    <Search
                                        size={28}
                                        className="mx-auto mb-4"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    />
                                    <p className="text-sm" style={{ color: 'var(--psj-text-2)' }}>
                                        No solutions match your criteria
                                    </p>
                                    <button
                                        onClick={() => {
                                            setActiveCategory('All');
                                            setActiveIndustry('All Industries');
                                            setSearch('');
                                        }}
                                        className="mt-4 text-sm font-bold"
                                        style={{ color: 'var(--psj-blue)' }}
                                    >
                                        Reset filters
                                    </button>
                                </motion.div>
                            ) : (
                                <div className="space-y-3">
                                    {filtered.map((sol, i) => (
                                        <motion.div
                                            key={sol.id}
                                            layout
                                            initial={{ opacity: 0, y: 10 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            exit={{ opacity: 0 }}
                                            transition={{ duration: 0.3, delay: i * 0.04 }}
                                        >
                                            <SolutionCard
                                                sol={sol}
                                                onSelect={setSelectedSolution}
                                            />
                                        </motion.div>
                                    ))}
                                </div>
                            )}
                        </AnimatePresence>
                    </div>
                </div>
            </main>

            {/* ─────── BOTTOM CTA ─────── */}
            <section
                style={{ background: 'var(--psj-blue)', borderTop: '1px solid var(--psj-border)' }}
            >
                <div className="psj-container py-16">
                    <div className="grid md:grid-cols-2 gap-10 items-center">
                        <div>
                            <div
                                className="text-[10px] uppercase tracking-[0.25em] font-bold mb-3"
                                style={{ color: 'rgba(255,255,255,0.6)' }}
                            >
                                Custom Engineering
                            </div>
                            <h2 className="psj-h2 text-white mb-4 text-balance">
                                Don&apos;t see what you need?
                            </h2>
                            <p
                                className="leading-relaxed"
                                style={{ color: 'rgba(255,255,255,0.7)' }}
                            >
                                Our team specializes in custom CAE automation pipelines tailored to
                                your specific engineering challenges.
                            </p>
                        </div>
                        <div className="flex flex-col sm:flex-row gap-3 md:justify-end">
                            <a
                                href="#"
                                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 text-sm font-bold"
                                style={{ background: '#FFFFFF', color: 'var(--psj-blue)' }}
                            >
                                Request a quote <ArrowRight size={14} />
                            </a>
                            <a
                                href="#"
                                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 text-sm font-bold text-white"
                                style={{ border: '1px solid rgba(255,255,255,0.35)' }}
                            >
                                <Phone size={14} /> Schedule a call
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            {/* Layout provides footer */}

            {/* ─────── DETAIL MODAL ─────── */}
            <AnimatePresence>
                {selectedSolution && (
                    <DetailModal sol={selectedSolution} onClose={() => setSelectedSolution(null)} />
                )}
            </AnimatePresence>

            {/* ─────── MOBILE FILTERS DRAWER ─────── */}
            <AnimatePresence>
                {mobileFiltersOpen && (
                    <>
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="lg:hidden fixed inset-0 bg-black/50 z-50"
                            onClick={() => setMobileFiltersOpen(false)}
                        />
                        <motion.div
                            initial={{ x: '100%' }}
                            animate={{ x: 0 }}
                            exit={{ x: '100%' }}
                            transition={{ type: 'spring', damping: 30 }}
                            className="lg:hidden fixed top-0 right-0 h-full w-80 bg-bg z-50 overflow-y-auto"
                        >
                            <div className="p-6">
                                <button
                                    onClick={() => setMobileFiltersOpen(false)}
                                    className="mb-6"
                                >
                                    <X size={20} />
                                </button>
                                <h3 className="text-lg font-bold mb-4">Filter Solutions</h3>
                                {(
                                    Object.keys(categoryConfig) as Array<
                                        keyof typeof categoryConfig
                                    >
                                ).map((cat) => (
                                    <button
                                        key={cat}
                                        onClick={() => {
                                            setActiveCategory(cat);
                                            setMobileFiltersOpen(false);
                                        }}
                                        className={`w-full text-left px-3 py-2.5 text-sm ${
                                            activeCategory === cat
                                                ? 'bg-bg-elevated text-blue font-bold'
                                                : 'text-text-secondary'
                                        }`}
                                    >
                                        {cat}
                                    </button>
                                ))}
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </div>
    );
}

/* ─── Stat tile ─── */
function Stat({ icon, label, value }: { icon: React.ReactNode; label: string; value: string }) {
    return (
        <div
            className="p-5"
            style={{
                background: 'var(--psj-surface-0)',
                borderRight: '1px solid var(--psj-border)',
                borderBottom: '1px solid var(--psj-border)',
            }}
        >
            <div className="flex items-center gap-2 mb-2" style={{ color: 'var(--psj-text-3)' }}>
                {icon}
                <span className="text-[10px] uppercase tracking-widest font-bold">{label}</span>
            </div>
            <div
                className="text-2xl font-extrabold num-marker tracking-tighter"
                style={{ color: 'var(--psj-text-1)' }}
            >
                {value}
            </div>
        </div>
    );
}

/* ─── Solution Card (horizontal row) ─── */
function SolutionCard({ sol, onSelect }: { sol: Solution; onSelect: (s: Solution) => void }) {
    const config = categoryConfig[sol.category];
    return (
        <article className="psj-card group" style={{ borderLeft: `3px solid ${config.color}` }}>
            <div className="grid md:grid-cols-12">
                {/* Image */}
                <div
                    className="md:col-span-3 overflow-hidden"
                    style={{
                        background: 'var(--psj-surface-2)',
                        borderRight: '1px solid var(--psj-border)',
                    }}
                >
                    <div className="aspect-[4/3] md:aspect-auto md:h-full overflow-hidden">
                        <img
                            src={sol.image}
                            alt={sol.title}
                            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                        />
                    </div>
                </div>
                {/* Content */}
                <div
                    className="md:col-span-7 p-6 lg:p-7"
                    style={{ borderRight: '1px solid var(--psj-border)' }}
                >
                    <div className="flex items-center gap-3 mb-3">
                        <span
                            className="text-[10px] uppercase tracking-widest font-bold px-2 py-1 num-marker"
                            style={{ color: config.color, background: `${config.color}12` }}
                        >
                            {sol.code}
                        </span>
                        <span
                            className="text-[10px] uppercase tracking-widest font-medium flex items-center gap-1"
                            style={{ color: 'var(--psj-text-3)' }}
                        >
                            <config.icon size={11} /> {sol.category}
                        </span>
                        <span
                            className="text-[10px] uppercase tracking-widest border px-1.5 py-0.5 font-medium"
                            style={{ borderColor: 'var(--psj-border)', color: 'var(--psj-text-2)' }}
                        >
                            {sol.complexity}
                        </span>
                    </div>
                    <h3
                        className="text-lg font-bold leading-tight mb-2 transition-colors"
                        style={{ color: 'var(--psj-text-1)' }}
                    >
                        {sol.title}
                    </h3>
                    <p
                        className="text-sm leading-relaxed mb-4"
                        style={{ color: 'var(--psj-text-2)' }}
                    >
                        {sol.shortDesc}
                    </p>
                    <div className="grid grid-cols-2 gap-1.5 mb-4">
                        {sol.capabilities.slice(0, 4).map((c) => (
                            <div
                                key={c}
                                className="flex items-center gap-1.5 text-xs"
                                style={{ color: 'var(--psj-text-2)' }}
                            >
                                <CheckCircle2
                                    size={11}
                                    style={{ color: 'var(--psj-blue)', flexShrink: 0 }}
                                />
                                <span className="truncate">{c}</span>
                            </div>
                        ))}
                    </div>
                    <div
                        className="flex flex-wrap items-center gap-1.5 pt-3"
                        style={{ borderTop: '1px solid var(--psj-border)' }}
                    >
                        <span
                            className="text-[10px] uppercase tracking-widest font-bold mr-1"
                            style={{ color: 'var(--psj-text-3)' }}
                        >
                            Software:
                        </span>
                        {sol.software.map((s) => (
                            <span
                                key={s}
                                className="text-[10px] px-2 py-0.5 font-medium"
                                style={{
                                    background: 'var(--psj-surface-2)',
                                    color: 'var(--psj-text-2)',
                                }}
                            >
                                {s}
                            </span>
                        ))}
                    </div>
                </div>
                {/* Meta */}
                <div
                    className="md:col-span-2 p-5 flex flex-col justify-between"
                    style={{ background: 'var(--psj-surface-1)' }}
                >
                    <div className="space-y-4">
                        <div>
                            <div
                                className="text-[10px] uppercase tracking-widest font-bold mb-1"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                Duration
                            </div>
                            <div
                                className="text-sm font-bold flex items-center gap-1.5"
                                style={{ color: 'var(--psj-text-1)' }}
                            >
                                <Clock size={12} style={{ color: 'var(--psj-blue)' }} />{' '}
                                {sol.duration}
                            </div>
                        </div>
                        <div>
                            <div
                                className="text-[10px] uppercase tracking-widest font-bold mb-1"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                Industry
                            </div>
                            {sol.industry.slice(0, 2).map((i) => (
                                <div
                                    key={i}
                                    className="text-xs flex items-center gap-1"
                                    style={{ color: 'var(--psj-text-2)' }}
                                >
                                    <Building2 size={10} /> {i}
                                </div>
                            ))}
                        </div>
                    </div>
                    <div className="space-y-2 mt-4">
                        <button
                            onClick={() => onSelect(sol)}
                            className="psj-btn-primary w-full justify-center"
                            style={{ padding: '0.5rem' }}
                        >
                            Details <ArrowRight size={12} />
                        </button>
                        <button
                            className="psj-btn-secondary w-full justify-center"
                            style={{ padding: '0.5rem' }}
                        >
                            <FileText size={11} /> Datasheet
                        </button>
                    </div>
                </div>
            </div>
        </article>
    );
}

/* ─── Detail Modal ─── */
function DetailModal({ sol, onClose }: { sol: Solution; onClose: () => void }) {
    const config = categoryConfig[sol.category];
    return (
        <>
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="fixed inset-0 z-[60]"
                style={{ background: 'rgba(0,0,0,0.65)' }}
                onClick={onClose}
            />
            <motion.div
                initial={{ opacity: 0, scale: 0.97, y: 16 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                exit={{ opacity: 0, scale: 0.97, y: 16 }}
                transition={{ duration: 0.2 }}
                className="fixed inset-0 z-[70] flex items-center justify-center p-4 lg:p-10 pointer-events-none"
            >
                <div
                    className="max-w-5xl w-full max-h-[90vh] overflow-y-auto pointer-events-auto"
                    style={{
                        background: 'var(--psj-surface-0)',
                        border: '1px solid var(--psj-border)',
                    }}
                >
                    <div className="grid md:grid-cols-2">
                        <div style={{ background: 'var(--psj-surface-2)', minHeight: '240px' }}>
                            <img
                                src={sol.image}
                                alt={sol.title}
                                className="w-full h-full object-cover"
                            />
                        </div>
                        <div className="p-8">
                            <div className="flex items-center gap-2 mb-5">
                                <span
                                    className="text-[10px] uppercase tracking-widest font-bold px-2 py-1 num-marker"
                                    style={{ color: config.color, background: `${config.color}12` }}
                                >
                                    {sol.code}
                                </span>
                                <button
                                    onClick={onClose}
                                    className="ml-auto"
                                    style={{ color: 'var(--psj-text-3)' }}
                                >
                                    <X size={18} />
                                </button>
                            </div>
                            <h2 className="psj-h3 mb-3" style={{ color: 'var(--psj-text-1)' }}>
                                {sol.title}
                            </h2>
                            <p
                                className="leading-relaxed mb-6"
                                style={{ color: 'var(--psj-text-2)' }}
                            >
                                {sol.fullDesc}
                            </p>
                            <div className="space-y-5">
                                <div>
                                    <h4
                                        className="text-[10px] uppercase tracking-widest font-bold mb-2 flex items-center gap-1.5"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        <Settings size={12} /> Capabilities
                                    </h4>
                                    <ul className="space-y-1.5">
                                        {sol.capabilities.map((c) => (
                                            <li
                                                key={c}
                                                className="flex items-start gap-2 text-sm"
                                                style={{ color: 'var(--psj-text-2)' }}
                                            >
                                                <CheckCircle2
                                                    size={13}
                                                    style={{
                                                        color: 'var(--psj-blue)',
                                                        marginTop: '2px',
                                                        flexShrink: 0,
                                                    }}
                                                />{' '}
                                                {c}
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                                <div>
                                    <h4
                                        className="text-[10px] uppercase tracking-widest font-bold mb-2 flex items-center gap-1.5"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        <Box size={12} /> Deliverables
                                    </h4>
                                    <div className="flex flex-wrap gap-1.5">
                                        {sol.deliverables.map((d) => (
                                            <span
                                                key={d}
                                                className="text-xs px-2.5 py-1"
                                                style={{
                                                    border: '1px solid var(--psj-border)',
                                                    background: 'var(--psj-surface-1)',
                                                    color: 'var(--psj-text-2)',
                                                }}
                                            >
                                                {d}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                                <div
                                    className="grid grid-cols-2 gap-4 pt-4"
                                    style={{ borderTop: '1px solid var(--psj-border)' }}
                                >
                                    <div>
                                        <div
                                            className="text-[10px] uppercase tracking-widest font-bold mb-1"
                                            style={{ color: 'var(--psj-text-3)' }}
                                        >
                                            Duration
                                        </div>
                                        <div
                                            className="font-bold"
                                            style={{ color: 'var(--psj-text-1)' }}
                                        >
                                            {sol.duration}
                                        </div>
                                    </div>
                                    <div>
                                        <div
                                            className="text-[10px] uppercase tracking-widest font-bold mb-1"
                                            style={{ color: 'var(--psj-text-3)' }}
                                        >
                                            Complexity
                                        </div>
                                        <div
                                            className="font-bold"
                                            style={{ color: 'var(--psj-text-1)' }}
                                        >
                                            {sol.complexity}
                                        </div>
                                    </div>
                                </div>
                                <a href="#" className="psj-btn-primary w-full justify-center">
                                    Request Consultation
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </motion.div>
        </>
    );
}
