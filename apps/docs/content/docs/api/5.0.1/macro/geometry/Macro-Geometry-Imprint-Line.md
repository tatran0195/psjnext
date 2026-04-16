---
id: Imprint_Line
title: Imprint_Line()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint line(Points)

## Syntax

```psj
Imprint_Line(double[] Point_xyz,bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

### `1. Double[]`

Point xyz [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]

### `2. Bool`

Flag true = 1,false=0

### `3. Cursor[]`

Body Cursor([3:*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint_Line([[0.00555556, 0.00333333, 0.01], [0.00555556, 0.00666667, 0.01]], 1, [3:1])
```
