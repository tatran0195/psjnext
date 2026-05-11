'use client';
import Link from 'fumadocs-core/link';
import {
    ArrowRight,
    Atom,
    Award,
    Building2,
    Car,
    CheckCircle2,
    ChevronRight,
    Code2,
    Cpu,
    Factory,
    MousePointerClick,
    Plane,
    Play,
    Settings,
    Ship,
    Terminal,
    TrendingUp,
    Users,
    Wrench,
    Zap,
} from 'lucide-react';

import { CtaBand } from '@/components/sections/cta-band';
import { FadeUp } from '@/components/sections/fade-up';
import { SectionHeader } from '@/components/sections/section-header';
import { StatCard } from '@/components/sections/stat-card';
import { translations } from '@/lib/i18n-translations';

/* ═══════════════════════════════════════════════════════════════════════════════
   PAGE
   ═══════════════════════════════════════════════════════════════════════════════ */
export default function LandingPage({ params: { lang } }: { params: { lang: string } }) {
    const t = translations[lang as keyof typeof translations] || translations.en;
    const { landing } = t;

    const modules = [
        {
            icon: Play,
            label: landing.module_1_label,
            desc: landing.module_1_desc,
            color: 'var(--color-brand-cyan)',
        },
        {
            icon: Terminal,
            label: landing.module_2_label,
            desc: landing.module_2_desc,
            color: 'var(--color-brand-purple)',
        },
        {
            icon: Cpu,
            label: landing.module_3_label,
            desc: landing.module_3_desc,
            color: 'var(--color-brand-green)',
        },
        {
            icon: MousePointerClick,
            label: landing.module_4_label,
            desc: landing.module_4_desc,
            color: 'var(--color-brand-orange)',
        },
        {
            icon: Terminal,
            label: landing.module_5_label,
            desc: landing.module_5_desc,
            color: 'var(--color-brand-yellow)',
        },
        {
            icon: Code2,
            label: landing.module_6_label,
            desc: landing.module_6_desc,
            color: 'var(--color-brand-blue)',
        },
    ];

    const fourF = [
        {
            label: landing.phiFriendly_label,
            sub: landing.phiFriendly_sub,
            desc: landing.phiFriendly_desc,
            icon: MousePointerClick,
        },
        {
            label: landing.phiFast_label,
            sub: landing.phiFast_sub,
            desc: landing.phiFast_desc,
            icon: Zap,
        },
        {
            label: landing.phiFunctional_label,
            sub: landing.phiFunctional_sub,
            desc: landing.phiFunctional_desc,
            icon: Wrench,
        },
        {
            label: landing.phiFlexible_label,
            sub: landing.phiFlexible_sub,
            desc: landing.phiFlexible_desc,
            icon: Settings,
        },
    ];

    const industries = [
        { icon: Car, name: 'Automotive', clients: '40+' },
        { icon: Plane, name: 'Aerospace', clients: '25+' },
        { icon: Ship, name: 'Marine', clients: '15+' },
        { icon: Factory, name: 'Manufacturing', clients: '30+' },
        { icon: Atom, name: 'Energy', clients: '10+' },
    ];

    return (
        <>
            {/* ══════════════════════════════════════════════════════════════════
                HERO — CAE Engineering background
            ════════════════════════════════════════════════════════════════════ */}
            <section
                className="cae-hero-bg"
                style={{ borderBottom: '1px solid var(--psj-border)' }}
            >
                {/* Animated mesh dots */}
                <div className="cae-hero-dots" />
                {/* Animated scan line */}
                <div className="cae-scan-line" />

                <div className="psj-container py-20 lg:py-32 relative z-10">
                    <div className="grid lg:grid-cols-12 gap-12 lg:gap-16 items-center">
                        {/* Left — Text */}
                        <div className="lg:col-span-7">
                            <FadeUp>
                                <div
                                    className="inline-flex items-center gap-2 mb-8"
                                    style={{
                                        border: '1px solid var(--psj-blue)',
                                        background: 'var(--psj-blue-subtle)',
                                        padding: '5px 12px',
                                    }}
                                >
                                    <span
                                        className="w-1.5 h-1.5 rounded-full animate-pulse"
                                        style={{ background: 'var(--psj-blue)' }}
                                    />
                                    <span
                                        className="text-[10px] uppercase tracking-[0.25em] font-bold"
                                        style={{ color: 'var(--psj-blue)' }}
                                    >
                                        {landing.heroBadge}
                                    </span>
                                </div>
                            </FadeUp>

                            <FadeUp delay={80}>
                                <h1
                                    className="psj-h1 text-balance mb-6"
                                    style={{ color: 'var(--psj-text-1)' }}
                                >
                                    {landing.heroTitle_1}
                                    <br />
                                    <span style={{ color: 'var(--psj-blue)' }}>
                                        {landing.heroTitle_2}
                                    </span>
                                </h1>
                            </FadeUp>

                            <FadeUp delay={160}>
                                <p
                                    className="text-lg leading-relaxed max-w-xl mb-10 text-balance"
                                    style={{ color: 'var(--psj-text-2)' }}
                                >
                                    {landing.heroDesc}
                                </p>
                            </FadeUp>

                            <FadeUp delay={240}>
                                <div className="flex flex-wrap gap-4">
                                    <Link href="/docs" className="psj-btn-primary">
                                        {landing.heroGetStarted} <ArrowRight size={15} />
                                    </Link>
                                    <Link href="/tutorials" className="psj-btn-secondary">
                                        <Play size={15} /> {landing.heroViewTutorials}
                                    </Link>
                                </div>
                            </FadeUp>

                            <FadeUp delay={320}>
                                <div
                                    className="flex flex-wrap items-center gap-5 mt-10 pt-8 text-xs"
                                    style={{
                                        borderTop: '1px solid var(--psj-border)',
                                        color: 'var(--psj-text-3)',
                                    }}
                                >
                                    {landing.heroChecklist.map((t) => (
                                        <span key={t} className="flex items-center gap-1.5">
                                            <CheckCircle2
                                                size={11}
                                                style={{ color: 'var(--psj-blue)' }}
                                            />{' '}
                                            {t}
                                        </span>
                                    ))}
                                </div>
                            </FadeUp>
                        </div>

                        {/* Right — Code card */}
                        <FadeUp delay={200} className="lg:col-span-5">
                            <div
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                {/* Window chrome */}
                                <div
                                    className="flex items-center justify-between px-4 py-3"
                                    style={{
                                        borderBottom: '1px solid var(--psj-border)',
                                        background: 'var(--psj-surface-2)',
                                    }}
                                >
                                    <div className="flex items-center gap-1.5">
                                        {['#EF4444', '#F59E0B', '#22C55E'].map((c) => (
                                            <div
                                                key={c}
                                                style={{
                                                    width: '10px',
                                                    height: '10px',
                                                    background: c,
                                                    opacity: 0.7,
                                                }}
                                            />
                                        ))}
                                    </div>
                                    <span
                                        className="font-mono text-[10px]"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        {landing.heroCodeFilename}
                                    </span>
                                    <span
                                        className="text-[10px] font-medium px-2 py-0.5"
                                        style={{
                                            border: '1px solid var(--psj-border)',
                                            color: 'var(--psj-text-3)',
                                        }}
                                    >
                                        {landing.heroCodeLanguage}
                                    </span>
                                </div>
                                {/* Code */}
                                <div
                                    className="p-6 font-mono text-sm leading-relaxed"
                                    style={{
                                        background: 'var(--psj-surface-0)',
                                        color: 'var(--psj-text-2)',
                                    }}
                                >
                                    <div className="space-y-1">
                                        <p>
                                            <span
                                                style={{
                                                    color: 'var(--psj-blue)',
                                                    fontWeight: 600,
                                                }}
                                            >
                                                from
                                            </span>{' '}
                                            psj{' '}
                                            <span
                                                style={{
                                                    color: 'var(--psj-blue)',
                                                    fontWeight: 600,
                                                }}
                                            >
                                                import
                                            </span>{' '}
                                            *
                                        </p>
                                        <p
                                            className="text-[11px]"
                                            style={{ color: 'var(--psj-text-3)' }}
                                        >
                                            # Macro — auto-recorded after UI operation
                                        </p>
                                        <p>
                                            CreateCube([0,0,0], [10,10,10],{' '}
                                            <span style={{ color: '#D4570D' }}>
                                                &quot;Cube_1&quot;
                                            </span>
                                            )
                                        </p>
                                        <p>ImprintLines([[7.8,0,10],[2.2,10,10]], [6:26], 1)</p>
                                        <p
                                            className="mt-3 text-[11px]"
                                            style={{ color: 'var(--psj-text-3)' }}
                                        >
                                            # PSJ-Utility — query model data
                                        </p>
                                        <p>
                                            nodes = psj.utility.
                                            <span style={{ color: 'var(--psj-blue)' }}>
                                                get_node_coords
                                            </span>
                                            (model)
                                        </p>
                                        <p
                                            className="mt-3 text-[11px]"
                                            style={{ color: 'var(--psj-text-3)' }}
                                        >
                                            # PSJ-GUI — custom dialog
                                        </p>
                                        <p>
                                            dlg = psj.gui.
                                            <span style={{ color: 'var(--psj-blue)' }}>Dialog</span>
                                            (
                                            <span style={{ color: '#D4570D' }}>
                                                &quot;Bolt Generator&quot;
                                            </span>
                                            )
                                        </p>
                                        <p>
                                            dlg.
                                            <span style={{ color: 'var(--psj-blue)' }}>
                                                add_input
                                            </span>
                                            (
                                            <span style={{ color: '#D4570D' }}>
                                                &quot;diameter&quot;
                                            </span>
                                            , 12.0)
                                        </p>
                                        <p>
                                            dlg.
                                            <span style={{ color: 'var(--psj-blue)' }}>show</span>()
                                        </p>
                                        <p
                                            className="animate-pulse"
                                            style={{ color: 'var(--psj-blue)' }}
                                        >
                                            ▊
                                        </p>
                                    </div>
                                </div>
                                {/* Status bar */}
                                <div
                                    className="px-4 py-2 flex items-center justify-between text-[10px]"
                                    style={{
                                        borderTop: '1px solid var(--psj-border)',
                                        background: 'var(--psj-surface-2)',
                                        color: 'var(--psj-text-3)',
                                    }}
                                >
                                    <span className="flex items-center gap-1.5">
                                        <span
                                            style={{
                                                width: '6px',
                                                height: '6px',
                                                background: '#22C55E',
                                                display: 'inline-block',
                                            }}
                                        />
                                        {landing.heroCodeStatusBar_1}
                                    </span>
                                    <span>{landing.heroCodeStatusBar_2}</span>
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
                    <div
                        className="grid grid-cols-2 lg:grid-cols-4"
                        style={{
                            borderLeft: '1px solid var(--psj-border)',
                            borderTop: '1px solid var(--psj-border)',
                        }}
                    >
                        <StatCard
                            icon={<Award size={13} />}
                            value={landing.stats_1_value}
                            label={landing.stats_1_label}
                        />
                        <StatCard
                            icon={<Users size={13} />}
                            value={landing.stats_2_value}
                            label={landing.stats_2_label}
                        />
                        <StatCard
                            icon={<Building2 size={13} />}
                            value={landing.stats_3_value}
                            label={landing.stats_3_label}
                        />
                        <StatCard
                            icon={<TrendingUp size={13} />}
                            value={landing.stats_4_value}
                            label={landing.stats_4_label}
                        />
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════════════════════════════
                4F PHILOSOPHY
            ════════════════════════════════════════════════════════════════════ */}
            <section
                style={{
                    background: 'var(--psj-surface-1)',
                    borderBottom: '1px solid var(--psj-border)',
                }}
            >
                <div className="psj-container psj-section">
                    <div className="grid lg:grid-cols-12 gap-12 lg:gap-16 items-start">
                        {/* Left */}
                        <div className="lg:col-span-4">
                            <FadeUp>
                                <div className="psj-label mb-4">{landing.phiLabel}</div>
                                <h2
                                    className="psj-h2 text-balance mb-6"
                                    style={{ color: 'var(--psj-text-1)' }}
                                >
                                    {landing.phiTitle}
                                </h2>
                                <p
                                    className="text-base leading-relaxed mb-8"
                                    style={{ color: 'var(--psj-text-2)' }}
                                >
                                    {landing.phiDesc}
                                </p>
                                <Link
                                    href="/docs"
                                    className="group inline-flex items-center gap-2 text-sm font-bold transition-colors"
                                    style={{ color: 'var(--psj-blue)' }}
                                >
                                    {landing.phiReadDocs}
                                    <ArrowRight
                                        size={15}
                                        className="group-hover:translate-x-1 transition-transform"
                                    />
                                </Link>
                            </FadeUp>
                        </div>
                        {/* Right — grid of 4 cards */}
                        <div className="lg:col-span-8 grid sm:grid-cols-2 gap-5">
                            {fourF.map((f, i) => (
                                <FadeUp key={f.label} delay={i * 50}>
                                    <div className="psj-card-interactive p-7 h-full">
                                        <div className="flex items-center gap-4 mb-5">
                                            <div
                                                className="flex items-center justify-center w-11 h-11"
                                                style={{
                                                    background: 'var(--psj-blue-subtle)',
                                                    border: '1px solid var(--psj-blue-subtle2)',
                                                }}
                                            >
                                                <f.icon
                                                    size={20}
                                                    style={{ color: 'var(--psj-blue)' }}
                                                />
                                            </div>
                                            <div>
                                                <div
                                                    className="font-bold text-base tracking-tight"
                                                    style={{ color: 'var(--psj-text-1)' }}
                                                >
                                                    {f.label}
                                                </div>
                                                <div
                                                    className="text-[10px] uppercase tracking-widest font-bold"
                                                    style={{ color: 'var(--psj-blue)' }}
                                                >
                                                    {f.sub}
                                                </div>
                                            </div>
                                        </div>
                                        <p
                                            className="text-sm leading-relaxed"
                                            style={{ color: 'var(--psj-text-2)' }}
                                        >
                                            {f.desc}
                                        </p>
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
            <section
                style={{
                    background: 'var(--psj-surface-0)',
                    borderBottom: '1px solid var(--psj-border)',
                }}
            >
                <div className="psj-container psj-section">
                    <SectionHeader
                        label={landing.moduleHeader_label}
                        title={landing.moduleHeader_title}
                        link="/docs"
                        linkLabel={landing.moduleHeader_linkLabel}
                    />
                    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
                        {modules.map((m, i) => (
                            <FadeUp key={m.label} delay={i * 50}>
                                <div
                                    className="psj-card p-7 group h-full"
                                    style={{ borderTop: `2px solid ${m.color}` }}
                                >
                                    <div className="flex items-center gap-3 mb-5">
                                        <div
                                            className="w-10 h-10 flex items-center justify-center"
                                            style={{
                                                background: `${m.color}12`,
                                                border: `1px solid ${m.color}25`,
                                            }}
                                        >
                                            <m.icon size={17} style={{ color: m.color }} />
                                        </div>
                                        <span
                                            className="font-bold text-base tracking-tight"
                                            style={{ color: 'var(--psj-text-1)' }}
                                        >
                                            {m.label}
                                        </span>
                                    </div>
                                    <p
                                        className="text-sm leading-relaxed mb-5"
                                        style={{ color: 'var(--psj-text-2)' }}
                                    >
                                        {m.desc}
                                    </p>
                                    <Link
                                        href="/docs"
                                        className="inline-flex items-center gap-1 text-xs font-bold opacity-0 group-hover:opacity-100 transition-all translate-y-1 group-hover:translate-y-0"
                                        style={{ color: 'var(--psj-blue)' }}
                                    >
                                        {landing.exploreModule} <ChevronRight size={12} />
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
            <section
                style={{
                    background: 'var(--psj-surface-1)',
                    borderBottom: '1px solid var(--psj-border)',
                }}
            >
                <div className="psj-container psj-section-sm">
                    <div className="flex flex-col lg:flex-row items-start lg:items-center gap-12">
                        <div className="shrink-0 max-w-xs">
                            <div className="psj-label mb-3">{landing.industryHeader_label}</div>
                            <h3
                                className="psj-h3 text-balance mb-4"
                                style={{ color: 'var(--psj-text-1)' }}
                            >
                                {landing.industryHeader_title}
                            </h3>
                            <p
                                className="text-sm leading-relaxed"
                                style={{ color: 'var(--psj-text-2)' }}
                            >
                                {landing.industryHeader_desc}
                            </p>
                        </div>
                        <div className="flex-1 grid grid-cols-2 sm:grid-cols-5 gap-4">
                            {industries.map((ind) => (
                                <div
                                    key={ind.name}
                                    className="psj-card-interactive p-5 text-center group"
                                >
                                    <ind.icon
                                        size={22}
                                        className="mx-auto mb-3 transition-colors"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    />
                                    <div
                                        className="text-sm font-bold tracking-tight"
                                        style={{ color: 'var(--psj-text-1)' }}
                                    >
                                        {ind.name}
                                    </div>
                                    <div
                                        className="text-[10px] uppercase tracking-widest font-bold mt-1 num-marker"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        {ind.clients} {landing.industryClients}
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
            <CtaBand />
        </>
    );
}
