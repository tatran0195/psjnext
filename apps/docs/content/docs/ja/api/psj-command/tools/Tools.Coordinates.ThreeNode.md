---
title: "Tools.Coordinates.ThreeNode()"
description: "Create a Coordinate System by selecting 3 nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > ThreeNode"
---

## Description

Create a Coordinate System by selecting 3 nodes.

## Syntax

```psj
Tools.Coordinates.ThreeNode(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the Coordinate system.
- The default value is "CRect1".

<!-- @since:5.0.1 @optional -->
### iCoordType

- Specify the type of Coordinate system, which is one of the following:
  - If _iCoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - If _iCoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - If _iCoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOrder

- Specify the order of nodes or points when selecting the origin and axes of the Coordinate. This parameter can be one of the following:
  - If _iOrder=0_: O.Z.ZX Plane - Select in the order of Origin, a point on the Z-axis and a point on the ZX plane.
  - If _iOrder=1_: O.X.ZX Plane - Select in the order of Origin, a point on the X-axis and a point on the ZX plane.
  - If _iOrder=2_: O.Y.XY Plane - Select in the order of Origin, a point on the Y-axis and a point on the XY plane.
  - If _iOrder=3_: O.X.XY Plane - Select in the order of Origin, a point on the X-axis and a point on the XY plane.
  - If _iOrder=4_: O.Z.YZ Plane - Select in the order of Origin, a point on the Z-axis and a point on the YZ plane.
  - If _iOrder=5_: O.Y.YZ Plane - Select in the order of Origin, a point on the Y-axis and a point on the YZ plane.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the nodes to create the Coordinate.
- If the `veclPoints` is not defined, this argument will be a required input. If this parameter is not defined, `veclPoints` must be defined.

<!-- @since:5.0.1 @optional -->
### veclPoints

- Specify the points to create the Coordinate. This parameter can be used only when`crlNodes` is not defined, otherwise node selection will be prioritized.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crRefCoord

- Specify the coordinate reference system to create user Coordinate. The positions specified in`crlNodes` (or `veclPoints`) will be computed from this reference Coordinate.
- The default value is _None_ (Global Coordinate System).

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Coordinate. If this parameter is used, the specified Coordinate will be modified. If it is left _None_, a new Coordinate will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created _coord = Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                                           93, 
                                                           477)])

JPT.Debugger(created _coord)
```
