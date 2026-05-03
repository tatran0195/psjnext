---
title: "MidPlane.AdjustThickness()"
description: "Adjust thickness of midplane"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlane > AdjustThickness"
---

## Description

Adjust thickness of midplane

## Syntax

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `dRatio` @type(Double) @default(1.0)

- The ratio.

### `bAdjustFaceThick` @type(Boolean) @default(False)

- The adjust face thickness.

### `bAdjustPropThick` @type(Boolean) @default(False)

- The adjust property thickness.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.AdjustThickness(crlParts=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False)
```
