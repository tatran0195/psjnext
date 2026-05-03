---
title: "Geometry.FindFeature.Fillet()"
description: "Find feature in part by typical description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > FindFeature > Fillet"
---

## Description

Find feature in part by typical description

## Syntax

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dMinAngle` @type(Double) @default(1.0)

- The minimum angle.

### `dMaxAngle` @type(Double) @default(10.0)

- The maximum angle.

### `dMinFaceWidth` @type(Double) @default(1.0)

- The minimum face width.

### `dMaxFaceWidth` @type(Double) @default(10.0)

- The maximum face width.

### `dMinCurveRadius` @type(Double) @default(0.0)

- The minimum curve radius.

### `dMaxCurveRadius` @type(Double) @default(171)

- The maximum curve radius.

### `dScale` @type(Double) @default(1.0)

- The scale.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```
