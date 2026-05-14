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

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.
  0: COPY\_TRANS.
  1: COPY\_ROTATE.
  2: COPY\_MIRROR.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method.
  0: MATCH NODE.
  1: MATCH FEATURE.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posVecTrans`

- The vector trans.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dMagnitude`

- The magnitude.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTrandataDoffset`

- The trandata offset.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTargets=[])
```
