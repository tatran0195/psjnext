---
title: "Geometry.Part.Cube()"
description: "Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry ➡ Part ➡ Cube"
macro _link: "[CreateCube](../../macro/geometry/CreateCube)"
---

## Description

Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cube(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlOrigin`

- The X-, Y-, and Z-coordinates of the origin point.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.01,0.01,0.01] -->
### `dlLength`

- The cube length in meters in the X-, Y-, Z-axis direction.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[10,10,10] -->
### `ilAxialNodes`

- The number of nodes along to each X-, Y-, Z-axis.

<!-- @since:5.0.1 @type:String @optional @default:"Cube _1" -->
### `strName`

- The name of the newly created part.

<!-- @since:5.0.1 @type:Integer @optional @default:7105764 -->
### `iPartColor`

- The color of the newly created part.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system.

## Return Code

A _Cursor_ of cube if success, or _None_ if fail.

## Sample Code

```psj {1,2,3} 
created _cube = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                                  strName="Cube _1", 
                                  iPartColor=13259210)
JPT.Debugger(created _cube)
```
