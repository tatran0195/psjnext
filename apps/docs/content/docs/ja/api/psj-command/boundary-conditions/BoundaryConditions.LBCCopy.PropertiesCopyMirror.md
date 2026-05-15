---
title: "BoundaryConditions.LBCCopy.PropertiesCopyMirror()"
description: "Copy a property mirror"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > PropertiesCopyMirror"
---

## Description

Copy a property mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.PropertiesCopyMirror(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### poslPoints

- Specify the points.
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

- Specify the target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.PropertiesCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTargets=[])
```
