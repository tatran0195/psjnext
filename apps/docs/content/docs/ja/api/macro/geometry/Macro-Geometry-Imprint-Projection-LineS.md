---
title: "Imprint _Projection _LineS()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Projection line

## Syntax

```psj
Imprint _Projection _LineS(cursor[] taCrEdges, cursor[] taCrFaces, cursor[] taCrNodes,
    bool bBreakFace, int iType, bool bCheckGap, double dGap)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target edge for projection line cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target face for projecting line on cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target node cursor(\[10:Node ID]) corresponding to Vector Direction type 1

<!-- @since:5.0.1 -->
### 4. Bool

Whether break face or not True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Int

Vector Direction type

- 0: Target Face Normal
- 1: Two Nodes
- 2: Nearest Vector

<!-- @since:5.0.1 -->
### 6. Bool

Whether check Gap or not True =1, False = 0

<!-- @since:5.0.1 -->
### 7. Double

Gap value

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _Projection _LineS([5:568], [6:67], [10:1347, 10:1324], 1, 1, 1, 0.003)
```
