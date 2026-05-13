// ── Types ──────────────────────────────────────────────────────────────────────

export type NodeKind = 'root' | 'branch' | 'category' | 'leaf';

export interface NodeStyle {
    bg?: string;
    bd?: string;
    tx?: string;
}

export interface TreeNode {
    id: string;
    label: string;
    children?: TreeNode[];
    style?: NodeStyle;
}

export interface TokenSet {
    bg: string;
    bd: string;
    tx: string;
}

export interface ThemeTokens {
    root: TokenSet;
    branch: TokenSet;
    category: TokenSet;
    leaf: TokenSet;
}

export interface LayoutConfig {
    colW: number;
    colGap: number;
    rowGap: number;
    rootW: number;
    rootH: number;
    pad: number;
}

export interface LegendItem {
    kind: NodeKind;
    label: string;
}

export interface ChartConfig {
    title?: string;
    tree: TreeNode;
    theme: ThemeTokens;
    layout: LayoutConfig;
    legend: LegendItem[];
    chrome: {
        bg: string;
        panel: string;
        border: string;
        textMuted: string;
    };
}

// Internal — kind + resolved tokens baked in at layout time
export interface Rect {
    node: TreeNode;
    kind: NodeKind;
    tokens: TokenSet;
    x: number;
    y: number;
    w: number;
    h: number;
    depth: number;
}

// ── Kind derivation ────────────────────────────────────────────────────────────

export function deriveKind(depth: number, hasChildren: boolean): NodeKind {
    if (depth === 0) return 'root';
    if (!hasChildren) return 'leaf';
    if (depth === 1) return 'branch';
    return 'category';
}

// ── Token resolution ───────────────────────────────────────────────────────────

export function resolveTokens(base: TokenSet, override?: NodeStyle): TokenSet {
    if (!override) return base;
    return {
        bg: override.bg ?? base.bg,
        bd: override.bd ?? base.bd,
        tx: override.tx ?? base.tx,
    };
}

// ── Layout helpers ─────────────────────────────────────────────────────────────

export function nodeBoxH(depth: number, label: string, layout: LayoutConfig): number {
    if (depth === 0) return layout.rootH;
    const lines = label.split('\n').length;
    return lines === 1 ? 32 : lines === 2 ? 44 : 56;
}

export function subtreeH(node: TreeNode, depth: number, layout: LayoutConfig, collapsed: Set<string>): number {
    if (!node.children?.length || collapsed.has(node.id)) return nodeBoxH(depth, node.label, layout);

    const childHeights = node.children.map((c) => subtreeH(c, depth + 1, layout, collapsed));
    return childHeights.reduce((a, b) => a + b, 0) + layout.rowGap * (node.children.length - 1);
}

export function computeLayout(
    node: TreeNode,
    depth: number,
    x: number,
    y: number,
    layout: LayoutConfig,
    theme: ThemeTokens,
    collapsed: Set<string>,
    rects: Rect[] = [],
): Rect[] {
    const hasChildren = Boolean(node.children?.length);
    const kind = deriveKind(depth, hasChildren);
    const tokens = resolveTokens(theme[kind], node.style);
    const w = depth === 0 ? layout.rootW : layout.colW;
    const h = nodeBoxH(depth, node.label, layout);
    const sh = subtreeH(node, depth, layout, collapsed);

    rects.push({ node, kind, tokens, x, y: y + (sh - h) / 2, w, h, depth });

    if (hasChildren && !collapsed.has(node.id)) {
        let cy = y;
        for (const child of node.children!) {
            computeLayout(child, depth + 1, x + w + layout.colGap, cy, layout, theme, collapsed, rects);
            cy += subtreeH(child, depth + 1, layout, collapsed) + layout.rowGap;
        }
    }
    return rects;
}

export function allBranchIds(node: TreeNode, acc: string[] = []): string[] {
    if (node.children?.length) {
        acc.push(node.id);
        node.children.forEach((c) => allBranchIds(c, acc));
    }
    return acc;
}
