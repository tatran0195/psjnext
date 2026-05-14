---
title: "JPT.DrawLine()"
description: "Draw a line in Main Window"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Draw a line in Main Window

## Syntax

```psj
JPT.DrawLine()
```

## Inputs

<!-- @since:5.1.0 @type:list @optional -->
### `listStartPoint`

- The coordinates of the the starting point of the line (e.g., \[x1, y1, z1]).
- The value is in SI units \[meters].

<!-- @since:5.1.0 @type:list @optional -->
### `listEndPoint`

- The coordinates of the the ending point of the line (e.g., \[x2, y2, z2]).
- The value is in SI units \[meters].

<!-- @since:5.1.0 @type:Int @optional -->
### `color`

- The in hexadecimal format representing the arrow's color.
- The default color is cyan (RGB(0, 255, 255)).

<!-- @since:5.1.0 @type:Int @optional -->
### `width`

- The width of the arrow's shaft in pixels.
- The default is 1.

## Return Code

- A _Boolean_ specifying Succeeded or Failed.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {6,9,12}
#Prepare a model for view
Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
JPT.ViewFitToModel()

# Draw a white line from [0, 0, 0] to [10, 20, 30] with the default color and width:
JPT.DrawLine([0, 0, 0], [10, 20, 30])

# Draw a red line from [5, 5, 5] to [15, 15, 15] with a width of 2.5:
JPT.DrawLine([5, 5, 5], [15, 15, 15], 255, 2.5)
        
# Draw a green line from [1, 1, 1] to [2, 2, 2] with a width of 1.5:
JPT.DrawLine([1, 1, 1], [2, 2, 2], 65280, 1.5)
```
