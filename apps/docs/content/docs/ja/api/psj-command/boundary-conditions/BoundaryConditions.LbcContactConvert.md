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

<!-- @since:5.0.1 @required -->
### iConvertTo

- Specify the convert to.

<!-- @since:5.0.1 @required -->
### iTieConvType

- Specify the tie conv type.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LbcContactConvert(iConvertTo, iTieConvType, crlTargets)
```
