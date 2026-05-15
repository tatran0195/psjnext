---
title: "CreateCylinderFrustum()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create Frustum Body

## Syntax

```psj
CreateCylinderFrustum(double[3] vdOriginXYZ, double TopRadius, double bottomRadius, double height, int circleNodeCount,
    int axisNodeCount, string bodyName, color bodyColor, cursor crCoord)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Double\[3]

Point \[x,y,z]

<!-- @since:5.1.0 -->
### 2. Double

Top Radius

<!-- @since:5.1.0 -->
### 3. Double

Bottom Radius

<!-- @since:5.1.0 -->
### 4. Double

Height

<!-- @since:5.1.0 -->
### 5. Int

Circle Node Count

<!-- @since:5.1.0 -->
### 6. Int

Axis Node Count

<!-- @since:5.1.0 -->
### 7. String

Body Name

<!-- @since:5.1.0 -->
### 8. Color

Body Color

<!-- @since:5.1.0 -->
### 9. Cursor

Coordinate Cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateCylinderFrustum([0, 0, 0], 0.003, 0.01, 0.02, 20, 20, "Frustum _1", 14903267, 0:0)
```
