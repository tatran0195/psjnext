---
title: "CreateTorus()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Torus Body

## Syntax

```psj
CreateTorus(double[3] vdOriginXYZ, double dInnerRadius, double dRingRadius, int nLatitudeNodeCnt,
    int nLongitudeNodeCnt,string strBodyName, color colBody, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[3]

Origin coordinate Point(\[x, y, z])

<!-- @since:5.0.1 -->
### 2. Double

Inner radius value (m)

<!-- @since:5.0.1 -->
### 3. Double

Ring radius value (m)

<!-- @since:5.0.1 -->
### 4. Int

Latitude node count

<!-- @since:5.0.1 -->
### 5. Int

Longitude node count

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
CreateTorus([0, 0, 0], 0.015, 0.02, 20, 20, "Torus _1", 11882677, 0:0)
```
