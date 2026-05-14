---
title: "Tools.Coordinates.Rotate()"
description: "Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > Rotate"
macro _link: "[CreateCoordinateRotate](../../macro/tools/RotateCoordinate)"
---

## Description

Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.Rotate(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"CRect1" -->
### `strName`

- The name of the Coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoordType`

- The type of Coordinate system, which is one of the following:
  - If _iCoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - If _iCoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - If _iCoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively

<!-- @since:5.0.1 @type:Vector @optional @default:[0.0,0.0,0.0] -->
### `vecRotate`

- The rotation vector. Every component of this vector specified a degree to rotate the Coordinate about axis x, y, z, respectively. The unit of this argument is in degree (°).

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bCreateNew`

- The option to create a new Coordinate or not. This argument uses follow with`crEdit`, when `crEdit` is defined, the argument `bCreateNew` uses to allow creating a new one based on selected Coordinate System or just modified the selected Coordinate System.
  - If _True_: A new Coordinate will be created.
  - If _False_: The Coordinate specified in `crEdit` will be modified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None (Global Coordinate) -->
### `crRefCoord`

- The coordinate reference system to rotate the Coordinate specified in`crEdit`. The angles specified in `vecRotate` will be computed from this reference Coordinate.

<!-- @since:5.1.0 @type:Position @optional @default:None -->
### `posCenterRot`

- The position of rotation center.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Coordinate System to modify. If the`bCreateNew` is _False_, this specified Coordinate will be modified, while `bCreateNew` is _True_, a new Coordinate will be created.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {6,7,8,9,10}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                           63, 
                                           87)])

created _coord = Tools.Coordinates.Rotate(vecRotate=[59.9886811502157, 0.0, 0.0], 
                                         bCreateNew=False,
                                         crRefCoord=Coord(1),
                                         posCenterRot=None, 
                                         crEdit=Coord(1))

JPT.Debugger(created _coord)
```
