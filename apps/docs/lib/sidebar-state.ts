'use client';

/**
 * A lightweight persistent store for sidebar expansion states.
 * Uses a global Set to track folder IDs that have been manually expanded or auto-expanded.
 */

const expandedFolders = new Set<string>();

export function isFolderExpanded(id: string): boolean {
    if (typeof window === 'undefined') return false;
    return expandedFolders.has(id);
}

export function setFolderExpanded(id: string, expanded: boolean): void {
    if (typeof window === 'undefined') return;
    if (expanded) {
        expandedFolders.add(id);
    } else {
        expandedFolders.delete(id);
    }
}
