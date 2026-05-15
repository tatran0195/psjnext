---
title: "CreateSphere()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Sphere Body

## Syntax

```psj
CreateSphere(double[3] vdOriginXYZ, double dRadius, int nLatitudeNodeCnt, int nLongitudeNodeCnt,
    string strBodyName, color colBody, cursor crCoord)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[3]

Origin coordinate Point(\[x, y, z])

<!-- @since:5.0.1 -->
### 2. Double

Sphere radius value (m)

<!-- @since:5.0.1 -->
### 3. Int

Latitude node count

<!-- @since:5.0.1 -->
### 4. Int

Longitude node count

<!-- @since:5.0.1 -->
### 5. String

Part name

<!-- @since:5.0.1 -->
### 6. Color

```
Part color
```

<!-- @since:5.0.1 -->
### 7. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateSphere([0, 0, 0], 0.005, 50, 100, "Sphere _1", 11908427, 0:0)
```
