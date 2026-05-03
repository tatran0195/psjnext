---
title: "Geometry.Edge.PlanarLine()"
description: "Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Planar Line"
macro_link: "[ImprintPlannarLineS](../../macro/geometry/ImprintPlannarLineS)"
---
<!-- REVIEW FLAGS — requires human review
   [param_decorator_changed] Param 'dllPoints' @type changed from 'List[Vector]' to 'List[Position]' in v5.1.0
     context: {"param":"dllPoints","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"List[Vector]","toType":"List[Position]"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane.

## Syntax

```psj
Geometry.Edge.PlanarLine(...)
```

## Inputs

### `dllPoints` @type(List\[Position]) @required

- The points which to define the planar face or the specific point that line passes through. Each point can be a Node, point on edge, or point on face. A valid value may one or three points on the list.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate.

### `iAxisPlane` @type(Integer) @default(0)

- The reference axis plane. Possible values are 0, 1, 2 corresponding to XY, XZ, and YZ Plane. This option will only affect the functionality when there is a point i&#x6E;_&#x64;llPoint&#x73;_&#x6F;nly.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

edges = Geometry.Edge.PlanarLine(dllPoints=[[0.01, 0.005, 0.006]], 
                                 crlFaces=[Face(24, 26)], 
                                 iAxisPlane=1)

JPT.Debugger(edges)
```
