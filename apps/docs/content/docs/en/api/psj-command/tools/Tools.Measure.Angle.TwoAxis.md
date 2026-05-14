---
title: "Tools.Measure.Angle.TwoAxis()"
description: "Measure the angle created by 2 Axis."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Measure > Angle > TwoAxis"
---

## Description

Measure the angle created by 2 Axis.

## Syntax

```psj
Tools.Measure.Angle.TwoAxis(...)
```

## Inputs

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlXyz1`

- The xyz1.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlXyz2`

- The xyz2.

<!-- @since:5.0.1 @type:String @optional @default:"Angle" -->
### `strTarget`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:6 -->
### `iPrecision`

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {5}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 8, 5)])
Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(3, 7, 2)])

angle = Tools.Measure.Angle.TwoAxis(dlXyz1=[0.0, -1.0, 0.0], dlXyz2=[1.0, 0.0, 0.0])

JPT.Debugger(angle)
```
