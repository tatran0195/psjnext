---
title: "Geometry.Part.Trapezoid()"
description: "Create a trapezoid body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Trapezoid"
macro _link: "[CreateTrapezoid](../../macro/geometry/CreateTrapezoid)"
---

## Description

Create a trapezoid body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Trapezoid(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X, Y, and Z coordinates of the origin point (The center of the trapezoid).
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dlLength

- Specify the trapezoid length in the X, Y, Z direction in meter.
- The default value is \[0.01,0.01,0.01].

<!-- @since:5.0.1 @optional -->
### dTopXLength

- Specify the length in the X-axis direction at top face.
- The default value is 7.0.

<!-- @since:5.0.1 @optional -->
### dRadius

- Specify the radius in degrees of top face.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilAxialNodes

- Specify the number of nodes in X-, Y-, Z-axis direction, respectively.
- The default value is \[10,10,10].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the creating part.
- The default value is "Trapezoid\_1".

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

- _Cursor_: The trapezoid is created successfully.
- _None_: The trapezoid cannot be created.

## Sample Code

```psj {1,2,3}
trapezoid = Geometry.Part.Trapezoid(dlLength=[0.02, 0.01, 0.01],
                                    strName="Trapezoid _5",
                                    iPartColor=7961077)
JPT.Debugger(trapezoid)
```
