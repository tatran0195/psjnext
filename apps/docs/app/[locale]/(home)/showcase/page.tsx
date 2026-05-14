import { getTranslations } from 'next-intl/server';

import { HeroSection } from '@/components/hero-sections';
import { CtaBand } from '@/components/sections/cta-band';

import ShowcaseClient from './page.client';

export default async function CAEServicesPage({ params }: { params: Promise<{ locale: string }> }) {
    const { locale } = await params;
    const t = await getTranslations('showcase');

    return (
        <div
            style={{
                background: 'var(--psj-surface-0)',
                color: 'var(--psj-text-1)',
                minHeight: '100vh',
            }}
        >
            <HeroSection label={t('header.label')} title={t('header.title')} description={t('header.desc')} />

            {/* ─────── MAIN LAYOUT ─────── */}
            <ShowcaseClient locale={locale} />

            {/* ─────── BOTTOM CTA ─────── */}
            <CtaBand
                subtitle={t('cta.subtitle')}
                title={t('cta.title')}
                description={t('cta.desc')}
                primaryLink={{ href: '#', label: t('cta.primaryLabel') }}
                secondaryLink={{ href: '#', label: t('cta.secondaryLabel') }}
            />
        </div>
    );
}
