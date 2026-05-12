// components/mdx/mermaid-viewer.tsx
'use client';

import { useCallback, useEffect, useRef, useState } from 'react';

import { CodeBlock, Pre } from 'fumadocs-ui/components/codeblock';
import { Maximize2, ZoomIn, ZoomOut } from 'lucide-react';

import type Panzoom from '@panzoom/panzoom';

// ── Types ─────────────────────────────────────────────────────────────────────

type Props = { mode: 'svg'; svg: string; chart?: never } | { mode: 'mermaid'; chart: string; svg?: never };

type RenderResult = { svg: string; bindFunctions?: (el: Element) => void };

type PanzoomInstance = ReturnType<typeof Panzoom>;

// ── Constants ─────────────────────────────────────────────────────────────────

const MERMAID_CONFIG = {
    startOnLoad: false,
    securityLevel: 'loose',
    fontFamily: 'inherit',
    theme: 'default',
    layout: 'elk',
    flowchart: { curve: 'stepBefore', htmlLabels: false },
} as const;

const PANZOOM_OPTIONS = {
    maxScale: 8,
    minScale: 0.1,
    step: 0.15,
    contain: 'outside',
    canvas: true,
} as const;

// ── Mermaid singleton + render cache (client-only) ────────────────────────────

const mermaidCache = new Map<string, Promise<RenderResult>>();
let mermaidReady: Promise<typeof import('mermaid').default> | null = null;

async function getMermaid() {
    if (mermaidReady) return mermaidReady;

    mermaidReady = (async () => {
        const [{ default: mermaid }, { default: elkLayouts }] = await Promise.all([
            import('mermaid'),
            import('@mermaid-js/layout-elk'),
        ]);

        mermaid.registerLayoutLoaders(elkLayouts);
        mermaid.initialize(MERMAID_CONFIG);

        return mermaid;
    })();

    return mermaidReady;
}

async function renderWithMermaid(chart: string): Promise<RenderResult> {
    const mermaid = await getMermaid();
    const renderId = `mermaid-${Math.random().toString(36).slice(2)}`;

    // Attach an off-screen host required by mermaid internals
    const host = document.createElement('div');
    host.style.cssText = 'position:absolute;top:-9999px;left:-9999px;visibility:hidden';
    document.body.appendChild(host);

    // Patch JSON.stringify to swallow circular refs produced during render
    const origStringify = JSON.stringify;
    JSON.stringify = ((value: unknown, ...args: unknown[]) => {
        try {
            return (origStringify as (...a: unknown[]) => string)(value, ...args);
        } catch {
            return '"[circular]"';
        }
    }) as typeof JSON.stringify;

    try {
        return await mermaid.render(renderId, chart.replaceAll('\\n', '\n'));
    } finally {
        JSON.stringify = origStringify;
        host.remove();
    }
}

// ── Panzoom module cache ───────────────────────────────────────────────────────

let panzoomModulePromise: Promise<typeof Panzoom> | null = null;

function getPanzoom(): Promise<typeof Panzoom> {
    panzoomModulePromise ??= import('@panzoom/panzoom').then((m) => m.default);
    return panzoomModulePromise;
}

// ── Component ─────────────────────────────────────────────────────────────────

