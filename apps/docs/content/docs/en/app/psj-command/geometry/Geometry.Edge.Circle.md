---
title: "Geometry.Edge.Circle()"
description: "Imprint circular edges onto the specified face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Circle"
macro_link: "[ImprintCircleS](../../macro/geometry/ImprintCircleS)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Imprint circle lines onto face","Imprint circular edges onto the specified face"]}
   [param_rename_candidate] 'crlTargetFace' may be a rename of 'crlTargetsFace' (93% similar)
     context: {"from":"crlTargetsFace","to":"crlTargetFace","similarity":0.9285714285714286}
   [param_decorator_changed] Param 'veclPositions' @type changed from 'List[Vector]' to 'List[Position]' in v5.1.0
     context: {"param":"veclPositions","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"List[Vector]","toType":"List[Position]"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Imprint circular edges onto the specified face.

## Syntax

```psj
Geometry.Edge.Circle(...)
```

## Inputs

### `veclPositions` @type(List\[Position]) @required

- Points on faces where the circle will be imprinted.

### `crlTargetFace` @type(List\[Cursor]) @required @since(5.1.0)

- The target faces on which the edges are imprinted.

### `dInRadius` @type(Double) @default(1)

- Inner circle's radius. This argument is to be used when the value o&#x66;_&#x69;NoOfLaye&#x72;_&#x61;rgument is greater than 1. Possible values ar&#x65;_&#x30;.0_≤_dInRadius_≤_dOutRadius_. The unit is fixed to \[mm] unit.

### `dOutRadius` @type(Double) @default(4)

- Outer circle's radius. The unit is fixed to \[mm] unit.

### `iNoOfLayer` @type(Integer) @default(1)

- Number of layers to be imprinted from circle center.

### `iNoOfDiv` @type(Integer) @default(30)

- The number of segments in which the circle will be divided equally.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

### `crlTargetsFace` @type(List\[Cursor]) @required @deprecated @until(5.1.0)

- Faces to be imprinted.

## Return Code

A _List of Cursor_ specifying the created circle edges.

## Sample Code

```psj {3-6}
Geometry.Part.Cube()

circle_lines = Geometry.Edge.Circle(veclPositions=[[0.006666666666666666, 0.005555555555555556, 0.01], 
                                                [0.002222222222222222, 0.006666666666666666, 0.01]], 
                                                crlTargetFace=[Face(26)], 
                                                dOutRadius=2.0)
JPT.Debugger(circle_lines)
```
