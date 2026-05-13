import type { ReactNode } from 'react';

import * as fs from 'node:fs';
import * as path from 'node:path';
import yaml from 'yaml';

import { TreeCanvas } from './tree-canvas';
import { type ChartConfig } from './tree-utils';

// ── Root (server) component ────────────────────────────────────────────────────

interface TreeChartProps {
    chartPath: string;
    showLegend?: boolean;
    footer?: ReactNode;
}

export default function TreeChart({ chartPath, showLegend = false, footer }: TreeChartProps) {
    const raw = fs.readFileSync(path.join(process.cwd(), chartPath), 'utf8');
    const config = yaml.parse(raw) as ChartConfig;
    const { tree, theme, layout, legend, chrome, title } = config;

    return (
        <div
            style={{
                background: chrome.bg,
                borderRadius: 10,
                border: `1px solid ${chrome.border}`,
                overflow: 'hidden',
                fontFamily: 'system-ui, sans-serif',
            }}
        >
            {/* Interactive canvas — client boundary (now includes toolbar) */}
            <TreeCanvas
                tree={tree}
                theme={theme}
                layout={layout}
                chrome={chrome}
                title={title}
                legend={showLegend ? legend : undefined}
            />

            {/* Footer */}
            {footer && (
                <div
                    style={{
                        padding: '6px 14px',
                        borderTop: `1px solid ${chrome.border}`,
                        fontSize: 11,
                        color: chrome.textMuted,
                    }}
                >
                    {footer}
                </div>
            )}
        </div>
    );
}
