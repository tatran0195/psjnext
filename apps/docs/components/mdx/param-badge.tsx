'use client';

import React, { ComponentProps, createContext, useContext } from 'react';

import { Callout } from 'fumadocs-ui/components/callout';

import type { ResolvedParam } from '@/lib/mdx-plugins/remark-version-gate-params';

import { semverGte, type ApiVersion } from '@/lib/api-versions';
import { cn } from '@/lib/cn';

interface ParamContextValue extends ResolvedParam {
    isDeprecated: boolean;
}

const ParamContext = createContext<ParamContextValue | null>(null);

export function ParamHeader({ children, ...rest }: ComponentProps<'h3'>) {
    const param = useContext(ParamContext);

    if (!param) return <h3 {...rest}>{children}</h3>;
    const { isDeprecated, deprecatedMessage, note } = param;

    return (
        <>
            <h3
                {...rest}
                className={cn('flex flex-wrap items-center gap-2', rest.className)}
                style={{ opacity: isDeprecated ? 0.55 : 1 }}
            >
                {children}
            </h3>
            {isDeprecated && deprecatedMessage && (
                <Callout type="warn" className="whitespace-pre-wrap">
                    {deprecatedMessage}
                </Callout>
            )}
            {note && (
                <Callout type="info" className="whitespace-pre-wrap">
                    {note}
                </Callout>
            )}
        </>
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

    const isDeprecated =
        (param.deprecated ? semverGte(currentVersion, param.deprecated) : false) ||
        !!param.deprecatedMessage;

    return (
        <ParamContext.Provider value={{ ...param, isDeprecated }}>{children}</ParamContext.Provider>
    );
}
