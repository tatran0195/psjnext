---
title: "PostRotateMapping()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Copy (mapping) stress to create continuous stress data in the direction of rotation.

## Syntax

```psj
PostRotateMapping(doule dAngleInterval, int iRotateAxis, int iCoordinateReference, int iInterpolateType, doubled AreaTolerance, double dMeshTolerance, int iRegionType, cursor crPart)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. double

- A Double specifying the rotation angle in degree.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying the selection of rotation axis.

<!-- @since:5.1.0 -->
### 3. int

- An Integer specifying the coordinate reference.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the interpolation type when mapping.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the value of area tolerance.

<!-- @since:5.1.0 -->
### 6. double

- A Double specifying value of mesh tolerance.

<!-- @since:5.1.0 -->
### 7. int

- An Integer specifying the region type to map the result.

<!-- @since:5.1.0 -->
### 8. cursor

- A Cursor specifying the target to map the result. The target can be part if RegionType = By Part, or solid element if RegionType = By Group.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostRotateMapping(7.5, 3, 0, 1, 1, 0.05, 0, 0:0)
```
