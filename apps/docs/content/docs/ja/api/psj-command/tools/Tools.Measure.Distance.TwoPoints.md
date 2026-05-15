---
title: "Tools.Measure.Distance.TwoPoints()"
description: "measure distance 2 points"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Distance > TwoPoints"
---

## Description

Measure distance 2 points

## Syntax

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### posPoint1

- Specify the point1.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### posPoint2

- Specify the point2.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### strTarget

- Specify the target.
- The default value is "ALL".

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

<!-- @since:5.0.1 @optional -->
### crCoordinateSystem

- Specify the coordinate system.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```
