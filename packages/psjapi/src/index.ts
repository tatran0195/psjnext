/**
 * fumadocs-psjapi — root package exports
 *
 * Re-exports everything needed to configure and use the psjapi integration.
 *
 * Subpath exports (defined in package.json):
 *   fumadocs-psjapi          → this file (types + server factory)
 *   fumadocs-psjapi/ui       → src/ui/index.ts
 *   fumadocs-psjapi/server   → src/server/index.ts
 */

// Core types
export type {
    // Spec types
    SdkManifest,
    SdkInfo,
    VersionEntry,
    LocaleEntry,
    DomainEntry,
    Domain,
    ParamStyle,
    ReturnKind,
    CalloutLevel,
    ExampleLanguage,
    EnumValue,
    Param,
    GroupRef,
    ParamOrGroupRef,
    Returns,
    ReturnCode,
    Callout,
    Example,
    SeeAlsoRef,
    VersionDelta,
    ItemFile,
    ParamGroupFile,
    ItemLocaleSidecar,
    GroupLocaleSidecar,
    // Resolved types
    ResolvedParam,
    ResolvedItem,
    // Server types
    ProcessedSdk,
    PSJAPIServer,
    PSJAPIOptions,
} from './types';

// Server factory
export { createPSJAPI } from './loader';

// Static file generation
export { generateFiles, generateFilesOnly } from './generate-file';
export type { OutputFile, GenerateFilesConfig } from './generate-file';

// UI helpers re-exported for convenience
export type { Awaitable } from './ui/context';
export { DEFAULT_SHIKI_OPTIONS } from './ui/context';

// Builder types (useful when per: 'custom')
export type {
    OutputEntry,
    ItemOutput,
    GroupOutput,
    PageOutput,
    ItemRef,
    PsjPagesBuilderConfig,
} from './utils/pages/builder';
export { fromSdk, fromServer } from './utils/pages/builder';

// MDX text generation
export { toText, generateDocument } from './utils/pages/to-text';
export type { PsjToTextOptions } from './utils/pages/to-text';
