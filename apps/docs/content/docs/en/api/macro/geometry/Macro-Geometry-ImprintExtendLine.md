---
title: "ImprintExtendLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Extend line

## Syntax

```psj
ImprintExtendLine(cursor[] vcrEdge, int iMethod, int iPosition, int iNoFittingPoints, int iDiv, bool bBreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target edges for extending line cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 2. Int

Method type

- 0: Straight
- 1: Same Curvature

<!-- @since:5.0.1 -->
### 3. Int

Position to extend type

- 0: Nearest Edge
- 1: Boundary Edge

<!-- @since:5.0.1 -->
### 4. Int

Number of fitting points

<!-- @since:5.0.1 -->
### 5. Int

Number of divisions

<!-- @since:5.0.1 -->
### 6. Bool

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintExtendLine([5:27], 0, 0, 3, 2, 1)
```
