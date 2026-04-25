/**
 * psjapi core type definitions.
 *
 * These model the psjapi 1.0 YAML schema for the Jupiter CAE Desktop Platform SDK.
 * The types are framework-agnostic — UI components import them; the loader produces
 * them; utility functions consume them.
 */

// ─── Primitive helpers ──────────────────────────────────────────────────────

export type Domain = 'macro' | 'psj-command' | 'psj-utility' | 'psj-gui';
export type ParamStyle = 'positional' | 'named';
export type ReturnKind = 'typed' | 'macro_code' | 'void';
export type CalloutLevel = 'warn' | 'info' | 'danger';
export type ExampleLanguage = 'psj' | 'python';

// ─── Root manifest ───────────────────────────────────────────────────────────

export interface SdkManifest {
    psjapi: '1.0';
    sdk: SdkInfo;
    versions: VersionEntry[];
    current_version: string;
    locales: LocaleEntry[];
    domains: DomainEntry[];
}

export interface SdkInfo {
    name: string;
    vendor: string;
    vendor_url: string;
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
    label: string;
    description?: string;
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
    deprecated?: boolean;
    deprecated_in?: string;
    removed_in?: string;
    /** true = added by converter, not stated in source */
    inferred?: boolean;
}

// ─── Group reference in item params list ─────────────────────────────────────

export interface GroupRef {
    $group: string;
    exclude?: string[];
    insert_after?: string;
    insert?: Param[];
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
    level: CalloutLevel;
    text: string;
}

// ─── Example ─────────────────────────────────────────────────────────────────

export interface Example {
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
        deprecated?: boolean;
        enum_values?: EnumValuePatch;
    };
}

export interface VersionDelta {
    version: string;
    notes?: string;
    item?: {
        description?: string;
        ribbon?: string;
        deprecated?: boolean;
    };
    params?: {
        add?: (Param & { after?: string })[];
        remove?: string[];
        modify?: ParamPatch[];
    };
}

// ─── Item file ───────────────────────────────────────────────────────────────

export interface ItemFile {
    psjapi: '1.0';
    id: string;
    title: string;
    domain: Domain;
    group?: string;
    namespace?: string;
    ribbon?: string;
    author?: string;
    author_url?: string;
    description: string;
    version_introduced: string;
    /** id of the macro this command wraps (psj-command only) */
    macro_link?: string;
    /** id of the command that wraps this macro (macro only) */
    command_link?: string;
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
    psjapi: '1.0';
    kind: 'param_group';
    id: string;
    description?: string;
    extends?: string;
    params: Param[];
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
    level: CalloutLevel;
    text: string;
}

/** Item locale sidecar — named params keyed by name */
export interface ItemLocaleSidecar {
    psjapi: '1.0';
    locale: string;
    id: string;
    description?: string;
    callouts?: CalloutTranslation[];
    /** For named-param items: keyed by param name; for macros: keyed by position number */
    params?: Record<string, ParamTranslation>;
    returns?: {
        description?: string;
        codes?: ReturnCodeTranslations;
    };
    examples?: ExampleTranslation[];
}

/** Group locale sidecar — same shape as item sidecar but without per-item fields */
export type GroupLocaleSidecar = ItemLocaleSidecar;

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
    deprecated?: boolean;
    deprecated_in?: string;
    removed_in?: string;
    inferred?: boolean;
    /** group id this param came from, if any */
    _fromGroup?: string;
}

export interface ResolvedItem {
    id: string;
    title: string;
    domain: Domain;
    group?: string;
    namespace?: string;
    ribbon?: string;
    description: string;
    version_introduced: string;
    macro_link?: string;
    command_link?: string;
    syntax?: string;
    callouts: Callout[];
    params: ResolvedParam[];
    returns: Returns;
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
}

// ─── PSJAPIServer public interface ───────────────────────────────────────────

export interface PSJAPIServer {
    getProcessedSdk: (version?: string, locale?: string) => Promise<ProcessedSdk>;
    /**
     * Resolve a single item for a given version and locale.
     * All group refs are expanded, deltas applied, translations merged.
     */
    resolveItem: (
        id: string,
        version?: string,
        locale?: string,
    ) => Promise<ResolvedItem | undefined>;
    readonly options: PSJAPIOptions;
}

export interface PSJAPIOptions {
    /**
     * Path to the root `sdk.psjapi.yaml` manifest, or a directory that
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
