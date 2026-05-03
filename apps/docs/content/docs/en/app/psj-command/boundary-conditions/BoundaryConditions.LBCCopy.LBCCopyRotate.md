---
title: "BoundaryConditions.LBCCopy.LBCCopyRotate()"
description: "Copy a LBC rotate"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyRotate"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Copy a LBC rotate.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyRotate(...)
```

## Inputs

### `iMethod` @type(Integer) @default(1)

- The method.
  0: COPY\_TRANS.
  1: COPY\_ROTATE.
  2: COPY\_MIRROR.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.
  0: MATCH NODE.
  1: MATCH FEATURE.

### `posAxis` @type(Position) @default(\[0,0,0])

- The axis.

### `posCenter` @type(Position) @default(\[0,0,0])

- The center.

### `dAngle` @type(Double) @default(0.0)

- The angle.

### `dTol` @type(Double) @default(1)

- The tolerance.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The targets.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTargets=[])
```
