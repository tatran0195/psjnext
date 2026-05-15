---
title: "CreateCone()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Cone Body

## Syntax

```psj
CreateCone(double[3] vdOriginXYZ, double bottomRadius, double height, int circleNodeCount,
    int axisNodeCount, string bodyName, color bodyColor, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[3]

Point \[x,y,z]

<!-- @since:5.0.1 -->
### 2. Double

Bottom Radius

<!-- @since:5.0.1 -->
### 3. Double

Height

<!-- @since:5.0.1 -->
### 4. Int

Circle Node Count

<!-- @since:5.0.1 -->
### 5. Int

Axis Node Count

<!-- @since:5.0.1 -->
### 6. String

Body Name

<!-- @since:5.0.1 -->
### 7. Color

Body Color

<!-- @since:5.0.1 -->
### 8. Cursor

Coordinate Cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateCone([0, 0, 0], 0.01, 0.02, 100, 5, "Cone _1", 7138156, 0:0)
```
