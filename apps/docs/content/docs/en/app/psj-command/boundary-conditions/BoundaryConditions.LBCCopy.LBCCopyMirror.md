---
title: "BoundaryConditions.LBCCopy.LBCCopyMirror()"
description: "Copy a LBC mirror"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyMirror"
---

## Description

Copy a LBC mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyMirror(...)
```

## Inputs

### `iMethod` @type(Integer) @default(2)

- The method.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.
  0: MATCH NODE.
  1: MATCH FEATURE.

### `poslPoints` @type(Position List) @default(\[])

- Points on the mirror plane.

### `dOffset` @type(Double) @default(0)

- The offset.

### `dTol` @type(Double) @default(1)

- The tolerance.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target connections.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTargets=[])
```
