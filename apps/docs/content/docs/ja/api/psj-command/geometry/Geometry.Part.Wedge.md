---
title: "Geometry.Part.Wedge()"
description: "Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Wedge"
macro _link: "[CreateWedge](../../macro/geometry/CreateWedge)"
---

## Description

Create a wedge shaped body in a specific location. This relative location is computed to the specified local coordinate system.

## Syntax

```psj
Geometry.Part.Wedge(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dlOrigin

- Specify the X-, Y-, and Z-coordinates of f the center of the wedge.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dlLength

- Specify length in meters in the X-, Y-, Z-axis direction.
- The default value is \[0.01,0.01,0.01].

<!-- @since:5.0.1 @optional -->
### ilAxialNodes

- Specify the number of nodes along to each X-, Y-, Z-axis.
- The default value is \[10,10,10].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the newly created part.
- The default value is "Wedge\_1".

<!-- @since:5.0.1 @optional -->
### iPartColor

- Specify the color of the newly created part.
- The default value is 7105764.

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the new wedge body.

## Sample Code

```psj {1}
wedge = Geometry.Part.Wedge(dlOrigin=[0.005, 0.005, 0.005], strName="Wedge", iPartColor=6409934)

JPT.Debugger(wedge)
```
