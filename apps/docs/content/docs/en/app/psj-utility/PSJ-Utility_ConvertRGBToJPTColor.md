---
title: "JPT.ConvertRGBToJPTColor()"
description: "Convert RGB (Red, Green, Blue) color code to color value in Jupiter"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert RGB (Red, Green, Blue) color code to color value in Jupiter.

## Syntax

```psj
JPT.ConvertRGBToJPTColor(redValue, greenValue, blueValue)
```

## Inputs

### `redValue` @type(Integer) @required

- The red color code.

### `greenValue` @type(Integer) @required

- The green color code.

### `blueValue` @type(Integer) @required

- The blue color code.

## Return Code

An _Integer_ specifying color code in Jupiter.

## Sample Code

```psj {2}
# Convert the RGB color code to the color code in Jupiter
newColor = JPT.ConvertRGBToJPTColor(255,100,213) # Pink color
JPT.Debugger(newColor)
```
