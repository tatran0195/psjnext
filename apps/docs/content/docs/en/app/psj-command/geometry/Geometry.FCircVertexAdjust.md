---
title: "Geometry.FCircVertexAdjust()"
description: "Align the vertexes positions on the circles. Cylinder faces can also be split by 90 degree, for creating mapped mesh"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > FCirc Vertex Adjust"
---

## Description

Align the vertexes positions on the circles. Cylinder faces can also be split by 90 degree, for creating mapped mesh.

## Syntax

```psj
Geometry.FCircVertexAdjust(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The parts whose vertices will be adjusted.

### `bFullCylinder` @type(Boolean) @default(False)

- Whether to divide the full cylinder faces by 90 degree or not. I&#x66;_&#x62;FullCylinder=True_, the cylindrical surfaces and torus surfaces in the selected parts will be divided into four locations at each 90 degree. This splitting makes it easier to create a mapped mesh.

### `bCylinderMoreThan90` @type(Boolean) @default(False)

- Whether to divide the cylinder faces more than 90 degree interior angle or not. The cylinder surfaces in the selected part with an internal angle of 90 degree or more will be divided at the 90 degree position i&#x66;_&#x62;CylinderMoreThan90=True_.

### `dMinRadius` @type(Double) @default(0.0)

- The minimum radius of the cylinder faces to be split. Faces with radius less than the input value are kept.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {7}
# Make a cylinder with 2 misaligned vertex
Geometry.Part.Cylinder()
Geometry.BreakEntity.Edge(crlNodes=[Node(66)])
Geometry.BreakEntity.Edge(crlNodes=[Node(51)])

# Align vertex positions on 2 circles of the cylinder
adjust_status = Geometry.FCircVertexAdjust(crlParts=[Part(1)])

JPT.Debugger(adjust_status)
```
