import { ComponentProps } from 'react';

import { ArrowRight, Sparkles, Zap } from 'lucide-react';
import { type Locale } from 'next-intl';
import { getTranslations } from 'next-intl/server';

import { cn } from '@/lib/cn';

export const PromoCard = async ({ locale, ...props }: ComponentProps<'div'> & { locale: Locale }) => {
    const t = await getTranslations({ locale, namespace: 'docs.promoCard' });

    return (
        <div {...props} className={cn('-mx-1', props.className)}>
            <div className="relative overflow-hidden rounded-xl bg-gradient-to-br from-primary/15 via-primary/8 to-transparent border border-primary/20 p-4">
                {/* Background decorative elements */}
                <div className="absolute top-0 right-0 w-20 h-20 bg-primary/10 rounded-full -translate-y-8 translate-x-8 blur-xl" />
                <div className="absolute bottom-0 left-0 w-16 h-16 bg-primary/8 rounded-full translate-y-6 -translate-x-6 blur-lg" />

                {/* Subtle grid pattern */}
                <div
                    className="absolute inset-0 opacity-[0.03]"
                    style={{
                        backgroundImage: `radial-gradient(circle, currentColor 1px, transparent 1px)`,
                        backgroundSize: '12px 12px',
                    }}
                />

                <div className="relative">
                    {/* Badge */}
                    <div className="inline-flex items-center gap-1.5 mb-3">
                        <Sparkles size={10} className="text-primary" />
                        <span className="text-[10px] font-medium text-primary tracking-wide">{t('badge')}</span>
                    </div>

                    {/* Heading */}
                    <h4 className="text-sm font-bold text-foreground leading-snug mb-1.5">{t('heading')}</h4>

                    {/* Description */}
                    <p className="text-[11.5px] text-foreground/60 leading-relaxed mb-3.5">{t('description')}</p>

                    {/* CTA Button */}
                    <button className="group w-full flex items-center justify-between bg-primary hover:bg-primary/90 text-primary-foreground rounded-lg px-3 py-2.5 transition-all duration-200 hover:shadow-md hover:shadow-primary/25">
                        <div className="flex items-center gap-2">
                            <Zap size={11} className="fill-primary-foreground" />
                            <span className="text-[12px] font-semibold">{t('cta')}</span>
                        </div>
                        <ArrowRight
                            size={12}
                            className="transition-transform duration-200 group-hover:translate-x-0.5"
                        />
                    </button>
                </div>
            </div>
        </div>
    );
};
