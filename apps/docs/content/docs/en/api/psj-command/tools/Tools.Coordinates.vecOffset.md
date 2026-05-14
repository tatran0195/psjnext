---
title: "Tools.Coordinates.vecOffset()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > vecOffset"
---

## Description

Unknown Description

## Syntax

```psj
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"CRect1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoordType`

- The coordinate type.

<!-- @since:5.0.1 @type:V _TRANSLATE @optional @default:[0.0,0.0,0.0] -->
### `vTranslate`

- The translate.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bCreateNew`

- The create new.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRefCoord`

- The reference coordinate.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```
