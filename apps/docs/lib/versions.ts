/**
 * SDK version utilities — shared between middleware, layout, and page components.
 *
 * Keep in sync with sdk.psjapi.yaml manifest.
 */

export interface SdkVersion {
  id: string;
  label: string;
  isCurrent: boolean;
}

export const SDK_VERSIONS: SdkVersion[] = [
  { id: '5.1.0', label: '5.1.0 (latest)', isCurrent: true },
  { id: '5.0.1', label: '5.0.1', isCurrent: false },
  { id: '5.0.0', label: '5.0.0', isCurrent: false },
];

export const CURRENT_VERSION = SDK_VERSIONS.find((v) => v.isCurrent)!.id;

/**
 * Build the URL for a different version of the current page.
 *
 * switchVersion('/en/sdk/5.0.1/psj-command/foo', '5.1.0')
 *   → '/en/sdk/5.1.0/psj-command/foo'
 */
export function switchVersion(currentPath: string, newVersion: string): string {
  // pathname: /[lang]/sdk/[version]/[...slug]
  const parts = currentPath.split('/');
  // parts: ['', lang, 'sdk', version, ...slug]
  if (parts.length >= 4 && parts[2] === 'sdk') {
    parts[3] = newVersion;
    return parts.join('/');
  }
  return currentPath;
}
