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

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iMethod`

- The mirror group copy method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method.
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.

<!-- @since:5.0.1 @type:Position List @optional @default:[] -->
### `poslPoints`

- The list of points that create the center line of mirror.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOffset`

- The offset value for mirror in unit of length.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTol`

- The tolerance value to be used for determination of conformity.
- Unit of length.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of targets.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.LBCCopy.GroupCopyMirror(iMethod=2, iMatchMethod=0,
    poslPoints=[], dOffset=0.0, dTol=1.0, crlTargets=[])

print(result) #for checking return value
```
