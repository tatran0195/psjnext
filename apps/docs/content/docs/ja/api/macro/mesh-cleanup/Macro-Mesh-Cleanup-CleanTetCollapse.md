---
title: "CleanTetCollapse()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Cleanup tetrahedral mesh by Metric:Tet Collapse.

## Syntax

```psj
CleanTetCollapse(cursor[] crlElems, int iKeepSurfMesh, int iCondition, double dLimitValue, int iMode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

The list of target element cursors.

<!-- @since:5.1.0 -->
### 2. Int

The keeping method of surface mesh.

- 0: Default, no keep.
- 1: Keep Surface Mesh for all the mesh.
- 2: Keep Surface Mesh at Freeze Mesh area.

<!-- @since:5.1.0 -->
### 3. Int

The condition.

- 0: <=, Collapse the elements to cleanup.
- 1: >=, Split the elements to cleanup.
- 2: <, Collapse the elements to cleanup.
- 3: >, Split the elements to cleanup.

<!-- @since:5.1.0 -->
### 4. Double

The cleaning threshold value.

<!-- @since:5.1.0 -->
### 5. Int

The cleaning mode.

- 0: Method S
- 1: Method A
- 2: Method D

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CleanTetCollapse([Elem(126, 151, 163)], 0, 0, 0.05, 0)
```
