// oxlint-disable typescript/no-explicit-any
'use client';

import { useRef, useState, type ReactNode } from 'react';

import { AnimatePresence, motion, useInView as useFramerInView } from 'framer-motion';
import {
    Activity,
    ArrowRight,
    ArrowUpRight,
    Box,
    Brain,
    ChevronDown,
    Cpu,
    ExternalLink,
    FileText,
    Filter,
    Globe,
    Layers,
    LayoutGrid,
    Monitor,
    Moon,
    Play,
    Search,
    Settings,
    Sparkles,
    Sun,
    Zap,
} from 'lucide-react';

/* ── Reveal Animation ── */
function Reveal({
    children,
    delay = 0,
    className = '',
}: {
    children: ReactNode;
    delay?: number;
    className?: string;
}) {
    const ref = useRef<HTMLDivElement>(null);
    const inView = useFramerInView(ref, { once: true, margin: '-60px' });
    return (
        <motion.div
            ref={ref}
            initial={{ opacity: 0, y: 30 }}
            animate={inView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.6, delay: delay * 0.001, ease: [0.22, 1, 0.36, 1] }}
            className={className}
        >
            {children}
        </motion.div>
    );
}

/* ── Application Card ── */
function AppCard({ app, index }: { app: any; index: number }) {
    const Icon = app.icon;
    const [hovered, setHovered] = useState(false);

    return (
        <Reveal delay={index * 60}>
            <div
                className="group relative bg-[var(--card)] border border-[var(--border)] overflow-hidden transition-all duration-500 hover:border-accent/40 hover:shadow-2xl hover:shadow-accent/5"
                onMouseEnter={() => setHovered(true)}
                onMouseLeave={() => setHovered(false)}
            >
                {/* Image Area */}
                <div className="relative h-52 bg-[var(--bg)] overflow-hidden border-b border-[var(--border)]">
                    <div
                        className={`absolute inset-0 bg-gradient-to-br ${app.gradient} opacity-10`}
                    />
                    <div className="absolute inset-0 flex items-center justify-center p-6">
                        <div
                            className={`w-full h-full rounded-none flex items-center justify-center transition-transform duration-700 ${hovered ? 'scale-105' : 'scale-100'}`}
                        >
                            {app.imageContent}
                        </div>
                    </div>
                    {/* Category badge */}
                    <div className="absolute top-4 left-4">
                        <span className="inline-flex items-center gap-1.5 bg-[var(--bg)]/90 backdrop-blur px-3 py-1 text-[10px] font-bold uppercase tracking-[0.15em] text-accent border border-[var(--border)]">
                            <Icon size={12} />
                            {app.category}
                        </span>
                    </div>
                    {/* Hover overlay */}
                    <AnimatePresence>
                        {hovered && (
                            <motion.div
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                exit={{ opacity: 0 }}
                                className="absolute inset-0 bg-accent/10 backdrop-blur-[2px] flex items-center justify-center"
                            >
                                <button className="bg-accent text-white px-6 py-3 text-xs font-bold uppercase tracking-[0.2em] flex items-center gap-2 hover:bg-accent/90 transition-colors">
                                    <Play size={14} /> Watch Demo
                                </button>
                            </motion.div>
                        )}
                    </AnimatePresence>
                </div>

                {/* Content */}
                <div className="p-6">
                    <h4 className="text-lg font-bold text-text tracking-tight mb-3 group-hover:text-accent transition-colors">
                        {app.title}
                    </h4>
                    <p className="text-sm text-muted leading-relaxed mb-5">{app.description}</p>
                    <div className="flex items-center justify-between pt-4 border-t border-[var(--border)]">
                        <span className="text-[10px] font-bold text-muted uppercase tracking-[0.15em]">
                            {app.tech}
                        </span>
                        <button className="text-xs font-bold text-accent flex items-center gap-1 group-hover:gap-2 transition-all">
                            Details <ArrowUpRight size={12} />
                        </button>
                    </div>
                </div>
            </div>
        </Reveal>
    );
}

/* ═══════════════════════════════════════════════════════════
   APPLICATIONS DATA
   ═══════════════════════════════════════════════════════════ */
