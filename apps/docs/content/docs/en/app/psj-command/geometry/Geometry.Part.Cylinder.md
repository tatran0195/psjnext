---
title: "Geometry.Part.Cylinder()"
description: "Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Cylinder"
---

## Description

Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cylinder(...)
```

## Inputs

### `strName` @type(String) @default("Cylinder\_1")

- The name of the newly created part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

### `bHollow` @type(Boolean) @default(False)

- Weather to hollow the created cylinder or not.
  - I&#x66;_&#x54;rue_, the cylinder will have a hollow at the center with radius defined by`dTopInnerRadius`and`dBottomInnerRadius`.
  - I&#x66;_&#x46;alse_, the cylinder will not have a hollow at the center.

### `bTapered` @type(Boolean) @default(False)

- Weather to make the cylinder tapered (radius at two ends is different).
  - I&#x66;_&#x54;rue_, the cylinder will be tapered with radius defined by`dBottomOuterRadius`.
  - I&#x66;_&#x46;alse_, the cylinder will not be tapered.

### `dlOrigin` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- Representing the X-, Y-, and Z-coordinates of the center of the cylinder.

### `dTopInnerRadius` @type(Double) @default(0.001)

- The inner radius in meters of the top end of the cylinder.

### `dTopOuterRadius` @type(Double) @default(0.01)

- The outer radius in meters of the top end of the cylinder.

### `dBottomInnerRadius` @type(Double) @default(0.001)

- The inner radius in meters of the bottom end of the cylinder.

### `dBottomOuterRadius` @type(Double) @default(0.01)

- The outer radius in meters of the bottom end of the cylinder.

### `dHeight` @type(Double) @default(0.01)

- The height of the cylinder.

### `iCircularNodes` @type(Integer) @default(36)

- The number of nodes to be generated on the circle at both ends.

### `iAxialNodes` @type(Integer) @default(10)

- The number of nodes in the axial direction of the cylinder.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the newly created part.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {1,2,3}
created_cylinder = Geometry.Part.Cylinder(dlOrigin=[0.005, 0.005, 0.005],
                                          strName="Cylinder_2", 
                                          iPartColor=7463537)

JPT.Debugger(created_cylinder)
```
