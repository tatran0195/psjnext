---
title: "Geom _FindFeatures()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Face/Edge selected of grouped by its feature

## Syntax

```psj
Geom _FindFeatures(int taItems, int nType, int nOption, TKey taEdgeItems, int bCylinder, bool bDisc,
    bool bFourCorners, double dMinThickness, double dMaxThickness, double dDiameterMin,
    double dDiameterMax, TKey taFaceItems)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Items ID

<!-- @since:5.0.1 -->
### 2. Int

If Type == 1 find faces, if type == 2 find edges

<!-- @since:5.0.1 -->
### 3. Int

Option

<!-- @since:5.0.1 -->
### 4. Int\[]

Edge ID

<!-- @since:5.0.1 -->
### 5. Bool

Cylinder flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 6. Bool

Disc flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 7. Bool

Four corners flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 8. Double

Min thickness value

<!-- @since:5.0.1 -->
### 9. Double

Max thickness value

<!-- @since:5.0.1 -->
### 10. Double

Min Diameter value

<!-- @since:5.0.1 -->
### 11. Double

Max diameter value

<!-- @since:5.0.1 -->
### 12. Int\[]

Face ID

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Geom _FindFeatures([1], 1, 0, [], 1, 0, 1, 0.1, 2, 1, 2, [])
```
