---
title: "BodyCutBySurfaceS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Body Cut By 3 Points

## Syntax

```psj
BodyCutBySurfaceS(cursor[] crBody, cursor cutFace, bool splitOnly, bool makeSectionFace, bool shareFace, bool SeparateFace)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:PartID])

<!-- @since:5.0.1 -->
### 2. Cursor

Target face for cutting

<!-- @since:5.0.1 -->
### 3. Bool

Whether split face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 4. Bool

Whether make section face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Whether share face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Whether separate face or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
BodyCutBySurfaceS([3:2], 3:9, 0, 1, 0, 0)
```
