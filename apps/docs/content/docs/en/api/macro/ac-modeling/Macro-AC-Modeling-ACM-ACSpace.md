---
title: "ACM _ACSpace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

ACM\_ACSpace

## Syntax

```psj
ACM _ACSpace(cursor crBodyKey, double dGradingFact, int iRegion, bool bIntNode, bool bSafeMode,
    bool bIntMeshOnly, bool bPML, bool bSweGrd, double dWidth, int iLayer, int iAxis,
    double dSweCoord, double dSweMeshSize, int iLayer)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Body key cursor(\[Part ID])

<!-- @since:5.0.1 -->
### 2. Double

Grading Factor

<!-- @since:5.0.1 -->
### 3. Int

Region type:

- 0: Main region
- 1: All region

<!-- @since:5.0.1 -->
### 4. Bool

Inter nodes bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Safe mode bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Internal mesh only bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

PML bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Bool

Sweep to ground bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 9. Double

PML width

<!-- @since:5.0.1 -->
### 10. Int

PML layer

<!-- @since:5.0.1 -->
### 11. Int

Axis type:

- 0: X
- 1: Y
- 2: Z

<!-- @since:5.0.1 -->
### 12. Double

Sweep to ground Coordinate

<!-- @since:5.0.1 -->
### 13. Double

Sweep to ground mesh size

<!-- @since:5.0.1 -->
### 14. Int

Sweep to ground layer

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ACM _ACSpace([1, 2], 10, 0, 0, 0, 0, 1, 0, 0.015, 3, 0, -0.02, 0.02, 1)
```
