import Link from 'fumadocs-core/link';
import { CodeBlock } from 'fumadocs-ui/components/codeblock';
import {
    ArrowRight,
    Atom,
    Car,
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
    Wrench,
    Zap,
} from 'lucide-react';
import { getTranslations } from 'next-intl/server';

import { CtaBand } from '@/components/sections/cta-band';
import { FadeUp } from '@/components/sections/fade-up';
import { SectionHeader } from '@/components/sections/section-header';

// Icon sets for the 4F philosophy cards and module items — indexed to match
// the translation arrays so order is the single source of truth.
const PHI_ICONS = [MousePointerClick, Zap, Wrench, Settings] as const;

const MODULE_ICONS = [Play, Terminal, Cpu, MousePointerClick, Terminal, Code2] as const;
const MODULE_COLORS = [
    'var(--color-brand-cyan)',
    'var(--color-brand-purple)',
    'var(--color-brand-green)',
    'var(--color-brand-orange)',
    'var(--color-brand-yellow)',
    'var(--color-brand-blue)',
] as const;

const INDUSTRY_ITEMS = [
    { icon: Car, fields: 'Crash · NVH · Powertrain' },
    { icon: Plane, fields: 'Structural · Aerodynamic' },
    { icon: Ship, fields: 'Hull · Hydrodynamics' },
    { icon: Factory, fields: 'Machinery · Production' },
    { icon: Atom, fields: 'Reactor · Thermal · Fluid' },
] as const;

