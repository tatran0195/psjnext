---
title: "BoundaryConditions.LBCCopy.LBCCopyTranslate()"
description: "Copy a LBC translate"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyTranslate"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Copy a LBC translate.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyTranslate(...)
```

## Inputs

### `iMethod` @type(Integer) @default(0)

- The method.
  0: COPY\_TRANS.
  1: COPY\_ROTATE.
  2: COPY\_MIRROR.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.
  0: MATCH NODE.
  1: MATCH FEATURE.

### `posVecTrans` @type(Position) @default(\[0,0,0])

- The vector trans.

### `dMagnitude` @type(Double) @default(1)

- The magnitude.

### `dTrandataDoffset` @type(Double) @default(0.0)

- The trandata offset.

### `dTol` @type(Double) @default(1)

- The tolerance.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTargets=[])
```
