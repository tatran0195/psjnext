---
title: "Geometry.Part.Trapezoid()"
description: "Create a trapezoid body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Trapezoid"
macro _link: "[CreateTrapezoid](../../macro/geometry/CreateTrapezoid)"
---

## Description

Create a trapezoid body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Trapezoid(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlOrigin`

- The X, Y, and Z coordinates of the origin point (The center of the trapezoid).

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.01,0.01,0.01] -->
### `dlLength`

- The trapezoid length in the X, Y, Z direction in meter.

<!-- @since:5.0.1 @type:Double @optional @default:7.0 -->
### `dTopXLength`

- The length in the X-axis direction at top face.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dRadius`

- The radius in degrees of top face.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[10,10,10] -->
### `ilAxialNodes`

- The number of nodes in X-, Y-, Z-axis direction, respectively.

<!-- @since:5.0.1 @type:String @optional @default:"Trapezoid _1" -->
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

- _Cursor_: The trapezoid is created successfully.
- _None_: The trapezoid cannot be created.

## Sample Code

```psj {1,2,3}
trapezoid = Geometry.Part.Trapezoid(dlLength=[0.02, 0.01, 0.01],
                                    strName="Trapezoid _5",
                                    iPartColor=7961077)
JPT.Debugger(trapezoid)
```
