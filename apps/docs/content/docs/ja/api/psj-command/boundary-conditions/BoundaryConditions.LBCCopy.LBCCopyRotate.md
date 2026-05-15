---
title: "BoundaryConditions.LBCCopy.LBCCopyRotate()"
description: "Copy a LBC rotate"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyRotate"
---

## Description

Copy a LBC rotate.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyRotate(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
  0: COPY\_TRANS.
  1: COPY\_ROTATE.
  2: COPY\_MIRROR.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
  0: MATCH NODE.
  1: MATCH FEATURE.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### posAxis

- Specify the axis.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### posCenter

- Specify the center.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dAngle

- Specify the angle.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the targets.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTargets=[])
```
