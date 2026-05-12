import type { LoaderPlugin } from 'fumadocs-core/source';

export function codeTitlesPlugin(): LoaderPlugin {
    return {
        transformPageTree: {
            file(node) {
                if (typeof node.name !== 'string') return node;
                const trimmed = node.name.trim();
                if (trimmed.endsWith('()') || /^<\w[\w.]*\s*\/>$/.test(trimmed)) {
                    return {
                        ...node,
                        name: (
                            <code key="0" className="text-[0.8125rem]">
                                {trimmed}
                            </code>
                        ),
                    };
                }
                return node;
            },
        },
    };
}
