---
title: "CutBodyByPlane()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Cut body by plane

## Syntax

```psj
CutBodyByPlane(cursor crBody, double[3] cutPosition, int iType, double dOffset,
    bool bSplit, bool bSectionFace, bool bshareFace, cursor crLocalCoor, bool SeparateFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Part key cursor(Part ID)

<!-- @since:5.0.1 -->
### 2. Double\[3]

Target 1 point for cutting

<!-- @since:5.0.1 -->
### 3. Int

Type option

<!-- @since:5.0.1 -->
### 4. Double

Offset value from cutting plane

<!-- @since:5.0.1 -->
### 5. Bool

Whether split face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Whether make section face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

Whether share face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 9. Bool

Whether separate face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CutBodyByPlane(3:3, [0.02, 0.01555555555555556, 0.007777777777777778], 0, 0, 0, 1, 0, 0:0, 1)
```
