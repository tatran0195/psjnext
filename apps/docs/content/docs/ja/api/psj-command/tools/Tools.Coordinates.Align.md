---
title: "Tools.Coordinates.Align()"
description: "Create a Coordinate System by aligning an Axis direction of Coordinate System follow with an Edge or 2 selected Nodes (1D Element). Besides, it also be used to modify an existing Coordinate System"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > Align"
---

## Description

Create a Coordinate System by aligning an Axis direction of Coordinate System follow with an Edge or 2 selected Nodes (1D Element). Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.Align(...)
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

<!-- @since:5.0.1 @optional -->
### iCoordAxis

- Specify the Coordinate Axis to align with. This option can be one of the following:
  - If _iCoordAxis=0_: X axis - Referenced to the X-axis direction, the desired CS will have X axis follow selection direction
  - If _iCoordAxis=1_: Y axis - Referenced to the Y-axis direction, the desired CS will have Y axis follow selection direction
  - If _iCoordAxis=2_: Z axis - Referenced to the Z-axis direction, the desired CS will have Z axis follow selection direction
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bCreateNew

- Specify the option to create a new Coordinate or not. This argument uses follow with`crEdit`, when `crEdit` is defined, the argument `bCreateNew` uses to allow creating a new one based on the selected Coordinate System or just modified the selected Coordinate System.
  - If _True_: A new Coordinate will be created.
  - If _False_: The Coordinate specified in `crEdit` will be modified.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the nodes to determine alignment direction of the Coordinate. This parameter is used only when`crEdge` is _None_, otherwise edge option is prioritized.
- If `crEdge` is not defined, this argument will be a required input. If this argument is not defined, `crEdge` must be defined.

<!-- @since:5.0.1 @required -->
### crEdge

- Specify an edge to determine alignment direction of the Coordinate. If`crlNodes` is \[], this parameter must be defined by a specified edge.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Coordinate System to modify. If the`bCreateNew` is _False_, this specified Coordinate will be modified, while `bCreateNew` is _True_, a new Coordinate will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {6,7,8,9,10}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                           63, 
                                           87)])

created _coord = Tools.Coordinates.Align(strName="CRect2", 
                                        bCreateNew=False, 
                                        crlNodes=[Node(179, 
                                                       194)],
                                        crEdit=Coord(1))

JPT.Debugger(created _coord)
```