const APPLICATIONS = [
    // FATIGUE
    {
        id: 'fatigue-shaft',
        category: 'Fatigue',
        icon: Activity,
        title: 'Shaft Under Fatigue Modelling',
        description:
            'From user inputs in MS Excel, shaft parameters are collected. This geometry and working conditions are modelled and analyzed by Jupiter and SunShine solver.',
        tech: 'Excel + Jupiter + SunShine',
        gradient: 'from-blue-600 to-cyan-500',
        imageContent: (
            <div className="flex items-center justify-center w-full h-full">
                <div className="relative">
                    <div className="w-32 h-32 border-2 border-blue-600/30 flex items-center justify-center">
                        <div className="w-24 h-24 bg-gradient-to-br from-blue-600/20 to-cyan-500/20 flex items-center justify-center">
                            <div className="text-4xl font-black text-blue-600/60">⚙</div>
                        </div>
                    </div>
                    <div className="absolute -bottom-3 -right-3 bg-blue-600 text-white text-[10px] font-bold px-3 py-1">
                        FEM
                    </div>
                </div>
            </div>
        ),
    },
    {
        id: 'fatigue-exhaust',
        category: 'Fatigue',
        icon: Activity,
        title: 'MBD Automation for Exhaust System',
        description:
            'Automate the MBD fatigue analysis process for exhaust systems: from thermal stress to modal and RFI analysis with a single script.',
        tech: 'MBD + Thermal + Modal',
        gradient: 'from-orange-500 to-red-500',
        imageContent: (
            <div className="flex items-center gap-4">
                <div className="w-20 h-20 border-2 border-orange-500/30 flex items-center justify-center">
                    <div className="w-16 h-16 bg-gradient-to-br from-orange-500/20 to-red-500/20 flex items-center justify-center">
                        <span className="text-2xl font-black text-orange-500/60">M</span>
                    </div>
                </div>
                <ArrowRight size={24} className="text-orange-500/40" />
                <div className="w-20 h-20 border-2 border-red-500/30 flex items-center justify-center">
                    <div className="w-16 h-16 bg-gradient-to-br from-red-500/20 to-orange-500/20 flex items-center justify-center">
                        <span className="text-2xl font-black text-red-500/60">F</span>
                    </div>
                </div>
            </div>
        ),
    },
    {
        id: 'fatigue-post',
        category: 'Fatigue',
        icon: Activity,
        title: 'Post-Processing for Fatigue Analysis',
        description:
            'After analysis results, users can export pictures, graphs, and animations directly to MS PowerPoint with just one click.',
        tech: 'PowerPoint + Automation',
        gradient: 'from-purple-500 to-pink-500',
        imageContent: (
            <div className="flex items-center gap-3">
                <div className="w-16 h-16 border-2 border-purple-500/30 flex items-center justify-center">
                    <FileText size={28} className="text-purple-500/60" />
                </div>
                <ArrowRight size={20} className="text-purple-500/40" />
                <div className="w-16 h-16 border-2 border-pink-500/30 flex items-center justify-center">
                    <Monitor size={28} className="text-pink-500/60" />
                </div>
            </div>
        ),
    },
    // AI
    {
        id: 'ai-smart-dialog',
        category: 'AI',
        icon: Brain,
        title: 'Smart Dialog',
        description:
            'After parameters are trained by user operations, dialog parameters are filled in automatically instead of default values, reducing operation time.',
        tech: 'ML Training + UI',
        gradient: 'from-emerald-500 to-teal-500',
        imageContent: (
            <div className="flex items-center justify-center">
                <div className="relative">
                    <Brain size={64} className="text-emerald-500/40" />
                    <div className="absolute -top-2 -right-2 w-6 h-6 bg-emerald-500/80 flex items-center justify-center">
                        <Sparkles size={14} className="text-white" />
                    </div>
                </div>
            </div>
        ),
    },
    {
        id: 'ai-ship-shapes',
        category: 'AI',
        icon: Brain,
        title: 'Generate Ship Shapes for AI Training',
        description:
            'Automatically generate variants of ship hull shapes for AI training purposes, enabling rapid dataset creation for neural networks.',
        tech: 'Generative + Hull Design',
        gradient: 'from-cyan-500 to-blue-500',
        imageContent: (
            <div className="flex items-center gap-2">
                <div className="w-14 h-14 border-2 border-cyan-500/30 flex items-center justify-center">
                    <span className="text-xs font-bold text-cyan-500/60">V1</span>
                </div>
                <div className="w-14 h-14 border-2 border-blue-500/30 flex items-center justify-center">
                    <span className="text-xs font-bold text-blue-500/60">V2</span>
                </div>
                <div className="w-14 h-14 border-2 border-teal-500/30 flex items-center justify-center">
                    <span className="text-xs font-bold text-teal-500/60">V3</span>
                </div>
            </div>
        ),
    },
    // AUTOMATION
    {
        id: 'auto-voronoi',
        category: 'Automation',
        icon: LayoutGrid,
        title: 'Voronoi Tessellation Modelling',
        description:
            'Generate a Voronoi-shaped assembly for metal microscale modeling, enabling advanced material structure simulations.',
        tech: 'Geometry + Meshing',
        gradient: 'from-violet-500 to-purple-500',
        imageContent: (
            <div className="grid grid-cols-3 gap-1 w-32 h-32">
                {Array.from({ length: 9 }).map((_, i) => (
                    <div
                        key={i}
                        className="bg-violet-500/10 border border-violet-500/20"
                        style={{
                            clipPath: 'polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%)',
                        }}
                    />
                ))}
            </div>
        ),
    },
    {
        id: 'auto-openfoam-coupling',
        category: 'Automation',
        icon: Zap,
        title: 'Coupling SunShine and OpenFOAM',
        description:
            'OpenFOAM solves heat-flow analysis, then transfers results to SunShine for continuous thermal analysis. Repeated iteratively until convergence.',
        tech: 'OpenFOAM + SunShine',
        gradient: 'from-amber-500 to-orange-500',
        imageContent: (
            <div className="flex items-center gap-4">
                <div className="text-center">
                    <div className="w-16 h-16 bg-amber-500/10 border border-amber-500/30 flex items-center justify-center mb-2">
                        <Zap size={24} className="text-amber-500/60" />
                    </div>
                    <span className="text-[10px] font-bold text-amber-500/60">Heat</span>
                </div>
                <div className="flex flex-col gap-1">
                    <ArrowRight size={16} className="text-amber-500/40" />
                    <ArrowRight size={16} className="text-orange-500/40" />
                </div>
                <div className="text-center">
                    <div className="w-16 h-16 bg-orange-500/10 border border-orange-500/30 flex items-center justify-center mb-2">
                        <Activity size={24} className="text-orange-500/60" />
                    </div>
                    <span className="text-[10px] font-bold text-orange-500/60">Thermal</span>
                </div>
            </div>
        ),
    },
    {
        id: 'auto-openfoam-mesh',
        category: 'Automation',
        icon: Box,
        title: 'Block Mesh by OpenFOAM',
        description:
            'Use OpenFOAM to generate specialized block meshes for complex geometries with precise control over element distribution.',
        tech: 'OpenFOAM + Meshing',
        gradient: 'from-sky-500 to-blue-500',
        imageContent: (
            <div className="relative w-28 h-28">
                <div className="absolute inset-0 border-2 border-sky-500/30" />
                <div className="absolute top-1/4 left-1/4 w-1/2 h-1/2 border border-sky-500/20" />
                <div className="absolute top-1/3 left-1/3 w-1/3 h-1/3 bg-sky-500/10" />
                <div className="absolute -bottom-2 -right-2 bg-sky-500/20 px-2 py-1">
                    <span className="text-[10px] font-bold text-sky-500/60">BLOCK</span>
                </div>
            </div>
        ),
    },
    {
        id: 'auto-mesh-settings',
        category: 'Automation',
        icon: Settings,
        title: 'Auto Generate Mesh Settings',
        description:
            'Set mesh size automatically based on geometric location and curvature, eliminating manual element sizing across complex assemblies.',
        tech: 'Auto-Mesh + Geometry',
        gradient: 'from-indigo-500 to-violet-500',
        imageContent: (
            <div className="flex items-center gap-3">
                <Settings
                    size={48}
                    className="text-indigo-500/40 animate-spin"
                    style={{ animationDuration: '8s' }}
                />
                <div className="flex flex-col gap-1">
                    <div className="w-16 h-2 bg-indigo-500/20" />
                    <div className="w-12 h-2 bg-indigo-500/20" />
                    <div className="w-14 h-2 bg-indigo-500/20" />
                </div>
            </div>
        ),
    },
    {
        id: 'auto-fe-model',
        category: 'Automation',
        icon: Cpu,
        title: 'Auto Generate FE Model',
        description:
            'Generate solid mesh, setup boundary conditions and materials automatically from high-level parameters — full model in seconds.',
        tech: 'Full Pipeline',
        gradient: 'from-rose-500 to-pink-500',
        imageContent: (
            <div className="grid grid-cols-2 gap-2 w-28">
                <div className="h-12 bg-rose-500/10 border border-rose-500/20 flex items-center justify-center">
                    <span className="text-[10px] font-bold text-rose-500/60">MESH</span>
                </div>
                <div className="h-12 bg-pink-500/10 border border-pink-500/20 flex items-center justify-center">
                    <span className="text-[10px] font-bold text-pink-500/60">BCs</span>
                </div>
                <div className="h-12 bg-rose-500/10 border border-rose-500/20 flex items-center justify-center">
                    <span className="text-[10px] font-bold text-rose-500/60">MAT</span>
                </div>
                <div className="h-12 bg-pink-500/10 border border-pink-500/20 flex items-center justify-center">
                    <span className="text-[10px] font-bold text-pink-500/60">SOLVE</span>
                </div>
            </div>
        ),
    },
    {
        id: 'auto-html-report',
        category: 'Automation',
        icon: FileText,
        title: 'Generate HTML Model Report',
        description:
            'Generate a customized HTML website report by Python and JavaScript: show/hide columns, zoom in/out pictures, smart filters, and more.',
        tech: 'Python + JavaScript',
        gradient: 'from-teal-500 to-emerald-500',
        imageContent: (
            <div className="w-28 h-28 bg-teal-500/5 border border-teal-500/20 p-2">
                <div className="w-full h-3 bg-teal-500/20 mb-2" />
                <div className="w-2/3 h-2 bg-teal-500/15 mb-2" />
                <div className="w-1/2 h-2 bg-teal-500/15 mb-2" />
                <div className="grid grid-cols-3 gap-1 mt-2">
                    <div className="h-8 bg-teal-500/10" />
                    <div className="h-8 bg-teal-500/10" />
                    <div className="h-8 bg-teal-500/10" />
                </div>
            </div>
        ),
    },
    {
        id: 'auto-excel-model',
        category: 'Automation',
        icon: Layers,
        title: 'Change Model Information by Excel',
        description:
            'Run Jupiter in background or foreground mode from MS Excel to renumber IDs and change model colors in batch operations.',
        tech: 'Excel + Batch Processing',
        gradient: 'from-green-500 to-emerald-500',
        imageContent: (
            <div className="flex items-center gap-3">
                <div className="w-14 h-14 bg-green-500/10 border border-green-500/30 flex items-center justify-center">
                    <span className="text-xs font-bold text-green-500/60">XLS</span>
                </div>
                <ArrowRight size={16} className="text-green-500/40" />
                <div className="w-14 h-14 bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center">
                    <span className="text-xs font-bold text-emerald-500/60">JDB</span>
                </div>
            </div>
        ),
    },
    {
        id: 'auto-excel-analyses',
        category: 'Automation',
        icon: Globe,
        title: 'Run Several Analyses from Excel',
        description:
            'Run multiple static and vibration analyses for Design of Experiments (DoE). Based on results, users can decide design changes for optimization.',
        tech: 'DoE + Optimization',
        gradient: 'from-blue-600 to-indigo-600',
        imageContent: (
            <div className="flex items-end gap-1 h-24">
                {[40, 65, 45, 80, 55, 90, 70].map((h, i) => (
                    <div
                        key={i}
                        className="w-4 bg-blue-600/20 border border-blue-600/30"
                        style={{ height: `${h}%` }}
                    />
                ))}
            </div>
        ),
    },
];

