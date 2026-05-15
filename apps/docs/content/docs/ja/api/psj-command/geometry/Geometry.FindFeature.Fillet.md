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

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMinAngle

- Specify the minimum angle.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dMaxAngle

- Specify the maximum angle.
- The default value is 10.0.

<!-- @since:5.0.1 @optional -->
### dMinFaceWidth

- Specify the minimum face width.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dMaxFaceWidth

- Specify the maximum face width.
- The default value is 10.0.

<!-- @since:5.0.1 @optional -->
### dMinCurveRadius

- Specify the minimum curve radius.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxCurveRadius

- Specify the maximum curve radius.
- The default value is 171.

<!-- @since:5.0.1 @optional -->
### dScale

- Specify the scale.
- The default value is 1.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.FindFeature.Fillet(crlParts=[], crlFaces=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```
