'use client';

import React, { ComponentProps, createContext, useContext } from 'react';

import type { ResolvedParam } from '@/lib/mdx-plugins/remark-param-gate-params';

import { semverGte, type ApiVersion } from '@/lib/api-versions';

// ─── Context ──────────────────────────────────────────────────────────────────

interface ParamContextValue extends ResolvedParam {
    isDeprecated: boolean;
}

const ParamContext = createContext<ParamContextValue | null>(null);

// ─── Badge ────────────────────────────────────────────────────────────────────

type BadgeVariant = 'secondary' | 'warning' | 'success' | 'info';

const BADGE_COLORS: Record<BadgeVariant, string> = {
    secondary: 'bg-secondary text-secondary-foreground',
    warning: 'bg-orange-500/20 text-orange-500 border-orange-500/20',
    success: 'bg-green-500/20 text-green-500 border-green-500/20',
    info: 'bg-blue-500/20 text-blue-500 border-blue-500/20',
};

function StatusBadge({ label, variant = 'secondary' }: { label: string; variant?: BadgeVariant }) {
    return (
        <span
            className={`ml-2 inline-flex items-center rounded-full border px-1.5 py-0 text-[10px] font-semibold uppercase ${BADGE_COLORS[variant]}`}
        >
            {label}
        </span>
    );
}

// ─── ParamHeader ───────────────────────────────────────────────────────────
// No version logic here — isDeprecated is pre-resolved by ParamSection.

export function ParamHeader({ children, ...rest }: ComponentProps<'h3'>) {
    const param = useContext(ParamContext);

    if (!param) return <h3 {...rest}>{children}</h3>;

    const { type, required, since, deprecated, isDeprecated } = param;

    return (
        <h3 {...rest} style={{ opacity: isDeprecated ? 0.55 : 1 }}>
            {children}
            {type && <StatusBadge label={type} variant="info" />}
            {required && !isDeprecated && <StatusBadge label="required" />}
            {since && <StatusBadge label={`since ${since}`} variant="success" />}
            {isDeprecated && <StatusBadge label={`deprecated ${deprecated}`} variant="warning" />}
        </h3>
    );
}

// ─── ParamSection ──────────────────────────────────────────────────────────

export function ParamSection({
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

    const isDeprecated = param.deprecated ? semverGte(currentVersion, param.deprecated) : false;

    return (
        <ParamContext.Provider value={{ ...param, isDeprecated }}>{children}</ParamContext.Provider>
    );
}
