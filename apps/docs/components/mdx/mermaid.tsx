// components/mdx/mermaid.tsx  (server component — unchanged API)
import { parseMermaid, renderMermaidSVG } from 'beautiful-mermaid';
import { CodeBlock, Pre } from 'fumadocs-ui/components/codeblock';

import { MermaidViewer } from './mermaid-viewer';

// Route to full Mermaid.js when beautiful-mermaid can't handle the syntax
const COMPLEX_NODE_THRESHOLD = 20;
const COMPLEX_FANOUT_THRESHOLD = 8;

function classify(chart: string): { complex: boolean; largeSvg: boolean; svg?: string } {
    try {
        const graph = parseMermaid(chart);
        const maxFanOut = Math.max(
            0,
            ...Object.values(
                graph.edges.reduce<Record<string, number>>((acc, e) => {
                    acc[e.source] = (acc[e.source] ?? 0) + 1;
                    return acc;
                }, {}),
            ),
        );

        const complex = graph.nodes.size > COMPLEX_NODE_THRESHOLD || maxFanOut > COMPLEX_FANOUT_THRESHOLD;

        if (complex) return { complex: true, largeSvg: true };

        // render and check SVG dimensions
        const svg = renderMermaidSVG(chart, {
            bg: 'var(--color-fd-background)',
            fg: 'var(--color-fd-foreground)',
            line: 'var(--color-fd-border)',
            accent: 'var(--color-fd-primary)',
            muted: 'var(--color-fd-muted-foreground)',
            surface: 'var(--color-fd-muted)',
            border: 'var(--color-fd-border)',
            transparent: true,
            interactive: true,
        });

        const vb = svg
            .match(/viewBox="([\d. ]+)"/)?.[1]
            .split(' ')
            .map(Number);
        const svgW = vb?.[2] ?? 0;
        const svgH = vb?.[3] ?? 0;
        const largeSvg = svgW > 800 || svgH > 500;

        return { complex: false, largeSvg, svg };
    } catch {
        return { complex: true, largeSvg: true };
    }
}

export async function Mermaid({ chart }: { chart: string }) {
    const { complex, largeSvg, svg } = classify(chart);

    // full Mermaid.js engine for complex/unsupported syntax
    if (complex) {
        return <MermaidViewer chart={chart} mode="mermaid" />;
    }

    // beautiful-mermaid rendered SVG, but needs pan/zoom
    if (largeSvg && svg) {
        return <MermaidViewer svg={svg} mode="svg" />;
    }

    // small SVG — inline, no interactivity needed
    if (svg) {
        return (
            <div
                dangerouslySetInnerHTML={{ __html: svg }}
                className="overflow-x-auto [&_svg]:max-w-full [&_svg]:h-auto"
            />
        );
    }

    return (
        <CodeBlock title="Mermaid">
            <Pre>{chart}</Pre>
        </CodeBlock>
    );
}
