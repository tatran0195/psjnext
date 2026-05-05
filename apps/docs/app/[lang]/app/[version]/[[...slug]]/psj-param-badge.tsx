'use client';

import React, { ComponentProps, createContext, useContext } from 'react';

import { ApiVersion } from '@/lib/api-versions';
import { semverGte } from '@/lib/mdx-plugins/utils';

type ParamMetadata = {
    name?: string;
    since?: string;
    removed?: string;
    deprecated?: string;
    type?: string;
    required?: string;
};

const ParamMetadataContext = createContext<ParamMetadata | null>(null);

function statusBadge(
    label: string,
    variant: 'secondary' | 'warning' | 'success' | 'info' = 'secondary',
) {
    const colors = {
        secondary: 'bg-secondary text-secondary-foreground',
        warning: 'bg-orange-500/20 text-orange-500 border-orange-500/20',
        success: 'bg-green-500/20 text-green-500 border-green-500/20',
        info: 'bg-blue-500/20 text-blue-500 border-blue-500/20',
    };

    return (
        <span
            className={`ml-2 inline-flex items-center rounded-full border px-1.5 py-0 text-[10px] font-semibold uppercase transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 ${colors[variant]}`}
        >
            {label}
        </span>
    );
}

export function PSJParamHeader({
    currentVersion,
    children: _children,
    ...rest
}: {
    currentVersion: ApiVersion;
} & ComponentProps<'h3'>) {
    const meta = useContext(ParamMetadataContext);

    // If no meta context, just render standard h3
    if (!meta) return <h3 {...rest}>{_children}</h3>;

    const { since, removed, deprecated, type, required } = meta;

    const isDeprecatedHere = deprecated ? semverGte(currentVersion, deprecated) : false;

    return (
        <h3 {...rest} style={{ opacity: isDeprecatedHere ? 0.55 : 1 }}>
            {_children}
            {type && statusBadge(type, 'info')}
            {required === 'true' && !isDeprecatedHere && statusBadge('required', 'secondary')}
            {since && statusBadge(`since ${since}`, 'success')}
            {isDeprecatedHere && statusBadge(`deprecated ${deprecated}`, 'warning')}
        </h3>
    );
}

export function PSJParamSection({
    children,
    since,
    removed,
    deprecated,
    type,
    required,
    currentVersion,
    debugId,
}: {
    children: React.ReactNode;
    since?: string;
    removed?: string;
    deprecated?: string;
    type?: string;
    required?: string;
    currentVersion: ApiVersion;
    debugId?: string;
}) {
    console.log(
        `[DEBUG-CLIENT] ParamSection: version=${currentVersion}, since=${since}, removed=${removed}, debugId=${debugId}`,
    );
    // Visibility gating
    if (since && !semverGte(currentVersion, since)) return null;
    if (removed && semverGte(currentVersion, removed)) return null;

    const meta = { since, removed, deprecated, type, required };

    return <ParamMetadataContext.Provider value={meta}>{children}</ParamMetadataContext.Provider>;
}
