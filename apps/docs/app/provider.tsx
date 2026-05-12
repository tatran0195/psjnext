import type { ReactNode } from 'react';

import { TooltipProvider } from '@radix-ui/react-tooltip';

import { LinkSidebarProvider } from '@/components/mdx/link-sidebar';
import { VersionProvider } from '@/contexts/versions';
import { i18nUI } from '@/lib/i18n';
import { getApiVersions } from '@/lib/source';

import { BaseProvider } from './provider.base';

type Props = {
    children: ReactNode;
    lang: string;
};

export function Provider({ children, lang }: Props) {
    const versions = getApiVersions();
    return (
        <BaseProvider
            i18n={i18nUI.provider(lang)}
            theme={{ enabled: true, defaultTheme: 'system', enableSystem: true }}
        >
            <VersionProvider versions={versions}>
                <TooltipProvider>
                    <LinkSidebarProvider>{children}</LinkSidebarProvider>
                </TooltipProvider>
            </VersionProvider>
        </BaseProvider>
    );
}
