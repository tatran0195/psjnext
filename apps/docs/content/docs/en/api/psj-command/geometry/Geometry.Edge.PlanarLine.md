---
title: "Geometry.Edge.PlanarLine()"
description: "Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Planar Line"
macro _link: "[ImprintPlannarLineS](../../macro/geometry/ImprintPlannarLineS)"
---

## Description

Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane.

## Syntax

```psj
Geometry.Edge.PlanarLine(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Vector] @required -->
<!-- @since:5.1.0 @type:List[Position] -->
### `dllPoints`

- The points which to define the planar face or the specific point that line passes through. Each point can be a Node, point on edge, or point on face. A valid value may one or three points on the list.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The target faces on which the edges are imprinted.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxisPlane`

- The reference axis plane. Possible values are 0, 1, 2 corresponding to XY, XZ, and YZ Plane. This option will only affect the functionality when there is a point in _dllPoints_ only.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bBreakFace`

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
