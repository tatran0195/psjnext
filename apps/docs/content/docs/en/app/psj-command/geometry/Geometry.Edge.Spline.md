---
title: "Geometry.Edge.Spline()"
description: "Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Spline"
macro_link: "[GeoImprintSplineS](../../macro/geometry/GeoImprintSplineS)"
---
<!-- REVIEW FLAGS — requires human review
   [param_decorator_changed] Param 'dllPoints' @type changed from 'Nested List of Double' to 'List[Position]' in v5.1.0
     context: {"param":"dllPoints","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"Nested List of Double","toType":"List[Position]"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes.

## Syntax

```psj
Geometry.Edge.Spline(...)
```

## Inputs

### `dllPoints` @type(List\[Position]) @required

- The point on the given faces that the spline must pass through.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the spline edges are imprinted.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given face where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created_splines = Geometry.Edge.Spline(dllPoints=[[0.01, 0.003, 0.01],
                                                  [0.007, 0.003, 0.01],
                                                  [0.005, 0.004, 0.01], 
                                                  [0.004, 0.006, 0.01], 
                                                  [0.002, 0.007, 0.01], 
                                                  [0.0, 0.003, 0.01]],
                                       crlFaces=[Face(26)])
JPT.Debugger(created_splines)
```
