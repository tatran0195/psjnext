---
title: "BoundaryConditions.LBCCopy.LBCCopyMirror()"
description: "Copy a LBC mirror"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyMirror"
---

## Description

Copy a LBC mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyMirror(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
  0: MATCH NODE.
  1: MATCH FEATURE.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### poslPoints

- Specify points on the mirror plane.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target connections.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTargets=[])
```
