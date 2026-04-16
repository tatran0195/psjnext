---
id: GeometoryImprintEdgeSpline
title: GeometoryImprintEdgeSpline()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint Spline

## Syntax

```psj
GeometoryImprintEdgeSpline(double[] Point xyz,bool Flag Break Face ,Cursor[] Body Cursor)
```

## Inputs

### `1. Double[]`

Point xyz [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]

### `2. Bool`

Flag true = 1,false=0

### `3. Int`

Body Cursor([3:*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometoryImprintEdgeSpline([0.00666667, 0.00222222, 0.01, 0.00777778, 0.00444444, 0.01, 0.00333333, 0.00666667, 0.01], 1, [3:1])
```
