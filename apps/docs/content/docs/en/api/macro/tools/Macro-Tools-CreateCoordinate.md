---
title: "CreateCoordinate()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create coordinate

## Syntax

```psj
CreateCoordinate(string name, int type, point point1, point point2, point point3, TCursor crRefCoord, TCursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Coordinate name

<!-- @since:5.0.1 -->
### 2. Int

Coordinate type (0: Rectangular, 1: Cylindrical, 2: Spherical)

<!-- @since:5.0.1 -->
### 3. Point

Coordinate definition point 1

<!-- @since:5.0.1 -->
### 4. Point

Coordinate definition point 2

<!-- @since:5.0.1 -->
### 5. Point

Coordinate definition point 3

<!-- @since:5.0.1 -->
### 6. TCursor

Reference coordinate

<!-- @since:5.0.1 -->
### 7. TCursor

Edit target coordinate

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateCoordinateThreeNode("CRect3", 0, 0, [10:466, 10:467, 10:475], [], 0:0, 0:0)
```
