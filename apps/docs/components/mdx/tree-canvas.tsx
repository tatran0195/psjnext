'use client';

import { useCallback, useMemo, useState, type CSSProperties, type FC } from 'react';

import { ChevronsDown, ChevronsUp } from 'lucide-react';

import {
    allBranchIds,
    computeLayout,
    type LayoutConfig,
    type LegendItem,
    type Rect,
    type ThemeTokens,
    type TreeNode,
} from './tree-utils';

// ── Collapse helpers ──

function useCollapse(tree: TreeNode) {
    const [collapsed, setCollapsed] = useState<Set<string>>(new Set());

    const toggle = useCallback((id: string) => {
        setCollapsed((prev) => {
            const next = new Set(prev);
            if (next.has(id)) {
                next.delete(id);
            } else {
                next.add(id);
            }
            return next;
        });
    }, []);

    const expandAll = useCallback(() => setCollapsed(new Set()), []);
    const collapseAll = useCallback(() => setCollapsed(new Set(allBranchIds(tree))), [tree]);

    return { collapsed, toggle, expandAll, collapseAll };
}

// ── Expand/collapse circle indicator ──────────────────────────────────────────
//
// Rendered as an absolutely-positioned SVG *sibling* to the node box,
// so it is never affected by writingMode / transform on root nodes.

const INDICATOR_R = 5; // circle radius px

const ExpandIndicator: FC<{
    open: boolean;
    color: string;
    /** Canvas-space centre of the right edge of the node box */
    cx: number;
    cy: number;
    onClick: () => void;
}> = ({ open, color, cx, cy, onClick }) => {
    const size = (INDICATOR_R + 2) * 2; // svg bounding box

    return (
        <svg
            width={size}
            height={size}
            viewBox={`0 0 ${size} ${size}`}
            style={{
                position: 'absolute',
                // centre the svg over (cx, cy)
                left: cx - size / 2,
                top: cy - size / 2,
                cursor: 'pointer',
                zIndex: 1,
            }}
            onClick={(e) => {
                e.stopPropagation();
                onClick();
            }}
            aria-label={open ? 'Collapse' : 'Expand'}
            role="button"
        >
            {/* filled circle */}
            <circle cx={size / 2} cy={size / 2} r={INDICATOR_R} fill={color} opacity={0.85} />
            {/* minus or plus */}
            <line
                x1={size / 2 - 2.5}
                y1={size / 2}
                x2={size / 2 + 2.5}
                y2={size / 2}
                stroke="white"
                strokeWidth={1.5}
                strokeLinecap="round"
            />
            {!open && (
                <line
                    x1={size / 2}
                    y1={size / 2 - 2.5}
                    x2={size / 2}
                    y2={size / 2 + 2.5}
                    stroke="white"
                    strokeWidth={1.5}
                    strokeLinecap="round"
                />
            )}
        </svg>
    );
};

// ── Connectors ──

interface Segment {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
    color: string;
    key: string;
}

