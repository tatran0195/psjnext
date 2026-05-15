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

<!-- @since:5.0.1 @optional -->
### dlXyz1

- Specify the xyz1.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### dlXyz2

- Specify the xyz2.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### strTarget

- Specify the target.
- The default value is "Angle".

<!-- @since:5.0.1 @optional -->
### iPrecision

- Specify the precision.
- The default value is 6.

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
