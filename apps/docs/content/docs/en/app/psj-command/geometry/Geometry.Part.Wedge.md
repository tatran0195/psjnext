---
title: "Geometry.Part.Wedge()"
description: "Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Wedge"
macro_link: "[CreateWedge](../../macro/geometry/CreateWedge)"
---

## Description

Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Wedge(...)
```

## Inputs

### `dlOrigin` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- Representing the X-, Y-, and Z-coordinates of f the center of the wedge.

### `dlLength` @type(List\[Double]) @default(\[0.01,0.01,0.01])

- Length in meters in the X-, Y-, Z-axis direction.

### `ilAxialNodes` @type(List\[Integer]) @default(\[10,10,10])

- The number of nodes along to each X-, Y-, Z-axis.

### `strName` @type(String) @default("Wedge\_1")

- The name of the newly created part.

### `iPartColor` @type(Integer) @default(7105764)

- The color of the newly created part.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system.

## Return Code

A _Cursor_ specifying the new wedge body.

## Sample Code

```psj {1}
wedge = Geometry.Part.Wedge(dlOrigin=[0.005, 0.005, 0.005], strName="Wedge", iPartColor=6409934)

JPT.Debugger(wedge)
```
