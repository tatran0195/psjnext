---
title: "MC _TET _EDGE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Command for cleaning tetrahedral mesh elements by edge length.

## Syntax

```psj
MC _TET _EDGE(cursor[] crlElements, int iCondition, double dLimitValue, int iMode, int iNonManifold, int iKeepSurfMesh, int iKeepSurfMeshMode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

The list of target element cursors.

<!-- @since:5.1.0 -->
### 2. Int

The cleanup condition.

<!-- @since:5.1.0 -->
### 3. Double

The cleanup threshold value.

<!-- @since:5.1.0 -->
### 4. Int

The cleanup mode.

- 0: Standard
- 1: Aggressive

<!-- @since:5.1.0 -->
### 5. Int

Whether to include non-manifold elements.

- 0: Exclude
- 1: Include

<!-- @since:5.1.0 -->
### 6. Int

The keeping method of surface mesh.

- 0: Default, no keep.
- 1: Keep Surface Mesh for all the mesh.
- 2: Keep Surface Mesh at Freeze Mesh area.

<!-- @since:5.1.0 -->
### 7. Int

The keeping mode of surface mesh.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC _TET _EDGE([Elem(126, 151, 163)], 0, 0.1, 0, 0, 0, 3)
```
