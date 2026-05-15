---
title: "CreateTrapezoid()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Trapezoid Body

## Syntax

```psj
CreateTrapezoid(double[3] vdOriginXYZ, double[3] vdLength, double dTopXLength, double dRadius,
    int[3] vlNodeCnt, string strBodyName, color colBody, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[3]

Origin coordinate Point(\[x, y, z])

<!-- @since:5.0.1 -->
### 2. Double\[3]

Length along the coordinate axis Length(\[x\_length, y\_length, z\_length])

<!-- @since:5.0.1 -->
### 3. Double

Length in X (Top)

<!-- @since:5.0.1 -->
### 4. Double

Radius corresponding to bool flag Circle Segment

<!-- @since:5.0.1 -->
### 5. Int\[3]

Number of node along the coordinate axis Node(\[x\_node, y\_node, z\_node])

<!-- @since:5.0.1 -->
### 6. String

Part name

<!-- @since:5.0.1 -->
### 7. Color

Part color

<!-- @since:5.0.1 -->
### 8. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateTrapezoid([0, 0, 0], [0.01, 0.015, 0.02], 0.007, 0.005, [10, 10, 10], "Trapezoid _1", 5000371, 0:0)
```
