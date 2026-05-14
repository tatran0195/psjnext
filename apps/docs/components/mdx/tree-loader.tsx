import type { ReactNode } from 'react';

import * as fs from 'node:fs';
import yaml from 'yaml';

import TreeChart from './tree-chart';
import { type ChartConfig } from './tree-utils';

interface TreeChartLoaderProps {
    chartPath: string;
    showLegend?: boolean;
    footer?: ReactNode;
}

export default function TreeChartLoader({ chartPath, showLegend, footer }: TreeChartLoaderProps) {
    const raw = fs.readFileSync(chartPath, 'utf8');
    const config = yaml.parse(raw) as ChartConfig;

    return <TreeChart config={config} showLegend={showLegend} footer={footer} />;
}
