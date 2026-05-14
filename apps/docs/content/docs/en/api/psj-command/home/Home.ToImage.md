---
title: "Home.ToImage()"
description: "Save the display window of Jupiter to an image file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ToImage"
---

## Description

Save the display window of Jupiter to an image file.

## Syntax

```psj
Home.ToImage(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strImgPath`

- The path for exporting image.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bWhiteBG`

- Whether to set background color to white.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTransparentBG`

- Whether to set background color to transparent. This option can only takes effect when export image is .png extension. Also, it cannot be used when`bWhiteBG` is set to True.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFixedSize`

- Whether to make the size of export image fixed.
  - If this parameter is True, the image will be exported with size specified in `iExportWidth` and `iExportHeight`.
  - If this parameter is False, the size of the export image is the same as the size of the view window.

<!-- @since:5.0.1 @type:Integer @optional @default:1200 -->
### `iExportWidth`

- The width of the export image.

<!-- @since:5.0.1 @type:Integer @optional @default:900 -->
### `iExportHeight`

- The height of the export image.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bAutoCapture`

- The to specify whether crop image to the displayed entity range.

### `listAdjust`

- A list of _Integer_ specifying the left, top, right and bottom margins from the minimized area.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The display window of Jupiter is saved to an image file.
- _False_: The display window of Jupiter cannot be saved to an image file.

## Sample Code

```psj {8,9,13-16}
import re
from os import environ

Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

export _status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                          "/TechnoStar/Cube.png")

JPT.Debugger(export _status)

export _status = Home.ToImage(strImgPath = re.sub(re.escape("\\"), "/", environ["Temp"]) + \
                                          "/TechnoStar/Cube _minimize.png",
                            bAutoCapture=True, 
                            listAdjust=[10,20,10,20])

JPT.Debugger(export _status)
```
