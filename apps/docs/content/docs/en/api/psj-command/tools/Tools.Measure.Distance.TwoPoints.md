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

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posPoint1`

- The point1.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posPoint2`

- The point2.

<!-- @since:5.0.1 @type:String @optional @default:"ALL" -->
### `strTarget`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinateSystem`

- The coordinate system.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```
