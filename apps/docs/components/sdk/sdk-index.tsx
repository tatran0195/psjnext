import Link from 'next/link';

import * as PageTree from 'fumadocs-core/page-tree';
import { Terminal } from 'lucide-react';

import { getFirstUrl } from '@/layouts/shared';
import { cn } from '@/lib/cn';
import { getSdk, source } from '@/lib/source';

interface SdkIndexProps {
    lang: string;
    versionId?: string;
}

export async function SdkIndex({ lang, versionId }: SdkIndexProps) {
    const { manifest } = await getSdk();
    const effectiveVersion = versionId || manifest.current_version;

    const tree = source.getPageTree(lang);
    const sdkNode = tree.children.find((node): node is PageTree.Folder => {
        if (node.type !== 'folder') return false;
        const title = (node as unknown as Record<string, unknown>).title || node.name;
        const url = (node as unknown as Record<string, unknown>).url || node.index?.url;

        if (title === 'API Reference' || node.name === 'api') return false;
        if (typeof url === 'string' && (url === '/api' || url.startsWith('/api/'))) return false;

        return (
            title === 'SDK' ||
            node.name === 'sdk' ||
            (typeof url === 'string' && (url === '/sdk' || url.startsWith('/sdk/')))
        );
    }) as PageTree.Folder | undefined;

    const versionNode = sdkNode?.children.find(
        (n) => n.type === 'folder' && n.name === effectiveVersion,
    ) as PageTree.Folder | undefined;

    const domainsWithUrls = manifest.domains.map((domain) => {
        const domainNode = versionNode?.children.find(
            (n): n is PageTree.Folder => n.type === 'folder' && n.name === domain.id,
        );

        const firstUrl = domainNode ? getFirstUrl(domainNode) : null;

        return {
            ...domain,
            url: firstUrl || `/${lang}/sdk/${effectiveVersion}/${domain.id}`,
        };
    });

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8">
            {domainsWithUrls.map((domain) => (
                <Link
                    key={domain.id}
                    href={domain.url}
                    className={cn(
                        'group flex items-start gap-4 p-4 rounded-2xl border bg-fd-card transition-all hover:shadow-lg hover:border-indigo-500/50',
                        'hover:bg-indigo-50/5 dark:hover:bg-indigo-500/5',
                    )}
                >
                    <div className="flex items-center justify-center rounded-xl size-12 shrink-0 bg-indigo-500/10 text-indigo-600 dark:bg-indigo-500/20 dark:text-indigo-400 group-hover:scale-110 transition-transform">
                        <Terminal className="size-6" />
                    </div>
                    <div className="flex flex-col gap-1">
                        <h3 className="font-bold text-lg group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
                            {domain.title}
                        </h3>
                        <p className="text-sm text-fd-muted-foreground line-clamp-2">
                            {`Explore the ${domain.title} reference and API documentation.`}
                        </p>
                        <div className="mt-2 text-xs font-semibold text-indigo-500 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                            View Reference <span>→</span>
                        </div>
                    </div>
                </Link>
            ))}
        </div>
    );
}
