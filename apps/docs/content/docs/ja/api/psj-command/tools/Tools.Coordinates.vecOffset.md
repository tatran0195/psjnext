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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "CRect1".

<!-- @since:5.0.1 @optional -->
### iCoordType

- Specify the coordinate type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### vTranslate

- Specify the translate.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### bCreateNew

- Specify the create new.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crRefCoord

- Specify the reference coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```
