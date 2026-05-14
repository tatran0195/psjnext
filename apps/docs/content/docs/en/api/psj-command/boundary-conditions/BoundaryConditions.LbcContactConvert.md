---
title: "BoundaryConditions.LbcContactConvert()"
description: "BoundaryConditions LbcContactConvert"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LbcContactConvert"
---

## Description

BoundaryConditions LbcContactConvert

## Syntax

```psj
BoundaryConditions.LbcContactConvert(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `iConvertTo`

- The convert to.

<!-- @since:5.0.1 @type:Integer @required -->
### `iTieConvType`

- The tie conv type.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LbcContactConvert(iConvertTo, iTieConvType, crlTargets)
```
