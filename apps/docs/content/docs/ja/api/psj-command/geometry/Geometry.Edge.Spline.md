---
title: "Geometry.Edge.Spline()"
description: "Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Spline"
macro _link: "[GeoImprintSplineS](../../macro/geometry/GeoImprintSplineS)"
---

## Description

Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes.

## Syntax

```psj
Geometry.Edge.Spline(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
<!-- @since:5.1.0 -->
### dllPoints

- Specify the point on the given faces that the spline must pass through.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces on which the spline edges are imprinted.

<!-- @since:5.0.1 @optional -->
### bBreakFace

- Specify whether to break the given face where possible.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created _splines = Geometry.Edge.Spline(dllPoints=[[0.01, 0.003, 0.01],
                                                  [0.007, 0.003, 0.01],
                                                  [0.005, 0.004, 0.01], 
                                                  [0.004, 0.006, 0.01], 
                                                  [0.002, 0.007, 0.01], 
                                                  [0.0, 0.003, 0.01]],
                                       crlFaces=[Face(26)])
JPT.Debugger(created _splines)
```
