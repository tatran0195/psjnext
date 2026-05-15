---
title: "BoundaryConditions.LBCCopy.GroupCopyRotate()"
description: "Copy a group rotate"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > GroupCopyRotate"
---

## Description

Copy a group rotate.

## Syntax

```psj
BoundaryConditions.LBCCopy.GroupCopyRotate(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
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

- Specify the target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.GroupCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTargets=[])
```
