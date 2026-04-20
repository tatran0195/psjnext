/**
 * Class-tree builder.
 *
 * Converts a flat list of PSJ commands (e.g. "Measurement.Section.getArea(arg)")
 * into a nested `ClassTree` that mirrors the Python class hierarchy we need to
 * generate.
 *
 * Each namespace segment becomes a branch; the terminal function signature is
 * stored under the special key `"own"` of the deepest branch node.
 */

import type { ClassTree, PsjCommand } from '@/types';

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Build the class tree from an array of collected PSJ commands.
 *
 * The tree has this shape (example):
 *
 *   {
 *     Measurement: {
 *       own: ["getProjectName(arg)"],
 *       Section: {
 *         own: ["getArea(arg1, arg2=0)"],
 *         Path: {
 *           own: ["getNodes()"]
 *         }
 *       }
 *     }
 *   }
 */
export function buildClassTree(commands: PsjCommand[]): ClassTree {
    const root: ClassTree = {};

    for (const cmd of commands) {
        if (cmd.namespace.length === 0 || !cmd.signature) continue;

        insertCommand(root, cmd.namespace, cmd.signature);
    }

    return root;
}

// ---------------------------------------------------------------------------
// Internal
// ---------------------------------------------------------------------------

function insertCommand(node: ClassTree, namespace: string[], signature: string): void {
    if (namespace.length === 0) {
        // Leaf: attach to "own"
        const own = node['own'];
        if (Array.isArray(own)) {
            own.push(signature);
        } else {
            node['own'] = [signature];
        }
        return;
    }

    const [head, ...tail] = namespace;
    if (head === undefined) return;

    if (tail.length === 0) {
        // One more segment left — the signature belongs at this level's "own"
        // unless we need to go deeper. Actually: if tail is empty, the next
        // call will set "own" at the child level. Keep recursing.
    }

    // Get or create the child branch
    let child = node[head];
    if (child === undefined || !isClassTree(child)) {
        child = {};
        node[head] = child;
    }

    insertCommand(child, tail, signature);
}

function isClassTree(v: ClassTree | string[] | undefined): v is ClassTree {
    return typeof v === 'object' && !Array.isArray(v);
}

// ---------------------------------------------------------------------------
// Tree introspection helpers (used by generators)
// ---------------------------------------------------------------------------

/** Return the list of sub-namespace keys (excluding "own"). */
export function subKeys(node: ClassTree): string[] {
    return Object.keys(node).filter((k) => k !== 'own');
}

/** Return "own" methods for a node, or []. */
export function ownMethods(node: ClassTree): string[] {
    const own = node['own'];
    return Array.isArray(own) ? own : [];
}

/** Get a child node safely. */
export function getChild(node: ClassTree, key: string): ClassTree | null {
    const child = node[key];
    if (child === undefined || Array.isArray(child)) return null;
    return child;
}
