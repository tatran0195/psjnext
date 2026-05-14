---
title: "Geometry.Part.Frustum()"
description: "Create a frustum body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > Part > Frustum"
macro _link: "[CreateCylinderFrustum](../../macro/geometry/CreateCylinderFrustum)"
---

## Description

Create a frustum body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Frustum(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Double] @optional @default:[0,0,0] -->
### `dlOrigin`

- The X, Y, and Z coordinates of the origin point (The center of the frustum).

<!-- @since:5.1.0 @type:Double @optional @default:0.005 -->
### `dTopRadius`

- The radius of the frustum in meter.

<!-- @since:5.1.0 @type:Double @optional @default:0.01 -->
### `dBottomRadius`

- The radius in meters of the bottom end of the frustum.

<!-- @since:5.1.0 @type:Double @optional @default:0.02 -->
### `dHeight`

- The height of the frustum..

<!-- @since:5.1.0 @type:Integer @optional @default:20 -->
### `iCircularNodes`

- The number of nodes to be generated on the circle at both ends.

<!-- @since:5.1.0 @type:Integer @optional @default:20 -->
### `iAxialNodes`

- The number of nodes in the axial direction of the cylinder.

<!-- @since:5.1.0 @type:String @optional @default:"Frustum _1" -->
### `strName`

- The name of the newly created part.

<!-- @since:5.1.0 @type:Integer @optional @default:7105764 -->
### `iPartColor`

- The color of the newly created part.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj
created _frustum = Geometry.Part.Frustum(dTopRadius=0.003, iPartColor=14903267)
JPT.Debugger(created _frustum)
```
