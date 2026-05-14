---
title: "MidPlane.AdjustThickness()"
description: "Adjust thickness of midplane"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlane > AdjustThickness"
---

## Description

Adjust thickness of midplane

## Syntax

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dRatio`

- The ratio.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAdjustFaceThick`

- The adjust face thickness.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAdjustPropThick`

- The adjust property thickness.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```
