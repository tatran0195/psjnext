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

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X-, Y-, and Z-coordinates of the origin point.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dlLength

- Specify the cube length in meters in the X-, Y-, Z-axis direction.
- The default value is \[0.01,0.01,0.01].

<!-- @since:5.0.1 @optional -->
### ilAxialNodes

- Specify the number of nodes along to each X-, Y-, Z-axis.
- The default value is \[10,10,10].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the newly created part.
- The default value is "Cube\_1".

<!-- @since:5.0.1 @optional -->
### iPartColor

- Specify the color of the newly created part.
- The default value is 7105764.

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system.
- The default value is _None_.

## Return Code

A _Cursor_ of cube if success, or _None_ if fail.

## Sample Code

```psj {1,2,3} 
created _cube = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                                  strName="Cube _1", 
                                  iPartColor=13259210)
JPT.Debugger(created _cube)
```