const Connectors: FC<{
    rects: Rect[];
    layout: LayoutConfig;
    width: number;
    height: number;
}> = ({ rects, layout, width, height }) => {
    const byId = Object.fromEntries(rects.map((r) => [r.node.id, r]));
    const segs: Segment[] = [];

    rects.forEach((r) => {
        if (!r.node.children?.length) return;

        const exitX = r.x + r.w;
        const exitY = r.y + r.h / 2;
        const midX = exitX + layout.colGap / 2;

        r.node.children.forEach((ch) => {
            const cr = byId[ch.id];
            if (!cr) return;

            const targetColor = cr.tokens.bd;

            // 1. Stem segment (shared horizontal part from parent to split point)
            segs.push({
                x1: exitX,
                y1: exitY,
                x2: midX,
                y2: exitY,
                color: targetColor,
                key: `${r.node.id}-${ch.id}-stem`,
            });

            // 2. Rail segment (vertical part to child's row)
            if (cr.y + cr.h / 2 !== exitY) {
                segs.push({
                    x1: midX,
                    y1: exitY,
                    x2: midX,
                    y2: cr.y + cr.h / 2,
                    color: targetColor,
                    key: `${r.node.id}-${ch.id}-rail`,
                });
            }

            // 3. Stub segment (horizontal part into child)
            segs.push({
                x1: midX,
                y1: cr.y + cr.h / 2,
                x2: cr.x,
                y2: cr.y + cr.h / 2,
                color: targetColor,
                key: `${r.node.id}-${ch.id}-stub`,
            });
        });
    });

    return (
        <svg
            width={width}
            height={height}
            style={{ position: 'absolute', top: 0, left: 0, overflow: 'visible', pointerEvents: 'none' }}
            aria-hidden="true"
        >
            {segs.map(({ x1, y1, x2, y2, color, key }) => (
                <line
                    key={key}
                    x1={x1}
                    y1={y1}
                    x2={x2}
                    y2={y2}
                    stroke={color}
                    strokeWidth={1.5}
                    strokeLinecap="round"
                />
            ))}
        </svg>
    );
};

// ── Node box ──

const NodeBox: FC<{
    rect: Rect;
    isOpen: boolean;
    onToggle?: () => void;
}> = ({ rect, isOpen, onToggle }) => {
    const { node, kind, tokens, x, y, w, h } = rect;
    const isRoot = kind === 'root';
    const hasKids = Boolean(node.children?.length);
    const lines = node.label.split('\n');

    const [isHovered, setIsHovered] = useState(false);

    const style: CSSProperties = {
        position: 'absolute',
        left: x,
        top: y,
        width: w,
        height: h,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        padding: isRoot ? '8px 6px' : '5px 10px',
        borderRadius: isRoot ? 8 : 6,
        border: `1.5px solid ${tokens.bd}`,
        background: tokens.bg,
        color: tokens.tx,
        fontSize: 11,
        fontWeight: isRoot ? 700 : kind === 'leaf' ? 400 : 500,
        lineHeight: 1.35,
        letterSpacing: isRoot ? '0.08em' : '0.01em',
        userSelect: 'none',
        writingMode: isRoot ? 'vertical-rl' : 'horizontal-tb',
        transform: isRoot ? 'rotate(180deg)' : 'none',
        // subtle dim when collapsed (non-root only), restored on hover
        opacity: !isRoot && hasKids && !isOpen && !isHovered ? 0.75 : 1,
        boxShadow: isHovered && hasKids ? `0 0 0 2px ${tokens.bd}44` : 'none',
        transition: 'opacity 0.15s, box-shadow 0.15s',
    };

    // Indicator sits on the right edge mid-height, in canvas space.
    const indicatorCX = x + w + INDICATOR_R;
    const indicatorCY = y + h / 2;

    return (
        <>
            <div
                style={{ ...style, cursor: onToggle ? 'pointer' : 'default' }}
                onClick={onToggle}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
            >
                {lines.map((l, i) => (
                    <span key={i}>{l}</span>
                ))}
            </div>

            {hasKids && onToggle && (
                <ExpandIndicator open={isOpen} color={tokens.bd} cx={indicatorCX} cy={indicatorCY} onClick={onToggle} />
            )}
        </>
    );
};

// ── Toolbar buttons ───

const ToolbarBtn: FC<{
    onClick: () => void;
    children: React.ReactNode;
    border: string;
    panel: string;
    textMuted: string;
    title?: string;
}> = ({ onClick, children, border, panel, textMuted, title }) => (
    <button
        onClick={onClick}
        title={title}
        style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            width: 28,
            height: 28,
            borderRadius: 6,
            border: `1px solid ${border}`,
            background: panel,
            color: textMuted,
            cursor: 'pointer',
            padding: 0,
            transition: 'all 0.15s',
            outline: 'none',
        }}
    >
        {children}
    </button>
);

// ── Legend (pure) ──────────────────────────────────────────────────────────────

