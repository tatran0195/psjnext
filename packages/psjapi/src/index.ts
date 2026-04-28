// Core types
export type {
    Callout, CalloutLevel, Domain, DomainEntry, EnumValue, Example, ExampleLanguage, GroupLocaleSidecar, GroupRef, ItemFile, ItemLocaleSidecar, LocaleEntry, Param, ParamGroupFile, ParamOrGroupRef, ParamStyle,
    // Server types
    ProcessedSdk, PSJAPIOptions, PSJAPIServer, ResolvedItem,
    // Resolved types
    ResolvedParam, ReturnCode, ReturnKind, Returns, SdkInfo,
    // Spec types
    SdkManifest, SeeAlsoRef,
    VersionDelta, VersionEntry
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
    GroupOutput, ItemOutput, ItemRef, OutputEntry, PageOutput, PsjPagesBuilderConfig
} from './utils/pages/builder';

// MDX text generation
export { generateDocument, toText } from './utils/pages/to-text';
export type { PsjToTextOptions } from './utils/pages/to-text';

// i18n — UI translations (re-exported for convenience; primary export is fumadocs-psjapi/i18n)
export { defaultTranslations, defineI18nPsjAPI } from './i18n';
export type { PsjAPITranslations } from './i18n';

