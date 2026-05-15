---
title: "Geometry.Part.Frustum()"
description: "Create a frustum body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > Part > Frustum"
macro _link: "[CreateCylinderFrustum](../../macro/geometry/CreateCylinderFrustum)"
---

## Description

Create a frustum body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Frustum(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### dlOrigin

- Specify the X, Y, and Z coordinates of the origin point (The center of the frustum).
- The default value is \[0,0,0].

<!-- @since:5.1.0 @optional -->
### dTopRadius

- Specify the radius of the frustum in meter.
- The default value is 0.005.

<!-- @since:5.1.0 @optional -->
### dBottomRadius

- Specify the radius in meters of the bottom end of the frustum.
- The default value is 0.01.

<!-- @since:5.1.0 @optional -->
### dHeight

- Specify the height of the frustum..
- The default value is 0.02.

<!-- @since:5.1.0 @optional -->
### iCircularNodes

- Specify the number of nodes to be generated on the circle at both ends.
- The default value is 20.

<!-- @since:5.1.0 @optional -->
### iAxialNodes

- Specify the number of nodes in the axial direction of the cylinder.
- The default value is 20.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of the newly created part.
- The default value is "Frustum\_1".

<!-- @since:5.1.0 @optional -->
### iPartColor

- Specify the color of the newly created part.
- The default value is 7105764.

<!-- @since:5.1.0 @optional -->
### crLocalCoordinate

- Specify the local coordinate system.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj
created _frustum = Geometry.Part.Frustum(dTopRadius=0.003, iPartColor=14903267)
JPT.Debugger(created _frustum)
```
