---
title: "Home.RectangularCapture.Clipboard()"
description: "Capture specified area in Main Window to clipboard."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > RectangularCapture > Clipboard"
macro_link: "Capture_Rectangular()"
---

## Description

Capture specified area in Main Window to clipboard.

## Syntax

```psj
Home.RectangularCapture.Clipboard(...)
```

## Inputs

### `iLeft` @type(Integer) @default(0)

- Pixel position of image left.

### `iTop` @type(Integer) @default(0)

- Pixel position of image top.

### `iRight` @type(Integer) @default(0)

- Pixel position of image right.

### `iBottom` @type(Integer) @default(0)

- Pixel position of image bottom.

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
