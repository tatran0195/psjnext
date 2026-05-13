'use client';
import { useRouter } from 'next/navigation';
import { useMemo, useState } from 'react';

import { useDocsSearch } from 'fumadocs-core/search/client';
import {
    SearchDialog,
    SearchDialogClose,
    SearchDialogContent,
    SearchDialogFooter,
    SearchDialogHeader,
    SearchDialogIcon,
    SearchDialogInput,
    SearchDialogList,
    SearchDialogOverlay,
    type SearchItemType,
    type SharedProps,
} from 'fumadocs-ui/components/dialog/search';
import { useI18n } from 'fumadocs-ui/contexts/i18n';
import { useTreeContext } from 'fumadocs-ui/contexts/tree';
import { ArrowRight } from 'lucide-react';

import { ListMenu } from '@/components/ui/list-menu';
import { useThrottledValue } from '@/hooks/use-throttle';
import { compareSemver, matchesSearch } from '@/lib/search';

import type { Item, Node } from 'fumadocs-core/page-tree';
import type { SortedResult } from 'fumadocs-core/search';

const TAGS = [
    {
        name: 'All',
        description: 'All results',
        value: undefined,
    },
];

const BEHAVIORS = [
    {
        name: 'Partial Match',
        description: 'Matches similar or partial terms',
        value: undefined,
    },
    {
        name: 'Phrases Match',
        description: 'Matches the term as a phrase',
        value: 'exact',
    },
];

export default function CustomSearchDialog(props: SharedProps) {
    const { locale } = useI18n();
    const [version, setVersion] = useState<string | undefined>();
    const [behavior, setBehavior] = useState<string | undefined>();
    const { search, setSearch, query } = useDocsSearch({
        type: 'fetch',
        tag: version,
        locale,
    });
    const { full } = useTreeContext();
    const router = useRouter();
    const throttledSearch = useThrottledValue(search, 100);
    const searchMap = useMemo(() => {
        const map = new Map<string, Item>();

        function onNode(node: Node) {
            if (node.type === 'page' && typeof node.name === 'string') {
                map.set(node.name.toLowerCase(), node);
            } else if (node.type === 'folder') {
                if (node.index) onNode(node.index);
                for (const item of node.children) onNode(item);
            }
        }

        for (const item of full.children) onNode(item);
        return map;
    }, [full]);

    const pageTreeAction = useMemo<SearchItemType | undefined>(() => {
        if (search.length === 0) return;

        const normalized = search.toLowerCase();
        for (const [k, page] of searchMap) {
            if (!k.startsWith(normalized)) continue;

            return {
                id: 'quick-action',
                type: 'action',
                node: (
                    <div className="inline-flex items-center gap-2 text-fd-muted-foreground">
                        <ArrowRight className="size-4" />
                        <p>
                            Jump to <span className="font-medium text-fd-foreground">{page.name}</span>
                        </p>
                    </div>
                ),
                onSelect: () => router.push(page.url),
            };
        }
    }, [router, search, searchMap]);

    const searchData = useMemo(() => {
        const filter = (_data: SortedResult<string>[] | 'empty' | undefined) => {
            const data = _data?.slice(0, 100);
            return [
                ...(Array.isArray(data)
                    ? data
                          .filter((item) => matchesSearch(item, throttledSearch, behavior === 'exact'))
                          .sort((a, b) => {
                              const versionRegex = /^\d+\.\d+\.\d+$/;
                              const aVersion = versionRegex.exec(a.id);
                              const bVersion = versionRegex.exec(b.id);
                              if (!aVersion || !bVersion) return 0;

                              return compareSemver(bVersion[0], aVersion[0]);
                          })
                    : []),
            ];
        };
        return query.data !== 'empty' || pageTreeAction
            ? [...(pageTreeAction ? [pageTreeAction] : []), ...filter(query.data)]
            : null;
    }, [behavior, throttledSearch, query.data, pageTreeAction]);

    return (
        <SearchDialog search={search} onSearchChange={setSearch} isLoading={query.isLoading} {...props}>
            <SearchDialogOverlay />
            <SearchDialogContent>
                <SearchDialogHeader>
                    <SearchDialogIcon />
                    <SearchDialogInput />
                    <SearchDialogClose />
                </SearchDialogHeader>
                <SearchDialogList items={searchData} />
                <SearchDialogFooter className="flex flex-row flex-wrap gap-2 items-center">
                    <ListMenu items={TAGS} label="Version" selected={version} setSelected={setVersion} />
                    <ListMenu items={BEHAVIORS} label="Behavior" selected={behavior} setSelected={setBehavior} />
                </SearchDialogFooter>
            </SearchDialogContent>
        </SearchDialog>
    );
}
