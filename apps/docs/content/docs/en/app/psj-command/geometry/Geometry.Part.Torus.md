---
title: "Geometry.Part.Torus()"
description: "Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Torus"
macro_link: "[CreateTorus](../../macro/geometry/CreateTorus)"
---

## Description

Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Torus(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The X, Y, and Z coordinates of the origin point (The center of the torus).

### `dInnerRadius` @type(Double) @default(0.015)

- The radius of the inner circle of the torus in meter.

### `dRingRadius` @type(Double) @default(0.02)

- The radius of the ring of the torus in meter.

### `iCircumNodes` @type(Integer) @default(20)

- The number of nodes to be generated on the circumference of the ring of the torus.

### `iRingNodes` @type(Integer) @default(20)

- The number of nodes to be generated on the cross-section of the ring of the torus.

### `strName` @type(String) @default("Torus\_1")

- The name of the creating part.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the creating part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The torus is created successfully.
- _None_: The torus cannot be created.

## Sample Code

```psj {1}
torus = Geometry.Part.Torus(dlOrigin=[0.005, 0.005, 0.005], strName="Torus", iPartColor=7697908)
JPT.Debugger(torus)
```
