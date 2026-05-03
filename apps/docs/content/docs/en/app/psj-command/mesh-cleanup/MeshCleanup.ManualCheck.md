---
title: "MeshCleanup.ManualCheck()"
description: "MeshCleanup ManualCheck"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > ManualCheck"
---

## Description

MeshCleanup ManualCheck

## Syntax

```psj
MeshCleanup.ManualCheck(crlParts=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElems=[])
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `iElemType` @type(Integer) @default(0)

- The element type.

### `iVeQuality` @type(Integer) @default(0)

- The ve quality.

### `iCheckCondition` @type(Integer) @default(0)

- The check condition.

### `dLimitValue` @type(Double) @default(0.0)

- The limit value.

### `dCFLValue` @type(Double) @default(0.0)

- The c l value.

### `iNonManifold` @type(Integer) @default(0)

- The non manifold.

### `iCleanupMode` @type(Integer) @default(0)

- The cleanup mode.

### `crlElems` @type(List\[Cursor]) @default(\[])

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ManualCheck(crlParts=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElems=[])
```
