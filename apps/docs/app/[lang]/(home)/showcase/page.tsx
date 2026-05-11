'use client';
import { use, useMemo, useState } from 'react';

import { AnimatePresence, motion } from 'framer-motion';
import {
    ArrowRight,
    Box,
    Building2,
    Check,
    CheckCircle2,
    ChevronDown,
    Clock,
    LucideIcon,
    Search,
    Settings,
    X,
} from 'lucide-react';

import { CtaBand } from '@/components/sections/cta-band';
import { cn } from '@/lib/cn';
import { translations } from '@/lib/i18n-translations';
import { categoryConfig, getIndustries, getSolutions, Solution } from '@/lib/showcase';

export default function CAEServices({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = use(params);

    const t = translations[lang as keyof typeof translations] || translations.en;
    const { showcase } = t;

    const solutions = getSolutions(lang);
    const industries = getIndustries(lang);

    const [activeCategory, setActiveCategory] = useState<keyof typeof categoryConfig>('All');
    const [activeIndustry, setActiveIndustry] = useState(industries[0]);
    const [search, setSearch] = useState('');
    const [selectedSolution, setSelectedSolution] = useState<Solution | null>(null);
    const [mobileFiltersOpen, setMobileFiltersOpen] = useState(false);

    const [sortBy, setSortBy] = useState<string>(showcase.sortByRelevant);

    const filtered = useMemo(() => {
        const result = [...solutions].filter((sol) => {
            const matchesCategory = activeCategory === 'All' || sol.category === activeCategory;
            const matchesIndustry =
                activeIndustry === industries[0] || sol.industry.includes(activeIndustry);
            const matchesSearch =
                sol.title.toLowerCase().includes(search.toLowerCase()) ||
                sol.code.toLowerCase().includes(search.toLowerCase());
            return matchesCategory && matchesIndustry && matchesSearch;
        });

        // Sorting
        if (sortBy === showcase.sortByCode) {
            result.sort((a, b) => a.code.localeCompare(b.code));
        } else if (sortBy === showcase.sortByComplexity) {
            const order = { Standard: 1, Advanced: 2, Enterprise: 3 };
            result.sort(
                (a, b) =>
                    order[a.complexity as keyof typeof order] -
                    order[b.complexity as keyof typeof order],
            );
        }

        return result;
    }, [activeCategory, activeIndustry, search, sortBy, solutions, industries, showcase]);

    return (
        <div
            style={{
                background: 'var(--psj-surface-0)',
                color: 'var(--psj-text-1)',
                minHeight: '100vh',
            }}
        >
            {/* layout provides header */}
            <section className="psj-subpage-hero">
                <div className="psj-container py-10 lg:py-14 relative z-10">
                    <div className="max-w-4xl">
                        <div className="psj-label mb-2">{showcase.showcaseLabel}</div>
                        <h1
                            className="psj-h1 mb-4 text-4xl lg:text-5xl"
                            style={{ color: 'var(--psj-text-1)' }}
                        >
                            {showcase.showcaseTitle}
                        </h1>
                        <p
                            className="text-base lg:text-lg leading-relaxed max-w-2xl"
                            style={{ color: 'var(--psj-text-2)' }}
                        >
                            {showcase.showcaseDesc}
                        </p>
                    </div>
                </div>
            </section>

            {/* ─────── MAIN LAYOUT ─────── */}
            <main id="catalog" className="psj-container py-10">
                <div className="max-w-7xl mx-auto">
                    {/* ── INLINE FILTER BAR ── */}
                    <div className="flex flex-col gap-6 mb-10">
                        {/* Primary Filters Row */}
                        <div className="flex flex-wrap items-center gap-4">
                            {/* Search */}
                            <div
                                className="flex items-center gap-3 px-4 py-2 flex-1 min-w-[280px]"
                                style={{
                                    border: '1px solid var(--psj-border)',
                                    background: 'var(--psj-surface-1)',
                                }}
                            >
                                <Search size={15} style={{ color: 'var(--psj-text-3)' }} />
                                <input
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    placeholder={showcase.searchByCode}
                                    className="bg-transparent text-sm outline-none flex-1"
                                    style={{ color: 'var(--psj-text-1)' }}
                                />
                                {search && (
                                    <button
                                        onClick={() => setSearch('')}
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        <X size={14} />
                                    </button>
                                )}
                            </div>

                            {/* Industry Dropdown */}
                            <FilterDropdown
                                value={activeIndustry}
                                options={industries}
                                onChange={setActiveIndustry}
                                icon={Building2}
                                prefix={showcase.industryPrefix}
                            />

                            {/* Sort */}
                            <FilterDropdown
                                value={sortBy}
                                options={[
                                    showcase.sortByRelevant,
                                    showcase.sortByCode,
                                    showcase.sortByComplexity,
                                ]}
                                onChange={setSortBy}
                                prefix={showcase.sortPrefix}
                            />
                        </div>

                        {/* Category Chips Row */}
                        <div className="flex flex-wrap items-center gap-2">
                            {(
                                Object.keys(categoryConfig) as Array<keyof typeof categoryConfig>
                            ).map((cat) => {
                                const active = activeCategory === cat;
                                const config = categoryConfig[cat];
                                const Icon = config.icon;
                                return (
                                    <button
                                        key={cat}
                                        onClick={() => setActiveCategory(cat)}
                                        className="flex items-center gap-2 px-4 py-2 text-xs font-bold transition-all"
                                        style={{
                                            border: '1px solid var(--psj-border)',
                                            background: active
                                                ? 'var(--psj-blue)'
                                                : 'var(--psj-surface-1)',
                                            color: active ? 'white' : 'var(--psj-text-2)',
                                            borderColor: active
                                                ? 'var(--psj-blue)'
                                                : 'var(--psj-border)',
                                        }}
                                    >
                                        <Icon size={12} />
                                        {cat}
                                    </button>
                                );
                            })}
                        </div>

                        <div className="flex items-center justify-between pt-2">
                            <div
                                className="text-[11px] uppercase tracking-widest font-bold"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                {showcase.showingResults
                                    .replace('{count}', filtered.length.toString())
                                    .replace('{total}', solutions.length.toString())}
                            </div>
                            {(activeCategory !== 'All' ||
                                activeIndustry !== industries[0] ||
                                search) && (
                                <button
                                    onClick={() => {
                                        setActiveCategory('All');
                                        setActiveIndustry(industries[0]);
                                        setSearch('');
                                    }}
                                    className="text-[11px] uppercase tracking-widest font-bold underline"
                                    style={{ color: 'var(--psj-blue)' }}
                                >
                                    {showcase.clearFilters}
                                </button>
                            )}
                        </div>
                    </div>

                    <div className="w-full">
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
                                        {showcase.noSolutions}
                                    </p>
                                    <button
                                        onClick={() => {
                                            setActiveCategory('All');
                                            setActiveIndustry(industries[0]);
                                            setSearch('');
                                        }}
                                        className="mt-4 text-sm font-bold"
                                        style={{ color: 'var(--psj-blue)' }}
                                    >
                                        {showcase.resetFilters}
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
                                                labels={showcase}
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
            <CtaBand
                subtitle={showcase.ctaSubtitle}
                title={showcase.ctaTitle}
                description={showcase.ctaDesc}
                primaryLink={{ href: '#', label: showcase.ctaPrimaryLabel }}
                secondaryLink={{ href: '#', label: showcase.ctaSecondaryLabel }}
            />

            {/* Layout provides footer */}

            {/* ─────── DETAIL MODAL ─────── */}
            <AnimatePresence>
                {selectedSolution && (
                    <DetailModal
                        sol={selectedSolution}
                        onClose={() => setSelectedSolution(null)}
                        labels={showcase}
                    />
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
                            className="lg:hidden fixed top-0 right-0 h-full w-80 z-50 overflow-y-auto"
                            style={{
                                background: 'var(--psj-surface-0)',
                                borderLeft: '1px solid var(--psj-border)',
                            }}
                        >
                            <div className="p-6">
                                <button
                                    onClick={() => setMobileFiltersOpen(false)}
                                    className="mb-6"
                                >
                                    <X size={20} />
                                </button>
                                <h3 className="text-lg font-bold mb-4">
                                    {showcase.filterSolutions}
                                </h3>
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
                                        className={`w-full text-left px-3 py-2.5 text-sm transition-colors`}
                                        style={{
                                            background:
                                                activeCategory === cat
                                                    ? 'var(--psj-blue-subtle)'
                                                    : 'transparent',
                                            color:
                                                activeCategory === cat
                                                    ? 'var(--psj-blue)'
                                                    : 'var(--psj-text-2)',
                                            fontWeight: activeCategory === cat ? 700 : 400,
                                            borderLeft:
                                                activeCategory === cat
                                                    ? '2px solid var(--psj-blue)'
                                                    : '2px solid transparent',
                                        }}
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

/* ── Filter Dropdown ── */
function FilterDropdown({
    value,
    options,
    onChange,
    icon: Icon,
    prefix,
}: {
    value: string;
    options: string[];
    onChange: (val: string) => void;
    icon?: LucideIcon;
    prefix?: string;
}) {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className="relative">
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="flex items-center gap-3 px-4 py-2 text-sm transition-all min-w-[200px] text-left group"
                style={{
                    border: '1px solid var(--psj-border)',
                    background: 'var(--psj-surface-1)',
                    color: 'var(--psj-text-1)',
                }}
            >
                {Icon && <Icon size={14} style={{ color: 'var(--psj-text-3)' }} />}
                <div className="flex-1 truncate">
                    {prefix && (
                        <span className="text-[10px] uppercase font-bold mr-2 opacity-50">
                            {prefix}
                        </span>
                    )}
                    {value}
                </div>
                <ChevronDown
                    size={14}
                    style={{
                        color: 'var(--psj-text-3)',
                        transform: isOpen ? 'rotate(180deg)' : 'none',
                    }}
                    className="transition-transform duration-200"
                    aria-hidden="true"
                />
            </button>

            <AnimatePresence>
                {isOpen && (
                    <>
                        <div className="fixed inset-0 z-40" onClick={() => setIsOpen(false)} />
                        <motion.div
                            initial={{ opacity: 0, y: 4 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: 4 }}
                            transition={{ duration: 0.15 }}
                            className="absolute left-0 right-0 top-full mt-1 z-50 overflow-hidden"
                            style={{
                                background: 'var(--psj-surface-0)',
                                border: '1px solid var(--psj-border)',
                                boxShadow: '0 12px 40px rgba(0,0,0,0.15)',
                            }}
                        >
                            <div className="max-h-[300px] overflow-y-auto py-1">
                                {options.map((opt) => (
                                    <button
                                        key={opt}
                                        onClick={() => {
                                            onChange(opt);
                                            setIsOpen(false);
                                        }}
                                        className="w-full text-left px-4 py-2.5 text-[13px] transition-colors flex items-center justify-between"
                                        style={{
                                            background:
                                                value === opt
                                                    ? 'var(--psj-surface-2)'
                                                    : 'transparent',
                                            color:
                                                value === opt
                                                    ? 'var(--psj-blue)'
                                                    : 'var(--psj-text-2)',
                                        }}
                                    >
                                        {opt}
                                        {value === opt && <Check size={14} />}
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

/* ── Helper Components ── */
function Tag({ children, className }: { children: React.ReactNode; className?: string }) {
    return (
        <span
            className={cn('text-[10px] px-2 py-0.5 font-medium', className)}
            style={{
                background: 'var(--psj-surface-2)',
                color: 'var(--psj-text-2)',
                border: '1px solid var(--psj-border)',
            }}
        >
            {children}
        </span>
    );
}

function CheckList({ items, limit }: { items: string[]; limit?: number }) {
    const displayItems = limit ? items.slice(0, limit) : items;
    return (
        <div className={cn('grid gap-1.5', limit ? 'grid-cols-2' : 'grid-cols-1')}>
            {displayItems.map((c) => (
                <div
                    key={c}
                    className="flex items-start gap-1.5 text-xs"
                    style={{ color: 'var(--psj-text-2)' }}
                >
                    <CheckCircle2
                        size={12}
                        style={{ color: 'var(--psj-blue)', flexShrink: 0, marginTop: '1px' }}
                    />
                    <span className="truncate">{c}</span>
                </div>
            ))}
        </div>
    );
}

function MetaItem({
    label,
    value,
    icon: Icon,
}: {
    label: string;
    value: string;
    icon?: LucideIcon;
}) {
    return (
        <div>
            <div
                className="text-[10px] uppercase tracking-widest font-bold mb-1"
                style={{ color: 'var(--psj-text-3)' }}
            >
                {label}
            </div>
            <div
                className="text-sm font-bold flex items-center gap-1.5"
                style={{ color: 'var(--psj-text-1)' }}
            >
                {Icon && <Icon size={12} style={{ color: 'var(--psj-blue)' }} />} {value}
            </div>
        </div>
    );
}

type SolutionConfig = {
    icon: LucideIcon;
    color: string;
    categoryLabel?: undefined;
};

function SolutionHeader({ sol, config }: { sol: Solution; config: SolutionConfig }) {
    const Icon = config.icon;
    return (
        <div className="flex flex-wrap items-center gap-3 mb-3">
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
                <Icon size={11} /> {sol.category}
            </span>
            <span
                className="text-[10px] uppercase tracking-widest border px-1.5 py-0.5 font-medium"
                style={{ borderColor: 'var(--psj-border)', color: 'var(--psj-text-2)' }}
            >
                {sol.complexity}
            </span>
        </div>
    );
}

/* ─── Solution Card ─── */
function SolutionCard({
    sol,
    onSelect,
    labels,
}: {
    sol: Solution;
    onSelect: (s: Solution) => void;
    labels: Record<string, string>;
}) {
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
                    <div className="aspect-4/3 md:aspect-auto md:h-full overflow-hidden">
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
                    <SolutionHeader sol={sol} config={config} />
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

                    <div className="mb-4">
                        <CheckList items={sol.capabilities} limit={4} />
                    </div>

                    <div
                        className="flex flex-wrap items-center gap-1.5 pt-3"
                        style={{ borderTop: '1px solid var(--psj-border)' }}
                    >
                        <span
                            className="text-[10px] uppercase tracking-widest font-bold mr-1"
                            style={{ color: 'var(--psj-text-3)' }}
                        >
                            {labels.software}
                        </span>
                        {sol.software.map((s) => (
                            <Tag key={s}>{s}</Tag>
                        ))}
                    </div>
                </div>
                {/* Meta */}
                <div
                    className="md:col-span-2 p-5 flex flex-col justify-between"
                    style={{ background: 'var(--psj-surface-1)' }}
                >
                    <div className="space-y-4">
                        <MetaItem label={labels.duration} value={sol.duration} icon={Clock} />
                        <div>
                            <div
                                className="text-[10px] uppercase tracking-widest font-bold mb-1"
                                style={{ color: 'var(--psj-text-3)' }}
                            >
                                {labels.industry}
                            </div>
                            {sol.industry.slice(0, 2).map((i) => (
                                <div
                                    key={i}
                                    className="text-xs flex items-center gap-1 mt-1"
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
                        >
                            {labels.details} <ArrowRight size={12} />
                        </button>
                    </div>
                </div>
            </div>
        </article>
    );
}

/* ─── Detail Modal ─── */
function DetailModal({
    sol,
    onClose,
    labels,
}: {
    sol: Solution;
    onClose: () => void;
    labels: Record<string, string>;
}) {
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
                                        className="text-[10px] uppercase tracking-widest font-bold mb-3 flex items-center gap-1.5"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        <Settings size={12} /> {labels.capabilities}
                                    </h4>
                                    <CheckList items={sol.capabilities} />
                                </div>
                                <div>
                                    <h4
                                        className="text-[10px] uppercase tracking-widest font-bold mb-3 flex items-center gap-1.5"
                                        style={{ color: 'var(--psj-text-3)' }}
                                    >
                                        <Box size={12} /> {labels.deliverables}
                                    </h4>
                                    <div className="flex flex-wrap gap-1.5">
                                        {sol.deliverables.map((d) => (
                                            <Tag key={d} className="text-xs px-2.5 py-1">
                                                {d}
                                            </Tag>
                                        ))}
                                    </div>
                                </div>
                                <div
                                    className="grid grid-cols-2 gap-4 pt-4"
                                    style={{ borderTop: '1px solid var(--psj-border)' }}
                                >
                                    <MetaItem label={labels.duration} value={sol.duration} />
                                    <MetaItem label={labels.complexity} value={sol.complexity} />
                                </div>
                                <a href="#" className="psj-btn-primary w-full justify-center">
                                    {labels.requestConsultation}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </motion.div>
        </>
    );
}
