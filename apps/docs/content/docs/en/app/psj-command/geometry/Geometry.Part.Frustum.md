---
title: "Geometry.Part.Frustum()"
description: "Create a frustum body in a specific location. Its relative location is computed to the specified local coordinate system"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > Part > Frustum"
macro_link: "[CreateCylinderFrustum](../../macro/geometry/CreateCylinderFrustum)"
---

## Description

Create a frustum body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Frustum(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0,0,0])

- Representing the X, Y, and Z coordinates of the origin point (The center of the frustum).

### `dTopRadius` @type(Double) @default(0.005)

- The radius of the frustum in meter.

### `dBottomRadius` @type(Double) @default(0.01)

- The radius in meters of the bottom end of the frustum.

### `dHeight` @type(Double) @default(0.02)

- The height of the frustum..

### `iCircularNodes` @type(Integer) @default(20)

- The number of nodes to be generated on the circle at both ends.

### `iAxialNodes` @type(Integer) @default(20)

- The number of nodes in the axial direction of the cylinder.

### `strName` @type(String) @default("Frustum\_1")

- The name of the newly created part.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the newly created part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj
created_frustum = Geometry.Part.Frustum(dTopRadius=0.003, iPartColor=14903267)
JPT.Debugger(created_frustum)
```
