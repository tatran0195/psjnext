---
title: "JPT.ConvertJPTColorToRGB()"
description: "Convert color value in Jupiter to a string specifying RGB (Red, Green, Blue) code"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert color value in Jupiter to a _String_ specifying RGB (Red, Green, Blue) code.

## Syntax

```psj
JPT.ConvertJPTColorToRGB(colorValue)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `colorValue`

- The color value in Jupiter.

## Return Code

A _String_ specifying the converted RGB code with value = RGB(redCode,greenCode,blueCode)

## Sample Code

```psj {2}
# Convert the color code = 255 in Jupiter to RGB color code
stringRGB = JPT.ConvertJPTColorToRGB(255) # Return RGB(255,0,0)
# Split the RGB code and store it as Red Green Blue color code
r, g, b = stringRGB[4:-1].strip().split(",") # String = RGB(255,0,0) -> List = [255, 0, 0]
print(f"Output value of this function: {stringRGB}")
print(f"It means: Red = {r} | Green = {g} | Blue = {b}")
```
