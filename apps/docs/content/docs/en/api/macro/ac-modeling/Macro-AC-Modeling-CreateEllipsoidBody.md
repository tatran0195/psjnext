---
title: "CreateEllipsoidBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create Ellipsoid Body

## Syntax

```psj
CreateEllipsoidBody(bool bAuto, double dTol, int[] taBodyK, double[] dOrigin, double[] dMajorPt, double[] dMinorPt, int iLatitudeNodeCnt, int iLongitudeNodeCnt, string strName, color colBody, cursor curCoord)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

Flag of Auto mode

- 0: OFF
- 1: ON

<!-- @since:5.1.0 -->
### 2. double

Tolerance

<!-- @since:5.1.0 -->
### 3. int\[]

A list of part IDs of objects enclosed by the created ellipsoid.

<!-- @since:5.1.0 -->
### 4. double\[]

Origin Coordinates（Center Point：X,Y,Z）

<!-- @since:5.1.0 -->
### 5. double\[]

長Major Axis Vector （Major Point：X,Y,Z）

<!-- @since:5.1.0 -->
### 6. double\[]

Minor Axis Vector（Minor Point：X,Y,Z）

<!-- @since:5.1.0 -->
### 7. int

Number of Latitude Nodes.

<!-- @since:5.1.0 -->
### 8. int

Number of Longitude Nodes.

<!-- @since:5.1.0 -->
### 9 string

Part Name

<!-- @since:5.1.0 -->
### 10 color

Part Color

<!-- @since:5.1.0 -->
### 11 cursor

Cursor of Reference Coordinate.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateEllipsoidBody(1, 0.01, [1], [0, 0, 0], [0, 0, 0], [0, 0, 0], 0, 0, "INBoundary", 6409934, 0:0)
```
