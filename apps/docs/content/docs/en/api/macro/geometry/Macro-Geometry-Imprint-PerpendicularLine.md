---
title: "Imprint _PerpendicularLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Perpendicular line

## Syntax

```psj
Imprint _PerpendicularLine(double[] Point _xyz, int[] FaceID, double Offset,bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Point xyz \[\[x1,y1,z1],\[x2,y2,z2]]

<!-- @since:5.0.1 -->
### 2. Int\[]

Face ID

<!-- @since:5.0.1 -->
### 3. Double

Offset Value

<!-- @since:5.0.1 -->
### 4. Bool

Flag Break Face true = 1,false=0

<!-- @since:5.0.1 -->
### 5. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _PerpendicularLine([[0.01, 0.00555556, 0.01], [0.01, 0.01, 0.00444444]], [24], 0, 1, [3:1])
```
