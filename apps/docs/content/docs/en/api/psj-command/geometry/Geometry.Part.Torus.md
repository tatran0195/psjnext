---
title: "Geometry.Part.Torus()"
description: "Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Torus"
macro _link: "[CreateTorus](../../macro/geometry/CreateTorus)"
---

## Description

Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Torus(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlOrigin`

- The X, Y, and Z coordinates of the origin point (The center of the torus).

<!-- @since:5.0.1 @type:Double @optional @default:0.015 -->
### `dInnerRadius`

- The radius of the inner circle of the torus in meter.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dRingRadius`

- The radius of the ring of the torus in meter.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iCircumNodes`

- The number of nodes to be generated on the circumference of the ring of the torus.

<!-- @since:5.0.1 @type:Integer @optional @default:20 -->
### `iRingNodes`

- The number of nodes to be generated on the cross-section of the ring of the torus.

<!-- @since:5.0.1 @type:String @optional @default:"Torus _1" -->
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

- _Cursor_: The torus is created successfully.
- _None_: The torus cannot be created.

## Sample Code

```psj {1}
torus = Geometry.Part.Torus(dlOrigin=[0.005, 0.005, 0.005], strName="Torus", iPartColor=7697908)
JPT.Debugger(torus)
```
