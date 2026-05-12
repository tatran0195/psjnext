import type { LoaderPlugin } from 'fumadocs-core/source';

export function codeTitlesPlugin(): LoaderPlugin {
    return {
        transformPageTree: {
            file(node) {
                if (typeof node.name === 'string' && (node.name.endsWith('()') || node.name.match(/^<\w+ \/>$/))) {
                    return {
                        ...node,
                        name: (
                            <code key="0" className="text-[0.8125rem]">
                                {node.name}
                            </code>
                        ),
                    };
                }
                return node;
            },
        },
    };
}
