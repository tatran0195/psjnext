---
title: "BoundaryConditions.LBCCopy.LBCCopyRotate()"
description: "Copy a LBC rotate"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > LBCCopyRotate"
---

## Description

Copy a LBC rotate.

## Syntax

```psj
BoundaryConditions.LBCCopy.LBCCopyRotate(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
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
### `posAxis`

- The axis.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posCenter`

- The center.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAngle`

- The angle.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The targets.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.LBCCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTargets=[])
```
