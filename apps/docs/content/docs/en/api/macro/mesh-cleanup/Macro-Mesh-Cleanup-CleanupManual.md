---
title: "CleanupManual()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Command for cleaning surface mesh elements that do not meet the specified quality criteria.

## Syntax

```psj
CleanupManual(cursor[] crlParts, int iElemType, int iVeQuality, int iCheckCondition, double dLimitValue, double dCFLValue, int iNonManifold, int iCleanupMode, cursor[] crlElems)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

The list of target part cursors.

<!-- @since:5.1.0 -->
### 2. Int

The type of target elements.

- 0: Tri
- 1: Quad

<!-- @since:5.1.0 -->
### 3. Int

The quality metric.

- 0: Stretch
- 1: Aspect Ratio
- 2: Edge Length
- 3: Area
- 4: Warp
- 5: Skew
- 6: VDS Stretch
- 7: Node Valence
- 8: Volume
- 9: Interior Angle
- 10: Jacobian
- 11: Taper
- 12: Node Free Edges
- 13: Duplicate Elements
- 14: Tet Collapse
- 15: Tet Skew
- 16: Tet Collapse 2
- 17: Vol Aspect Ratio
- 18: Unstable
- 19: CFL Condition

<!-- @since:5.1.0 -->
### 4. Int

The check condition.

- 0: <=
- 1: >=
- 2: <
- 3: >

<!-- @since:5.1.0 -->
### 5. Double

The quality threshold value.

<!-- @since:5.1.0 -->
### 6. Double

The CFL threshold value.

<!-- @since:5.1.0 -->
### 7. Int

Whether to include non-manifold elements.

- 0: Exclude
- 1: Include

<!-- @since:5.1.0 -->
### 8. Int

The cleanup mode.

- 0: Standard
- 1: Aggressive

<!-- @since:5.1.0 -->
### 9. Cursor\[]

The list of target element cursors.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CleanupManual([3:1], 0, 1, 3, 10, 0.1, 0, 0, [11:82, 11:83])
```
