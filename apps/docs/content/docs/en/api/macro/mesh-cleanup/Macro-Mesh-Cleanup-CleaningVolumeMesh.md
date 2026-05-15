---
title: "CleaningVolumeMesh()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Cleanup tetrahedral mesh by Metric:Volume.

## Syntax

```psj
CleaningVolumeMesh(cursor[] crlParts, cursor[] crlElems, double dLimitValue, int iMode)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

The list of target part cursors.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

The list of target element cursors.

<!-- @since:5.1.0 -->
### 3. Double

The cleaning threshold value (e.g., minimum volume).

<!-- @since:5.1.0 -->
### 4. Int

The cleaning mode.

- 0: Standard
- 1: Aggressive
- 2: Remove

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CleaningVolumeMesh([Part(1)], [], 2e-09, 1)
```
