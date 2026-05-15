---
title: "ImprintCircleS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint circle line

## Syntax

```psj
ImprintCircleS(double[] taPositions, cursor[] taTargetFace, double dInRadius, double dOutRadius,
    int iNoofLayer, int iNoOfDiv, bool bBreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Target points for imprinting -> Point\_n(\[xi, yi, zi])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target faces cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Double

Inner radius

<!-- @since:5.0.1 -->
### 4. Double

Outer radius

<!-- @since:5.0.1 -->
### 5. Int

Number of layers

<!-- @since:5.0.1 -->
### 6. Int

Number of divisions

<!-- @since:5.0.1 -->
### 7. Bool

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintCircleS([[0.007777777777777778, 0.006666666666666666, 0.01]], [6:26], 0.001, 0.002, 1, 30, 1)
```
