---
title: "Tools.Measure.Angle.TwoAxis()"
description: "Measure the angle created by 2 Axis."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Angle > TwoAxis"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure the angle created by 2 Axis.

## Syntax

```psj
Tools.Measure.Angle.TwoAxis(...)
```

## Inputs

### `dlXyz1` @type(Double List) @default(\[0, 0, 0])

- The xyz1.

### `dlXyz2` @type(Double List) @default(\[0, 0, 0])

- The xyz2.

### `strTarget` @type(String) @default("Angle")

- The target.

### `iPrecision` @type(Integer) @default(6)

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
