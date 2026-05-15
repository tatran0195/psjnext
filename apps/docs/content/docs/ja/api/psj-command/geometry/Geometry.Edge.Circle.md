---
title: "Geometry.Edge.Circle()"
description: "Imprint circular edges onto the specified face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Circle"
macro _link: "[ImprintCircleS](../../macro/geometry/ImprintCircleS)"
---

## Description

Imprint circular edges onto the specified face.

## Syntax

```psj
Geometry.Edge.Circle(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
<!-- @since:5.1.0 -->
### veclPositions

- Specify points on faces where the circle will be imprinted.

<!-- @since:5.1.0 @required -->
### crlTargetFace

- Specify the target faces on which the edges are imprinted.

<!-- @since:5.0.1 @optional -->
### dInRadius

- Specify inner circle's radius. This argument is to be used when the value of _iNoOfLayer_ argument is greater than 1. Possible values are _0.0_ ≤ _dInRadius_ ≤ _dOutRadius_. The unit is fixed to \[mm] unit.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dOutRadius

- Specify outer circle's radius. The unit is fixed to \[mm] unit.
- The default value is 4.

<!-- @since:5.0.1 @optional -->
### iNoOfLayer

- Specify number of layers to be imprinted from circle center.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iNoOfDiv

- Specify the number of segments in which the circle will be divided equally.
- The default value is 30.

<!-- @since:5.0.1 @optional -->
### bBreakFace

- Specify whether to break the given faces where possible.
- The default value is _True_.

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### crlTargetsFace

- Specify faces to be imprinted.

## Return Code

A _List of Cursor_ specifying the created circle edges.

## Sample Code

```psj {3-6}
Geometry.Part.Cube()

circle _lines = Geometry.Edge.Circle(veclPositions=[[0.006666666666666666, 0.005555555555555556, 0.01], 
                                                [0.002222222222222222, 0.006666666666666666, 0.01]], 
                                                crlTargetFace=[Face(26)], 
                                                dOutRadius=2.0)
JPT.Debugger(circle _lines)
```
