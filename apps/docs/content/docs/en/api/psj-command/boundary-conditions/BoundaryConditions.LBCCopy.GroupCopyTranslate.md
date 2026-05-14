---
title: "BoundaryConditions.LBCCopy.GroupCopyTranslate()"
description: "Copy a group translate"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > GroupCopyTranslate"
---

## Description

Copy a group translate.

## Syntax

```psj
BoundaryConditions.LBCCopy.GroupCopyTranslate(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method.

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
BoundaryConditions.LBCCopy.GroupCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTargets=[])
```
