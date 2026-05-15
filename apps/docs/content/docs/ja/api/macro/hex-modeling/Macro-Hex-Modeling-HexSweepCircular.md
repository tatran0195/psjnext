---
title: "HexSweepCircular"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Hex mesh by circular sweep

## Syntax

```psj
HexSweepCircular(int[] taFaceKey, double dAngle, double dTol, int iLayer, double[3] vAxisCenterPt,
    double[3] vAxisVect, bool bInterfaceElem, bool bExtrusion, double dTranslationExtrusion,
    bool bDeleteOriginalParts)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Face key cursor(\[Face ID])

<!-- @since:5.0.1 -->
### 2. Double

Circular angle

<!-- @since:5.0.1 -->
### 3. Double

Axis tolerance

<!-- @since:5.0.1 -->
### 4. Int

Number of layer

<!-- @since:5.0.1 -->
### 5. Double\[3]

Sweeping axis center point

<!-- @since:5.0.1 -->
### 6. Double\[3]

Sweeping axis vector point

<!-- @since:5.0.1 -->
### 7. Bool

Interface Elems bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Bool

Total revolution and extrusion bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 9. Double

Translation distance

<!-- @since:5.0.1 -->
### 10. Bool

Delete original parts bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
HexSweepCircular([131], 360, 1e-07, 100, [-0.004, 0, -8.67362e-19], [0, 0, 1], 1, 1, 0.0122, 1)
```
