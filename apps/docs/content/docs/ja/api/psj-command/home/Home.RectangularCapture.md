---
title: "Home.RectangularCapture()"
description: "Save the specified range of Jupiter's display window to the clipboard"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > RectangularCapture"
---

## Description

Save the specified range of Jupiter's display window to the clipboard.

## Syntax

```psj
Home.RectangularCapture(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iLeft

- Specify the left position. This is the position of the starting point in horizontal axis of the`screen coordinate`. The `screen coordinate` is a coordinate whose origin is at the top left corner of the view window. Its horizontal axis expands rightward and the vertical axis expands downward.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTop

- Specify the top position. This is the position of the starting point in vertical axis of the`screen coordinate`.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRight

- Specify the right position. This is the position of the ending point in horizontal axis of the`screen coordinate`.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iBottom

- Specify the bottom position. This is the position of the ending point in vertical axis of the`screen coordinate`.
- The default value is 0.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The specified range of display window of Jupiter is saved to clipboard.
- _False_: The specified range of display window cannot be saved to clipboard.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

copy = Home.RectangularCapture(iLeft=477,
                               iTop=159,
                               iRight=900,
                               iBottom=562)

JPT.Debugger(copy)
```
