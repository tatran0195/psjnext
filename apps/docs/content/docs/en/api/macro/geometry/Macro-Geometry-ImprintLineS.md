---
title: "ImprintLineS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint line(Points)

## Syntax

```psj
GeoImprintSplineS(double[] taPositions, cursor[] taTargetFace, bool bBreakFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Target points for imprinting -> Point\_n(\[xi, yi, zi])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target faces cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Bool

Whether break face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintLineS([[0.007777777777777778, 0.01, 0.001111111111111111], [0.005555555555555556, 0.01, 0.001111111111111111]], [6:22], 1)
```
