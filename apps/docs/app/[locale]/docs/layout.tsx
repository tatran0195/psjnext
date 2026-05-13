import { Locale } from 'next-intl';

import { PsjLogo } from '@/components/icons/psj-logo';
import { PromoCard } from '@/components/promo-card';
import { DocsLayout } from '@/layouts/docs';
import { navLinks } from '@/lib/nav-links';
import { source } from '@/lib/source';

export default async function Layout({ children, params }: LayoutProps<'/[locale]'>) {
    const { locale } = await params;
    const tree = source.getPageTree(locale);
    return (
        <DocsLayout
            tree={tree}
            tabs={[]}
            links={navLinks}
            nav={{ mode: 'top', title: <PsjLogo /> }}
            sidebar={{ footer: <PromoCard locale={locale as Locale} key="promo-card" /> }}
        >
            {children}
        </DocsLayout>
    );
}
