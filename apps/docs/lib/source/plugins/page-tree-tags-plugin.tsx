import type { LoaderPlugin } from 'fumadocs-core/source';

const DEFAULT_TAG_STYLES: Record<string, string> = {
    New: 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300',
    Alpha: 'bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300',
    Beta: 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300',
    Experimental: 'bg-amber-100 text-amber-700 dark:bg-amber-900 dark:text-amber-300',
    Deprecated: 'bg-rose-100 text-rose-700 dark:bg-rose-900 dark:text-rose-300',
};

export function pageTreeTagsPlugin(
    styles: Record<string, string> = DEFAULT_TAG_STYLES,
): LoaderPlugin {
    return {
        transformPageTree: {
            file(node, filePath) {
                const path = filePath || (node as { $ref?: { file: string } }).$ref?.file;
                const data =
                    (node as unknown as { data?: { tag?: string } }).data ||
                    (path
                        ? (this.storage.read(path)?.data as { tag?: string } | undefined)
                        : undefined);
                const tag = (data as { tag?: string } | undefined)?.tag;

                if (!tag || typeof tag !== 'string') return node;

                const style =
                    styles[tag] ??
                    'bg-neutral-100 text-neutral-700 dark:bg-neutral-800 dark:text-neutral-300';

                return {
                    ...node,
                    name: (
                        <span
                            key="tag-wrapper"
                            className="flex items-center gap-2 overflow-hidden w-full"
                        >
                            <span className="truncate flex-1">{node.name}</span>
                            <span
                                className={`rounded-md px-1.5 py-0.5 text-[9px] font-bold leading-none uppercase tracking-wider shrink-0 select-none ${style}`}
                            >
                                {tag}
                            </span>
                        </span>
                    ),
                };
            },
        },
    };
}
