---
id: Imprint_PerpendicularLine
title: Imprint_PerpendicularLine()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint Perpendicular line

## Syntax

```psj
Imprint_PerpendicularLine(double[] Point_xyz, int[] FaceID, double Offset,bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

### `1. Double[]`

Point xyz [[x1,y1,z1],[x2,y2,z2]]

### `2. Int[]`

Face ID

### `3. Double`

Offset Value

### `4. Bool`

Flag Break Face true = 1,false=0

### `5. Cursor[]`

Body Cursor([3:*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint_PerpendicularLine([[0.01, 0.00555556, 0.01], [0.01, 0.01, 0.00444444]], [24], 0, 1, [3:1])
```
