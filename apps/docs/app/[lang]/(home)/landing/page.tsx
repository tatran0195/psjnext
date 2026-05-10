'use client';
import Link from 'next/link';
import { motion } from 'framer-motion';
import {
    ArrowRight, CheckCircle2, ChevronRight,
    Cpu, Zap, Settings, Layers, Globe2,
    Users, Award, Building2, TrendingUp,
    Car, Plane, Ship, Factory, Atom,
    Play, BarChart3, MousePointerClick, Code2, Terminal, Wrench,
} from 'lucide-react';

/* ── Animation helper ──────────────────────────────────────────────────────── */
function FadeUp({
    children,
    delay = 0,
    className = '',
}: { children: React.ReactNode; delay?: number; className?: string }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 18 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: '-40px' }}
            transition={{ duration: 0.45, delay: delay * 0.001, ease: [0.16, 1, 0.3, 1] }}
            className={className}
        >
            {children}
        </motion.div>
    );
}

/* ── Stat card ─────────────────────────────────────────────────────────────── */
function StatCard({ icon, value, label }: { icon: React.ReactNode; value: string; label: string }) {
    return (
        <div
            className="flex flex-col gap-2 p-6"
            style={{ borderRight: '1px solid var(--psj-border)', borderBottom: '1px solid var(--psj-border)' }}
        >
            <div className="flex items-center gap-2 text-[10px] uppercase tracking-widest font-bold"
                style={{ color: 'var(--psj-text-3)' }}>
                {icon} {label}
            </div>
            <div className="text-3xl font-extrabold num-marker tracking-tighter"
                style={{ color: 'var(--psj-text-1)' }}>
                {value}
            </div>
        </div>
    );
}

/* ── Section header ────────────────────────────────────────────────────────── */
function SectionHeader({
    label, title, subtitle, link, linkLabel,
}: {
    label: string; title: string; subtitle?: string;
    link?: string; linkLabel?: string;
}) {
    return (
        <FadeUp className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
            <div>
                <div className="psj-label mb-3">{label}</div>
                <h2 className="psj-h2 text-balance" style={{ color: 'var(--psj-text-1)' }}>{title}</h2>
                {subtitle && (
                    <p className="mt-3 text-base leading-relaxed max-w-xl" style={{ color: 'var(--psj-text-2)' }}>
                        {subtitle}
                    </p>
                )}
            </div>
            {link && linkLabel && (
                <Link
                    href={link}
                    className="group inline-flex items-center gap-2 text-sm font-bold shrink-0 transition-colors"
                    style={{ color: 'var(--psj-blue)' }}
                >
                    {linkLabel}
                    <ArrowRight size={15} className="group-hover:translate-x-1 transition-transform" />
                </Link>
            )}
        </FadeUp>
    );
}

/* ═══════════════════════════════════════════════════════════════════════════════
   PAGE
   ═══════════════════════════════════════════════════════════════════════════════ */
