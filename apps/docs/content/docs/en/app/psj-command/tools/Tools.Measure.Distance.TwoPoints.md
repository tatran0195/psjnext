---
title: "Tools.Measure.Distance.TwoPoints()"
description: "measure distance 2 points"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > TwoPoints"
---

## Description

Measure distance 2 points

## Syntax

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```

## Inputs

### `posPoint1` @type(Position) @default(\[0,0,0])

- The point1.

### `posPoint2` @type(Position) @default(\[0,0,0])

- The point2.

### `strTarget` @type(String) @default("ALL")

- The target.

### `iPrecision` @type(Integer) @default(6)

- The precision.

### `crCoordinateSystem` @type(Cursor) @default(None)

- The coordinate system.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Measure.Distance.TwoPoints(posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```
