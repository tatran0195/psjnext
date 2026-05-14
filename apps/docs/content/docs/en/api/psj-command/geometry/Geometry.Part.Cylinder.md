---
title: "Geometry.Part.Cylinder()"
description: "Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Cylinder"
---

## Description

Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cylinder(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Cylinder _1" -->
### `strName`

- The name of the newly created part.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bHollow`

- The weather to hollow the created cylinder or not.
  - If _True_, the cylinder will have a hollow at the center with radius defined by `dTopInnerRadius` and `dBottomInnerRadius`.
  - If _False_, the cylinder will not have a hollow at the center.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTapered`

- The weather to make the cylinder tapered (radius at two ends is different).
  - If _True_, the cylinder will be tapered with radius defined by `dBottomOuterRadius`.
  - If _False_, the cylinder will not be tapered.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlOrigin`

- The X-, Y-, and Z-coordinates of the center of the cylinder.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dTopInnerRadius`

- The inner radius in meters of the top end of the cylinder.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dTopOuterRadius`

- The outer radius in meters of the top end of the cylinder.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dBottomInnerRadius`

- The inner radius in meters of the bottom end of the cylinder.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dBottomOuterRadius`

- The outer radius in meters of the bottom end of the cylinder.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dHeight`

- The height of the cylinder.

<!-- @since:5.0.1 @type:Integer @optional @default:36 -->
### `iCircularNodes`

- The number of nodes to be generated on the circle at both ends.

<!-- @since:5.0.1 @type:Integer @optional @default:10 -->
### `iAxialNodes`

- The number of nodes in the axial direction of the cylinder.

<!-- @since:5.0.1 @type:Integer @optional @default:7105764 -->
### `iPartColor`

- The color of the newly created part.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {1,2,3}
created _cylinder = Geometry.Part.Cylinder(dlOrigin=[0.005, 0.005, 0.005],
                                          strName="Cylinder _2", 
                                          iPartColor=7463537)

JPT.Debugger(created _cylinder)
```