export function MermaidViewer({ mode, svg: staticSvg, chart }: Props) {
    const viewportRef = useRef<HTMLDivElement>(null);
    const panzoomRef = useRef<PanzoomInstance | null>(null);

    const [result, setResult] = useState<RenderResult | null>(staticSvg ? { svg: staticSvg } : null);
    const [error, setError] = useState(false);

    // Mermaid mode: render client-side with caching
    useEffect(() => {
        if (mode !== 'mermaid' || !chart) return;

        let cancelled = false;
        const key = `mermaid::${chart}`;

        if (!mermaidCache.has(key)) {
            mermaidCache.set(key, renderWithMermaid(chart));
        }

        mermaidCache
            .get(key)!
            .then((r) => {
                if (!cancelled) setResult(r);
            })
            .catch(() => {
                if (!cancelled) setError(true);
            });

        return () => {
            cancelled = true;
        };
    }, [chart, mode]);

    // Wire panzoom after SVG is mounted
    useEffect(() => {
        const viewport = viewportRef.current;
        if (!viewport || !result) return;

        result.bindFunctions?.(viewport);

        const svgEl = viewport.querySelector<SVGSVGElement>('svg');
        if (!svgEl) return;

        // Make the SVG fluid so panzoom can scale it freely
        Object.assign(svgEl.style, { width: '100%', height: '100%', overflow: 'visible' });
        svgEl.removeAttribute('width');
        svgEl.removeAttribute('height');

        let destroyed = false;
        let pz: PanzoomInstance | null = null;
        const parent = viewport.parentElement;

        getPanzoom().then((PanzoomCtor) => {
            if (destroyed) return;

            pz = PanzoomCtor(svgEl, PANZOOM_OPTIONS);
            parent?.addEventListener('wheel', pz.zoomWithWheel, { passive: false });
            panzoomRef.current = pz;
        });

        return () => {
            destroyed = true;
            // pz may still be null if the import hasn't resolved yet
            if (pz) {
                parent?.removeEventListener('wheel', pz.zoomWithWheel);
                pz.destroy();
            }
            panzoomRef.current = null;
        };
    }, [result]);

    const zoomIn = useCallback(() => panzoomRef.current?.zoomIn(), []);
    const zoomOut = useCallback(() => panzoomRef.current?.zoomOut(), []);
    const reset = useCallback(() => panzoomRef.current?.reset(), []);

    if (error) {
        return (
            <CodeBlock title="Mermaid">
                <Pre>{chart ?? ''}</Pre>
            </CodeBlock>
        );
    }

    return (
        <div className="group relative w-full overflow-hidden rounded-lg border border-fd-border bg-fd-background">
            {/* Toolbar */}
            <div className="absolute right-3 top-3 z-10 flex items-center gap-1 rounded-md border border-fd-border bg-fd-background/90 p-1 shadow-sm backdrop-blur-sm opacity-0 transition-opacity duration-150 group-hover:opacity-100">
                <ToolBtn title="Zoom in" onClick={zoomIn}>
                    {' '}
                    <ZoomIn size={13} />
                </ToolBtn>
                <ToolBtn title="Zoom out" onClick={zoomOut}>
                    {' '}
                    <ZoomOut size={13} />
                </ToolBtn>
                <div className="mx-0.5 h-3.5 w-px bg-fd-border" />
                <ToolBtn title="Reset" onClick={reset}>
                    {' '}
                    <Maximize2 size={13} />
                </ToolBtn>
            </div>

            {/* Hint */}
            <p className="pointer-events-none absolute bottom-0 left-1/2 -translate-x-1/2 whitespace-nowrap text-[11px] text-fd-muted-foreground opacity-0 transition-opacity duration-150 group-hover:opacity-100">
                Scroll to zoom · Drag to pan
            </p>

            {/* Viewport */}
            <div className="h-[520px] w-full cursor-grab overflow-hidden active:cursor-grabbing">
                {result ? (
                    <div ref={viewportRef} className="h-full w-full" dangerouslySetInnerHTML={{ __html: result.svg }} />
                ) : (
                    <MermaidSkeleton />
                )}
            </div>
        </div>
    );
}

// ── Sub-components ────────────────────────────────────────────────────────────

function ToolBtn({ title, onClick, children }: { title: string; onClick(): void; children: React.ReactNode }) {
    return (
        <button
            title={title}
            onClick={onClick}
            className="flex h-6 w-6 items-center justify-center rounded text-fd-muted-foreground transition-colors duration-100 hover:bg-fd-muted hover:text-fd-foreground"
        >
            {children}
        </button>
    );
}

function MermaidSkeleton() {
    return (
        <div className="flex h-full w-full animate-pulse items-center justify-center">
            <div className="flex flex-col items-center gap-3 opacity-40">
                <div className="h-10 w-36 rounded-md bg-fd-muted" />
                <div className="h-6 w-px bg-fd-muted" />
                <div className="flex gap-6">
                    <div className="h-10 w-28 rounded-md bg-fd-muted" />
                    <div className="h-10 w-28 rounded-md bg-fd-muted" />
                </div>
                <div className="h-6 w-px bg-fd-muted" />
                <div className="flex gap-4">
                    <div className="h-10 w-24 rounded-md bg-fd-muted" />
                    <div className="h-10 w-32 rounded-md bg-fd-muted" />
                </div>
            </div>
        </div>
    );
}
