---
title: "Geometry.Part.Cone()"
description: "Create a cone shaped body in a specific location. Its relative location is computed to the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Cone"
macro_link: "[CreateCone](../../macro/geometry/CreateCone)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a cone body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cone(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The X, Y, and Z coordinates of the origin point.

### `dBottomRadius` @type(Double) @default(0.01)

- The radius of the bottom face in meter.

### `dHeight` @type(Double) @default(0.02)

- The cone height in meter.

### `iCircularNodes` @type(Integer) @default(20)

- The number of nodes to be generated on the arc.

### `iAxialNodes` @type(Integer) @default(20)

- The number of nodes to be generated on the axial direction of the cylinder.

### `strName` @type(String) @default("Cone\_1")

- The name of the creating cone.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the newly created part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The cone is created successfully.
- _None_: The cone cannot be created.

## Sample Code

```psj {1}
cone = Geometry.Part.Cone(dlOrigin=[0.005, 0.005, 0.005], iPartColor=7829501)
JPT.Debugger(cone)
```
