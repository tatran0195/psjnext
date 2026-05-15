---
title: "Tools.Coordinates.AttachNode()"
description: "Create a Coordinate System at the specific node. Besides, it also be used to modify an existing Coordinate System"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > Attach Node"
---

## Description

Create a Coordinate System at the specific node. Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.AttachNode(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the Coordinate.
- The default value is "CRect1".

<!-- @since:5.0.1 @optional -->
### iCoordType

- Specify the type of Coordinate system, which is one of the following:
  - If _iCoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - If _iCoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - If _iCoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively
- The default value is 0.

<!-- @since:5.0.1 @required -->
### crNode

- Specify the node at which the Coordinate is created.

<!-- @since:5.0.1 @optional -->
### bCreateNew

- Specify the option to create a new Coordinate or not. This argument uses follow with`crEdit`, when `crEdit` is defined, the argument `bCreateNew` uses to allow creating a new one based on selected Coordinate System or just modified the selected Coordinate System.
  - If _True_: A new Coordinate will be created.
  - If _False_: The Coordinate specified in `crEdit` will be modified.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Coordinate System to modify. If the`bCreateNew` is _False_, this specified Coordinate will be moved to the node specified in `crNode`, while `bCreateNew` is _True_, a new Coordinate will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {6,7,8}
Geometry.Part.Cylinder()
Tools.Coordinates.ThreeNode(veclPoints=[[0.01, 0.01, 0.01], 
                                        [0.002, 0.002, 0.002], 
                                        [0.01, 0.001, 0.01]])

created _coord = Tools.Coordinates.AttachNode(strName="CRect3", 
                                             crNode=Node(141), 
                                             crEdit=Coord(1))

JPT.Debugger(created _coord)
```
