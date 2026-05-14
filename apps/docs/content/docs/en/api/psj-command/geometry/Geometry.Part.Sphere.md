---
title: "Geometry.Part.Sphere()"
description: "Create a sphere body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Sphere"
macro _link: "[CreateSphere](../../macro/geometry/CreateSphere)"
---

## Description

Create a sphere body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Sphere(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0,0,0] -->
### `dlOrigin`

- The X, Y, and Z coordinates of the origin point (The center of the sphere).

<!-- @since:5.0.1 @type:Double @optional @default:0.005 -->
### `dRadius`

- The radius of the sphere in meter.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iLatitudeDivisions`

- The number of nodes to be generated on the latitude direction.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iLongitudeDivisions`

- The number of nodes to be generated on the longitudinal direction.

<!-- @since:5.0.1 @type:String @optional @default:"Sphere _1" -->
### `strName`

- The name of the creating part.

<!-- @since:5.0.1 @type:Integer @optional @default:7105764 -->
### `iPartColor`

- The color of the creating part.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The sphere is created successfully.
- _None_: The sphere cannot be created.

## Sample Code

```psj {1}
sphere = Geometry.Part.Sphere(dlOrigin=[0.005, 0.0, 0.0], iPartColor=13259210)
JPT.Debugger(sphere)
```
