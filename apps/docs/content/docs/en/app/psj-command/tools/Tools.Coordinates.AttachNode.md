---
title: "Tools.Coordinates.AttachNode()"
description: "Create a Coordinate System at the specific node. Besides, it also be used to modify an existing Coordinate System"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > Attach Node"
---

## Description

Create a Coordinate System at the specific node. Besides, it also be used to modify an existing Coordinate System.

## Syntax

```psj
Tools.Coordinates.AttachNode(...)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name of the Coordinate.

### `iCoordType` @type(Integer) @default(0)

- The type of Coordinate system, which is one of the following:
  - I&#x66;_&#x69;CoordType=0_: Rectangular Coordinate - which can be known as Cartesian Coordinate System (Oxyz)
  - I&#x66;_&#x69;CoordType=1_: Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively
  - I&#x66;_&#x69;CoordType=2_: Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively

### `crNode` @type(Cursor) @required

- The node at which the Coordinate is created.

### `bCreateNew` @type(Boolean) @default(True)

- The option to create a new Coordinate or not. This argument uses follow with`crEdit`, when`crEdit`is defined, the argument`bCreateNew`uses to allow creating a new one based on selected Coordinate System or just modified the selected Coordinate System.
  - I&#x66;_&#x54;rue_: A new Coordinate will be created.
  - I&#x66;_&#x46;alse_: The Coordinate specified in`crEdit`will be modified.

### `crEdit` @type(Cursor) @default(None)

- An existing Coordinate System to modify. If the`bCreateNew`i&#x73;_&#x46;alse_, this specified Coordinate will be moved to the node specified in`crNode`, while`bCreateNew`i&#x73;_&#x54;rue_, a new Coordinate will be created.

## Return Code

A _Cursor_ specifying the created Coordinate.

## Sample Code

```psj {6,7,8}
Geometry.Part.Cylinder()
Tools.Coordinates.ThreeNode(veclPoints=[[0.01, 0.01, 0.01], 
                                        [0.002, 0.002, 0.002], 
                                        [0.01, 0.001, 0.01]])

created_coord = Tools.Coordinates.AttachNode(strName="CRect3", 
                                             crNode=Node(141), 
                                             crEdit=Coord(1))

JPT.Debugger(created_coord)
```
