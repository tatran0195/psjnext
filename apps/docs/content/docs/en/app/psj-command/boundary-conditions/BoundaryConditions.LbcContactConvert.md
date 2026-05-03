---
title: "BoundaryConditions.LbcContactConvert()"
description: "BoundaryConditions LbcContactConvert"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LbcContactConvert"
---

## Description

BoundaryConditions LbcContactConvert

## Syntax

```psj
BoundaryConditions.LbcContactConvert(...)
```

## Inputs

### `iConvertTo` @type(Integer) @required

- The convert to.

### `iTieConvType` @type(Integer) @required

- The tie conv type.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LbcContactConvert(iConvertTo, iTieConvType, crlTargets)
```
