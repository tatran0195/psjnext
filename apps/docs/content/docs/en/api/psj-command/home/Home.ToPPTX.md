---
title: "Home.ToPPTX()"
description: "Save the display window of Jupiter to an image file in pptx."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ToImage > 2D Image"
---

## Description

Save the display window of Jupiter to an image file in pptx.

## Syntax

```psj
Home.ToPPTX(...)
```

## Inputs

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bAutoCapture`

- The to specify whether crop image to the displayed entity range.

### `listAdjust`

- A list of _Integer_ specifying the left, top, right and bottom margins from the minimized area.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The display window of Jupiter is saved to an image file in pptx.
- _False_: The display window of Jupiter cannot be saved to an image file in pptx.

## Sample Code

```psj {9,10}
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

copy _paste = Home.ToPPTX()

JPT.Debugger(copy _paste)

export _status = Home.ToPPTX(bAutoCapture=True, 
                            listAdjust=[10,20,10,20])

JPT.Debugger(copy _paste)
```
