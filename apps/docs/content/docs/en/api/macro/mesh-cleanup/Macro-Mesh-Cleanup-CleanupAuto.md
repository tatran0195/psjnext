---
title: "CleanupAuto()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Cleanup elements found by Auto Check (Tri)

## Syntax

```psj
CleanupAuto(cursor[] taBodyCur, int elemType, int[] inequalitySigns, int[] flagsOfMetrics, double[] values, cursor[] taElemCur)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

The list of Target part cursor(3:Part ID)

<!-- @since:5.1.0 -->
### 2. Int

Element type. Set to 0 (Tri).

<!-- @since:5.1.0 -->
### 3. Int\[]

Direction of the inequality signs (fixed) corresponding to 4.Int\[] list.

- 0 : {'<='}
- 1 : {'>='}

<!-- @since:5.1.0 -->
### 4. Int\[]

Flags of metrics

- 0 : Stretch
- 1 : Aspect Ratio
- 2 : Edge Length
- 3 : Area
- 7 : Node Valence
- 9 : Duplicate Elements
- 13: Interior Angle

<!-- @since:5.1.0 -->
### 5. Double\[]

Values for each metric corresponding to 4.Int\[] list.
For Duplicate Elements, put 0 if enabled.

<!-- @since:5.1.0 -->
### 6. Cursor\[]

The list of target element cursor(11:Element ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CleanupAuto([3:1, 3:2, 3:3], 0, [0, 1, 0, 0, 1, 0, 0], [0, 1, 2, 3, 7, 9, 13], [0.1, 10, 0.0001, 1e-08, 10, 10, 0], [11:539, 11:532, 11:559, 11:566])
```
