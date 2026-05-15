---
title: "SearchTargetFacesInModel()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Search target faces in model

## Syntax

```psj
SearchTargetFacesInModel(int BodyType, double[3] OriginPoint, double[3] LengthXYZ,
    double[3] CenterPoint, double[3] MajorPoint, double[3] MinorPoint, bool Enclosed)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Body Type

- 0: Cube
- 1: Spheroid

<!-- @since:5.0.1 -->
### 2. Double\[3]

Origin Point

<!-- @since:5.0.1 -->
### 3. Double\[3]

Length X, Y, Z

<!-- @since:5.0.1 -->
### 4. Double\[3]

Center point

<!-- @since:5.0.1 -->
### 5. Double\[3]

Major point

<!-- @since:5.0.1 -->
### 6. Double\[3]

Minor point

<!-- @since:5.0.1 -->
### 7. Bool

Enclosed bool flag 0: False, 1: True

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SearchTargetFacesInModel(0, [0, 0, 0], [0.01, 0.01, 0.01], [0, 0, 0], [0, 0, 0.01], [0.005, 0, 0], 0)
```
