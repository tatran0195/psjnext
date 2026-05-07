'use client';

import React, { ComponentProps, createContext, useContext } from 'react';

import type { ApiVersion } from '@/lib/api-versions';
import { ResolvedParam } from '../../../../../../lib/mdx-plugins/remark-param-gate-params';

// ─── Context ─────────────────────────────────────────────────────────────────

// Context carries only the already-resolved param for the current version
const ParamContext = createContext<ResolvedParam | null>(null);

// ─── Badge ────────────────────────────────────────────────────────────────────

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
            className={`ml-2 inline-flex items-center rounded-full border px-1.5 py-0 text-[10px] font-semibold uppercase ${colors[variant]}`}
        >
            {label}
        </span>
    );
}

// ─── PSJParamHeader ───────────────────────────────────────────────────────────

export function PSJParamHeader({ children, ...rest }: ComponentProps<'h3'>) {
    const param = useContext(ParamContext);

    if (!param) return <h3 {...rest}>{children}</h3>;

    const { type, required, since, deprecated } = param;
    const isDeprecated = !!deprecated;

    return (
        <h3 {...rest} style={{ opacity: isDeprecated ? 0.55 : 1 }}>
            {children}
            {type && statusBadge(type, 'info')}
            {required && !isDeprecated && statusBadge('required', 'secondary')}
            {since && statusBadge(`since ${since}`, 'success')}
            {isDeprecated && statusBadge(`deprecated ${deprecated}`, 'warning')}
        </h3>
    );
}

// ─── PSJParamSection ──────────────────────────────────────────────────────────

export function PSJParamSection({
    children,
    versionMap,
    currentVersion,
}: {
    children: React.ReactNode;
    versionMap: string;
    currentVersion: ApiVersion;
}) {
    const param: ResolvedParam = JSON.parse(versionMap)[currentVersion];

    if (!param?.visible) return null;

    return <ParamContext.Provider value={param}>{children}</ParamContext.Provider>;
}
