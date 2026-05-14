---
title: "Geometry.FindFeature.Fillet()"
description: "Find feature in part by typical description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > FindFeature > Fillet"
---

## Description

Find feature in part by typical description

## Syntax

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMinAngle`

- The minimum angle.

<!-- @since:5.0.1 @type:Double @optional @default:10.0 -->
### `dMaxAngle`

- The maximum angle.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMinFaceWidth`

- The minimum face width.

<!-- @since:5.0.1 @type:Double @optional @default:10.0 -->
### `dMaxFaceWidth`

- The maximum face width.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinCurveRadius`

- The minimum curve radius.

<!-- @since:5.0.1 @type:Double @optional @default:171 -->
### `dMaxCurveRadius`

- The maximum curve radius.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dScale`

- The scale.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```
