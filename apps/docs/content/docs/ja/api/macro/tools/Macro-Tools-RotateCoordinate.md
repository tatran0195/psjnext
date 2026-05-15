---
title: "RotateCoordinate()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Rotate coordinate

## Syntax

```psj
CreateCoordinateRotate(string strName, int iCoordType, vector vecRotate, bool bCreateNew, cursor crRefCoord, position posCenterRot, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

Coordinate name

<!-- @since:5.1.0 -->
### 2. Int

Coordinate type (0: Rectangular, 1: Cylindrical, 2: Spherical)

<!-- @since:5.1.0 -->
### 3. Vector

Coordinate rotation

<!-- @since:5.1.0 -->
### 4. Bool

New creation bool flag True = 1, False = 0

<!-- @since:5.1.0 -->
### 5. TCursor

Reference coordinate

<!-- @since:5.1.0 -->
### 6. Position

Position of rotation center

<!-- @since:5.1.0 -->
### 7. TCursor

Edit target coordinate

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateCoordinateRotate("CRect _2", 0, [1.570796326794412, 1.047197551196275, 1.570796326794412], 1, 27:1, [0.01, 0, 0.01], 27:1)
```
