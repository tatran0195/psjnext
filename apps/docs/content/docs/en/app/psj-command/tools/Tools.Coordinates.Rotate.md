---
title: "Tools.Coordinates.Rotate()"
description: "Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > Rotate"
macro_link: "[CreateCoordinateRotate](../../macro/tools/RotateCoordinate)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.Rotate(...)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name of the Coordinate.

### `iCoordType` @type(Integer) @default(0)

- The type of Coordinate system, which is one of the following:
  - I&#x66;_&#x69;CoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - I&#x66;_&#x69;CoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - I&#x66;_&#x69;CoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively

### `vecRotate` @type(Vector) @default(\[0.0,0.0,0.0])

- The rotation vector. Every component of this vector specified a degree to rotate the Coordinate about axis x, y, z, respectively. The unit of this argument is in degree (°).

### `bCreateNew` @type(Boolean) @default(True)

- The option to create a new Coordinate or not. This argument uses follow with`crEdit`, when`crEdit`is defined, the argument`bCreateNew`uses to allow creating a new one based on selected Coordinate System or just modified the selected Coordinate System.
  - I&#x66;_&#x54;rue_: A new Coordinate will be created.
  - I&#x66;_&#x46;alse_: The Coordinate specified in`crEdit`will be modified.

### `crRefCoord` @type(Cursor) @default(None (Global Coordinate))

- The coordinate reference system to rotate the Coordinate specified in`crEdit`. The angles specified in`vecRotate`will be computed from this reference Coordinate.

### `posCenterRot` @type(Position) @default(None) @since(5.1.0)

- The position of rotation center.

### `crEdit` @type(Cursor) @default(None)

- An existing Coordinate System to modify. If the`bCreateNew`i&#x73;_&#x46;alse_, this specified Coordinate will be modified, while`bCreateNew`i&#x73;_&#x54;rue_, a new Coordinate will be created.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {6,7,8,9,10}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                           63, 
                                           87)])

created_coord = Tools.Coordinates.Rotate(vecRotate=[59.9886811502157, 0.0, 0.0], 
                                         bCreateNew=False,
                                         crRefCoord=Coord(1),
                                         posCenterRot=None, 
                                         crEdit=Coord(1))

JPT.Debugger(created_coord)
```
