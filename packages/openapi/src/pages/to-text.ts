/**
 * Converts a PageOutput entry into MDX file content.
 *
 * Each item's MDX body is just:
 *   <JCallPage id="<id>" />
 *
 * All the actual rendering happens in the React component.
 * The frontmatter carries the data needed for SEO, TOC, and source-API metadata.
 */
import { dump } from 'js-yaml';

import type { ResolvedItem } from '../types';
import type { PageOutput } from './builder';

export interface ToTextOptions {
    /**
     * Additional MDX imports to inject.
     */
    imports?: { names: string[]; from: string }[];
    /**
     * Customize the MDX frontmatter.
     */
    frontmatter?: (item: ResolvedItem) => Record<string, unknown>;
    /**
     * Add auto-generated file comment. Default: true.
     */
    addGeneratedComment?: boolean | string;
}

export function toText(entry: PageOutput, options: ToTextOptions = {}): string {
    const { item } = entry;
    const { addGeneratedComment = true, imports, frontmatter } = options;

    const customFm = frontmatter?.(item) ?? {};
    const fm: Record<string, unknown> = {
        title: item.title,
        description: item.description,
        full: true,
        ...customFm,
        _jcall: {
            id: item.id,
            domain: item.domain,
            group: item.group,
            version: item.resolved_version,
            deprecated: item.deprecated,
            ...(customFm._jcall as object | undefined),
        },
    };

    const out: string[] = [];

    // Frontmatter
    const banner = dump(fm).trimEnd();
    if (banner.length > 0) out.push(`---\n${banner}\n---`);

    // Generated comment
    if (addGeneratedComment) {
        const text =
            typeof addGeneratedComment === 'string'
                ? addGeneratedComment
                : 'This file was generated from the JCALL SDK. Do not edit directly.';
        out.push(`{/* ${text.replaceAll('/', '\\/')} */}`);
    }

    // Extra imports
    if (imports?.length) {
        out.push(
            imports.map((i) => `import { ${i.names.join(', ')} } from "${i.from}";`).join('\n'),
        );
    }

    // Content
    out.push(`<JCallPage id="${item.id}" />`);

    return out.join('\n\n');
}

export function generateDocument(
    frontmatter: Record<string, unknown>,
    content: string,
    options: Pick<ToTextOptions, 'addGeneratedComment' | 'imports'>,
): string {
    return toText(
        // dummy entry used for index/overview pages
        {
            type: 'page',
            path: '',
            info: {
                title: String(frontmatter.title ?? ''),
                description: String(frontmatter.description ?? ''),
            },
            item: {} as ResolvedItem,
        },
        { ...options, frontmatter: () => frontmatter },
    ).replace('<JCallPage id="" />', content);
}
