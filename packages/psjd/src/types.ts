// psjd/src/types.ts
// Complete TypeScript mirror of the psjd v2 spec.

// ─── Primitives ───────────────────────────────────────────────────────────────

export type ParamStyle = 'positional' | 'named';
export type DomainId = 'macro' | 'psj-command' | 'psj-utility' | 'psj-gui';
export type CalloutLevel = 'warn' | 'info' | 'danger';
export type ReturnKind = 'typed' | 'macro_code' | 'void';
export type ExampleLanguage = 'psj' | 'python';

// ─── sdk.psjd.yaml ───────────────────────────────────────────────────────────

export interface SDKManifest {
    psjd: '2.0';
    sdk: {
        name: string;
        vendor: string;
        vendor_url?: string;
    };
    /** Ordered oldest → newest */
    versions: SDKVersion[];
    current_version: string;
    domains: SDKDomain[];
}

export interface SDKVersion {
    id: string;
    notes?: string;
}

export interface SDKDomain {
    id: DomainId;
    title: string;
    param_style: ParamStyle;
}

// ─── Param ────────────────────────────────────────────────────────────────────

export interface EnumValue {
    id: number | string;
    label: string;
    description?: string;
}

export interface Param {
    /** 1-based; present for macro positional args */
    position?: number;
    /** Required for named params; optional for macro positional */
    name?: string;
    /** Clean display label when `name` is a cryptic C-style identifier */
    display_name?: string;
    /**
     * Primitive scalar, "$ref:data-type/<id>", "List[Primitive]",
     * or "List[$ref:data-type/<id>]"
     */
    type: string;
    required?: boolean;
    /** Exact default value as a string literal; null means undocumented */
    default?: string | null;
    description?: string;
    enum_values?: EnumValue[];
    /** True if inferred by a converter, not stated in source */
    inferred?: boolean;
    deprecated?: boolean;
    deprecated_in?: string;
    removed_in?: string;
}

// ─── GroupRef (appears inline in a params list) ───────────────────────────────

export interface GroupRef {
    $group: string;
    /** Param names to drop from the expanded group */
    exclude?: string[];
    /** Param name after which to splice `insert` params */
    insert_after?: string;
    /** Params to splice at the `insert_after` position */
    insert?: Param[];
}

export type ParamOrGroupRef = Param | GroupRef;

// ─── Returns ──────────────────────────────────────────────────────────────────

export interface ReturnCode {
    value: string;
    meaning: string;
}

export interface Returns {
    kind: ReturnKind;
    /** Present when kind === 'typed' */
    type?: string;
    description?: string;
    /** Present when kind === 'macro_code' */
    codes?: ReturnCode[];
}

// ─── Callout ──────────────────────────────────────────────────────────────────

export interface Callout {
    level: CalloutLevel;
    text: string;
}

// ─── Example ──────────────────────────────────────────────────────────────────

export interface Example {
    title?: string;
    language: ExampleLanguage;
    code: string;
}

// ─── Cross-reference ──────────────────────────────────────────────────────────

export interface Ref {
    /** "<domain>/<id>" */
    $ref: string;
    label?: string;
    inferred?: boolean;
}

// ─── Version delta ────────────────────────────────────────────────────────────

export interface ParamPatch {
    name: string;
    changes: {
        description?: string;
        default?: string | null;
        required?: boolean;
        enum_values?: {
            add?: EnumValue[];
            /** Enum value ids to remove */
            remove?: Array<number | string>;
        };
    };
}

export interface ParamsDelta {
    /** Each entry may have an optional `after` key naming the insertion point */
    add?: Array<Param & { after?: string }>;
    /** Names of params to remove */
    remove?: string[];
    modify?: ParamPatch[];
}

export interface VersionDelta {
    version: string;
    /** Top-level item field overrides */
    item?: {
        description?: string;
        ribbon?: string;
        deprecated?: boolean;
        notes?: string;
    };
    params?: ParamsDelta;
    notes?: string;
}

// ─── Item file (<domain>/<id>.yaml) ──────────────────────────────────────────

export interface ItemFile {
    psjd: '2.0';
    id: string;
    title: string;
    domain: DomainId;
    group?: string;
    namespace?: string;
    ribbon?: string;
    author?: string;
    author_url?: string;
    description: string;
    version_introduced: string;
    /** ID of the macro this command wraps (psj-command only) */
    macro_link?: string;
    /** ID of the command that wraps this (macro only) */
    command_link?: string;
    /** Verbatim call signature; auto-generated when absent */
    syntax?: string;
    callouts?: Callout[];
    params: ParamOrGroupRef[];
    returns: Returns;
    examples?: Example[];
    see_also?: Ref[];
    changes?: VersionDelta[];
    deprecated?: boolean;
    deprecated_in?: string;
    removed_in?: string;
}

// ─── Param group file (_groups/<id>.yaml) ─────────────────────────────────────

export interface ParamGroupFile {
    psjd: '2.0';
    kind: 'param_group';
    id: string;
    description?: string;
    /** ID of another group this one inherits from */
    extends?: string;
    params: Param[];
}

// ─── Parsed in-memory index ───────────────────────────────────────────────────

export interface ParsedSDK {
    manifest: SDKManifest;
    /** All callable items, keyed by item id */
    items: Map<string, ItemFile>;
    /** All param groups, keyed by group id */
    groups: Map<string, ParamGroupFile>;
    /** Shortcut for manifest.current_version */
    currentVersion: string;
    /** All version IDs ordered oldest → newest */
    versionIds: string[];
}

// ─── Resolved output (serializable POJOs) ────────────────────────────────────

/** A Param with all $group references expanded and all deltas applied. */
export interface ResolvedParam extends Param {
    /** Always present after resolution */
    name: string;
}

/**
 * The fully resolved, serializable representation of a callable item
 * at a specific SDK version. Contains no Map/Set — safe to pass across
 * the RSC/client boundary.
 */
export interface ResolvedItem {
    // Item identity
    id: string;
    title: string;
    domain: DomainId;
    group?: string;
    namespace?: string;
    ribbon?: string;
    author?: string;
    author_url?: string;
    description: string;
    version_introduced: string;
    macro_link?: string;
    command_link?: string;
    syntax?: string;
    callouts?: Callout[];
    returns: Returns;
    examples?: Example[];
    see_also?: Ref[];
    deprecated?: boolean;
    deprecated_in?: string;
    removed_in?: string;
    // Resolution outputs
    resolvedParams: ResolvedParam[];
    resolvedVersion: string;
    /** The domain's param_style, copied in for the renderer */
    paramStyle: ParamStyle;
    /** Human-readable notes for the resolved version (from VersionDelta.item) */
    versionNotes?: string;
}
