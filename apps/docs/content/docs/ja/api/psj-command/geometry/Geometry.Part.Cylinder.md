---
title: "Geometry.Part.Cylinder()"
description: "Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Cylinder"
---

## Description

Create a cylindrical body at a specific location. Its relative location is computed based on the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Cylinder(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the newly created part.
- The default value is "Cylinder\_1".

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bHollow

- Specify weather to hollow the created cylinder or not.
  - If _True_, the cylinder will have a hollow at the center with radius defined by `dTopInnerRadius` and `dBottomInnerRadius`.
  - If _False_, the cylinder will not have a hollow at the center.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bTapered

- Specify weather to make the cylinder tapered (radius at two ends is different).
  - If _True_, the cylinder will be tapered with radius defined by `dBottomOuterRadius`.
  - If _False_, the cylinder will not be tapered.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X-, Y-, and Z-coordinates of the center of the cylinder.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dTopInnerRadius

- Specify the inner radius in meters of the top end of the cylinder.
- The default value is 0.001.

<!-- @since:5.0.1 @optional -->
### dTopOuterRadius

- Specify the outer radius in meters of the top end of the cylinder.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### dBottomInnerRadius

- Specify the inner radius in meters of the bottom end of the cylinder.
- The default value is 0.001.

<!-- @since:5.0.1 @optional -->
### dBottomOuterRadius

- Specify the outer radius in meters of the bottom end of the cylinder.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### dHeight

- Specify the height of the cylinder.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### iCircularNodes

- Specify the number of nodes to be generated on the circle at both ends.
- The default value is 36.

<!-- @since:5.0.1 @optional -->
### iAxialNodes

- Specify the number of nodes in the axial direction of the cylinder.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### iPartColor

- Specify the color of the newly created part.
- The default value is 7105764.

## Return Code

A _Cursor_ specifying the created part.

## Sample Code

```psj {1,2,3}
created _cylinder = Geometry.Part.Cylinder(dlOrigin=[0.005, 0.005, 0.005],
                                          strName="Cylinder _2", 
                                          iPartColor=7463537)

JPT.Debugger(created _cylinder)
```
