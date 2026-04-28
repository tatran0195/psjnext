'use client';
import type { ComponentProps } from 'react';

import { NextProvider } from 'fumadocs-core/framework/next';

import { RootProvider as BaseProvider } from './base';

export type RootProviderProps = ComponentProps<typeof BaseProvider>;

export function RootProvider({ ...props }: RootProviderProps) {
    return (
        <NextProvider>
            <BaseProvider {...props}>{props.children}</BaseProvider>
        </NextProvider>
    );
}
