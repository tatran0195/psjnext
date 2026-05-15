---
title: "JPT.ConvertRGBToJPTColor()"
description: "Convert RGB (Red, Green, Blue) color code to color value in Jupiter"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert RGB (Red, Green, Blue) color code to color value in Jupiter.

## Syntax

```psj
JPT.ConvertRGBToJPTColor(redValue, greenValue, blueValue)
```

## Inputs

<!-- @since:5.0.1 @required -->
### redValue

- Specify the red color code.

<!-- @since:5.0.1 @required -->
### greenValue

- Specify the green color code.

<!-- @since:5.0.1 @required -->
### blueValue

- Specify the blue color code.

## Return Code

An _Integer_ specifying color code in Jupiter.

## Sample Code

```psj {2}
# Convert the RGB color code to the color code in Jupiter
newColor = JPT.ConvertRGBToJPTColor(255,100,213) # Pink color
JPT.Debugger(newColor)
```
