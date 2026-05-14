---
title: "BoundaryConditions.LBCCopy.GroupCopyRotate()"
description: "Copy a group rotate"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > GroupCopyRotate"
---

## Description

Copy a group rotate.

## Syntax

```psj
BoundaryConditions.LBCCopy.GroupCopyRotate(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method.

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

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.GroupCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTargets=[])
```
