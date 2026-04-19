'use client';

import dynamic from 'next/dynamic';
import type { ReactNode } from 'react';

import { TooltipProvider } from '@radix-ui/react-tooltip';
import { RootProvider } from 'fumadocs-ui/provider/base';

const SearchDialog = dynamic(() => import('@/components/layouts/search'), {
    ssr: false,
});

export function Provider({ children }: { children: ReactNode }) {
    return (
        <RootProvider search={{ SearchDialog }}>
            <TooltipProvider>{children}</TooltipProvider>
        </RootProvider>
    );
}
