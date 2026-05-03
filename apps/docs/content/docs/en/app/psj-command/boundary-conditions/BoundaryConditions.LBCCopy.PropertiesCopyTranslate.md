---
title: "BoundaryConditions.LBCCopy.PropertiesCopyTranslate()"
description: "Copy a property translate"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopy > PropertiesCopyTranslate"
---

## Description

Copy a property translate.

## Syntax

```psj
BoundaryConditions.LBCCopy.PropertiesCopyTranslate(...)
```

## Inputs

### `iMethod` @type(Integer) @default(0)

- The method.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.

### `posVecTrans` @type(Position) @default(\[0,0,0])

- The vector trans.

### `dMagnitude` @type(Double) @default(1)

- The magnitude.

### `dTrandataDoffset` @type(Double) @default(0.0)

- The trandata offset.

### `dTol` @type(Double) @default(1)

- The tolerance.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopy.PropertiesCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTargets=[])
```
