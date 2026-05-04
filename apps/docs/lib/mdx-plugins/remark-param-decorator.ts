import type { Heading, PhrasingContent, Root, RootContent } from 'mdast';
import type { MdxJsxAttribute, MdxJsxFlowElement } from 'mdast-util-mdx-jsx';
import type { Plugin } from 'unified';

// ─── Types ────────────────────────────────────────────────────────────────────

interface DecoratorParseResult {
    paramName: string;
    type: string;
    default?: string;
    required: boolean;
    deprecated: boolean;
    experimental: boolean;
    since?: string;
    until?: string;
}

interface PluginOptions {
    // Sections that contain param headings
    paramSections?: string[];
}

// ─── Regex (compiled once at module load) ─────────────────────────────────────

const DECORATOR_RE =
    /@(type|default|required|deprecated|experimental|since|until)(?:\(([^)]*)\))?/g;

const PARAM_NAME_RE = /^`([^`]+)`/;

// ─── Plugin ───────────────────────────────────────────────────────────────────

/**
 * remark-param-decorator
 *
 * Transforms param headings from:
 *   ### `paramName` @type(Type) @default(Value) @required @since(5.1.0)
 *
 * Into:
 *   ### paramName                    ← clean heading, no decorators
 *   <div class="param-meta"          ← injected metadata node
 *     data-since="5.1.0"
 *     data-until="..."
 *   >
 *     <span>optional</span>
 *     <span>Type</span>
 *     <span>default: Value</span>
 *   </div>
 *
 * The data-since and data-until attributes enable minimal client-side
 * visibility gating without full React rendering.
 *
 * This plugin runs at build time in the unified/MDX pipeline.
 * No runtime React component is required for the metadata strip itself.
 * Only a minimal client wrapper handles the version-visibility toggle.
 */
const remarkParamDecorator: Plugin<[PluginOptions?], Root> = (options = {}) => {
    const paramSections = new Set(options.paramSections ?? ['Inputs', 'Return Code']);

    return (tree: Root) => {
        // ── Phase 1: Identify which h3 headings are inside param sections ────────
        // We need to track whether we are currently inside a param section.
        // We do a two-pass approach:
        //   Pass 1: Build an index of which node indices are inside param sections.
        //   Pass 2: Transform those heading nodes.

        const paramSectionIndices = findParamSectionIndices(tree, paramSections);

        // ── Phase 2: Collect transform candidates ───────────────────────────────
        // We cannot mutate during visit safely when inserting siblings,
        // so we collect (index, result) pairs and apply transforms in reverse.

        const transforms: Array<{
            index: number;
            headingNode: Heading;
            parsed: DecoratorParseResult;
        }> = [];

        for (let i = 0; i < tree.children.length; i++) {
            const node = tree.children[i];

            if (
                node.type !== 'heading' ||
                (node as Heading).depth !== 3 ||
                !paramSectionIndices.has(i)
            ) {
                continue;
            }

            const heading = node as Heading;
            const headingText = extractHeadingText(heading);
            const parsed = parseDecorators(headingText);

            if (!parsed) continue;

            transforms.push({ index: i, headingNode: heading, parsed });
        }

        // ── Phase 3: Apply transforms in REVERSE order ───────────────────────────
        // Reverse order preserves index validity when inserting nodes.

        for (let t = transforms.length - 1; t >= 0; t--) {
            const { index, headingNode, parsed } = transforms[t];

            // Mutate heading: strip decorators, keep only param name
            rewriteHeadingNode(headingNode, parsed.paramName);

            // Build the param-meta MDX JSX element
            const metaNode = buildParamMetaNode(parsed);

            // Insert meta node immediately after the heading
            tree.children.splice(index + 1, 0, metaNode as unknown as RootContent);
        }
    };
};

// ─── Section Index Finder ─────────────────────────────────────────────────────

/**
 * Returns a Set of AST child indices that fall within param sections.
 * A param section is an h2 named "Inputs" or "Return Code".
 */
function findParamSectionIndices(tree: Root, paramSections: Set<string>): Set<number> {
    const indices = new Set<number>();
    let inParamSection = false;

    for (let i = 0; i < tree.children.length; i++) {
        const node = tree.children[i];

        if (node.type === 'heading' && (node as Heading).depth === 2) {
            const text = extractHeadingText(node as Heading);
            inParamSection = paramSections.has(text);
        }

        if (inParamSection) {
            indices.add(i);
        }
    }

    return indices;
}

// ─── Heading Text Extraction ──────────────────────────────────────────────────

function extractHeadingText(node: Heading): string {
    const parts: string[] = [];

    for (const child of node.children) {
        if (child.type === 'text') {
            parts.push((child as { type: 'text'; value: string }).value);
        } else if (child.type === 'inlineCode') {
            parts.push(`\`${(child as { type: 'inlineCode'; value: string }).value}\``);
        } else if ('value' in child) {
            parts.push((child as unknown as { value: string }).value);
        }
    }

    return parts.join('').trim();
}

