---
title: "Tools.Coordinates.vecOffset()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > vecOffset"
---

## Description

Unknown Description

## Syntax

```psj
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name.

### `iCoordType` @type(Integer) @default(0)

- The coordinate type.

### `vTranslate` @type(V\_TRANSLATE) @default(\[0.0,0.0,0.0])

- The translate.

### `bCreateNew` @type(Boolean) @default(True)

- The create new.

### `crRefCoord` @type(Cursor) @default(None)

- The reference coordinate.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```
