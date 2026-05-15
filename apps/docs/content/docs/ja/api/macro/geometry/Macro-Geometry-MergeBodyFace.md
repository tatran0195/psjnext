---
title: "MergeBodyFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge Body Face

## Syntax

```psj
MergeBodyFace(int[] taBodyKey, int[] taFaceKey, bool bAngle, double dToleranceAngle, bool bWidth, double dToleranceWidth)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Part cursor(\[Part ID])

<!-- @since:5.0.1 -->
### 2. Int\[]

Face cursor(\[Face ID])

<!-- @since:5.0.1 -->
### 3. Bool

Whether select angle or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 4. Double

Insert tolerance angle value

<!-- @since:5.0.1 -->
### 5. Bool

Whether select width or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Double

Insert tolerance width value

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergeBodyFace([1], [29], 1, 20, 1, 0.0002)
```
