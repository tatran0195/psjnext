// ─── Primitive helpers ──────────────────────────────────────────────────────

export type Domain = 'macro' | 'psj-command' | 'psj-utility' | 'psj-gui';
export type ParamStyle = 'positional' | 'named';
export type ReturnKind = 'typed' | 'macro_code' | 'void';
export type CalloutLevel = 'warn' | 'info' | 'danger';
export type ExampleLanguage = 'psj' | 'python';
export type Stability = 'stable' | 'experimental' | 'deprecated';

// ─── SDK Version ────────────────────────────────────────────────────────────

/** A single SDK version entry with a display label. */
export interface SdkVersion {
    /** Version identifier, e.g. '5.1.0' */
    id: string;
    /** Human-readable label, e.g. '5.1.0 (latest)' */
    label: string;
    /** True for the manifest's `current_version`. */
    isCurrent: boolean;
}

/**
 * Rich value object returned by {@link PSJAPIServer.getVersions}.
 *
 * Prefer this over the raw manifest when you need version info in
 * components or route handlers — no manifest passing required.
 */
export interface SdkVersions {
    /** Full ordered list (newest-first by manifest convention). */
    all: SdkVersion[];
    /** The version flagged as `current_version` in the manifest. */
    current: SdkVersion;
    /** Convenience shortcut — just the id strings. */
    ids: string[];
    /** Find a version by id. Returns `undefined` if not found. */
    find(id: string): SdkVersion | undefined;
}

// ─── Root manifest ───────────────────────────────────────────────────────────

export interface SdkManifest {
    psj: '3.3';
    versions: VersionEntry[];
    current_version: string;
    locales: LocaleEntry[];
    domains: DomainEntry[];
}

export interface VersionEntry {
    id: string;
    notes?: string;
}

export interface LocaleEntry {
    id: string;
    label: string;
    default?: boolean;
}

export interface DomainEntry {
    id: Domain;
    title: string;
    param_style: ParamStyle;
}

// ─── Enum value ──────────────────────────────────────────────────────────────

export interface EnumValue {
    id: number | string;
    name?: string;
    label: string;
    description?: string;
    deprecated?: boolean;
}

// ─── Param ───────────────────────────────────────────────────────────────────

export interface Param {
    /** 1-based position for macro positional params */
    position?: number;
    /** Source identifier (required for named params) */
    name?: string;
    /** Clean UI label when the name is cryptic */
    display_name?: string;
    type: string;
    required: boolean;
    default?: string;
    description: string;
    enum_values?: EnumValue[];
    /** Reason string when deprecated; presence implies deprecated */
    deprecated?: string;
    deprecated_in?: string;
    removed_in?: string;
    /** true = added by converter, not stated in source */
    inferred?: boolean;
}

/** Field used in class data-types — like Param but with remarks */
export interface Field {
    name: string;
    type: string;
    required: boolean;
    default?: string;
    description: string;
    enum_values?: EnumValue[];
    remarks?: string;
    /** Reason string when deprecated; presence implies deprecated */
    deprecated?: string;
}

// ─── Group reference in item params list ─────────────────────────────────────

export interface GroupRef {
    $group: string;
    exclude?: string[];
    insert_after?: string;
    insert?: Param[];
    /** Patch specific params from the group without excluding them */
    override?: Record<string, { description?: string; default?: string; required?: boolean }>;
}

export type ParamOrGroupRef = Param | GroupRef;

// ─── Returns ─────────────────────────────────────────────────────────────────

export interface ReturnCode {
    value: string;
    meaning: string;
}

export interface Returns {
    kind: ReturnKind;
    type?: string;
    description?: string;
    codes?: ReturnCode[];
}

// ─── Callout ─────────────────────────────────────────────────────────────────

export interface Callout {
    /** Stable identifier for sidecar matching */
    id: string;
    level: CalloutLevel;
    text: string;
}

// ─── Example ─────────────────────────────────────────────────────────────────

export interface Example {
    /** Stable identifier for sidecar matching */
    id: string;
    title?: string;
    language: ExampleLanguage;
    code: string;
}

// ─── See-also ref ────────────────────────────────────────────────────────────

export interface SeeAlsoRef {
    $ref: string; // "<domain>/<id>"
    label?: string;
    inferred?: boolean;
}

// ─── Version delta ────────────────────────────────────────────────────────────

export interface EnumValuePatch {
    add?: EnumValue[];
    remove?: (number | string)[];
}

