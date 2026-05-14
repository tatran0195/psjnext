---
title: "Home.RectangularCapture.Clipboard()"
description: "Capture specified area in Main Window to clipboard."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > RectangularCapture > Clipboard"
macro _link: "Capture _Rectangular()"
---

## Description

Capture specified area in Main Window to clipboard.

## Syntax

```psj
Home.RectangularCapture.Clipboard(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLeft`

- The pixel position of image left.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTop`

- The pixel position of image top.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iRight`

- The pixel position of image right.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBottom`

- The pixel position of image bottom.

## Return Code

A _Boolean_ specifying whether the function is successfully executed or not.

## Sample Code

```psj {3-7}
Geometry.Part.Cube()
JPT.ViewFitToModel
Home.RectangularCapture.Clipboard(
    iLeft=157, 
    iTop=175, 
    iRight=408, 
    iBottom=297)
```
