---
title: "CreateCube()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

This function creates a cube shape body in a specific location.
User can select coordinate system and its relative location to this coordinate.

## Syntax

```psj
CreateCube(double[3] vdOriginXYZ, double[3] vdLength, int[3] vlNodeCnt, string strBodyName,
    color colBody, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[3]

Origin coordinate Point(\[x, y, z])

<!-- @since:5.0.1 -->
### 2. Double\[3]

Length along the coordinate axis Length(\[x\_length, y\_length, z\_length])

<!-- @since:5.0.1 -->
### 3. Int\[3]

Number of node along the coordinate axis Node(\[x\_node, y\_node, z\_node])

<!-- @since:5.0.1 -->
### 4. String

Part name

<!-- @since:5.0.1 -->
### 5. Color

Part color

<!-- @since:5.0.1 -->
### 6. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube _1", 5093709, 0:0)
```
