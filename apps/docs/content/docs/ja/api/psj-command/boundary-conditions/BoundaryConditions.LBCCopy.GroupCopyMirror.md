---
title: "BoundaryConditions.LBCCopy.GroupCopyMirror()"
description: "Copy a group mirror"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > GroupCopyMirror"
---

## Description

Copy a group mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.GroupCopyMirror(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the mirror group copy method.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iMatchMethod

- Specify the match method.
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### poslPoints

- Specify the list of points that create the center line of mirror.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset value for mirror in unit of length.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance value to be used for determination of conformity.
- Unit of length.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets.
- The default value is \[].

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.LBCCopy.GroupCopyMirror(iMethod=2, iMatchMethod=0,
    poslPoints=[], dOffset=0.0, dTol=1.0, crlTargets=[])

print(result) #for checking return value
```
