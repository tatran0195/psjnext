---
title: "SurfaceDistanceDistanceCalculate()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display the distance between parts as a contour.

## Syntax

```psj
SurfaceDistanceDistanceCalculate(str strTitle, int iRegionType, double dTolerance, int iTypeMesh, int iAxisDirection, double[] dlDirection, cursor crRefNode, cursor crPartGroup1, cursor crPartGroup2)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying the name of the result to be created.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying the region type to make the comparison.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the tolerance between edges.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the position of mesh nodes.

<!-- @since:5.1.0 -->
### 5. int

- An Integer specifying the axis direction.

<!-- @since:5.1.0 -->
### 6. double\[]

- A List of Double specifying the direction vector to be calculated.

<!-- @since:5.1.0 -->
### 7. cursor

- A Cursor specifying the reference node.

<!-- @since:5.1.0 -->
### 8. cursor

- A Cursor specifying the first target. The target can be Part or Group Element depend on the selection of iCompareRegionType.

<!-- @since:5.1.0 -->
### 9. cursor

- A Cursor specifying the second target. The target can be Part or Group depend on the selection of iCompareRegionType.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SurfaceDistanceDistanceCalculate("Untitled", 0, 2.0, 0, 0, [1.0, 0.0, 0.0], 10:124, 3:4, 3:6)
```
