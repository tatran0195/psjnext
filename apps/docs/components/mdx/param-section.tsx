'use client';

import React, { ComponentProps, createContext, useContext } from 'react';

import { Callout } from 'fumadocs-ui/components/callout';

import type { ResolvedParam } from '@/lib/mdx-plugins/remark-version-gate-params';

import { semverGte } from '@/lib/api-versions';
import { cn } from '@/lib/cn';

interface ParamContextValue extends ResolvedParam {
    isDeprecated: boolean;
}

const ParamContext = createContext<ParamContextValue | null>(null);

export function ParamHeader({ children, ...rest }: ComponentProps<'h3'>) {
    const param = useContext(ParamContext);

    if (!param) return <h3 {...rest}>{children}</h3>;
    const { isDeprecated, deprecatedMessage, note, type, required } = param;

    return (
        <>
            <h3
                {...rest}
                className={cn(
                    'flex flex-wrap items-baseline gap-x-2 gap-y-1 mt-8 mb-1 text-[16px] font-bold group/param',
                    '[&_[data-param-asterisk]]:hidden',
                    rest.className,
                )}
                style={{ opacity: isDeprecated ? 0.55 : 1 }}
            >
                <span className="text-fd-foreground [&_code]:bg-transparent [&_code]:p-0 [&_code]:border-none [&_code]:text-current [&_code]:font-bold">
                    {children}
                </span>
                {type && (
                    <span className="font-mono text-[13px] font-medium text-fd-muted-foreground/50 ml-1">{type}</span>
                )}
                {required && (
                    <span className="text-[10px] font-bold text-red-600 dark:text-red-500 uppercase tracking-widest ml-1">
                        REQUIRED
                    </span>
                )}
            </h3>
            {isDeprecated && deprecatedMessage && (
                <Callout type="warn" className="whitespace-pre-wrap mt-2">
                    {deprecatedMessage}
                </Callout>
            )}
            {note && (
                <Callout type="info" className="whitespace-pre-wrap mt-2">
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
    currentVersion: string;
}) {
    const param: ResolvedParam = JSON.parse(versionMap)[currentVersion];

    if (!param?.visible) return null;

    const isDeprecated =
        (param.deprecated ? semverGte(currentVersion, param.deprecated) : false) || !!param.deprecatedMessage;

    return (
        <ParamContext.Provider value={{ ...param, isDeprecated }}>
            <div className="border-t border-fd-border/60 first:border-none first:pt-0">{children}</div>
        </ParamContext.Provider>
    );
}
