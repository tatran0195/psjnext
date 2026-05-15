---
title: "ImprintPlannarLineS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint planar line

## Syntax

```psj
ImprintPlannarLineS(double[] taPositions, cursor[] taTargetFace, cursor crLocalCoor, int iType, bool bBreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Target points for imprinting -> Point\_n(\[xi, yi, zi])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target faces cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 4. Int

Type option

<!-- @since:5.0.1 -->
### 5. Bool

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintPlannarLineS([[0.0017364817766693, 0.004444444444444444, -0.009848077530122082]], [6:5], 0:0, 1, 0)
```
