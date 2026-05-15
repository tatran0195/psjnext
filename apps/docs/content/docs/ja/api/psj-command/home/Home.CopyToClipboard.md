---
title: "Home.CopyToClipboard()"
description: "Save the current display window of Jupiter to the clipboard"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > CopyToClipboard"
---

## Description

Save the current display window of Jupiter to the clipboard.

## Syntax

```psj
Home.CopyToClipboard(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### bWhiteBG

- Specify whether to set background color to white.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bTransparentBG

- Specify whether to set background color to transparent.
  This option can only takes effect when export image is .png extension. Also, it cannot be used when`bWhiteBG` is set to True.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bFixedSize

- Specify whether to make the size of export image fixed.
  If this parameter is True, the image will be exported with size specified in`iExportWidth` and `iExportHeight`.
  If this parameter is False, the size of the export image is the same as the size of the view window.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iWidth

- Specify the width of the export image.
- The default value is 1200.

<!-- @since:5.0.1 @optional -->
### iHeight

- Specify the height of the export image.
- The default value is 900.

### `bAutoCapture`

- A _Boolean_ to specify whether crop image to the displayed entity range.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### listAdjust

- Specify the left, top, right and bottom margins from the minimized area.
- The default value is \[0,0,0,0]

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The current display window of Jupiter is saved to clipboard.
- _False_: The current display window cannot be saved to clipboard.

## Sample Code

```psj {5-9,13-19}
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

copy = Home.CopyToClipboard(bWhiteBG=False,
                            bTransparentBG=False,
                            bFixedSize=False,
                            iWidth=1200,
                            iHeight=900)

JPT.Debugger(copy)

copy = Home.CopyToClipboard(bWhiteBG=False,
                            bTransparentBG=False,
                            bFixedSize=False,
                            iWidth=1200,
                            iHeight=900,
                            bAutoCapture=True, 
                            listAdjust=[10,20,10,20])

JPT.Debugger(copy)
```