export interface ParamPatch {
    name: string;
    changes: {
        description?: string;
        default?: string;
        required?: boolean;
        deprecated?: string;
        enum_values?: EnumValuePatch;
    };
}

export interface ValuePatch {
    id: number | string;
    changes: {
        label?: string;
        description?: string;
        deprecated?: boolean;
    };
}

export interface FieldPatch {
    name: string;
    changes: {
        description?: string;
        default?: string;
        required?: boolean;
        remarks?: string;
        deprecated?: string;
        enum_values?: EnumValuePatch;
    };
}

export interface VersionDelta {
    version: string;
    notes?: string;
    item?: {
        description?: string;
        ribbon?: string;
        stability?: Stability;
    };
    /** Item files only */
    params?: {
        add?: (Param & { after?: string })[];
        remove?: string[];
        modify?: ParamPatch[];
    };
    /** built-in and enumeration data-type files only */
    values?: {
        add?: (EnumValue & { after?: number | string })[];
        remove?: (number | string)[];
        modify?: ValuePatch[];
    };
    /** class data-type files only */
    fields?: {
        add?: (Field & { after?: string })[];
        remove?: string[];
        modify?: FieldPatch[];
    };
}

// ─── Item file ───────────────────────────────────────────────────────────────

export interface ItemFile {
    psj: '3.3';
    id: string;
    title: string;
    domain: Domain;
    namespace?: string;
    ribbon?: string;
    stability?: Stability;
    description: string;
    since: string;
    /** id of the macro this command wraps (psj-command only) */
    macro_link?: string;
    /** id of the command that wraps this macro (macro only) */
    command_link?: string;
    /** data-type path id; psj-gui only */
    class_ref?: string;
    syntax?: string;
    callouts?: Callout[];
    params: ParamOrGroupRef[];
    returns: Returns;
    examples?: Example[];
    see_also?: SeeAlsoRef[];
    changes?: VersionDelta[];
}

// ─── Param group file ─────────────────────────────────────────────────────────

export interface ParamGroupFile {
    psj: '3.3';
    kind: 'param_group';
    id: string;
    description?: string;
    extends?: string;
    params: Param[];
}

// ─── Data-Type and Group Meta ────────────────────────────────────────────────

export interface DataTypeFile {
    psj: '3.3';
    kind: 'data_type';
    id: string;
    title: string;
    category: 'built-in' | 'enumeration' | 'class';
    namespace?: string;
    description: string;
    since: string;
    stability?: Stability;

    // category: built-in or enumeration
    values?: EnumValue[];

    // category: class
    constructor_syntax?: string;
    fields?: Field[];
    /** $ref entries pointing to item files (any domain) */
    methods?: SeeAlsoRef[];

    examples?: Example[];
    see_also?: SeeAlsoRef[];
    changes?: VersionDelta[];
}

export interface GroupMetaFile {
    psj: '3.3';
    kind: 'group_meta';
    title: string;
    description?: string;
    order?: string[];
    icon?: string;
}

// ─── Locale sidecars ─────────────────────────────────────────────────────────

/** Translation for a single enum value in a sidecar — just the label string */
export type EnumValueTranslations = Record<string | number, string>;

export interface ParamTranslation {
    display_name?: string;
    description?: string;
    enum_values?: EnumValueTranslations;
}

export interface ReturnCodeTranslations {
    /** key = value string e.g. '"1"' */
    [value: string]: string;
}

export interface ExampleTranslation {
    title?: string;
}

export interface CalloutTranslation {
    text: string;
}

/** Item locale sidecar — named params keyed by name */
export interface ItemLocaleSidecar {
    psj: '3.3';
    kind?: 'locale_sidecar';
    locale: string;
    id: string;
    description?: string;
    /** keyed by callout id */
    callouts?: Record<string, CalloutTranslation>;
    /** For named-param items: keyed by param name; for macros: keyed by position number */
    params?: Record<string, ParamTranslation>;
    returns?: {
        description?: string;
        codes?: ReturnCodeTranslations;
    };
    /** keyed by example id */
    examples?: Record<string, ExampleTranslation>;
}

/** Group locale sidecar — same shape as item sidecar but without per-item fields */
export type GroupLocaleSidecar = ItemLocaleSidecar;

