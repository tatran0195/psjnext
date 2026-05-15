---
title: "Geometry.Part.Cone()"
description: "Create a cone shaped body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Cone"
macro _link: "[CreateCone](../../macro/geometry/CreateCone)"
---

## Description

Create a cone body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cone(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X, Y, and Z coordinates of the origin point.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dBottomRadius

- Specify the radius of the bottom face in meter.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### dHeight

- Specify the cone height in meter.
- The default value is 0.02.

<!-- @since:5.0.1 @optional -->
### iCircularNodes

- Specify the number of nodes to be generated on the arc.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### iAxialNodes

- Specify the number of nodes to be generated on the axial direction of the cylinder.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the creating cone.
- The default value is "Cone\_1".

<!-- @since:5.0.1 @optional -->
### iPartColor

- Specify the color of the newly created part.
- The default value is 7105764.

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system.
- The default value is _None_.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The cone is created successfully.
- _None_: The cone cannot be created.

## Sample Code

```psj {1}
cone = Geometry.Part.Cone(dlOrigin=[0.005, 0.005, 0.005], iPartColor=7829501)
JPT.Debugger(cone)
```
