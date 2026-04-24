/**
 * psjapi Fumadocs Source API integration
 *
 * Analogous to fumadocs-openapi's openapiSource() / openapiPlugin().
 * Call psjSource() to generate virtual pages, and pass psjPlugin() to
 * the `plugins` array in Fumadocs loader().
 */

import type { ReactNode } from 'react';
import type {
  Source,
  LoaderPlugin,
  MetaData,
  PageData,
  VirtualFile,
  PageTreeTransformer,
} from 'fumadocs-core/source';
import type { StructuredData } from 'fumadocs-core/mdx-plugins';
import type { TOCItemType } from 'fumadocs-core/toc';
import type { PSJAPIServer, ResolvedItem } from '../types';
import type { PsjPagesBuilderConfig, ItemOutput, PageOutput, OutputEntry } from '../utils/pages/builder';
import { fromServer } from '../utils/pages/builder';
import * as path from 'node:path';
import { PathUtils } from 'fumadocs-core/source';

// ─── Augment PageData ────────────────────────────────────────────────────────

declare module 'fumadocs-core/source' {
  interface PageData {
    _psjapi?: InternalPsjMeta;
  }
}

export interface InternalPsjMeta {
  domain?: string;
  group?: string;
}

// ─── Plugin ───────────────────────────────────────────────────────────────────

/**
 * Fumadocs Source API loader plugin.
 * Adds domain badges to sidebar items (analogous to HTTP method badges in OpenAPI).
 */
export function psjPlugin(): LoaderPlugin {
  return {
    name: 'fumadocs:psjapi',
    enforce: 'pre',
    transformPageTree: {
      file(node, filePath) {
        if (!filePath) return node;
        const file = this.storage.read(filePath);
        if (!file || file.format !== 'page') return node;

        const meta = file.data._psjapi;
        if (!meta || typeof meta !== 'object') return node;

        if (meta.domain) {
          const domainLabel = domainBadge(meta.domain);
          if (domainLabel) {
            node.name = (
              <>
                {node.name}{' '}
                <span className="ms-auto border border-current px-1 rounded-lg text-xs text-nowrap font-mono">
                  {domainLabel}
                </span>
              </>
            );
          }
        }

        return node;
      },
    },
  };
}

function domainBadge(domain: string): string | null {
  const map: Record<string, string> = {
    macro: 'macro',
    'psj-command': 'cmd',
    'psj-utility': 'util',
    'psj-gui': 'gui',
  };
  return map[domain] ?? null;
}

// ─── Page data types ──────────────────────────────────────────────────────────

export interface PSJPageData extends PageData {
  /** Resolve item for this page (single-item pages) */
  getItem: (version?: string, locale?: string) => Promise<ResolvedItem | undefined>;
  /** For multi-item pages: item keys */
  itemKeys?: string[];
  structuredData: StructuredData;
  toc: TOCItemType[];
}

export type PsjSourceOptions = PsjPagesBuilderConfig & {
  baseDir?: string;
  /** Generate meta.json files */
  meta?: boolean | { folderStyle?: 'folder' | 'separator' };
};

// ─── psjSource ────────────────────────────────────────────────────────────────

/**
 * Generate virtual pages for Fumadocs Source API from a PSJAPIServer.
 *
 * Usage:
 * ```ts
 * import { loader } from 'fumadocs-core/source';
 * import { psjSource, psjPlugin } from 'fumadocs-psjapi/source';
 *
 * export const { getPage, getPages, pageTree } = loader({
 *   source: await psjSource(server, { groupBy: 'domain' }),
 *   plugins: [psjPlugin()],
 * });
 * ```
 */
export async function psjSource(
  server: PSJAPIServer,
  options: PsjSourceOptions = {},
): Promise<
  Source<{
    metaData: MetaData;
    pageData: PSJPageData;
  }>
> {
  const { baseDir = '', meta = false } = options;

  const files: VirtualFile<{
    pageData: PSJPageData;
    metaData: MetaData;
  }>[] = [];

  const allEntries = await fromServer(server, options);

  for (const [schemaId, list] of Object.entries(allEntries)) {
    function onEntry(entry: ItemOutput | PageOutput) {
      const filePath = `${baseDir}/${entry.path}`;

      let psjMeta: InternalPsjMeta = {};

      if (entry.type === 'item') {
        psjMeta = { domain: entry.item.domain };
      } else if (entry.type === 'page' && entry.items.length > 0) {
        psjMeta = { domain: entry.items[0].domain };
      }

      files.push({
        type: 'page',
        path: filePath,
        data: {
          title: entry.info.title,
          description: entry.info.description,
          _psjapi: psjMeta,
          async getItem(version?: string, locale?: string) {
            if (entry.type === 'item') {
              return server.resolveItem(entry.item.key, version, locale);
            }
            // For page-type entries, resolve first item
            if (entry.type === 'page' && entry.items.length > 0) {
              return server.resolveItem(entry.items[0].key, version, locale);
            }
            return undefined;
          },
          itemKeys:
            entry.type === 'page'
              ? entry.items.map((i) => i.key)
              : [entry.type === 'item' ? entry.item.key : ''],
          // Static data for search indexing
          structuredData: {
            headings: [],
            contents: [
              {
                content: entry.info.description ?? entry.info.title,
              },
            ],
          },
          toc: [],
        } satisfies PSJPageData,
      });
    }

    function onEntries(entries: OutputEntry[], parent?: OutputEntry) {
      if (!meta) {
        for (const entry of entries) {
          if (entry.type === 'group') {
            onEntries(entry.entries, entry);
          } else {
            onEntry(entry as ItemOutput | PageOutput);
          }
        }
        return;
      }

      const { folderStyle = 'folder' } = meta === true ? {} : meta;
      const pages: string[] = [];

      for (const entry of entries) {
        const relativePath = PathUtils.slash(
          parent ? path.relative(parent.path, entry.path) : entry.path,
        );

        if (entry.type === 'group') {
          onEntries(entry.entries, entry);
          if (folderStyle === 'folder') {
            pages.push(relativePath);
          } else {
            pages.push(`---${entry.info.title}---`, `...${relativePath}`);
          }
        } else {
          onEntry(entry as ItemOutput | PageOutput);
          pages.push(relativePath.slice(0, -PathUtils.extname(entry.path).length));
        }
      }

      if (pages.length === 0) return;
      files.push({
        type: 'meta',
        path: path.join(baseDir, parent?.path ?? '', 'meta.json'),
        data: {
          title: parent?.info.title,
          description: parent?.info.description,
          pages,
        },
      });
    }

    onEntries(list);
  }

  return { files };
}

/**
 * @deprecated use psjPlugin()
 */
export function transformerPsj(): PageTreeTransformer {
  return psjPlugin().transformPageTree!;
}
