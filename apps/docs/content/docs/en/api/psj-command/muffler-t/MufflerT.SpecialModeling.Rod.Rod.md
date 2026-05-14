---
title: "MufflerT.SpecialModeling.Rod.Rod()"
description: "create rod"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MufflerT > SpecialModeling > Rod > Rod"
---

## Description

Create rod

## Syntax

```psj
MufflerT.SpecialModeling.Rod.Rod(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Double @required -->
### `dRadius`

- The radius.

<!-- @since:5.0.1 @type:Integer @required -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Double @required -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:Double @required -->
### `dStartDist`

- The start dist.

<!-- @since:5.0.1 @type:Double @required -->
### `dWeldDist`

- The weld dist.

<!-- @since:5.0.1 @type:Integer @required -->
### `iDivNumber`

- The divide number.

<!-- @since:5.0.1 @type:Double @required -->
### `dDeformWidth`

- The deformation width.

<!-- @since:5.0.1 @type:Integer @required -->
### `iTransitionElem`

- The transition element.

<!-- @since:5.0.1 @type:Double List @required -->
### `dlPosDir`

- The position direction.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerT.SpecialModeling.Rod.Rod(crlNodes, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
```
