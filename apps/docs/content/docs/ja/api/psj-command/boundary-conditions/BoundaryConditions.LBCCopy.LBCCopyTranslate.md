---
title: "BoundaryConditions.LBCCopy.LBCCopyTranslate()"
description: "Copy a LBC translate"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyTranslate"
---

## Description

Copy a LBC translate.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyTranslate(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
  0: COPY\_TRANS.
  1: COPY\_ROTATE.
  2: COPY\_MIRROR.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
  0: MATCH NODE.
  1: MATCH FEATURE.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### posVecTrans

- Specify the vector trans.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dMagnitude

- Specify the magnitude.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dTrandataDoffset

- Specify the trandata offset.
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
BoundaryConditions.LBCCopy.LBCCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTargets=[])
```
