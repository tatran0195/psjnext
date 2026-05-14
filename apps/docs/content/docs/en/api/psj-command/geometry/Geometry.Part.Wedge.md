---
title: "Geometry.Part.Wedge()"
description: "Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Wedge"
macro _link: "[CreateWedge](../../macro/geometry/CreateWedge)"
---

## Description

Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Wedge(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlOrigin`

- The X-, Y-, and Z-coordinates of f the center of the wedge.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.01,0.01,0.01] -->
### `dlLength`

- The length in meters in the X-, Y-, Z-axis direction.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[10,10,10] -->
### `ilAxialNodes`

- The number of nodes along to each X-, Y-, Z-axis.

<!-- @since:5.0.1 @type:String @optional @default:"Wedge _1" -->
### `strName`

- The name of the newly created part.

<!-- @since:5.0.1 @type:Integer @optional @default:7105764 -->
### `iPartColor`

- The color of the newly created part.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system.

## Return Code

A _Cursor_ specifying the new wedge body.

## Sample Code

```psj {1}
wedge = Geometry.Part.Wedge(dlOrigin=[0.005, 0.005, 0.005], strName="Wedge", iPartColor=6409934)

JPT.Debugger(wedge)
```
