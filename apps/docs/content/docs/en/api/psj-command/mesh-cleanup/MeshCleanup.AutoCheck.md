---
title: "MeshCleanup.AutoCheck()"
description: "check meshing quality"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > AutoCheck"
---

## Description

Check meshing quality

## Syntax

```psj
MeshCleanup.AutoCheck(crlParts, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElems)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Integer @required -->
### `iElemType`

- The element type.

<!-- @since:5.0.1 @type:Boolean List @required -->
### `blCheckCondition`

- The check condition.

<!-- @since:5.0.1 @type:Boolean List @required -->
### `blElemQuality`

- The element quality.

<!-- @since:5.0.1 @type:Double List @required -->
### `dlLimitValue`

- The limit value.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.AutoCheck(crlParts, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElems)
```
