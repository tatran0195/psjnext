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

<!-- @since:5.1.0 @optional -->
### iLeft

- Specify pixel position of image left.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iTop

- Specify pixel position of image top.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iRight

- Specify pixel position of image right.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iBottom

- Specify pixel position of image bottom.
- The default value is 0.

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
