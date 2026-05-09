'use client';
// oxlint-disable react/no-unescaped-entities
import { useEffect, useRef, useState, type ReactNode } from 'react';

import { motion, useInView as useFramerInView } from 'framer-motion';
import {
    ArrowRight,
    ArrowUpRight,
    BarChart3,
    BookOpen,
    Box,
    Boxes,
    Braces,
    Bug,
    Building,
    Car,
    CheckCircle2,
    ChevronRight,
    Code2,
    Cpu,
    Database,
    ExternalLink,
    FileText,
    Flame,
    FlaskConical,
    Gauge,
    Globe,
    Hash,
    LayoutGrid,
    Menu,
    Microscope,
    Monitor,
    MousePointerClick,
    Palette,
    Plane,
    Play,
    Presentation,
    PuzzleIcon,
    Repeat,
    Settings,
    Shield,
    Ship,
    Sparkles,
    Target,
    Terminal,
    Wrench,
    X,
} from 'lucide-react';

import '@/styles/global.css';

/* ── Animation wrapper ── */
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
    const inView = useFramerInView(ref, { once: true, margin: '-80px' });
    return (
        <motion.div
            ref={ref}
            initial={{ opacity: 0, y: 40 }}
            animate={inView ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.7, delay: delay * 0.001, ease: [0.25, 0.46, 0.45, 0.94] }}
            className={className}
        >
            {children}
        </motion.div>
    );
}

/* ── Animated counter ── */
function Counter({ end, suffix = '' }: { end: number; suffix?: string }) {
    const ref = useRef<HTMLSpanElement>(null);
    const inView = useFramerInView(ref, { once: true });
    const [val, setVal] = useState(0);
    useEffect(() => {
        if (!inView) return;
        let n = 0;
        const step = end / 60;
        const t = setInterval(() => {
            n += step;
            if (n >= end) {
                setVal(end);
                clearInterval(t);
            } else setVal(Math.floor(n));
        }, 25);
        return () => clearInterval(t);
    }, [inView, end]);
    return (
        <span ref={ref}>
            {val}
            {suffix}
        </span>
    );
}

/* ── Section label ── */
function SectionLabel({ label }: { label: string }) {
    return (
        <div className="flex items-center gap-3 mb-6">
            <div className="w-8 h-px bg-blue" />
            <span className="text-xs font-semibold tracking-[0.2em] uppercase text-blue">
                {label}
            </span>
        </div>
    );
}

/* ── Glowing card wrapper ── */
function GlowCard({
    children,
    className = '',
    hoverGlow = true,
}: {
    children: ReactNode;
    className?: string;
    hoverGlow?: boolean;
}) {
    return (
        <div className={`relative group ${className}`}>
            {hoverGlow && (
                <div className="absolute -inset-px bg-gradient-to-b from-blue/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none" />
            )}
            <div className="relative h-full bg-bg-card border border-landing-border group-hover:border-landing-border-hover transition-all duration-300">
                {children}
            </div>
        </div>
    );
}

/* ══════════════════════════════════════════════════════
   PAGE — Fumadocs landing homepage
   ══════════════════════════════════════════════════════ */
