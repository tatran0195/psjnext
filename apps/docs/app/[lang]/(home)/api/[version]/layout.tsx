// app/[lang]/api/[version]/layout.tsx
//
// Layout cho tất cả pages trong một version.
// Resolve alias trước (stable → 5.1.0), load đúng source, render sidebar.
//
// Version switcher được inject qua tabs prop của DocsLayout —
// fumadocs-ui không có built-in version switcher nên dùng links.

import { VersionSwitcher } from '@/components/layouts/VersionSwitcher'
import { LinkSidebarProvider } from '@/components/mdx/link-sidebar'
import { baseOptions } from '@/lib/layout.shared'
import { apiSources, type ApiVersion } from '@/lib/source'
import { isVersionActive, resolveVersion } from '@/lib/versions'
import { I18nProvider } from 'fumadocs-ui/contexts/i18n'
import { DocsLayout } from 'fumadocs-ui/layouts/docs'
import { notFound } from 'next/navigation'
import type { ReactNode } from 'react'

export default async function ApiVersionLayout({
  params,
  children,
}: {
  params: Promise<{ lang: string; version: string }>
  children: ReactNode
}) {
  const { lang, version } = await params
  console.log({ lang, version })
  if (!isVersionActive(version)) notFound()

  const canonical = resolveVersion(version)
  console.log(canonical)
  if (!canonical) notFound()

  const source = apiSources[canonical as ApiVersion]
  console.log({ source, apiSources })
  if (!source) notFound()

  return (
    <I18nProvider >
      <LinkSidebarProvider>
        <DocsLayout
          tree={source.getPageTree(lang)}
          {...baseOptions(lang)}
          sidebar={{
            // VersionSwitcher render phía trên sidebar tree
            // Client component — detect version từ URL params tự động
            banner: <VersionSwitcher />,
          }}
        >
          {children}
        </DocsLayout>
      </LinkSidebarProvider>
    </I18nProvider>
  )
}
