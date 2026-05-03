---
title: "Geometry.Part.Cube()"
description: "Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry ➡ Part ➡ Cube"
macro_link: "[CreateCube](../../macro/geometry/CreateCube)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a cuboid body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cube(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- Representing the X-, Y-, and Z-coordinates of the origin point.

### `dlLength` @type(List\[Double]) @default(\[0.01,0.01,0.01])

- The cube length in meters in the X-, Y-, Z-axis direction.

### `ilAxialNodes` @type(List\[Integer]) @default(\[10,10,10])

- The number of nodes along to each X-, Y-, Z-axis.

### `strName` @type(String) @default("Cube\_1")

- The name of the newly created part.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the newly created part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

A _Cursor_ of cube if success, or _None_ if fail.

## Sample Code

```psj {1,2,3} 
created_cube = Geometry.Part.Cube(dlOrigin=[0.005, 0.005, 0.005], 
                                  strName="Cube_1", 
                                  iPartColor=13259210)
JPT.Debugger(created_cube)
```
