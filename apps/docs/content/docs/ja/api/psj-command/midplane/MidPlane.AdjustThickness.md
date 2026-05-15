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

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dRatio

- Specify the ratio.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### bAdjustFaceThick

- Specify the adjust face thickness.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bAdjustPropThick

- Specify the adjust property thickness.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```