export default function LandingPage() {
    const modules = [
        { icon: Play,              label: 'Macro',         desc: 'Auto-recorded script equivalents of Jupiter GUI operations.', color: '#0099CC' },
        { icon: Terminal,          label: 'PSJ-Command',   desc: 'Command-language replay of any Jupiter dialog function.',     color: '#5B3BB8' },
        { icon: Cpu,               label: 'PSJ-Utility',   desc: 'Query model database: IDs, names, colors, geometry.',         color: '#00875A' },
        { icon: MousePointerClick, label: 'PSJ-GUI',       desc: 'Visual GUI Command Builder — no code required.',              color: '#D4570D' },
        { icon: Terminal,          label: 'Custom Shell',  desc: 'Interactive debug shell with real-time error output.',        color: '#B86E00' },
        { icon: Code2,             label: 'Custom IDE',    desc: 'Smart IDE with auto-complete and predictive tips.',           color: '#004EA2' },
    ];

    const fourF = [
        { label: 'Friendly',   sub: 'Even non-programmers',  desc: 'Macro recording means anyone can automate workflows without writing code.',           icon: MousePointerClick },
        { label: 'Fast',       sub: 'Through automation',    desc: 'Eliminate repetitive operations. Hours of work become seconds of script.',            icon: Zap },
        { label: 'Functional', sub: 'IDE & GUI Builder',     desc: 'Built-in development tools with full predictive tips and dialog builder.',            icon: Wrench },
        { label: 'Flexible',   sub: 'Advanced simulation',   desc: 'Full Python 3 ecosystem — NumPy, Pandas, scikit-learn, pptx and more.',              icon: Settings },
    ];

    const industries = [
        { icon: Car,     name: 'Automotive',    clients: '40+' },
        { icon: Plane,   name: 'Aerospace',     clients: '25+' },
        { icon: Ship,    name: 'Marine',        clients: '15+' },
        { icon: Factory, name: 'Manufacturing', clients: '30+' },
        { icon: Atom,    name: 'Energy',        clients: '10+' },
    ];

    return (
        <>
            {/* ══════════════════════════════════════════════════════════════════
                HERO — CAE Engineering background
            ════════════════════════════════════════════════════════════════════ */}
            <section className="cae-hero-bg" style={{ borderBottom: '1px solid var(--psj-border)' }}>
                {/* Animated mesh dots */}
                <div className="cae-hero-dots" />
                {/* Animated scan line */}
                <div className="cae-scan-line" />

                <div className="psj-container py-20 lg:py-32 relative z-10">
                    <div className="grid lg:grid-cols-12 gap-12 lg:gap-16 items-center">
                        {/* Left — Text */}
                        <div className="lg:col-span-7">
                            <FadeUp>
                                <div className="inline-flex items-center gap-2 mb-8"
                                    style={{
                                        border: '1px solid var(--psj-blue)',
                                        background: 'var(--psj-blue-subtle)',
                                        padding: '5px 12px',
                                    }}>
                                    <span className="w-1.5 h-1.5 rounded-full animate-pulse" style={{ background: 'var(--psj-blue)' }} />
                                    <span className="text-[10px] uppercase tracking-[0.25em] font-bold"
                                        style={{ color: 'var(--psj-blue)' }}>
                                        PSJ v5.1 — Production Release
                                    </span>
                                </div>
                            </FadeUp>

                            <FadeUp delay={80}>
                                <h1 className="psj-h1 text-balance mb-6" style={{ color: 'var(--psj-text-1)' }}>
                                    Python Scripting<br />
                                    <span style={{ color: 'var(--psj-blue)' }}>for Jupiter</span>
                                </h1>
                            </FadeUp>

                            <FadeUp delay={160}>
                                <p className="text-lg leading-relaxed max-w-xl mb-10 text-balance"
                                    style={{ color: 'var(--psj-text-2)' }}>
                                    The industry-standard CAE automation platform. Build production-grade
                                    simulation workflows with the full power of Python 3.
                                </p>
                            </FadeUp>

                            <FadeUp delay={240}>
                                <div className="flex flex-wrap gap-4">
                                    <Link href="/docs" className="psj-btn-primary">
                                        Get Started <ArrowRight size={15} />
                                    </Link>
                                    <Link href="/tutorials" className="psj-btn-secondary">
                                        <Play size={15} /> View Tutorials
                                    </Link>
                                </div>
                            </FadeUp>

                            <FadeUp delay={320}>
                                <div className="flex flex-wrap items-center gap-5 mt-10 pt-8 text-xs"
                                    style={{ borderTop: '1px solid var(--psj-border)', color: 'var(--psj-text-3)' }}>
                                    {['Python 3.x Built-in', 'NumPy · Pandas · scikit-learn', 'VS Code Extension', 'PowerPoint Export'].map(t => (
                                        <span key={t} className="flex items-center gap-1.5">
                                            <CheckCircle2 size={11} style={{ color: 'var(--psj-blue)' }} /> {t}
                                        </span>
                                    ))}
                                </div>
                            </FadeUp>
                        </div>

                        {/* Right — Code card */}
                        <FadeUp delay={200} className="lg:col-span-5">
                            <div style={{
                                border: '1px solid var(--psj-border)',
                                background: 'var(--psj-surface-1)',
                            }}>
                                {/* Window chrome */}
                                <div className="flex items-center justify-between px-4 py-3"
                                    style={{ borderBottom: '1px solid var(--psj-border)', background: 'var(--psj-surface-2)' }}>
                                    <div className="flex items-center gap-1.5">
                                        {['#EF4444', '#F59E0B', '#22C55E'].map(c => (
                                            <div key={c} style={{ width: '10px', height: '10px', background: c, opacity: 0.7 }} />
                                        ))}
                                    </div>
                                    <span className="font-mono text-[10px]" style={{ color: 'var(--psj-text-3)' }}>
                                        automate.py — PSJ v5.1
                                    </span>
                                    <span className="text-[10px] font-medium px-2 py-0.5"
                                        style={{ border: '1px solid var(--psj-border)', color: 'var(--psj-text-3)' }}>
                                        Python 3.x
                                    </span>
                                </div>
                                {/* Code */}
                                <div className="p-6 font-mono text-sm leading-relaxed"
                                    style={{ background: 'var(--psj-surface-0)', color: 'var(--psj-text-2)' }}>
                                    <div className="space-y-1">
                                        <p>
                                            <span style={{ color: 'var(--psj-blue)', fontWeight: 600 }}>from</span>
                                            {' '}psj{' '}
                                            <span style={{ color: 'var(--psj-blue)', fontWeight: 600 }}>import</span>
                                            {' '}*
                                        </p>
                                        <p className="text-[11px]" style={{ color: 'var(--psj-text-3)' }}># Macro — auto-recorded after UI operation</p>
                                        <p>CreateCube([0,0,0], [10,10,10], <span style={{ color: '#D4570D' }}>"Cube_1"</span>)</p>
                                        <p>ImprintLines([[7.8,0,10],[2.2,10,10]], [6:26], 1)</p>
                                        <p className="mt-3 text-[11px]" style={{ color: 'var(--psj-text-3)' }}># PSJ-Utility — query model data</p>
                                        <p>nodes = psj.utility.<span style={{ color: 'var(--psj-blue)' }}>get_node_coords</span>(model)</p>
                                        <p className="mt-3 text-[11px]" style={{ color: 'var(--psj-text-3)' }}># PSJ-GUI — custom dialog</p>
                                        <p>dlg = psj.gui.<span style={{ color: 'var(--psj-blue)' }}>Dialog</span>(<span style={{ color: '#D4570D' }}>"Bolt Generator"</span>)</p>
                                        <p>dlg.<span style={{ color: 'var(--psj-blue)' }}>add_input</span>(<span style={{ color: '#D4570D' }}>"diameter"</span>, 12.0)</p>
                                        <p>dlg.<span style={{ color: 'var(--psj-blue)' }}>show</span>()</p>
                                        <p className="animate-pulse" style={{ color: 'var(--psj-blue)' }}>▊</p>
                                    </div>
                                </div>
                                {/* Status bar */}
                                <div className="px-4 py-2 flex items-center justify-between text-[10px]"
                                    style={{ borderTop: '1px solid var(--psj-border)', background: 'var(--psj-surface-2)', color: 'var(--psj-text-3)' }}>
                                    <span className="flex items-center gap-1.5">
                                        <span style={{ width: '6px', height: '6px', background: '#22C55E', display: 'inline-block' }} />
                                        Connected to Jupiter
                                    </span>
                                    <span>PSJ v5.1.1 Stable</span>
                                </div>
                            </div>
                        </FadeUp>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════════════════════════════
                STATS
            ════════════════════════════════════════════════════════════════════ */}
            <section style={{ borderBottom: '1px solid var(--psj-border)' }}>
                <div className="psj-container">
                    <div className="grid grid-cols-2 lg:grid-cols-4"
                        style={{ borderLeft: '1px solid var(--psj-border)', borderTop: '1px solid var(--psj-border)' }}>
                        <StatCard icon={<Award size={13} />}     value="15+"  label="Years Experience" />
                        <StatCard icon={<Users size={13} />}     value="120+" label="Global Clients" />
                        <StatCard icon={<Building2 size={13} />} value="40+"  label="Specialists" />
                        <StatCard icon={<TrendingUp size={13} />} value="10×" label="Faster Workflow" />
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════════════════════════════
                4F PHILOSOPHY
            ════════════════════════════════════════════════════════════════════ */}
            <section style={{ background: 'var(--psj-surface-1)', borderBottom: '1px solid var(--psj-border)' }}>
                <div className="psj-container psj-section">
                    <div className="grid lg:grid-cols-12 gap-12 lg:gap-16 items-start">
                        {/* Left */}
                        <div className="lg:col-span-4">
                            <FadeUp>
                                <div className="psj-label mb-4">Core Philosophy</div>
                                <h2 className="psj-h2 text-balance mb-6" style={{ color: 'var(--psj-text-1)' }}>
                                    The 4F Design Principle
                                </h2>
                                <p className="text-base leading-relaxed mb-8" style={{ color: 'var(--psj-text-2)' }}>
                                    PSJ is built around four core engineering principles — designed to solve every
                                    CAE automation challenge across organizations of all sizes.
                                </p>
                                <Link href="/docs"
                                    className="group inline-flex items-center gap-2 text-sm font-bold transition-colors"
                                    style={{ color: 'var(--psj-blue)' }}>
                                    Read the documentation
                                    <ArrowRight size={15} className="group-hover:translate-x-1 transition-transform" />
                                </Link>
                            </FadeUp>
                        </div>
                        {/* Right — grid of 4 cards */}
                        <div className="lg:col-span-8 grid sm:grid-cols-2 gap-5">
                            {fourF.map((f, i) => (
                                <FadeUp key={f.label} delay={i * 50}>
                                    <div className="psj-card-interactive p-7 h-full">
                                        <div className="flex items-center gap-4 mb-5">
                                            <div className="flex items-center justify-center w-11 h-11"
                                                style={{ background: 'var(--psj-blue-subtle)', border: '1px solid var(--psj-blue-subtle2)' }}>
                                                <f.icon size={20} style={{ color: 'var(--psj-blue)' }} />
                                            </div>
                                            <div>
                                                <div className="font-bold text-base tracking-tight" style={{ color: 'var(--psj-text-1)' }}>{f.label}</div>
                                                <div className="text-[10px] uppercase tracking-widest font-bold" style={{ color: 'var(--psj-blue)' }}>{f.sub}</div>
                                            </div>
                                        </div>
                                        <p className="text-sm leading-relaxed" style={{ color: 'var(--psj-text-2)' }}>{f.desc}</p>
                                    </div>
                                </FadeUp>
                            ))}
                        </div>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════════════════════════════
                MODULES
            ════════════════════════════════════════════════════════════════════ */}
            <section style={{ background: 'var(--psj-surface-0)', borderBottom: '1px solid var(--psj-border)' }}>
                <div className="psj-container psj-section">
                    <SectionHeader
                        label="System Architecture"
                        title="Six Integrated Modules"
                        link="/docs"
                        linkLabel="View architecture docs"
                    />
                    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
                        {modules.map((m, i) => (
                            <FadeUp key={m.label} delay={i * 50}>
                                <div className="psj-card p-7 group h-full"
                                    style={{ borderTop: `2px solid ${m.color}` }}>
                                    <div className="flex items-center gap-3 mb-5">
                                        <div className="w-10 h-10 flex items-center justify-center"
                                            style={{
                                                background: `${m.color}12`,
                                                border: `1px solid ${m.color}25`,
                                            }}>
                                            <m.icon size={17} style={{ color: m.color }} />
                                        </div>
                                        <span className="font-bold text-base tracking-tight" style={{ color: 'var(--psj-text-1)' }}>
                                            {m.label}
                                        </span>
                                    </div>
                                    <p className="text-sm leading-relaxed mb-5" style={{ color: 'var(--psj-text-2)' }}>{m.desc}</p>
                                    <Link href="/docs"
                                        className="inline-flex items-center gap-1 text-xs font-bold opacity-0 group-hover:opacity-100 transition-all translate-y-1 group-hover:translate-y-0"
                                        style={{ color: 'var(--psj-blue)' }}>
                                        Explore module <ChevronRight size={12} />
                                    </Link>
                                </div>
                            </FadeUp>
                        ))}
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════════════════════════════
                INDUSTRIES
            ════════════════════════════════════════════════════════════════════ */}
            <section style={{ background: 'var(--psj-surface-1)', borderBottom: '1px solid var(--psj-border)' }}>
                <div className="psj-container psj-section-sm">
                    <div className="flex flex-col lg:flex-row items-start lg:items-center gap-12">
                        <div className="shrink-0 max-w-xs">
                            <div className="psj-label mb-3">Industries Served</div>
                            <h3 className="psj-h3 text-balance mb-4" style={{ color: 'var(--psj-text-1)' }}>
                                Trusted by 120+ leading manufacturers
                            </h3>
                            <p className="text-sm leading-relaxed" style={{ color: 'var(--psj-text-2)' }}>
                                Deployed across major industrial sectors, providing mission-critical
                                automation for tier-1 suppliers and OEMs.
                            </p>
                        </div>
                        <div className="flex-1 grid grid-cols-2 sm:grid-cols-5 gap-4">
                            {industries.map((ind) => (
                                <div key={ind.name} className="psj-card-interactive p-5 text-center group">
                                    <ind.icon size={22} className="mx-auto mb-3 transition-colors"
                                        style={{ color: 'var(--psj-text-3)' }} />
                                    <div className="text-sm font-bold tracking-tight" style={{ color: 'var(--psj-text-1)' }}>
                                        {ind.name}
                                    </div>
                                    <div className="text-[10px] uppercase tracking-widest font-bold mt-1 num-marker"
                                        style={{ color: 'var(--psj-text-3)' }}>
                                        {ind.clients} clients
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════════════════════════════
                CTA BAND
            ════════════════════════════════════════════════════════════════════ */}
            <section style={{ background: 'var(--psj-blue)' }}>
                <div className="psj-container psj-section">
                    <div className="grid md:grid-cols-2 gap-10 items-center">
                        <div>
                            <div className="text-[10px] uppercase tracking-[0.25em] font-bold mb-4"
                                style={{ color: 'rgba(255,255,255,0.6)' }}>
                                Ready to Start?
                            </div>
                            <h2 className="psj-h2 text-balance mb-4 text-white">
                                Start automating your CAE workflow today
                            </h2>
                            <p className="text-sm leading-relaxed max-w-md"
                                style={{ color: 'rgba(255,255,255,0.7)' }}>
                                Explore the documentation, run through tutorials, or speak with
                                our team to find the right solution.
                            </p>
                        </div>
                        <div className="flex flex-col sm:flex-row gap-3 md:justify-end">
                            <Link href="/docs"
                                className="inline-flex items-center justify-center gap-2 px-7 py-4 text-sm font-bold transition-colors"
                                style={{ background: '#FFFFFF', color: 'var(--psj-blue)' }}
                                onMouseEnter={e => (e.currentTarget.style.background = 'rgba(255,255,255,0.9)')}
                                onMouseLeave={e => (e.currentTarget.style.background = '#FFFFFF')}>
                                Read Documentation <ArrowRight size={15} />
                            </Link>
                            <Link href="/tutorials"
                                className="inline-flex items-center justify-center gap-2 px-7 py-4 text-sm font-bold transition-colors text-white"
                                style={{ border: '1px solid rgba(255,255,255,0.35)' }}
                                onMouseEnter={e => (e.currentTarget.style.background = 'rgba(255,255,255,0.1)')}
                                onMouseLeave={e => (e.currentTarget.style.background = 'transparent')}>
                                <Play size={15} /> Start Tutorials
                            </Link>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
}