const CATEGORIES = [
    { label: 'All', value: 'all', icon: LayoutGrid },
    { label: 'Fatigue', value: 'Fatigue', icon: Activity },
    { label: 'AI', value: 'AI', icon: Brain },
    { label: 'Automation', value: 'Automation', icon: Zap },
];

/* ═══════════════════════════════════════════════════════════
   MAIN COMPONENT
   ═══════════════════════════════════════════════════════════ */
export default function Showcase() {
    const [isDark, setIsDark] = useState(true);
    const [activeFilter, setActiveFilter] = useState('all');
    const [searchQuery, setSearchQuery] = useState('');

    const filteredApps = APPLICATIONS.filter((app) => {
        const matchesCategory = activeFilter === 'all' || app.category === activeFilter;
        const matchesSearch =
            !searchQuery ||
            app.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
            app.description.toLowerCase().includes(searchQuery.toLowerCase());
        return matchesCategory && matchesSearch;
    });

    return (
        <div className="min-h-screen bg-[var(--bg)] text-[var(--text)] transition-colors duration-300">
            {/* ── NAVBAR ── */}
            <nav className="fixed top-0 w-full z-50 border-b border-[var(--border)] bg-[var(--bg)]/80 backdrop-blur-xl">
                <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                    <div className="flex items-center gap-8">
                        <a href="/" className="flex items-center gap-3">
                            <div className="w-8 h-8 bg-blue-600 flex items-center justify-center">
                                <span className="text-white font-black text-xs">P</span>
                            </div>
                            <span className="text-lg font-bold tracking-tight text-text">
                                PSJ Showcase
                            </span>
                        </a>
                        <div className="hidden md:flex items-center gap-1 text-sm">
                            <a
                                href="/"
                                className="px-4 py-2 text-muted hover:text-text transition-colors"
                            >
                                Home
                            </a>
                            <a href="#" className="px-4 py-2 text-accent font-bold bg-accent/5">
                                Showcase
                            </a>
                            <a
                                href="#"
                                className="px-4 py-2 text-muted hover:text-text transition-colors"
                            >
                                Docs
                            </a>
                        </div>
                    </div>

                    <div className="flex items-center gap-3">
                        <button
                            onClick={() => setIsDark(!isDark)}
                            className="w-9 h-9 flex items-center justify-center border border-[var(--border)] hover:border-accent/40 transition-colors"
                        >
                            {isDark ? <Sun size={16} /> : <Moon size={16} />}
                        </button>
                        <button className="hidden sm:block bg-blue-600 text-white px-5 py-2 text-xs font-bold uppercase tracking-[0.15em] hover:bg-blue-700 transition-colors">
                            Contact Us
                        </button>
                    </div>
                </div>
            </nav>

            {/* ── HERO ── */}
            <section className="relative pt-28 pb-16 lg:pt-40 lg:pb-24 overflow-hidden">
                <div className="absolute inset-0 bg-grid pointer-events-none" />
                <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-blue-600/5 blur-[120px] rounded-full pointer-events-none" />

                <div className="relative max-w-7xl mx-auto px-6 text-center">
                    <Reveal>
                        <div className="inline-flex items-center gap-2 bg-blue-600/10 border border-blue-600/20 px-4 py-2 mb-8">
                            <Sparkles size={14} className="text-blue-600" />
                            <span className="text-[10px] font-black text-blue-600 uppercase tracking-[0.3em]">
                                PSJ v5 — Production Ready
                            </span>
                        </div>
                    </Reveal>

                    <Reveal delay={100}>
                        <h1 className="text-5xl md:text-7xl lg:text-8xl font-black text-text uppercase tracking-tighter leading-[0.85] mb-6">
                            Applications
                            <br />
                            <span className="text-accent">Built with PSJ</span>
                        </h1>
                    </Reveal>

                    <Reveal delay={200}>
                        <p className="text-lg md:text-xl text-muted max-w-2xl mx-auto leading-relaxed mb-10">
                            Explore real-world engineering automation solutions — from fatigue
                            analysis and AI-driven design to full OpenFOAM coupling workflows.
                        </p>
                    </Reveal>

                    <Reveal delay={300}>
                        <div className="flex flex-wrap justify-center gap-4">
                            <a
                                href="#apps"
                                className="bg-blue-600 text-white px-8 py-4 text-sm font-bold uppercase tracking-[0.15em] hover:bg-blue-700 transition-all flex items-center gap-2"
                            >
                                Browse Applications <ChevronDown size={16} />
                            </a>
                            <a
                                href="#"
                                className="border border-[var(--border)] text-text px-8 py-4 text-sm font-bold uppercase tracking-[0.15em] hover:border-accent/40 transition-all flex items-center gap-2"
                            >
                                <ExternalLink size={14} /> View Documentation
                            </a>
                        </div>
                    </Reveal>

                    {/* Stats */}
                    <Reveal delay={400}>
                        <div className="grid grid-cols-3 gap-8 max-w-lg mx-auto mt-16 pt-10 border-t border-[var(--border)]">
                            {[
                                { value: '13', label: 'Applications' },
                                { value: '3', label: 'Categories' },
                                { value: 'v5', label: 'Platform' },
                            ].map((s) => (
                                <div key={s.label} className="text-center">
                                    <div className="text-2xl md:text-3xl font-black text-text">
                                        {s.value}
                                    </div>
                                    <div className="text-[10px] font-bold text-muted uppercase tracking-[0.2em] mt-1">
                                        {s.label}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </Reveal>
                </div>
            </section>

            {/* ── FILTERS ── */}
            <section
                id="apps"
                className="py-8 border-y border-[var(--border)] bg-[var(--card)]/50 sticky top-16 z-40 backdrop-blur-xl"
            >
                <div className="max-w-7xl mx-auto px-6">
                    <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
                        {/* Category filters */}
                        <div className="flex flex-wrap gap-1 bg-[var(--bg)] border border-[var(--border)] p-1">
                            {CATEGORIES.map((cat) => {
                                const Icon = cat.icon;
                                const isActive = activeFilter === cat.value;
                                return (
                                    <button
                                        key={cat.value}
                                        onClick={() => setActiveFilter(cat.value)}
                                        className={`flex items-center gap-2 px-4 py-2 text-[11px] font-bold uppercase tracking-[0.1em] transition-all ${
                                            isActive
                                                ? 'bg-blue-600 text-white shadow-lg shadow-blue-600/20'
                                                : 'text-muted hover:text-text'
                                        }`}
                                    >
                                        <Icon size={14} />
                                        {cat.label}
                                        {isActive && (
                                            <span className="ml-1 w-5 h-5 bg-white/20 flex items-center justify-center text-[10px]">
                                                {
                                                    APPLICATIONS.filter(
                                                        (a) =>
                                                            cat.value === 'all' ||
                                                            a.category === cat.value,
                                                    ).length
                                                }
                                            </span>
                                        )}
                                    </button>
                                );
                            })}
                        </div>

                        {/* Search */}
                        <div className="relative w-full sm:w-64">
                            <Search
                                size={14}
                                className="absolute left-3 top-1/2 -translate-y-1/2 text-muted"
                            />
                            <input
                                type="text"
                                placeholder="Search applications..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                className="w-full pl-10 pr-4 py-2.5 bg-[var(--bg)] border border-[var(--border)] text-sm text-text placeholder:text-muted/50 focus:border-blue-600/40 focus:outline-none transition-colors"
                            />
                        </div>
                    </div>
                </div>
            </section>

            {/* ── APPLICATIONS GRID ── */}
            <section className="py-16 lg:py-24 relative">
                <div className="max-w-7xl mx-auto px-6">
                    {/* Results count */}
                    <div className="flex items-center justify-between mb-10">
                        <p className="text-sm text-muted">
                            Showing{' '}
                            <span className="text-text font-bold">{filteredApps.length}</span> of{' '}
                            {APPLICATIONS.length} applications
                        </p>
                        <button className="text-xs text-muted hover:text-text flex items-center gap-1 transition-colors">
                            <Filter size={12} /> Sort
                        </button>
                    </div>

                    {/* Grid */}
                    <AnimatePresence mode="wait">
                        {filteredApps.length > 0 ? (
                            <motion.div
                                key={activeFilter + searchQuery}
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                exit={{ opacity: 0 }}
                                className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6"
                            >
                                {filteredApps.map((app, i) => (
                                    <AppCard key={app.id} app={app} index={i} />
                                ))}
                            </motion.div>
                        ) : (
                            <motion.div
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                className="text-center py-24"
                            >
                                <div className="w-16 h-16 border-2 border-[var(--border)] flex items-center justify-center mx-auto mb-6">
                                    <Search size={24} className="text-muted" />
                                </div>
                                <h3 className="text-xl font-bold text-text mb-2">
                                    No applications found
                                </h3>
                                <p className="text-muted text-sm">
                                    Try adjusting your search or filter criteria.
                                </p>
                                <button
                                    onClick={() => {
                                        setActiveFilter('all');
                                        setSearchQuery('');
                                    }}
                                    className="mt-6 text-sm text-blue-600 font-bold hover:underline"
                                >
                                    Clear all filters
                                </button>
                            </motion.div>
                        )}
                    </AnimatePresence>
                </div>
            </section>

            {/* ── CTA ── */}
            <section className="py-24 bg-blue-600 relative overflow-hidden">
                <div className="absolute inset-0 bg-grid opacity-20 pointer-events-none" />
                <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-white/5 blur-[100px] rounded-full pointer-events-none" />

                <div className="relative max-w-4xl mx-auto px-6 text-center">
                    <Reveal>
                        <h2 className="text-4xl md:text-6xl font-black text-white uppercase tracking-tighter leading-[0.85] mb-6">
                            Need a custom
                            <br />
                            automation solution?
                        </h2>
                    </Reveal>
                    <Reveal delay={100}>
                        <p className="text-lg text-white/70 max-w-xl mx-auto mb-10 leading-relaxed">
                            Our team can build bespoke PSJ scripts and GUI tools tailored to your
                            specific engineering workflows.
                        </p>
                    </Reveal>
                    <Reveal delay={200}>
                        <div className="flex flex-wrap justify-center gap-4">
                            <button className="bg-white text-blue-600 px-10 py-4 text-sm font-black uppercase tracking-[0.2em] hover:bg-white/90 transition-all flex items-center gap-2">
                                Contact Us <ArrowRight size={16} />
                            </button>
                            <button className="border border-white/30 text-white px-10 py-4 text-sm font-black uppercase tracking-[0.2em] hover:bg-white/5 transition-all">
                                Request Demo
                            </button>
                        </div>
                    </Reveal>
                </div>
            </section>

            {/* ── FOOTER ── */}
            <footer className="py-12 border-t border-[var(--border)] bg-[var(--card)]/30">
                <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-6">
                    <div className="flex items-center gap-3">
                        <div className="w-7 h-7 bg-blue-600 flex items-center justify-center">
                            <span className="text-white font-black text-[10px]">P</span>
                        </div>
                        <span className="text-sm font-bold text-text">PSJ by TechnoStar</span>
                    </div>
                    <div className="flex items-center gap-8 text-xs text-muted">
                        <a href="#" className="hover:text-text transition-colors">
                            Documentation
                        </a>
                        <a href="#" className="hover:text-text transition-colors">
                            Support
                        </a>
                        <a
                            href="https://www.e-technostar.com"
                            target="_blank"
                            rel="noreferrer"
                            className="hover:text-text transition-colors flex items-center gap-1"
                        >
                            e-TechnoStar <ExternalLink size={10} />
                        </a>
                    </div>
                    <p className="text-xs text-muted">© 2026 TechnoStar Co., Ltd.</p>
                </div>
            </footer>
        </div>
    );
}
