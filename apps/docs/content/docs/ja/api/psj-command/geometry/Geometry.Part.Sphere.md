---
title: "Geometry.Part.Sphere()"
description: "Create a sphere body in a specific location. Its relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Sphere"
macro _link: "[CreateSphere](../../macro/geometry/CreateSphere)"
---

## Description

Create a sphere body in a specific location.
Its relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Sphere(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X, Y, and Z coordinates of the origin point (The center of the sphere).
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dRadius

- Specify the radius of the sphere in meter.
- The default value is 0.005.

<!-- @since:5.0.1 @optional -->
### iLatitudeDivisions

- Specify the number of nodes to be generated on the latitude direction.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### iLongitudeDivisions

- Specify the number of nodes to be generated on the longitudinal direction.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the creating part.
- The default value is "Sphere\_1".

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

- _Cursor_: The sphere is created successfully.
- _None_: The sphere cannot be created.

## Sample Code

```psj {1}
sphere = Geometry.Part.Sphere(dlOrigin=[0.005, 0.0, 0.0], iPartColor=13259210)
JPT.Debugger(sphere)
```
