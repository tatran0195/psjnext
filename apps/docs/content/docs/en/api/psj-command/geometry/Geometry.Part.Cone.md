---
title: "Geometry.Part.Cone()"
description: "Create a cone shaped body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Cone"
macro _link: "[CreateCone](../../macro/geometry/CreateCone)"
---

## Description

Create a cone body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cone(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlOrigin`

- The X, Y, and Z coordinates of the origin point.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dBottomRadius`

- The radius of the bottom face in meter.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dHeight`

- The cone height in meter.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iCircularNodes`

- The number of nodes to be generated on the arc.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iAxialNodes`

- The number of nodes to be generated on the axial direction of the cylinder.

<!-- @since:5.0.1 @type:String @optional @default:"Cone _1" -->
### `strName`

- The name of the creating cone.

<!-- @since:5.0.1 @type:Integer @optional @default:7105764 -->
### `iPartColor`

- The color of the newly created part.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The cone is created successfully.
- _None_: The cone cannot be created.

## Sample Code

```psj {1}
cone = Geometry.Part.Cone(dlOrigin=[0.005, 0.005, 0.005], iPartColor=7829501)
JPT.Debugger(cone)
```
