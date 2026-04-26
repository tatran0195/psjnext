import { psjDocsSource } from '@/lib/psj-source';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import type { ReactNode } from 'react';

export default async function DocsI18nLayout({
  params,
  children,
}: {
  params: Promise<{ lang: string }>;
  children: ReactNode;
}) {
  const { lang } = await params;

  return (
    <DocsLayout
      // pageTree is a Record<string, PageTree> in i18n mode — index by lang
      tree={psjDocsSource.pageTree[lang]}
      nav={{ title: 'PSJ SDK' }}
      sidebar={{ defaultOpenLevel: 1 }}
    >
      {children}
    </DocsLayout>
  );
}