export default async function Page() {
    const t = await getTranslations('enterprise');

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
                                        {t('hero.badge')}
                                    </span>
                                </div>
                            </FadeUp>

                            <FadeUp delay={80}>
                                <h1 className="psj-h1 text-balance mb-6" style={{ color: 'var(--psj-text-1)' }}>
                                    {t('hero.title0')}
                                    <br />
                                    <span style={{ color: 'var(--psj-blue)' }}>{t('hero.title1')}</span>
                                </h1>
                            </FadeUp>

                            <FadeUp delay={160}>
                                <p
                                    className="text-lg leading-relaxed max-w-xl mb-10 text-balance"
                                    style={{ color: 'var(--psj-text-2)' }}
                                >
                                    {t('hero.desc')}
                                </p>
                            </FadeUp>

                            <FadeUp delay={240}>
                                <div className="flex flex-wrap gap-4">
                                    <Link href="/docs" className="psj-btn-primary">
                                        {t('hero.cta.primary')} <ArrowRight size={15} />
                                    </Link>
                                    <Link href="/tutorials" className="psj-btn-secondary">
                                        <Play size={15} /> {t('hero.cta.secondary')}
                                    </Link>
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
                                        {(['#EF4444', '#F59E0B', '#22C55E'] as const).map((c) => (
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
                                    <span className="font-mono text-[10px]" style={{ color: 'var(--psj-text-3)' }}>
                                        {t('hero.code.filename')}
                                    </span>
                                    <span
                                        className="text-[10px] font-medium px-2 py-0.5"
                                        style={{
                                            border: '1px solid var(--psj-border)',
                                            color: 'var(--psj-text-3)',
                                        }}
                                    >
                                        {t('hero.code.language')}
                                    </span>
                                </div>
                                {/* Code */}
                                <CodeBlock
                                    content={`
                                        from psj import *
                                        # Macro — auto-recorded after UI operation
                                        CreateCube([0,0,0], [10,10,10], "Cube_1")
                                        ImprintLines([[7.8,0,10],[2.2,10,10]], [6:26], 1)
                                        # PSJ-Utility — query model data
                                        nodes = psj.utility.get_node_coords(model)
                                        # PSJ-GUI — custom dialog
                                        dlg = psj.gui.Dialog("Bolt Generator")
                                        dlg.add_input("diameter", 12.0)
                                        dlg.show()
                                    `}
                                />
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
                                        {t('hero.code.statusBar0')}
                                    </span>
                                    <span>{t('hero.code.statusBar1')}</span>
                                </div>
                            </div>
                        </FadeUp>
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
                                <div className="psj-label mb-4">{t('phi.label')}</div>
                                <h2 className="psj-h2 text-balance mb-6" style={{ color: 'var(--psj-text-1)' }}>
                                    {t('phi.title')}
                                </h2>
                                <p className="text-base leading-relaxed mb-8" style={{ color: 'var(--psj-text-2)' }}>
                                    {t('phi.desc')}
                                </p>
                                <Link
                                    href="/docs"
                                    className="group inline-flex items-center gap-2 text-sm font-bold transition-colors"
                                    style={{ color: 'var(--psj-blue)' }}
                                >
                                    {t('phi.readDocs')}
                                    <ArrowRight size={15} className="group-hover:translate-x-1 transition-transform" />
                                </Link>
                            </FadeUp>
                        </div>

                        {/* Right — 4 cards */}
                        <div className="lg:col-span-8 grid sm:grid-cols-2 gap-5">
                            {(t.raw('phi.cards') as { label: string; sub: string; desc: string }[]).map((card, i) => {
                                const Icon = PHI_ICONS[i];
                                return (
                                    <FadeUp key={card.label} delay={i * 50}>
                                        <div className="psj-card-interactive p-7 h-full">
                                            <div className="flex items-center gap-4 mb-5">
                                                <div
                                                    className="flex items-center justify-center w-11 h-11"
                                                    style={{
                                                        background: 'var(--psj-blue-subtle)',
                                                        border: '1px solid var(--psj-blue-subtle2)',
                                                    }}
                                                >
                                                    <Icon size={20} style={{ color: 'var(--psj-blue)' }} />
                                                </div>
                                                <div>
                                                    <div
                                                        className="font-bold text-base tracking-tight"
                                                        style={{ color: 'var(--psj-text-1)' }}
                                                    >
                                                        {card.label}
                                                    </div>
                                                    <div
                                                        className="text-[10px] uppercase tracking-widest font-bold"
                                                        style={{ color: 'var(--psj-blue)' }}
                                                    >
                                                        {card.sub}
                                                    </div>
                                                </div>
                                            </div>
                                            <p
                                                className="text-sm leading-relaxed"
                                                style={{ color: 'var(--psj-text-2)' }}
                                            >
                                                {card.desc}
                                            </p>
                                        </div>
                                    </FadeUp>
                                );
                            })}
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
                        label={t.raw('modules.header.label')}
                        title={t.raw('modules.header.title')}
                        link="/docs"
                        linkLabel={t.raw('modules.header.linkLabel')}
                    />
                    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
                        {(t.raw('modules.items') as { label: string; sub: string; desc: string }[]).map((mod, i) => {
                            const Icon = MODULE_ICONS[i];
                            const color = MODULE_COLORS[i];
                            return (
                                <FadeUp key={mod.label} delay={i * 50}>
                                    <div
                                        className="psj-card p-7 group h-full"
                                        style={{ borderTop: `2px solid ${color}` }}
                                    >
                                        <div className="flex items-center gap-3 mb-5">
                                            <div
                                                className="w-10 h-10 flex items-center justify-center"
                                                style={{
                                                    background: `${color}12`,
                                                    border: `1px solid ${color}25`,
                                                }}
                                            >
                                                <Icon size={17} style={{ color }} />
                                            </div>
                                            <span
                                                className="font-bold text-base tracking-tight"
                                                style={{ color: 'var(--psj-text-1)' }}
                                            >
                                                {mod.label}
                                            </span>
                                        </div>
                                        <p
                                            className="text-sm leading-relaxed mb-5"
                                            style={{ color: 'var(--psj-text-2)' }}
                                        >
                                            {mod.desc}
                                        </p>
                                        <Link
                                            href="/docs"
                                            className="inline-flex items-center gap-1 text-xs font-bold opacity-0 group-hover:opacity-100 transition-all translate-y-1 group-hover:translate-y-0"
                                            style={{ color: 'var(--psj-blue)' }}
                                        >
                                            {t.raw('modules.exploreLabel')} <ChevronRight size={12} />
                                        </Link>
                                    </div>
                                </FadeUp>
                            );
                        })}
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
                            <div className="psj-label mb-3">{t('industries.header.label')}</div>
                            <h3 className="psj-h3 text-balance mb-4" style={{ color: 'var(--psj-text-1)' }}>
                                {t('industries.header.title')}
                            </h3>
                            <p className="text-sm leading-relaxed" style={{ color: 'var(--psj-text-2)' }}>
                                {t('industries.header.desc')}
                            </p>
                        </div>
                        <div className="flex-1 grid grid-cols-2 sm:grid-cols-5 gap-4">
                            {INDUSTRY_ITEMS.map(({ icon: Icon, fields }, i) => (
                                <div key={i} className="psj-card-interactive p-5 text-center group">
                                    <Icon
                                        size={22}
                                        className="mx-auto mb-3 transition-colors"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    />
                                    <div
                                        className="text-sm font-bold tracking-tight"
                                        style={{ color: 'var(--psj-text-1)' }}
                                    >
                                        {/* Industry names are not translated — they're proper nouns */}
                                        {['Automotive', 'Aerospace', 'Marine', 'Manufacturing', 'Energy'][i]}
                                    </div>
                                    <div
                                        className="text-[10px] uppercase tracking-widest font-bold mt-1 num-marker"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        {fields}
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
