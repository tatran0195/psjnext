---
title: "MakeFacePlanar()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Make planar faces by given plane points

## Syntax

```psj
MakeFacePlanar(double[3] dPlanePt1, double[3] dPlanePt2, double[3] dPlanePt3, int[] nFaceIDs, bool mergeFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[3]

Plane point 1

<!-- @since:5.0.1 -->
### 2. Double\[3]

Plane point 2

<!-- @since:5.0.1 -->
### 3. Double\[3]

Plane point 3

<!-- @since:5.0.1 -->
### 4. Int\[]

Target faces for making planar surface(\[Face ID])

<!-- @since:5.0.1 -->
### 5. Bool

Whether merge face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MakeFacePlanar([0.01, 0.01, 0.007272871569190634], [0.01, 0.01, 0], [0.003333333333333333, 0.01, 0], [47], 0)
```
