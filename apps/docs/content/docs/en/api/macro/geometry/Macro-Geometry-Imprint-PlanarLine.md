---
title: "Imprint _PlanarLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Planar line

## Syntax

```psj
Imprint _PlanarLine(double[] Point _xyz, int[] FaceID,Cursor Coordinate, int PlaneType,
    bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Point xyz \[\[x1,y1,z1]]

<!-- @since:5.0.1 -->
### 2. Int\[]

Face ID

<!-- @since:5.0.1 -->
### 3. Cursor

Coordinate System (\[0:0]=Global)

<!-- @since:5.0.1 -->
### 4. Int

Plane Type (YZ=0,ZX=1,XY=2,3Points=3)

<!-- @since:5.0.1 -->
### 5. Bool

Flag Break Face true = 1,false=0

<!-- @since:5.0.1 -->
### 6. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _PlanarLine([[0.005, 0.0111111, 0.00866025]], [5], 0:0, 1, 1, [3:1])
```
