'use client';

import { useParams, usePathname, useRouter } from 'next/navigation';

import { i18n } from '@/lib/i18n';
import { ACTIVE_VERSIONS } from '@/lib/versions';

export function VersionSwitcher() {
    const params = useParams();
    const pathname = usePathname();
    const router = useRouter();

    const currentVersion = (params['version'] as string | undefined) ?? 'latest';
    const lang = (params['lang'] as string | undefined) ?? i18n.defaultLanguage;
    const prefix = lang === i18n.defaultLanguage ? '' : `/${lang}`;

    function handleChange(e: React.ChangeEvent<HTMLSelectElement>) {
        const next = e.target.value;
        const replaced = pathname.replace(
            `${prefix}/api/${currentVersion}`,
            `${prefix}/api/${next}`,
        );
        router.push(replaced);
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
                    return (
                        <option key={v} value={v}>
                            {v}
                        </option>
                    );
                })}
            </select>
        </div>
    );
}
