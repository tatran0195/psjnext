---
title: "BoundaryConditions.LBCCopy.PropertiesCopyMirror()"
description: "Copy a property mirror"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopy > PropertiesCopyMirror"
---

## Description

Copy a property mirror.

## Syntax

```psj
BoundaryConditions.LBCCopy.PropertiesCopyMirror(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method.

<!-- @since:5.0.1 @type:Position List @optional @default:[] -->
### `poslPoints`

- The points.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dOffset`

- The offset.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.PropertiesCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTargets=[])
```
