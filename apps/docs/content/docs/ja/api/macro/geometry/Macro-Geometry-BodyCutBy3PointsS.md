---
title: "BodyCutBy3PointsS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Body Cut By 3 Points

## Syntax

```psj
BodyCutBy3PointsS(cursor crBody, double[] cutPosition, double dOffset , bool bSplit, bool makeSectionFace, bool shareFace, bool SeparateFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Part key cursor(Part ID)

<!-- @since:5.0.1 -->
### 2. Double\[]

Target points for cutting

<!-- @since:5.0.1 -->
### 3. Double

Offset value from cutting plane

<!-- @since:5.0.1 -->
### 4. Bool

Whether split face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Whether make section face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Whether share face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

Whether separate face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
BodyCutBy3PointsS(3:2, [[0.01, 0.003333333333333333, 0.01], [0.02, 0.003333333333333333, 0.01], [0.02, 0.003333333333333333, 0]], 0.0022, 0, 1, 0, 1)
```
