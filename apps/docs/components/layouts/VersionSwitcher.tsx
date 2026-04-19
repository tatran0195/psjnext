// components/VersionSwitcher.tsx
//
// Standalone version switcher dropdown.
// Dùng khi muốn embed vào vị trí custom (sidebar header, navbar, v.v.)
// thay vì thông qua DocsLayout links.
//
// Cách dùng trong DocsLayout:
//   sidebar={{ banner: <VersionSwitcher /> }}

'use client'

import { useParams, usePathname, useRouter } from 'next/navigation'
import { ACTIVE_VERSIONS, resolveVersion } from '@/lib/versions'
import { i18n } from '@/lib/i18n'

export function VersionSwitcher() {
  const params  = useParams()
  const pathname = usePathname()
  const router  = useRouter()

  const currentVersion = (params['version'] as string | undefined) ?? 'latest'
  const lang = (params['lang'] as string | undefined) ?? i18n.defaultLanguage
  const prefix = lang === i18n.defaultLanguage ? '' : `/${lang}`

  function handleChange(e: React.ChangeEvent<HTMLSelectElement>) {
    const next = e.target.value
    // Thay segment version trong pathname hiện tại
    // /api/5.1.0/getting-started → /api/{next}/getting-started
    const replaced = pathname.replace(
      `${prefix}/api/${currentVersion}`,
      `${prefix}/api/${next}`,
    )
    router.push(replaced)
  }

  return (
    <div className="px-2 py-2">
      <label
        htmlFor="version-select"
        className="mb-1 block text-xs font-medium text-fd-muted-foreground"
      >
        {lang === 'ja' ? 'バージョン' : 'Version'}
      </label>
      <select
        id="version-select"
        value={currentVersion}
        onChange={handleChange}
        className="w-full rounded-md border border-fd-border bg-fd-background px-2 py-1.5 text-sm text-fd-foreground focus:outline-none focus:ring-2 focus:ring-fd-ring"
        aria-label={lang === 'ja' ? 'バージョンを選択' : 'Select version'}
      >
        {ACTIVE_VERSIONS.map((v) => {
          const canonical = resolveVersion(v)
          const isAlias   = v !== canonical
          return (
            <option key={v} value={v}>
              {v}{isAlias && canonical ? ` → ${canonical}` : ''}
            </option>
          )
        })}
      </select>
    </div>
  )
}
