import type { ReactNode } from 'react';

import { TreeCanvas } from './tree-canvas';
import { type ChartConfig } from './tree-utils';

interface TreeChartProps {
    config: ChartConfig;
    showLegend?: boolean;
    footer?: ReactNode;
}

export default function TreeChart({ config, showLegend = false, footer }: TreeChartProps) {
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
