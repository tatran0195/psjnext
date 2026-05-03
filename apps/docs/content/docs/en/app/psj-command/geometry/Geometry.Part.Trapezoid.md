---
title: "Geometry.Part.Trapezoid()"
description: "Create a trapezoid body in a specific location. Its relative location is computed to the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Trapezoid"
macro_link: "[CreateTrapezoid](../../macro/geometry/CreateTrapezoid)"
---

## Description

Create a trapezoid body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Trapezoid(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The X, Y, and Z coordinates of the origin point (The center of the trapezoid).

### `dlLength` @type(List\[Double]) @default(\[0.01,0.01,0.01])

- The trapezoid length in the X, Y, Z direction in meter.

### `dTopXLength` @type(Double) @default(7.0)

- The length in the X-axis direction at top face.

### `dRadius` @type(Double) @default(0)

- The radius in degrees of top face.

### `ilAxialNodes` @type(List\[Integer]) @default(\[10,10,10])

- The number of nodes in X-, Y-, Z-axis direction, respectively.

### `strName` @type(String) @default("Trapezoid\_1")

- The name of the creating part.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the creating part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The trapezoid is created successfully.
- _None_: The trapezoid cannot be created.

## Sample Code

```psj {1,2,3}
trapezoid = Geometry.Part.Trapezoid(dlLength=[0.02, 0.01, 0.01],
                                    strName="Trapezoid_5",
                                    iPartColor=7961077)
JPT.Debugger(trapezoid)
```