// ─── Decorator Parser ─────────────────────────────────────────────────────────

function parseDecorators(headingText: string): DecoratorParseResult | null {
    if (!headingText.includes('@type(')) return null;

    const nameMatch = PARAM_NAME_RE.exec(headingText);
    if (!nameMatch) return null;

    const paramName = nameMatch[1];

    const result: DecoratorParseResult = {
        paramName,
        type: '',
        required: false,
        deprecated: false,
        experimental: false,
    };

    DECORATOR_RE.lastIndex = 0;
    let match: RegExpExecArray | null;

    while ((match = DECORATOR_RE.exec(headingText)) !== null) {
        const [, decorator, value] = match;

        switch (decorator) {
            case 'type':
                result.type = value ?? '';
                break;
            case 'default':
                result.default = value ?? '';
                break;
            case 'required':
                result.required = true;
                break;
            case 'deprecated':
                result.deprecated = true;
                break;
            case 'experimental':
                result.experimental = true;
                break;
            case 'since':
                result.since = value;
                break;
            case 'until':
                result.until = value;
                break;
        }
    }

    if (!result.type) return null;

    return result;
}

// ─── Heading Rewriter ─────────────────────────────────────────────────────────

/**
 * Mutate heading node in-place:
 * Replace all children with a single inlineCode node containing the param name.
 * This strips all @decorator text from the rendered heading.
 */
function rewriteHeadingNode(node: Heading, paramName: string): void {
    node.children = [
        {
            type: 'inlineCode',
            value: paramName,
        } as PhrasingContent,
    ];
}

// ─── Param Meta Node Builder ──────────────────────────────────────────────────

/**
 * Build an MDX JSX flow element representing the param metadata strip.
 *
 * Output equivalent:
 * <div
 *   className="param-meta"
 *   data-since="5.1.0"    // only if @since present
 *   data-until="5.2.0"    // only if @until present
 *   data-deprecated="true" // only if @deprecated
 *   data-experimental="true" // only if @experimental
 * >
 *   <span className="param-badge param-badge--optional">optional</span>  // if not @required
 *   <span className="param-badge param-badge--required">required</span>  // if @required
 *   <span className="param-badge param-badge--deprecated">deprecated</span> // if @deprecated
 *   <span className="param-badge param-badge--experimental">experimental</span> // if @experimental
 *   <span className="param-badge param-badge--type">Type</span>
 *   <span className="param-badge param-badge--default">default: Value</span> // if @default
 * </div>
 */
function buildParamMetaNode(parsed: DecoratorParseResult): MdxJsxFlowElement {
    const attributes: MdxJsxAttribute[] = [
        {
            type: 'mdxJsxAttribute',
            name: 'className',
            value: 'param-meta',
        },
    ];

    // Version gating data attributes
    if (parsed.since) {
        attributes.push({
            type: 'mdxJsxAttribute',
            name: 'data-since',
            value: parsed.since,
        });
    }

    if (parsed.until) {
        attributes.push({
            type: 'mdxJsxAttribute',
            name: 'data-until',
            value: parsed.until,
        });
    }

    if (parsed.deprecated) {
        attributes.push({
            type: 'mdxJsxAttribute',
            name: 'data-deprecated',
            value: 'true',
        });
    }

    if (parsed.experimental) {
        attributes.push({
            type: 'mdxJsxAttribute',
            name: 'data-experimental',
            value: 'true',
        });
    }

    const children: MdxJsxFlowElement[] = [];

    // Required/Optional badge
    children.push(
        buildSpan(
            parsed.required ? 'required' : 'optional',
            `param-badge param-badge--${parsed.required ? 'required' : 'optional'}`,
        ),
    );

    // Deprecated badge
    if (parsed.deprecated) {
        children.push(buildSpan('deprecated', 'param-badge param-badge--deprecated'));
    }

    // Experimental badge
    if (parsed.experimental) {
        children.push(buildSpan('experimental', 'param-badge param-badge--experimental'));
    }

    // Type badge
    children.push(buildSpan(parsed.type, 'param-badge param-badge--type'));

    // Default badge
    if (parsed.default !== undefined) {
        children.push(buildSpan(`default: ${parsed.default}`, 'param-badge param-badge--default'));
    }

    // Since badge (visible in rendered output for reference)
    if (parsed.since) {
        children.push(buildSpan(`since: ${parsed.since}`, 'param-badge param-badge--since'));
    }

    return {
        type: 'mdxJsxFlowElement',
        name: 'div',
        attributes,
        children: children as unknown as MdxJsxFlowElement['children'],
    };
}

function buildSpan(text: string, className: string): MdxJsxFlowElement {
    return {
        type: 'mdxJsxFlowElement',
        name: 'span',
        attributes: [
            {
                type: 'mdxJsxAttribute',
                name: 'className',
                value: className,
            },
        ],
        children: [
            {
                type: 'text',
                value: text,
            } as unknown as MdxJsxFlowElement['children'][0],
        ],
    };
}

export default remarkParamDecorator;