export default function HomePage() {
    const [menuOpen, setMenuOpen] = useState(false);
    const [scrolled, setScrolled] = useState(false);
    const [activeArch, setActiveArch] = useState(0);

    useEffect(() => {
        const fn = () => setScrolled(window.scrollY > 40);
        window.addEventListener('scroll', fn, { passive: true });
        return () => window.removeEventListener('scroll', fn);
    }, []);

    /* ── Data ── */
    const navLinks = [
        { label: 'Overview', href: '#overview' },
        { label: 'Features', href: '#features' },
        { label: 'Architecture', href: '#architecture' },
        { label: 'Use Cases', href: '#usecases' },
        { label: 'Resources', href: '#resources' },
    ];

    const archTabs = [
        {
            name: 'Macro',
            icon: <Play size={16} />,
            desc: 'Equivalent to Jupiter built-in dialog functions, without GUI. Auto-generated after each successful dialog operation.',
            code: `# Macro — auto-recorded from Jupiter dialog\nCreateCube([0,0,0], [10,10,10], [10,10,10],\n  "Cube_1", 7105764, 0:0)\n\nImprintLines([[7.8,0,10], [2.2,10,10]],\n  [6:26], 1)\n\n# Record → Run → Save → Reload\n# via the Macro window`,
        },
        {
            name: 'PSJ-Command',
            icon: <Terminal size={16} />,
            desc: 'Command language representing the same operations as dialog functions. Replay Jupiter operations programmatically.',
            code: `# PSJ-Command — programmatic replay\nimport psj\n\npsj.command.mesh.create_hex(\n  body="Cube_1",\n  size=2.0,\n  quality="high"\n)\n\npsj.command.analysis.run_static(\n  loadcase="LC_01"\n)`,
        },
        {
            name: 'PSJ-Utility',
            icon: <Database size={16} />,
            desc: 'Query model database for names, IDs, colors, coordinates and all entity properties in your Jupiter model.',
            code: `# PSJ-Utility — query model database\nimport psj.utility as util\n\n# Get all node coordinates\nnodes = util.get_node_coords(model)\nprint(f"Total nodes: {len(nodes)}")\n\n# Query element properties\nprops = util.get_elem_property(\n  model, elem_ids=[1,2,3]\n)`,
        },
        {
            name: 'PSJ-GUI',
            icon: <LayoutGrid size={16} />,
            desc: 'GUI Command Builder — create custom dialog interfaces equivalent to Jupiter built-in dialogs for your own tools.',
            code: `# PSJ-GUI — build custom dialogs\nimport psj.gui as gui\n\ndlg = gui.Dialog("Bolt Generator")\ndlg.add_input("diameter", 10.0)\ndlg.add_dropdown("type",\n  ["Hex","Socket","Carriage"])\ndlg.add_button("Generate",\n  callback=create_bolt)\ndlg.show()`,
        },
        {
            name: 'Custom Shell',
            icon: <Bug size={16} />,
            desc: 'Dedicated shell with error output, debugging tools, and real-time execution feedback for PSJ scripts.',
            code: `# Customized Shell — debug output\n>>> run_script("mesh_auto.py")\n[INFO] Loading model: chassis_v3.jdb\n[INFO] Meshing 24 bodies...\n[INFO] Body "Frame_L" — 12,847 elems\n[WARN] Body "Bracket_R" — skewed elem\n[INFO] Quality check: 98.2% passed\n[INFO] Total: 156,203 elements\n>>> _`,
        },
        {
            name: 'Custom IDE',
            icon: <Code2 size={16} />,
            desc: 'Built-in IDE with intelligent code completion, syntax highlighting, and predictive suggestions for all PSJ APIs.',
            code: `# Customized IDE features:\n# ✦ Auto-complete for PSJ API\n# ✦ Syntax highlighting\n# ✦ Inline documentation\n# ✦ Error detection\n# ✦ VS Code extension available\n\nimport psj\npsj.  # ← shows all modules\n  ├── command\n  ├── utility\n  ├── gui\n  └── macro`,
        },
    ];

    const fourF = [
        {
            title: 'Friendly',
            subtitle: 'Even for non-programmers',
            desc: 'Macro recording captures your actions as code. No programming experience required to start automating.',
            icon: <MousePointerClick size={28} />,
            color: 'from-blue/20 to-cyan/10',
        },
        {
            title: 'Fast',
            subtitle: 'Through automation',
            desc: 'Eliminate hours of repetitive manual work. Automate meshing, solving, and post-processing in seconds.',
            icon: <Gauge size={28} />,
            color: 'from-cyan/20 to-blue/10',
        },
        {
            title: 'Functional',
            subtitle: 'IDE & GUI Builder',
            desc: 'Full-featured IDE with code completion and a visual GUI builder to create professional dialog interfaces.',
            icon: <PuzzleIcon size={28} />,
            color: 'from-purple/20 to-blue/10',
        },
        {
            title: 'Flexible',
            subtitle: 'For advanced simulation',
            desc: 'Built on Python 3 with numpy, pandas, scikit-learn, matplotlib and more. Extend without limits.',
            icon: <Sparkles size={28} />,
            color: 'from-orange/20 to-purple/10',
        },
    ];

    const features = [
        {
            icon: <Braces size={24} />,
            title: 'Jupiter Functions in Python',
            desc: "Access Jupiter's full Pre/Post processing power through native Python scripting. Connect with any external software.",
            bullets: [
                'Full Pre/Post API access',
                'Python 3.x compatible',
                'Connect with external tools',
            ],
        },
        {
            icon: <LayoutGrid size={24} />,
            title: 'GUI Command Builder',
            desc: 'Create custom dialog interfaces equivalent to Jupiter built-in dialogs. No Qt or Tkinter knowledge needed.',
            bullets: ['Drag & drop design', 'Built-in widgets', 'Event callbacks'],
        },
        {
            icon: <Code2 size={24} />,
            title: 'Customized IDE',
            desc: 'Dedicated development environment with intelligent auto-complete, predictive tips, and inline documentation.',
            bullets: ['Smart auto-complete', 'Syntax highlighting', 'VS Code extension'],
        },
        {
            icon: <Terminal size={24} />,
            title: 'Customized Shell',
            desc: 'Interactive shell with structured error output, execution logging, and real-time debugging support.',
            bullets: ['Error tracing', 'Execution logs', 'Interactive debugging'],
        },
        {
            icon: <Boxes size={24} />,
            title: 'Python Libraries Built-in',
            desc: 'Includes pandas, numpy, matplotlib, pptx, scikit-learn, numba and more — ready to use out of the box.',
            bullets: ['NumPy & Pandas', 'Matplotlib & pptx', 'scikit-learn & numba'],
        },
        {
            icon: <Globe size={24} />,
            title: 'VS Code Integration',
            desc: 'Use our customized VS Code extension to develop PSJ scripts in your preferred editor environment.',
            bullets: ['Custom extension', 'Remote debugging', 'Seamless workflow'],
        },
    ];

    const useCases = [
        {
            icon: <Wrench size={22} />,
            title: 'Custom Bolt Modeling',
            desc: 'Parametric bolt generation with custom thread patterns, automated placement, and structural validation.',
        },
        {
            icon: <Microscope size={22} />,
            title: 'Microstructure Modeling',
            desc: 'Voronoi structure generation and polycrystalline material simulation for advanced material analysis.',
        },
        {
            icon: <FileText size={22} />,
            title: 'Excel-driven FEM',
            desc: 'Read design parameters from Excel spreadsheets, auto-generate FE models, and write results back.',
        },
        {
            icon: <Presentation size={22} />,
            title: 'Automated Reporting',
            desc: 'Export analysis results to PowerPoint presentations and web browsers with automated chart generation.',
        },
        {
            icon: <Box size={22} />,
            title: 'AI Hull Design',
            desc: 'Machine learning-driven hull form optimization using PSJ with scikit-learn and parametric geometry.',
        },
        {
            icon: <Repeat size={22} />,
            title: 'Fatigue Analysis',
            desc: 'Low-cycle fatigue workflow automation with custom material models and life prediction algorithms.',
        },
    ];

    const industries = [
        {
            icon: <Car size={24} />,
            name: 'Automotive',
            desc: 'Body, chassis, powertrain simulation',
        },
        { icon: <Plane size={24} />, name: 'Aerospace', desc: 'Structural & thermal analysis' },
        {
            icon: <Ship size={24} />,
            name: 'Shipbuilding',
            desc: 'Hull design & structural integrity',
        },
        { icon: <Flame size={24} />, name: 'Energy', desc: 'Turbine & plant simulation' },
        {
            icon: <Building size={24} />,
            name: 'Civil Engineering',
            desc: 'Structural analysis & design',
        },
        { icon: <FlaskConical size={24} />, name: 'Research', desc: 'Academic & R&D innovation' },
    ];

    /* ── Render ── */
    return (
        <div className="min-h-screen overflow-x-hidden bg-bg text-text">
            {/* ════════════ NAVBAR ════════════ */}
            <nav
                className={[
                    'fixed top-0 w-full z-50 transition-all duration-300',
                    scrolled
                        ? 'bg-bg/90 backdrop-blur-xl border-b border-landing-border'
                        : 'bg-transparent',
                ].join(' ')}
            >
                <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                    {/* Logo */}
                    <a href="#" className="flex items-center gap-3">
                        <div className="w-8 h-8 bg-blue flex items-center justify-center">
                            <span className="text-white font-black text-sm">PSJ</span>
                        </div>
                        <span className="hidden sm:block text-sm font-semibold text-text">
                            Python Scripting for Jupiter
                        </span>
                    </a>

                    {/* Desktop links */}
                    <div className="hidden lg:flex items-center gap-8">
                        {navLinks.map((l) => (
                            <a
                                key={l.label}
                                href={l.href}
                                className="text-sm text-text-secondary hover:text-text transition-colors"
                            >
                                {l.label}
                            </a>
                        ))}
                    </div>

                    {/* Actions */}
                    <div className="flex items-center gap-3">
                        <a
                            href="https://www.e-technostar.com/our-products/15394"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="hidden sm:flex items-center gap-2 text-sm text-text-secondary hover:text-text transition-colors"
                        >
                            Documentation <ExternalLink size={14} />
                        </a>
                        <a
                            href="#contact"
                            className="bg-blue hover:bg-blue-bright text-white text-sm font-medium px-5 py-2 transition-colors"
                        >
                            Request Demo
                        </a>
                        <button
                            onClick={() => setMenuOpen(!menuOpen)}
                            className="lg:hidden text-text-secondary hover:text-text p-1"
                            aria-label="Toggle menu"
                        >
                            {menuOpen ? <X size={22} /> : <Menu size={22} />}
                        </button>
                    </div>
                </div>

                {/* Mobile menu */}
                {menuOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="lg:hidden bg-bg-elevated border-b border-landing-border"
                    >
                        <div className="px-6 py-4 flex flex-col gap-3">
                            {navLinks.map((l) => (
                                <a
                                    key={l.label}
                                    href={l.href}
                                    onClick={() => setMenuOpen(false)}
                                    className="text-sm text-text-secondary hover:text-text py-2"
                                >
                                    {l.label}
                                </a>
                            ))}
                        </div>
                    </motion.div>
                )}
            </nav>

            {/* ════════════ HERO ════════════ */}
            <section className="relative min-h-screen flex items-center justify-center pt-16">
                {/* Background layers */}
                <div className="absolute inset-0">
                    <img
                        src="/images/hero-mesh.jpg"
                        alt=""
                        className="w-full h-full object-cover opacity-30"
                    />
                    <div className="absolute inset-0 bg-gradient-to-b from-bg/60 via-bg/40 to-bg" />
                    <div className="absolute inset-0 bg-grid opacity-40" />
                </div>

                {/* Ambient orbs */}
                <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue/[0.08] blur-[120px] orb-1" />
                <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-cyan/[0.06] blur-[100px] orb-2" />

                <div className="relative z-10 max-w-7xl mx-auto px-6 py-24">
                    <div className="grid lg:grid-cols-2 gap-16 items-center">
                        {/* Left — headline */}
                        <div>
                            <Reveal>
                                <div className="inline-flex items-center gap-2 border border-landing-border px-4 py-1.5 mb-8 text-xs tracking-wider uppercase text-text-secondary">
                                    <div className="w-1.5 h-1.5 bg-blue" />
                                    Python Scripting for Jupiter — v5.1
                                </div>
                            </Reveal>

                            <Reveal delay={100}>
                                <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold leading-[0.95] tracking-tight mb-8">
                                    <span className="gradient-text-white">Automate</span>
                                    <br />
                                    <span className="gradient-text-white">your entire</span>
                                    <br />
                                    <span className="gradient-text-blue">CAE workflow</span>
                                </h1>
                            </Reveal>

                            <Reveal delay={200}>
                                <p className="text-lg text-text-secondary leading-relaxed max-w-lg mb-10">
                                    PSJ is a fully-featured Python API for Jupiter, enabling
                                    engineers to eliminate repetitive operations, reduce human
                                    error, and build custom automation tools — with or without
                                    programming experience.
                                </p>
                            </Reveal>

                            <Reveal delay={300}>
                                <div className="flex flex-wrap gap-4">
                                    <a
                                        href="#overview"
                                        className="group bg-blue hover:bg-blue-bright text-white font-medium px-7 py-3.5 text-sm flex items-center gap-2 transition-all"
                                    >
                                        Explore PSJ{' '}
                                        <ArrowRight
                                            size={16}
                                            className="group-hover:translate-x-1 transition-transform"
                                        />
                                    </a>
                                    <a
                                        href="#architecture"
                                        className="group border border-landing-border hover:border-landing-border-hover text-text-secondary hover:text-text font-medium px-7 py-3.5 text-sm flex items-center gap-2 transition-all"
                                    >
                                        <Play size={16} /> See How It Works
                                    </a>
                                </div>
                            </Reveal>

                            <Reveal delay={400}>
                                <div className="flex flex-wrap gap-6 mt-12 text-xs text-text-muted">
                                    {[
                                        'Python 3.x',
                                        'NumPy',
                                        'Pandas',
                                        'scikit-learn',
                                        'Matplotlib',
                                    ].map((t) => (
                                        <span key={t} className="flex items-center gap-1.5">
                                            <div className="w-1 h-1 bg-text-muted" />
                                            {t}
                                        </span>
                                    ))}
                                </div>
                            </Reveal>
                        </div>

                        {/* Right — code card */}
                        <Reveal delay={200} className="hidden lg:block">
                            <div className="relative">
                                <div className="absolute -inset-px bg-gradient-to-b from-blue/30 via-blue/5 to-transparent" />
                                <div className="relative bg-bg-card border border-landing-border">
                                    <div className="flex items-center gap-2 px-5 py-3 border-b border-landing-border bg-bg-elevated/50">
                                        <div className="w-2.5 h-2.5 bg-red-500/60" />
                                        <div className="w-2.5 h-2.5 bg-yellow-500/60" />
                                        <div className="w-2.5 h-2.5 bg-green-500/60" />
                                        <span className="ml-3 text-xs text-text-muted code-font">
                                            automate.py
                                        </span>
                                    </div>
                                    <pre className="p-6 text-sm leading-7 code-font overflow-x-auto">
                                        <code>
                                            <span className="text-text-muted">
                                                # PSJ Automation Script
                                            </span>
                                            {'\n'}
                                            <span className="text-purple">import</span>{' '}
                                            <span className="text-cyan">psj</span>
                                            {'\n'}
                                            <span className="text-purple">from</span>{' '}
                                            <span className="text-cyan">psj.utility</span>{' '}
                                            <span className="text-purple">import</span> get_model
                                            {'\n\n'}
                                            <span className="text-text-muted">
                                                # Load and mesh the model
                                            </span>
                                            {'\n'}
                                            <span className="text-text">model</span>{' '}
                                            <span className="text-text-muted">=</span>{' '}
                                            <span className="text-cyan">psj</span>.
                                            <span className="text-blue-bright">load</span>(
                                            <span className="text-orange">"chassis.jdb"</span>)
                                            {'\n'}
                                            <span className="text-cyan">psj</span>.
                                            <span className="text-blue-bright">mesh</span>
                                            .auto_hex(model,{' '}
                                            <span className="text-orange">size</span>=
                                            <span className="text-cyan">2.0</span>){'\n\n'}
                                            <span className="text-text-muted"># Run analysis</span>
                                            {'\n'}
                                            <span className="text-cyan">psj</span>.
                                            <span className="text-blue-bright">analysis</span>
                                            .run_static(model)
                                            {'\n\n'}
                                            <span className="text-text-muted"># Export report</span>
                                            {'\n'}
                                            <span className="text-cyan">psj</span>.
                                            <span className="text-blue-bright">report</span>
                                            .to_pptx(model,{'\n'}
                                            {'  '}
                                            <span className="text-orange">template</span>=
                                            <span className="text-orange">"standard.pptx"</span>)
                                            {'\n'}
                                        </code>
                                    </pre>
                                </div>
                            </div>
                        </Reveal>
                    </div>
                </div>

                {/* Scroll indicator */}
                <div className="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2">
                    <span className="text-[10px] tracking-[0.2em] uppercase text-text-muted">
                        Scroll
                    </span>
                    <div className="w-px h-8 bg-gradient-to-b from-text-muted to-transparent" />
                </div>
            </section>

            {/* ════════════ INDUSTRY BAR ════════════ */}
            <section className="border-y border-landing-border bg-bg-elevated/50">
                <div className="max-w-7xl mx-auto px-6 py-8">
                    <div className="flex flex-col sm:flex-row items-center gap-8 justify-between">
                        <span className="text-xs tracking-[0.15em] uppercase text-text-muted whitespace-nowrap">
                            Trusted across industries
                        </span>
                        <div className="flex flex-wrap items-center gap-8 justify-center">
                            {[
                                'Automotive',
                                'Aerospace',
                                'Shipbuilding',
                                'Energy',
                                'Civil Engineering',
                                'Manufacturing',
                            ].map((s) => (
                                <span key={s} className="text-sm text-text-muted/70 font-medium">
                                    {s}
                                </span>
                            ))}
                        </div>
                    </div>
                </div>
            </section>

            {/* ════════════ OVERVIEW / PROBLEMS ════════════ */}
            <section id="overview" className="py-32 bg-bg relative">
                <div className="absolute inset-0 bg-grid opacity-30" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <div className="grid lg:grid-cols-2 gap-20">
                        {/* Left: Problems */}
                        <div>
                            <Reveal>
                                <SectionLabel label="The Problem" />
                                <h2 className="text-4xl sm:text-5xl font-bold leading-tight mb-6">
                                    Daily CAE work is
                                    <br />
                                    <span className="text-text-secondary">broken by design</span>
                                </h2>
                                <p className="text-text-secondary leading-relaxed mb-10">
                                    Engineers spend hours on repetitive operations, fight against
                                    tight deadlines, and struggle with error-prone manual processes
                                    — while every firm needs different workflows.
                                </p>
                            </Reveal>

                            <div className="space-y-5">
                                {[
                                    {
                                        icon: <Repeat size={18} />,
                                        text: 'Repeated operations make daily work boring and error-prone',
                                    },
                                    {
                                        icon: <Gauge size={18} />,
                                        text: 'Iterative work without automation misses critical deadlines',
                                    },
                                    {
                                        icon: <Shield size={18} />,
                                        text: 'Manual operations inevitably create costly mistakes',
                                    },
                                    {
                                        icon: <BookOpen size={18} />,
                                        text: 'In-depth CAE training is required for complex modeling',
                                    },
                                    {
                                        icon: <Settings size={18} />,
                                        text: 'Each firm needs customized UI for its own design rules',
                                    },
                                ].map((item, i) => (
                                    <Reveal key={i} delay={i * 80}>
                                        <div className="flex items-start gap-4 p-4 border border-landing-border bg-bg-card/50 hover:border-landing-border-hover transition-colors">
                                            <div className="text-text-muted mt-0.5">
                                                {item.icon}
                                            </div>
                                            <span className="text-sm text-text-secondary leading-relaxed">
                                                {item.text}
                                            </span>
                                        </div>
                                    </Reveal>
                                ))}
                            </div>
                        </div>

                        {/* Right: User personas */}
                        <div>
                            <Reveal delay={100}>
                                <SectionLabel label="Who Needs PSJ" />
                                <h2 className="text-4xl sm:text-5xl font-bold leading-tight mb-10">
                                    Built for every
                                    <br />
                                    <span className="text-text-secondary">CAE professional</span>
                                </h2>
                            </Reveal>

                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                {[
                                    {
                                        role: 'CAD Designer',
                                        icon: <Palette size={20} />,
                                        desc: 'Automate simple, repeated analysis tasks using recorded macros and custom design-rule interfaces.',
                                    },
                                    {
                                        role: 'CAE Engineer',
                                        icon: <Monitor size={20} />,
                                        desc: 'Reduce modeling time, cut workload, and improve productivity through workflow automation.',
                                    },
                                    {
                                        role: 'CAE Expert',
                                        icon: <Code2 size={20} />,
                                        desc: 'Build advanced simulations with multi-software data exchange and custom algorithms.',
                                    },
                                    {
                                        role: 'CAE Company',
                                        icon: <Building size={20} />,
                                        desc: 'Build in-house CAD-CAE automation systems with custom templates, wizards, and reports.',
                                    },
                                ].map((p, i) => (
                                    <Reveal key={i} delay={150 + i * 80}>
                                        <GlowCard>
                                            <div className="p-6">
                                                <div className="text-blue mb-4">{p.icon}</div>
                                                <h4 className="font-semibold text-sm mb-2">
                                                    {p.role}
                                                </h4>
                                                <p className="text-xs text-text-secondary leading-relaxed">
                                                    {p.desc}
                                                </p>
                                            </div>
                                        </GlowCard>
                                    </Reveal>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ════════════ 4F PHILOSOPHY ════════════ */}
            <section className="py-32 bg-bg-elevated relative">
                <div className="absolute inset-0 bg-dots opacity-50" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-20">
                            <SectionLabel label="Philosophy" />
                            <h2 className="text-4xl sm:text-5xl font-bold mb-4">
                                The <span className="gradient-text-blue">4F</span> Design Principle
                            </h2>
                            <p className="text-text-secondary max-w-2xl mx-auto">
                                PSJ is developed with four core principles to solve every CAE
                                automation challenge — from beginners to enterprise-grade
                                deployment.
                            </p>
                        </div>
                    </Reveal>

                    {/* Bento grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-px bg-border">
                        {fourF.map((f, i) => (
                            <Reveal key={i} delay={i * 100}>
                                <div className="bg-bg-elevated p-8 lg:p-10 h-full group hover:bg-bg-card transition-colors duration-300 relative overflow-hidden">
                                    <div
                                        className={`absolute top-0 left-0 right-0 h-px bg-gradient-to-r ${f.color}`}
                                    />
                                    <div className="text-blue mb-6 group-hover:scale-110 transition-transform duration-300">
                                        {f.icon}
                                    </div>
                                    <h3 className="text-2xl font-bold mb-1">{f.title}</h3>
                                    <p className="text-xs text-blue mb-4 font-medium">
                                        {f.subtitle}
                                    </p>
                                    <p className="text-sm text-text-secondary leading-relaxed">
                                        {f.desc}
                                    </p>
                                </div>
                            </Reveal>
                        ))}
                    </div>
                </div>
            </section>

            {/* ════════════ PRODUCT SHOWCASE ════════════ */}
            <section className="py-32 bg-bg relative">
                <div className="absolute inset-0 bg-grid opacity-20" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <div className="grid lg:grid-cols-2 gap-16 items-center">
                        <Reveal>
                            <div className="relative">
                                <div className="absolute -inset-4 bg-gradient-to-br from-blue/10 via-transparent to-cyan/5" />
                                <img
                                    src="/images/product-ui.jpg"
                                    alt="PSJ Workspace"
                                    className="relative w-full border border-landing-border"
                                />
                                <div className="absolute -bottom-4 -right-4 bg-bg-card border border-landing-border px-4 py-2 flex items-center gap-2">
                                    <div className="w-2 h-2 bg-green-500 animate-pulse" />
                                    <span className="text-xs text-text-secondary">
                                        Live workspace
                                    </span>
                                </div>
                            </div>
                        </Reveal>

                        <div>
                            <Reveal delay={100}>
                                <SectionLabel label="Product" />
                                <h2 className="text-4xl sm:text-5xl font-bold leading-tight mb-6">
                                    Complete Python
                                    <br />
                                    <span className="text-text-secondary">
                                        development environment
                                    </span>
                                </h2>
                            </Reveal>
                            <Reveal delay={200}>
                                <p className="text-text-secondary leading-relaxed mb-8">
                                    PSJ provides a complete suite of tools — from macro recording
                                    for non-programmers to a full-featured IDE for experts — all
                                    integrated directly into Jupiter.
                                </p>
                            </Reveal>
                            <div className="space-y-4">
                                {[
                                    'Record macros without writing code',
                                    'Customized IDE with intelligent auto-complete',
                                    'Visual GUI builder for custom dialogs',
                                    'Interactive debugging shell',
                                    'Built-in Python 3 compiler',
                                    'VS Code extension available',
                                ].map((item, i) => (
                                    <Reveal key={i} delay={250 + i * 60}>
                                        <div className="flex items-center gap-3">
                                            <CheckCircle2
                                                size={16}
                                                className="text-blue shrink-0"
                                            />
                                            <span className="text-sm text-text-secondary">
                                                {item}
                                            </span>
                                        </div>
                                    </Reveal>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ════════════ ARCHITECTURE ════════════ */}
            <section id="architecture" className="py-32 bg-bg-elevated relative">
                <div className="absolute inset-0 bg-grid-dense opacity-30" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-16">
                            <SectionLabel label="Architecture" />
                            <h2 className="text-4xl sm:text-5xl font-bold mb-4">
                                Six integrated <span className="gradient-text-blue">modules</span>
                            </h2>
                            <p className="text-text-secondary max-w-2xl mx-auto">
                                PSJ is fully featured with tools and utilities that support writing
                                Python API scripts for Jupiter with ease — from recording to
                                deployment.
                            </p>
                        </div>
                    </Reveal>

                    {/* Module tabs */}
                    <Reveal delay={100}>
                        <div className="flex flex-wrap gap-0 border border-landing-border mb-0 bg-bg-card overflow-x-auto">
                            {archTabs.map((tab, i) => (
                                <button
                                    key={i}
                                    onClick={() => setActiveArch(i)}
                                    className={[
                                        'flex items-center gap-2 px-5 py-3.5 text-sm font-medium transition-all whitespace-nowrap',
                                        activeArch === i
                                            ? 'bg-blue text-white'
                                            : 'text-text-secondary hover:text-text hover:bg-bg-card-hover',
                                    ].join(' ')}
                                >
                                    {tab.icon} {tab.name}
                                </button>
                            ))}
                        </div>
                    </Reveal>

                    <Reveal delay={150}>
                        <div className="grid lg:grid-cols-2 gap-0 border border-t-0 border-landing-border">
                            {/* Description panel */}
                            <div className="p-8 lg:p-12 bg-bg-card flex flex-col justify-center border-b lg:border-b-0 lg:border-r border-landing-border">
                                <div className="text-blue mb-4">{archTabs[activeArch].icon}</div>
                                <h3 className="text-2xl font-bold mb-3">
                                    {archTabs[activeArch].name}
                                </h3>
                                <p className="text-text-secondary leading-relaxed">
                                    {archTabs[activeArch].desc}
                                </p>

                                {/* Flow breadcrumb */}
                                <div className="mt-8 flex flex-wrap items-center gap-2 text-xs text-text-muted">
                                    <span className="border border-landing-border px-2 py-1">
                                        Jupiter Dialog
                                    </span>
                                    <ChevronRight size={12} />
                                    <span
                                        className={`border px-2 py-1 ${activeArch < 3 ? 'border-blue text-blue' : 'border-landing-border'}`}
                                    >
                                        {activeArch < 3 ? archTabs[activeArch].name : 'PSJ Core'}
                                    </span>
                                    <ChevronRight size={12} />
                                    <span
                                        className={`border px-2 py-1 ${activeArch >= 3 ? 'border-blue text-blue' : 'border-landing-border'}`}
                                    >
                                        {activeArch >= 3 ? archTabs[activeArch].name : 'Tools'}
                                    </span>
                                    <ChevronRight size={12} />
                                    <span className="border border-landing-border px-2 py-1">
                                        User Function
                                    </span>
                                </div>
                            </div>

                            {/* Code panel */}
                            <div className="bg-bg-elevated p-0">
                                <div className="flex items-center gap-2 px-5 py-3 border-b border-landing-border bg-bg-elevated/30">
                                    <Hash size={12} className="text-text-muted" />
                                    <span className="text-xs text-text-muted code-font">
                                        {archTabs[activeArch].name
                                            .toLowerCase()
                                            .replace(/\s/g, '_')}
                                        .py
                                    </span>
                                </div>
                                <pre className="p-6 text-sm leading-7 code-font text-text-secondary overflow-x-auto whitespace-pre">
                                    {archTabs[activeArch].code}
                                </pre>
                            </div>
                        </div>
                    </Reveal>
                </div>
            </section>

            {/* ════════════ FEATURES GRID ════════════ */}
            <section id="features" className="py-32 bg-bg relative">
                <div className="absolute inset-0 bg-grid opacity-20" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-20">
                            <SectionLabel label="Features" />
                            <h2 className="text-4xl sm:text-5xl font-bold mb-4">
                                Everything you need to
                                <br />
                                <span className="text-text-secondary">automate CAE</span>
                            </h2>
                        </div>
                    </Reveal>

                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-px bg-border">
                        {features.map((f, i) => (
                            <Reveal key={i} delay={i * 80}>
                                <div className="bg-bg p-8 lg:p-10 h-full group hover:bg-bg-card/50 transition-colors duration-300">
                                    <div className="text-blue mb-5">{f.icon}</div>
                                    <h3 className="text-lg font-semibold mb-2">{f.title}</h3>
                                    <p className="text-sm text-text-secondary leading-relaxed mb-5">
                                        {f.desc}
                                    </p>
                                    <ul className="space-y-2">
                                        {f.bullets.map((b, j) => (
                                            <li
                                                key={j}
                                                className="flex items-center gap-2 text-xs text-text-muted"
                                            >
                                                <div className="w-1 h-1 bg-blue" />
                                                {b}
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            </Reveal>
                        ))}
                    </div>
                </div>
            </section>

            {/* ════════════ STATS BAND ════════════ */}
            <section className="py-20 bg-blue relative overflow-hidden">
                <div className="absolute inset-0 bg-grid opacity-10" />
                <div className="absolute -top-20 -right-20 w-80 h-80 bg-white/5 blur-[80px]" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <div className="grid grid-cols-2 lg:grid-cols-4 gap-px">
                        {[
                            { value: 10, suffix: 'x', label: 'Faster workflow' },
                            { value: 500, suffix: '+', label: 'Engineers worldwide' },
                            { value: 98, suffix: '%', label: 'Task automation' },
                            { value: 50, suffix: '+', label: 'API modules' },
                        ].map((s, i) => (
                            <div key={i} className="text-center py-6">
                                <div className="text-4xl sm:text-5xl font-bold text-white mb-2">
                                    <Counter end={s.value} suffix={s.suffix} />
                                </div>
                                <div className="text-sm text-white/60">{s.label}</div>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* ════════════ USE CASES ════════════ */}
            <section id="usecases" className="py-32 bg-bg relative">
                <div className="absolute inset-0 bg-dots opacity-30" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <div className="grid lg:grid-cols-5 gap-16">
                        {/* Left */}
                        <div className="lg:col-span-2">
                            <Reveal>
                                <SectionLabel label="Applications" />
                                <h2 className="text-4xl sm:text-5xl font-bold leading-tight mb-6">
                                    Real-world
                                    <br />
                                    <span className="text-text-secondary">applications</span>
                                </h2>
                                <p className="text-text-secondary leading-relaxed mb-8">
                                    From parametric bolt modeling to AI-driven hull design — PSJ
                                    powers production-grade CAE automation across industries.
                                </p>
                            </Reveal>

                            <Reveal delay={100}>
                                <div className="relative">
                                    <div className="absolute -inset-3 bg-gradient-to-br from-blue/10 to-transparent" />
                                    <img
                                        src="/images/cae-analysis.jpg"
                                        alt="CAE Analysis"
                                        className="relative w-full border border-landing-border"
                                    />
                                </div>
                            </Reveal>
                        </div>

                        {/* Right: use-case cards */}
                        <div className="lg:col-span-3 grid sm:grid-cols-2 gap-4">
                            {useCases.map((uc, i) => (
                                <Reveal key={i} delay={i * 80}>
                                    <GlowCard className="h-full">
                                        <div className="p-6">
                                            <div className="text-blue mb-4">{uc.icon}</div>
                                            <h4 className="font-semibold text-sm mb-2">
                                                {uc.title}
                                            </h4>
                                            <p className="text-xs text-text-secondary leading-relaxed">
                                                {uc.desc}
                                            </p>
                                        </div>
                                    </GlowCard>
                                </Reveal>
                            ))}
                        </div>
                    </div>
                </div>
            </section>

            {/* ════════════ END-TO-END PIPELINE ════════════ */}
            <section className="py-32 bg-bg-elevated relative overflow-hidden">
                <div className="absolute inset-0 bg-grid-dense opacity-20" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-20">
                            <SectionLabel label="Pipeline" />
                            <h2 className="text-4xl sm:text-5xl font-bold mb-4">
                                End-to-end <span className="gradient-text-blue">automation</span>
                            </h2>
                            <p className="text-text-secondary max-w-2xl mx-auto">
                                From model import to report generation — one Python script controls
                                the entire workflow.
                            </p>
                        </div>
                    </Reveal>

                    {/* Pipeline steps */}
                    <div className="grid grid-cols-2 md:grid-cols-5 gap-px bg-border mb-16">
                        {[
                            {
                                step: '01',
                                label: 'Import',
                                icon: <Database size={20} />,
                                desc: 'Load CAD & FEM',
                            },
                            {
                                step: '02',
                                label: 'Mesh',
                                icon: <Boxes size={20} />,
                                desc: 'Auto hex/tet mesh',
                            },
                            {
                                step: '03',
                                label: 'Solve',
                                icon: <Cpu size={20} />,
                                desc: 'Run analysis',
                            },
                            {
                                step: '04',
                                label: 'Analyze',
                                icon: <BarChart3 size={20} />,
                                desc: 'Post-process',
                            },
                            {
                                step: '05',
                                label: 'Report',
                                icon: <FileText size={20} />,
                                desc: 'Export results',
                            },
                        ].map((p, i) => (
                            <Reveal key={i} delay={i * 100}>
                                <div className="bg-bg-elevated p-6 lg:p-8 text-center group hover:bg-bg-card transition-colors">
                                    <span className="text-[10px] tracking-[0.2em] uppercase text-text-muted block mb-4">
                                        {p.step}
                                    </span>
                                    <div className="text-blue mb-3 flex justify-center group-hover:scale-110 transition-transform">
                                        {p.icon}
                                    </div>
                                    <h4 className="font-semibold text-sm mb-1">{p.label}</h4>
                                    <p className="text-xs text-text-muted">{p.desc}</p>
                                </div>
                            </Reveal>
                        ))}
                    </div>

                    {/* Full pipeline code block */}
                    <Reveal delay={200}>
                        <div className="relative max-w-4xl mx-auto">
                            <div className="absolute -inset-px bg-gradient-to-b from-blue/20 via-transparent to-transparent" />
                            <div className="relative bg-bg-elevated border border-landing-border">
                                <div className="flex items-center justify-between px-5 py-3 border-b border-landing-border">
                                    <div className="flex items-center gap-2">
                                        <Terminal size={14} className="text-text-muted" />
                                        <span className="text-xs text-text-muted code-font">
                                            pipeline.py
                                        </span>
                                    </div>
                                    <span className="text-[10px] text-text-muted border border-landing-border px-2 py-0.5">
                                        Python 3.x
                                    </span>
                                </div>
                                <pre className="p-6 sm:p-8 text-sm leading-7 code-font text-text-secondary overflow-x-auto">{`import psj
from psj.utility import get_model_info
import pandas as pd

# Step 1: Import model
model = psj.load("vehicle_chassis.jdb")
info = get_model_info(model)
print(f"Loaded: {info['name']} — {info['bodies']} bodies")

# Step 2: Automated meshing
for body in model.bodies:
    psj.mesh.auto_hex(body, size=2.0, quality="high")

# Step 3: Apply loads and solve
psj.analysis.apply_load("LC_gravity", type="gravity")
psj.analysis.run_static(model, solver="direct")

# Step 4: Post-process results
stress = psj.post.get_stress(model, type="vonMises")
critical = stress[stress.max() > 250.0]

# Step 5: Generate report
psj.report.to_pptx(model, template="report_v2.pptx")
psj.report.to_html(model, output="results/index.html")`}</pre>
                            </div>
                        </div>
                    </Reveal>
                </div>
            </section>

            {/* ════════════ INDUSTRIES ════════════ */}
            <section className="py-32 bg-bg relative">
                <div className="absolute inset-0 bg-grid opacity-20" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-20">
                            <SectionLabel label="Industries" />
                            <h2 className="text-4xl sm:text-5xl font-bold mb-4">
                                Powering simulation across
                                <br />
                                <span className="text-text-secondary">every engineering field</span>
                            </h2>
                        </div>
                    </Reveal>

                    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-px bg-border">
                        {industries.map((ind, i) => (
                            <Reveal key={i} delay={i * 60}>
                                <div className="bg-bg p-6 lg:p-8 text-center group hover:bg-bg-card/50 transition-colors h-full">
                                    <div className="text-text-muted group-hover:text-blue transition-colors mb-4 flex justify-center">
                                        {ind.icon}
                                    </div>
                                    <h4 className="font-semibold text-sm mb-1">{ind.name}</h4>
                                    <p className="text-[11px] text-text-muted leading-relaxed">
                                        {ind.desc}
                                    </p>
                                </div>
                            </Reveal>
                        ))}
                    </div>
                </div>
            </section>

            {/* ════════════ PYTHON ECOSYSTEM ════════════ */}
            <section className="py-24 bg-bg-elevated border-y border-landing-border relative">
                <div className="absolute inset-0 bg-dots opacity-30" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-16">
                            <SectionLabel label="Ecosystem" />
                            <h2 className="text-3xl sm:text-4xl font-bold mb-3">
                                Built on <span className="gradient-text-blue">Python 3</span>
                            </h2>
                            <p className="text-text-secondary max-w-xl mx-auto text-sm">
                                PSJ includes the most popular scientific Python libraries out of the
                                box.
                            </p>
                        </div>
                    </Reveal>

                    <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-px bg-border">
                        {[
                            { name: 'NumPy', desc: 'Numerical computing' },
                            { name: 'Pandas', desc: 'Data analysis' },
                            { name: 'Matplotlib', desc: 'Visualization' },
                            { name: 'scikit-learn', desc: 'Machine learning' },
                            { name: 'numba', desc: 'JIT compilation' },
                            { name: 'python-pptx', desc: 'Report generation' },
                        ].map((lib, i) => (
                            <Reveal key={i} delay={i * 60}>
                                <div className="bg-bg-elevated p-6 text-center group hover:bg-bg-card transition-colors">
                                    <div className="text-lg font-bold text-text group-hover:text-blue transition-colors mb-1">
                                        {lib.name}
                                    </div>
                                    <p className="text-[11px] text-text-muted">{lib.desc}</p>
                                </div>
                            </Reveal>
                        ))}
                    </div>
                </div>
            </section>

            {/* ════════════ RESOURCES ════════════ */}
            <section id="resources" className="py-32 bg-bg relative">
                <div className="absolute inset-0 bg-grid opacity-15" />
                <div className="relative max-w-7xl mx-auto px-6">
                    <Reveal>
                        <div className="text-center mb-20">
                            <SectionLabel label="Resources" />
                            <h2 className="text-4xl sm:text-5xl font-bold mb-4">
                                Get started <span className="text-text-secondary">quickly</span>
                            </h2>
                        </div>
                    </Reveal>

                    <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-px bg-border">
                        {[
                            {
                                icon: <BookOpen size={22} />,
                                title: 'Documentation',
                                desc: 'Complete API reference, guides, and tutorials for every PSJ module.',
                            },
                            {
                                icon: <Play size={22} />,
                                title: 'Video Tutorials',
                                desc: 'Step-by-step video walkthroughs from basic macro recording to advanced scripting.',
                            },
                            {
                                icon: <Code2 size={22} />,
                                title: 'Code Examples',
                                desc: 'Production-ready sample scripts for common CAE automation tasks.',
                            },
                            {
                                icon: <Target size={22} />,
                                title: 'Sample Applications',
                                desc: 'Full application examples including bolt modeling, report generation, and more.',
                            },
                        ].map((r, i) => (
                            <Reveal key={i} delay={i * 80}>
                                <div className="bg-bg p-8 h-full group hover:bg-bg-card/50 transition-colors">
                                    <div className="text-text-muted group-hover:text-blue transition-colors mb-5">
                                        {r.icon}
                                    </div>
                                    <h4 className="font-semibold mb-2">{r.title}</h4>
                                    <p className="text-sm text-text-secondary leading-relaxed mb-4">
                                        {r.desc}
                                    </p>
                                    <span className="inline-flex items-center gap-1 text-xs text-blue font-medium group-hover:gap-2 transition-all">
                                        Learn more <ArrowUpRight size={12} />
                                    </span>
                                </div>
                            </Reveal>
                        ))}
                    </div>
                </div>
            </section>

            {/* ════════════ CTA ════════════ */}
            <section id="contact" className="py-32 bg-bg-elevated relative overflow-hidden">
                <div className="absolute inset-0 bg-grid opacity-20" />
                <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-blue/[0.08] blur-[150px]" />
                <div className="relative max-w-3xl mx-auto px-6 text-center">
                    <Reveal>
                        <SectionLabel label="Get Started" />
                    </Reveal>
                    <Reveal delay={100}>
                        <h2 className="text-4xl sm:text-6xl font-bold leading-tight mb-6">
                            Ready to automate
                            <br />
                            your CAE workflow?
                        </h2>
                    </Reveal>
                    <Reveal delay={200}>
                        <p className="text-lg text-text-secondary mb-10 max-w-xl mx-auto">
                            Join hundreds of engineers worldwide who use PSJ to eliminate repetitive
                            tasks and build custom automation solutions.
                        </p>
                    </Reveal>
                    <Reveal delay={300}>
                        <div className="flex flex-wrap justify-center gap-4">
                            <a
                                href="https://www.e-technostar.com/our-products/15394"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="group bg-blue hover:bg-blue-bright text-white font-medium px-8 py-4 text-sm flex items-center gap-2 transition-all"
                            >
                                Request a Demo{' '}
                                <ArrowRight
                                    size={16}
                                    className="group-hover:translate-x-1 transition-transform"
                                />
                            </a>
                            <a
                                href="https://www.e-technostar.com/our-products/15394"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="group border border-landing-border hover:border-landing-border-hover text-text-secondary hover:text-text font-medium px-8 py-4 text-sm flex items-center gap-2 transition-all"
                            >
                                View Documentation <ExternalLink size={14} />
                            </a>
                        </div>
                    </Reveal>
                    <Reveal delay={400}>
                        <div className="flex flex-wrap justify-center gap-6 mt-12 text-xs text-text-muted">
                            {[
                                'Free evaluation available',
                                'Enterprise licensing',
                                'Dedicated support',
                            ].map((t) => (
                                <span key={t} className="flex items-center gap-2">
                                    <CheckCircle2 size={12} className="text-blue" />
                                    {t}
                                </span>
                            ))}
                        </div>
                    </Reveal>
                </div>
            </section>

            {/* ════════════ FOOTER ════════════ */}
            <footer className="border-t border-landing-border bg-bg py-16">
                <div className="max-w-7xl mx-auto px-6">
                    <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                        {/* Brand */}
                        <div>
                            <div className="flex items-center gap-3 mb-4">
                                <div className="w-7 h-7 bg-blue flex items-center justify-center">
                                    <span className="text-white font-black text-xs">PSJ</span>
                                </div>
                                <span className="text-sm font-semibold">
                                    Python Scripting for Jupiter
                                </span>
                            </div>
                            <p className="text-xs text-text-muted leading-relaxed">
                                A product of e-TechnoStar Co., Ltd.
                                <br />
                                Enabling CAE automation through Python scripting.
                            </p>
                        </div>

                        {/* Product links */}
                        <div>
                            <h5 className="text-xs font-semibold tracking-[0.15em] uppercase text-text-muted mb-4">
                                Product
                            </h5>
                            <ul className="space-y-2.5 text-sm text-text-secondary">
                                {[
                                    { label: 'Overview', href: '#overview' },
                                    { label: 'Features', href: '#features' },
                                    { label: 'Architecture', href: '#architecture' },
                                    { label: 'Use Cases', href: '#usecases' },
                                ].map(({ label, href }) => (
                                    <li key={label}>
                                        <a
                                            href={href}
                                            className="hover:text-text transition-colors"
                                        >
                                            {label}
                                        </a>
                                    </li>
                                ))}
                            </ul>
                        </div>

                        {/* Module links */}
                        <div>
                            <h5 className="text-xs font-semibold tracking-[0.15em] uppercase text-text-muted mb-4">
                                Modules
                            </h5>
                            <ul className="space-y-2.5 text-sm text-text-secondary">
                                {['Macro', 'PSJ-Command', 'PSJ-Utility', 'PSJ-GUI'].map((m) => (
                                    <li key={m}>
                                        <a
                                            href="#architecture"
                                            className="hover:text-text transition-colors"
                                        >
                                            {m}
                                        </a>
                                    </li>
                                ))}
                            </ul>
                        </div>

                        {/* Company links */}
                        <div>
                            <h5 className="text-xs font-semibold tracking-[0.15em] uppercase text-text-muted mb-4">
                                Company
                            </h5>
                            <ul className="space-y-2.5 text-sm text-text-secondary">
                                <li>
                                    <a
                                        href="https://www.e-technostar.com"
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="hover:text-text transition-colors"
                                    >
                                        e-TechnoStar
                                    </a>
                                </li>
                                <li>
                                    <a
                                        href="https://www.e-technostar.com/our-products/15394"
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="hover:text-text transition-colors"
                                    >
                                        Documentation
                                    </a>
                                </li>
                                <li>
                                    <a
                                        href="#contact"
                                        className="hover:text-text transition-colors"
                                    >
                                        Contact
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>

                    {/* Bottom bar */}
                    <div className="border-t border-landing-border pt-8 flex flex-col sm:flex-row items-center justify-between gap-4">
                        <p className="text-xs text-text-muted">
                            © {new Date().getFullYear()} e-TechnoStar Co., Ltd. All rights reserved.
                        </p>
                        <div className="flex items-center gap-6 text-xs text-text-muted">
                            <a href="#" className="hover:text-text transition-colors">
                                Privacy
                            </a>
                            <a href="#" className="hover:text-text transition-colors">
                                Terms
                            </a>
                            <a
                                href="https://www.e-technostar.com"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="hover:text-text transition-colors flex items-center gap-1"
                            >
                                e-technostar.com <ExternalLink size={10} />
                            </a>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
}
