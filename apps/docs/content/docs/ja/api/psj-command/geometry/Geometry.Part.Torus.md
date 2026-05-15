---
title: "Geometry.Part.Torus()"
description: "Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Torus"
macro _link: "[CreateTorus](../../macro/geometry/CreateTorus)"
---

## Description

Create a donut body in a specific location. Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Torus(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X, Y, and Z coordinates of the origin point (The center of the torus).
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dInnerRadius

- Specify the radius of the inner circle of the torus in meter.
- The default value is 0.015.

<!-- @since:5.0.1 @optional -->
### dRingRadius

- Specify the radius of the ring of the torus in meter.
- The default value is 0.02.

<!-- @since:5.0.1 @optional -->
### iCircumNodes

- Specify the number of nodes to be generated on the circumference of the ring of the torus.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### iRingNodes

- Specify the number of nodes to be generated on the cross-section of the ring of the torus.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the creating part.
- The default value is "Torus\_1".

<!-- @since:5.0.1 @optional -->
### iPartColor

- Specify the color of the creating part.
- The default value is 7105764.

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system.
- The default value is _None_.

## Return Code

The return value depends on the status of the creating process:

- _Cursor_: The torus is created successfully.
- _None_: The torus cannot be created.

## Sample Code

```psj {1}
torus = Geometry.Part.Torus(dlOrigin=[0.005, 0.005, 0.005], strName="Torus", iPartColor=7697908)
JPT.Debugger(torus)
```
