---
title: "Geometry.Part.Sphere()"
description: "Create a sphere body in a specific location. Its relative location is computed to the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Sphere"
macro_link: "[CreateSphere](../../macro/geometry/CreateSphere)"
---

## Description

Create a sphere body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Sphere(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0,0,0])

- Representing the X, Y, and Z coordinates of the origin point (The center of the sphere).

### `dRadius` @type(Double) @default(0.005)

- The radius of the sphere in meter.

### `iLatitudeDivisions` @type(Integer) @default(20)

- The number of nodes to be generated on the latitude direction.

### `iLongitudeDivisions` @type(Integer) @default(20)

- The number of nodes to be generated on the longitudinal direction.

### `strName` @type(String) @default("Sphere\_1")

- The name of the creating part.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the creating part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The sphere is created successfully.
- _None_: The sphere cannot be created.

## Sample Code

```psj {1}
sphere = Geometry.Part.Sphere(dlOrigin=[0.005, 0.0, 0.0], iPartColor=13259210)
JPT.Debugger(sphere)
```