const Legend: FC<{ items: LegendItem[]; theme: ThemeTokens; textMuted: string }> = ({ items, theme, textMuted }) => (
    <div style={{ display: 'flex', gap: 14, alignItems: 'center' }}>
        {items.map(({ kind, label }) => {
            const t = theme[kind];
            return (
                <div key={kind} style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    <div
                        style={{
                            width: 10,
                            height: 10,
                            borderRadius: '50%',
                            flexShrink: 0,
                            background: t.bg,
                            border: `1.5px solid ${t.bd}`,
                        }}
                    />
                    <span style={{ fontSize: 11, color: textMuted, fontWeight: 500 }}>{label}</span>
                </div>
            );
        })}
    </div>
);

// ── TreeCanvas (client) ────────────────────────────────────────────────────────

interface TreeCanvasProps {
    tree: TreeNode;
    theme: ThemeTokens;
    layout: LayoutConfig;
    chrome: {
        bg: string;
        panel: string;
        border: string;
        textMuted: string;
    };
    title?: string;
    legend?: LegendItem[];
}

export function TreeCanvas({ tree, theme, layout, chrome, title, legend }: TreeCanvasProps) {
    const { collapsed, toggle, expandAll, collapseAll } = useCollapse(tree);

    const rects = useMemo(
        () => computeLayout(tree, 0, 0, 0, layout, theme, collapsed),
        [tree, layout, theme, collapsed],
    );

    const canvasW = Math.max(...rects.map((r) => r.x + r.w)) + layout.pad;
    const canvasH = Math.max(...rects.map((r) => r.y + r.h)) + layout.pad;

    return (
        <>
            {/* Merged Toolbar */}
            <div
                style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '6px 12px',
                    borderBottom: `1px solid ${chrome.border}`,
                    background: chrome.panel,
                    minHeight: 40,
                }}
            >
                {/* Left: Title */}
                <div
                    style={{
                        fontSize: 12,
                        fontWeight: 600,
                        color: chrome.textMuted,
                        letterSpacing: '0.04em',
                    }}
                >
                    {title || 'Tree Chart'}
                </div>

                {/* Right: Controls + Legend */}
                <div style={{ display: 'flex', gap: 20, alignItems: 'center' }}>
                    {legend && <Legend items={legend} theme={theme} textMuted={chrome.textMuted} />}

                    <div
                        style={{
                            display: 'flex',
                            gap: 4,
                            paddingLeft: legend ? 16 : 0,
                            borderLeft: legend ? `1px solid ${chrome.border}` : 'none',
                        }}
                    >
                        <ToolbarBtn
                            onClick={expandAll}
                            border={chrome.border}
                            panel={chrome.panel}
                            textMuted={chrome.textMuted}
                            title="Expand all"
                        >
                            <ChevronsDown size={14} />
                        </ToolbarBtn>
                        <ToolbarBtn
                            onClick={collapseAll}
                            border={chrome.border}
                            panel={chrome.panel}
                            textMuted={chrome.textMuted}
                            title="Collapse all"
                        >
                            <ChevronsUp size={14} />
                        </ToolbarBtn>
                    </div>
                </div>
            </div>

            {/* Canvas Container */}
            <div
                style={{
                    overflow: 'auto',
                    padding: layout.pad,
                    display: 'flex',
                    justifyContent: canvasW < 800 ? 'center' : 'flex-start', // dynamic centering
                    background: chrome.bg,
                }}
            >
                <div
                    style={{
                        position: 'relative',
                        width: canvasW,
                        height: canvasH,
                        flexShrink: 0,
                    }}
                >
                    <Connectors rects={rects} layout={layout} width={canvasW} height={canvasH} />
                    {rects.map((r) => (
                        <NodeBox
                            key={r.node.id}
                            rect={r}
                            isOpen={!collapsed.has(r.node.id)}
                            onToggle={r.node.children?.length ? () => toggle(r.node.id) : undefined}
                        />
                    ))}
                </div>
            </div>
        </>
    );
}
