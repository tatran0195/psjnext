/**
 * JCALL v2 — TypeScript type system
 * Mirrors the full field reference from jcall.spec §7
 */

// ─── Primitive Building Blocks ────────────────────────────────────────────────

export interface EnumValue {
    id: number | string;
    label: string;
    description?: string;
}

export interface Callout {
    level: 'warn' | 'info' | 'danger';
    text: string;
}

/** A cross-reference to another item: "<domain>/<id>" */
export interface Ref {
    $ref: string;
    label?: string;
    inferred?: boolean;
}

export interface Example {
    title?: string;
    language: string;
    code?: string;
    file?: string;
}

export interface ReturnCode {
    value: string;
    meaning: string;
}

// ─── Returns ─────────────────────────────────────────────────────────────────

export type Returns =
    | { kind: 'typed'; type: string; description?: string }
    | { kind: 'macro_code'; description?: string; codes: ReturnCode[] }
    | { kind: 'void'; description?: string };

// ─── Params ──────────────────────────────────────────────────────────────────

export interface Param {
    /** 1-based; present for macro positional args, absent otherwise */
    position?: number;
    /** Source identifier; required for named params */
    name?: string;
    /** Clean label for UI when name is cryptic */
    display_name?: string;
    /** Primitive, "$ref:data-type/<id>", or "List[$ref:...]" */
    type: string;
    required: boolean;
    /** Exact default value as string; null if undocumented */
    default?: string | null;
    description: string;
    enum_values?: EnumValue[];
    deprecated?: boolean;
    deprecated_in?: string;
    removed_in?: string;
    /** true if this field was inferred, not stated in source */
    inferred?: boolean;
}

/** A param that sits at a position to be inserted after another */
export interface ParamWithAfter extends Param {
    after?: string;
}

/** Reference to a _groups/<id>.yaml file inside an item's params list */
export interface GroupRef {
    $group: string;
    /** Param names to drop from the group */
    exclude?: string[];
    /** Param name after which to insert the following params */
    insert_after?: string;
    /** Params to insert at the insert_after position */
    insert?: Param[];
}

export type ParamOrGroupRef = Param | GroupRef;

export function isGroupRef(p: ParamOrGroupRef): p is GroupRef {
    return '$group' in p;
}

// ─── Version Deltas ───────────────────────────────────────────────────────────

export interface ParamPatch {
    name: string;
    changes: {
        description?: string;
        default?: string | null;
        required?: boolean;
        type?: string;
        enum_values?: {
            add?: EnumValue[];
            /** enum value ids to remove */
            remove?: (number | string)[];
        };
    };
}

export interface VersionDelta {
    version: string;
    /** Top-level item-field changes */
    item?: {
        description?: string;
        ribbon?: string;
        deprecated?: boolean;
        notes?: string;
    };
    params?: {
        add?: ParamWithAfter[];
        remove?: string[];
        modify?: ParamPatch[];
    };
}

// ─── File Schemas ─────────────────────────────────────────────────────────────

export interface ParamGroupFile {
    jcall: '2.0';
    kind: 'param_group';
    id: string;
    description?: string;
    /** id of another param group this one extends */
    extends?: string;
    params: Param[];
}

export type Domain = 'macro' | 'psj-command' | 'psj-utility' | 'psj-gui';

export interface ItemFile {
    jcall: '2.0';
    id: string;
    title: string;
    domain: Domain;
    group?: string;
    namespace?: string;
    /** UI ribbon path (psj-command only) */
    ribbon?: string;
    author?: string;
    author_url?: string;
    description: string;
    version_introduced: string;
    /** id of macro this command wraps (psj-command only) */
    macro_link?: string;
    /** id of command that wraps this (macro only) */
    command_link?: string;
    /** Verbatim call signature; auto-generated if absent */
    syntax?: string;
    callouts?: Callout[];
    params: ParamOrGroupRef[];
    returns: Returns;
    examples?: Example[];
    see_also?: Ref[];
    changes?: VersionDelta[];
}

// ─── Root Manifest ────────────────────────────────────────────────────────────

export interface ManifestVersion {
    id: string;
    notes?: string;
}

export interface ManifestDomain {
    id: Domain;
    title: string;
    /** 'positional' shows Position column; 'named' shows Name column */
    param_style: 'positional' | 'named';
}

export interface JCallManifest {
    jcall: '2.0';
    sdk: {
        name: string;
        vendor?: string;
        vendor_url?: string;
    };
    /** Ordered oldest→newest */
    versions: ManifestVersion[];
    current_version: string;
    domains: ManifestDomain[];
}

// ─── Resolved (post-expansion) Types ─────────────────────────────────────────

/**
 * A fully-expanded param: no GroupRefs, all deltas applied for the
 * requested version.
 */
export interface ResolvedParam extends Param {
    name: string; // always present after resolution
}

/**
 * A fully-resolved item for a specific SDK version.
 * All $group references expanded, all version deltas applied.
 */
export interface ResolvedItem {
    /** Original item id */
    id: string;
    title: string;
    domain: Domain;
    /** param_style from the manifest domain definition */
    param_style: 'positional' | 'named';
    group?: string;
    namespace?: string;
    ribbon?: string;
    description: string;
    version_introduced: string;
    macro_link?: string;
    command_link?: string;
    syntax?: string;
    callouts?: Callout[];
    params: ResolvedParam[];
    returns: Returns;
    examples?: Example[];
    see_also?: Ref[];
    deprecated?: boolean;
    /** The SDK version this was resolved for */
    resolved_version: string;
}

// ─── SDK Container (in-memory after full load) ────────────────────────────────

export interface LoadedSDK {
    manifest: JCallManifest;
    /** id → ParamGroupFile */
    groups: Map<string, ParamGroupFile>;
    /** id → ItemFile */
    items: Map<string, ItemFile>;
    rootDir?: string;
}
