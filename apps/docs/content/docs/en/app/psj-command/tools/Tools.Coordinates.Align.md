---
title: "Tools.Coordinates.Align()"
description: "Create a Coordinate System by aligning an Axis direction of Coordinate System follow with an Edge or 2 selected Nodes (1D Element). Besides, it also be used to modify an existing Coordinate System"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > Align"
---

## Description

Create a Coordinate System by aligning an Axis direction of Coordinate System follow with an Edge or 2 selected Nodes (1D Element). Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.Align(...)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name of the Coordinate.

### `iCoordType` @type(Integer) @default(0)

- The type of Coordinate system, which is one of the following:
  - I&#x66;_&#x69;CoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - I&#x66;_&#x69;CoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - I&#x66;_&#x69;CoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively

### `iCoordAxis` @type(Integer) @default(0)

- The Coordinate Axis to align with. This option can be one of the following:
  - I&#x66;_&#x69;CoordAxis=0_: X axis - Referenced to the X-axis direction, the desired CS will have X axis follow selection direction
  - I&#x66;_&#x69;CoordAxis=1_: Y axis - Referenced to the Y-axis direction, the desired CS will have Y axis follow selection direction
  - I&#x66;_&#x69;CoordAxis=2_: Z axis - Referenced to the Z-axis direction, the desired CS will have Z axis follow selection direction

### `bCreateNew` @type(Boolean) @default(True)

- The option to create a new Coordinate or not. This argument uses follow with`crEdit`, when`crEdit`is defined, the argument`bCreateNew`uses to allow creating a new one based on the selected Coordinate System or just modified the selected Coordinate System.
  - I&#x66;_&#x54;rue_: A new Coordinate will be created.
  - I&#x66;_&#x46;alse_: The Coordinate specified in`crEdit`will be modified.

### `crlNodes` @type(List\[Cursor])

- The nodes to determine alignment direction of the Coordinate. This parameter is used only when`crEdge`i&#x73;_&#x4E;one_, otherwise edge option is prioritized.
- If`crEdge`is not defined, this argument will be a required input. If this argument is not defined,`crEdge`must be defined.

### `crEdge` @type(Cursor) @required

- An edge to determine alignment direction of the Coordinate. If`crlNodes`is \[], this parameter must be defined by a specified edge.

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

created_coord = Tools.Coordinates.Align(strName="CRect2", 
                                        bCreateNew=False, 
                                        crlNodes=[Node(179, 
                                                       194)],
                                        crEdit=Coord(1))

JPT.Debugger(created_coord)
```
