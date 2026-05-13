import type { ReactNode } from 'react';

import { TooltipProvider } from '@radix-ui/react-tooltip';

import { LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { i18nUI } from '@/lib/i18n';

import { BaseProvider } from './provider.base';

type Props = {
    children: ReactNode;
    lang: string;
};

export function Provider({ children, lang }: Props) {
    return (
        <BaseProvider
            i18n={i18nUI.provider(lang)}
            theme={{ enabled: true, defaultTheme: 'system', enableSystem: true }}
        >
            <TooltipProvider>
                <LinkSidebarProvider>{children}</LinkSidebarProvider>
            </TooltipProvider>
        </BaseProvider>
    );
}
