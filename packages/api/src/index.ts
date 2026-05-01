// Core types
export type {
    Callout,
    CalloutLevel,
    DataTypeFile,
    DataTypeLocaleSidecar,
    Domain,
    DomainEntry,
    EnumValue,
    Example,
    ExampleLanguage,
    Field,
    FieldPatch,
    GroupLocaleSidecar,
    GroupMetaFile,
    GroupRef,
    ItemFile,
    ItemLocaleSidecar,
    LocaleEntry,
    PSJAPIOptions,
    PSJAPIServer,
    Param,
    ParamGroupFile,
    ParamOrGroupRef,
    ParamStyle,
    // Server types
    ProcessedSdk,
    ResolvedItem,
    ResolvedDataType,
    // Resolved types
    ResolvedParam,
    ResolvedField,
    ReturnCode,
    ReturnKind,
    Returns,
    // Spec types
    SdkManifest,
    SeeAlsoRef,
    Stability,
    ValuePatch,
    VersionDelta,
    VersionEntry,
} from './types';

// Server factory
export { createPSJAPI } from './loader';

// Static file generation
export { generateFiles, generateFilesOnly } from './generate-file';
export type { GenerateFilesConfig, OutputFile } from './generate-file';

// UI helpers re-exported for convenience
export { DEFAULT_SHIKI_OPTIONS } from './ui/context';
export type { Awaitable } from './ui/context';

// Builder types (useful when per: 'custom')
export { fromSdk, fromServer } from './utils/pages/builder';
export type {
    GroupOutput,
    ItemOutput,
    ItemRef,
    OutputEntry,
    PageOutput,
    PsjPagesBuilderConfig,
} from './utils/pages/builder';

// MDX text generation
export { generateDocument, toText } from './utils/pages/to-text';
export type { PsjToTextOptions } from './utils/pages/to-text';

// i18n — UI translations (re-exported for convenience; primary export is @psj/api/i18n)
export { defaultTranslations, defineI18nPsjAPI } from './i18n';
export type { PsjAPITranslations } from './i18n';

// Version utilities — SdkVersions value object, URL helper, server convenience
export type { SdkVersion, SdkVersions } from './types';
