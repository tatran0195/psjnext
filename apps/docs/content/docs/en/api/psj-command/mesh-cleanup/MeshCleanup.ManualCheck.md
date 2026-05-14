---
title: "MeshCleanup.ManualCheck()"
description: "MeshCleanup ManualCheck"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > ManualCheck"
---

## Description

MeshCleanup ManualCheck

## Syntax

```psj
MeshCleanup.ManualCheck(crlParts=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElems=[])
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iElemType`

- The element type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iVeQuality`

- The ve quality.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCheckCondition`

- The check condition.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dLimitValue`

- The limit value.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dCFLValue`

- The c l value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNonManifold`

- The non manifold.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCleanupMode`

- The cleanup mode.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElems`

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ManualCheck(crlParts=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElems=[])
```