/** DataType locale sidecar */
export interface DataTypeLocaleSidecar {
    psj: '3.3';
    kind: 'locale_sidecar';
    locale: string;
    id: string;
    description?: string;
    /** keyed by value id; built-in or enumeration */
    values?: Record<string | number, { label?: string; description?: string }>;
    /** keyed by field name; class */
    fields?: Record<
        string,
        {
            description?: string;
            remarks?: string;
            deprecated?: string;
            enum_values?: Record<string | number, string>;
        }
    >;
    /** keyed by example id */
    examples?: Record<string, ExampleTranslation>;
}

// ─── Resolved / fully-materialised item ───────────────────────────────────────
//
// After the loader has:
//   1. expanded all $group references,
//   2. applied version deltas,
//   3. merged locale translations,
//
// it produces a ResolvedItem — what the UI components receive.

export interface ResolvedParam {
    position?: number;
    name: string;
    display_name?: string;
    type: string;
    required: boolean;
    default?: string;
    description: string;
    enum_values?: EnumValue[];
    deprecated?: string | boolean;
    deprecated_in?: string;
    removed_in?: string;
    /** true when removed_in <= current viewed version (set by resolveItem) */
    removed?: boolean;
    inferred?: boolean;
    /** group id this param came from, if any */
    _fromGroup?: string;
}

export interface ResolvedItem {
    id: string;
    title: string;
    domain: Domain;
    namespace?: string;
    ribbon?: string;
    stability: Stability;
    description: string;
    since: string;
    macro_link?: string;
    command_link?: string;
    class_ref?: string;
    syntax?: string;
    callouts: Callout[];
    params: ResolvedParam[];
    returns: Returns;
    examples: Example[];
    see_also: SeeAlsoRef[];
    deprecated?: boolean;
}

export interface ResolvedField extends ResolvedParam {
    remarks?: string;
}

export interface ResolvedDataType {
    id: string;
    title: string;
    category: 'built-in' | 'enumeration' | 'class';
    namespace?: string;
    description: string;
    since: string;
    stability: Stability;

    // category: built-in or enumeration
    values?: EnumValue[];

    // category: class
    constructor_syntax?: string;
    fields?: ResolvedField[];
    methods?: SeeAlsoRef[];

    examples: Example[];
    see_also: SeeAlsoRef[];
    deprecated?: boolean;
}

// ─── Processed SDK — what the PSJAPIServer produces ──────────────────────────

export interface ProcessedSdk {
    manifest: SdkManifest;
    /**
     * All items across all domains, keyed by `<domain>/<id>`.
     * Already expanded (groups resolved, no deltas applied — deltas are applied
     * per requested version by resolveItem()).
     */
    items: Map<string, ItemFile>;
    /**
     * Param group definitions keyed by group id.
     */
    groups: Map<string, ParamGroupFile>;

    /**
     * Data types definitions.
     */
    dataTypes: Map<string, DataTypeFile>;

    /**
     * Directory metadata.
     */
    groupMetas: Map<string, GroupMetaFile>;
}

// ─── PSJAPIServer public interface ───────────────────────────────────────────

export interface PSJAPIServer {
    getProcessedSdk: (version?: string, locale?: string) => Promise<ProcessedSdk>;
    /**
     * Resolve a single item for a given version and locale.
     * All group refs are expanded, deltas applied, translations merged.
     */
    resolveItem: (id: string, version?: string, locale?: string) => Promise<ResolvedItem | undefined>;
    /**
     * Resolve a single data-type for a given version and locale.
     * Deltas applied, translations merged.
     */
    resolveDataType: (id: string, version?: string, locale?: string) => Promise<ResolvedDataType | undefined>;
    /**
     * Return a {@link SdkVersions} value object derived from the manifest.
     *
     * No need to fetch or pass the manifest yourself — the server reads it
     * internally and exposes a rich API for version-related operations.
     *
     * @example
     * const versions = await psjServer.getVersions();
     * versions.all          // SdkVersion[]
     * versions.current      // SdkVersion
     * versions.find('5.0.1') // SdkVersion | undefined
     * versions.switch(pathname, '5.1.0') // rewritten URL
     */
    getVersions(): Promise<SdkVersions>;
    readonly options: PSJAPIOptions;
}

export interface PSJAPIOptions {
    /**
     * Path to the root `sdk.psj.yaml` manifest, or a directory that
     * contains one.
     */
    root: string;

    /**
     * Default locale. Falls back to 'en' if not set.
     */
    defaultLocale?: string;

    /**
     * Disable result caching (useful during development watches).
     */
    disableCache?: boolean;
}
