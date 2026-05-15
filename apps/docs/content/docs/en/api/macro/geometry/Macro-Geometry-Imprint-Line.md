---
title: "Imprint _Line()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint line(Points)

## Syntax

```psj
Imprint _Line(double[] Point _xyz,bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Point xyz \[\[x1,y1,z1],\[x2,y2,z2],\[x3,y3,z3]]

<!-- @since:5.0.1 -->
### 2. Bool

Flag true = 1,false=0

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _Line([[0.00555556, 0.00333333, 0.01], [0.00555556, 0.00666667, 0.01]], 1, [3:1])
```
