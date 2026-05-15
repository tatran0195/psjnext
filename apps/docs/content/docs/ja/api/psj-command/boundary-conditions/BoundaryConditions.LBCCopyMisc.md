---
title: "BoundaryConditions.LBCCopyMisc()"
description: "Copy the loads and boundary conditions set on one part to another part."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopyMisc"
---

## Description

Copy the loads and boundary conditions set on one part to another part.

## Syntax

```psj
BoundaryConditions.LBCCopyMisc(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlTransVec

- Specify the trans vector.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dTransMag

- Specify the trans mag.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTransOffset

- Specify the trans offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTransTol

- Specify the trans tolerance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crTranscrCoord

- Specify the transcr coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dlTransaxisVec

- Specify the transaxis vector.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dlTranscenterVec

- Specify the transcenter vector.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dRotateAngle

- Specify the rotate angle.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRotateTol

- Specify the rotate tolerance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crRotatecrCoord

- Specify the rotatecr coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### veclMirrorPoint

- Specify the mirror point.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMirrordOffset

- Specify the mirrord offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMirrorTol

- Specify the mirror tolerance.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTargets=[])
```
