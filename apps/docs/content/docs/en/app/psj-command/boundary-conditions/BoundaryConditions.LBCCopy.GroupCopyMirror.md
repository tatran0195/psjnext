---
title: "BoundaryConditions.LBCCopy.GroupCopyMirror()"
description: "Copy a group mirror"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > GroupCopyMirror"
---

## Description

Copy a group mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.GroupCopyMirror(...)
```

## Inputs

### `iMethod` @type(Integer) @default(2)

- The mirror group copy method.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.
  - 0: Node method. This matching method matches the exact nodes of the target to get matching results. It is useful when the target features are different.
  - 1: Feature method. This matching method is very fast, especially for large models, and requires face-to-face, vertex to vertex like feature matching.

### `poslPoints` @type(Position List) @default(\[])

- The list of points that create the center line of mirror.

### `dOffset` @type(Double) @default(0.0)

- The offset value for mirror in unit of length.

### `dTol` @type(Double) @default(1.0)

- The tolerance value to be used for determination of conformity.
- Unit of length.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.LBCCopy.GroupCopyMirror(iMethod=2, iMatchMethod=0,
    poslPoints=[], dOffset=0.0, dTol=1.0, crlTargets=[])

print(result) #for checking return value
```
