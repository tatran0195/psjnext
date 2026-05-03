---
title: "Tools.Coordinates.ThreeNode()"
description: "Create a Coordinate System by selecting 3 nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > ThreeNode"
---

## Description

Create a Coordinate System by selecting 3 nodes.

## Syntax

```psj
Tools.Coordinates.ThreeNode(...)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name of the Coordinate system.

### `iCoordType` @type(Integer) @default(0)

- The type of Coordinate system, which is one of the following:
  - I&#x66;_&#x69;CoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - I&#x66;_&#x69;CoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - I&#x66;_&#x69;CoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively

### `iOrder` @type(Integer) @default(0)

- The order of nodes or points when selecting the origin and axes of the Coordinate. This parameter can be one of the following:
  - I&#x66;_&#x69;Order=0_: O.Z.ZX Plane - Select in the order of Origin, a point on the Z-axis and a point on the ZX plane.
  - I&#x66;_&#x69;Order=1_: O.X.ZX Plane - Select in the order of Origin, a point on the X-axis and a point on the ZX plane.
  - I&#x66;_&#x69;Order=2_: O.Y.XY Plane - Select in the order of Origin, a point on the Y-axis and a point on the XY plane.
  - I&#x66;_&#x69;Order=3_: O.X.XY Plane - Select in the order of Origin, a point on the X-axis and a point on the XY plane.
  - I&#x66;_&#x69;Order=4_: O.Z.YZ Plane - Select in the order of Origin, a point on the Z-axis and a point on the YZ plane.
  - I&#x66;_&#x69;Order=5_: O.Y.YZ Plane - Select in the order of Origin, a point on the Y-axis and a point on the YZ plane.

### `crlNodes` @type(List\[Cursor])

- The nodes to create the Coordinate.
- If the`veclPoints`is not defined, this argument will be a required input. If this parameter is not defined,`veclPoints`must be defined.

### `veclPoints` @type(List\[Vector]) @default(\[])

- The points to create the Coordinate. This parameter can be used only when`crlNodes`is not defined, otherwise node selection will be prioritized.

### `crRefCoord` @type(Cursor) @default(None (Global Coordinate System))

- The coordinate reference system to create user Coordinate. The positions specified in`crlNodes`(or`veclPoints`) will be computed from this reference Coordinate.

### `crEdit` @type(Cursor) @default(None)

- An existing Coordinate. If this parameter is used, the specified Coordinate will be modified. If it is lef&#x74;_&#x4E;one_, a new Coordinate will be created.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_coord = Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                                           93, 
                                                           477)])

JPT.Debugger(created_coord)
```
