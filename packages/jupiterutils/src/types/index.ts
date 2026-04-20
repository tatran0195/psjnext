/**
 * Core domain types for psj-editor code generation pipeline.
 */

// ---------------------------------------------------------------------------
// Parameter model
// ---------------------------------------------------------------------------

/** A single Python function parameter, possibly with a default value. */
export interface Param {
    name: string;
    defaultValue: string | null;
}

// ---------------------------------------------------------------------------
// PSJ Command (macro) model
// ---------------------------------------------------------------------------

/**
 * A fully-qualified PSJ command function path, e.g.
 *   namespace = ["Foo", "Bar", "Baz"]
 *   signature  = "doThing(arg1, arg2=0)"
 */
export interface PsjCommand {
    /** Module path segments, e.g. ["Measurement", "Section"] */
    namespace: string[];
    /** Raw function signature including parens, e.g. "doThing(arg1, arg2=0)" */
    signature: string;
}

// ---------------------------------------------------------------------------
// Utility / GUI function model
// ---------------------------------------------------------------------------

export interface UtilFunction {
    /** Function name without parens, e.g. "GetAllByTypeID" */
    name: string;
    /** Raw parameter string from the list file, e.g. "typeID=0, flag=True" */
    rawParams: string;
}

// ---------------------------------------------------------------------------
// Markdown documentation model
// ---------------------------------------------------------------------------

export interface MdDocSection {
    /** Lines starting from "## Description" */
    lines: string[];
}

// ---------------------------------------------------------------------------
// Class-tree model used for PSJ_Classes.py generation
// ---------------------------------------------------------------------------

/**
 * Recursive tree node.
 * - leaf nodes (no children) hold `own` method signatures
 * - branch nodes hold sub-namespace keys and optionally `own` methods
 */
export type ClassTree = {
    own?: string[];
    [subKey: string]: ClassTree | string[] | undefined;
};

// ---------------------------------------------------------------------------
// Entity-type enum entry
// ---------------------------------------------------------------------------

export interface EntityEntry {
    varName: string;
    value: string;
}

// ---------------------------------------------------------------------------
// Config / environment
// ---------------------------------------------------------------------------

export interface Config {
    /** Root of the documentation website, e.g. C:/website */
    webRoot: string;
    /** Root of the macro Python sources, e.g. C:/project/macro */
    macroRoot: string;
    /** Absolute path to the directory this tool runs from */
    projectRoot: string;
}
