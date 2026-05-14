---
title: "JPT.DrawArrow()"
description: "Draw an arrow in Main Window"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Draw an arrow in Main Window.

## Syntax

```psj
JPT.DrawArrow()
```

## Inputs

<!-- @since:5.1.0 @type:List @optional -->
### `listStartPoint `

- Coordinates of the starting point of the arrow (e.g., \[x1, y1, z1]).
  - The value is in SI units \[meters].

<!-- @since:5.1.0 @type:List @optional -->
### `listEndPoint `

- Coordinates of the ending point of the arrow (e.g., \[x2, y2, z2]).
  - The value is in SI units \[meters].

<!-- @since:5.1.0 @type:Int @optional -->
### `color`

- The in hexadecimal format representing the arrow's color.
- The default color is cyan (RGB(0, 255, 255)).

<!-- @since:5.1.0 @type:Float @optional -->
### `width`

- The width of the arrow's shaft in pixels. The default is 1.0.

<!-- @since:5.1.0 @type:Bool @optional -->
### `bothSides`

- The drawing arrow direction.
  - _False_: the program will draw only one specified arrow.
  - _True_: the program will draw two arrows -  one pointing from the starting point to the endpoint and another pointing in the reverse direction.
- The default valueis _False_.

<!-- @since:5.1.0 @type:Bool @optional @default:True -->
### `threeDArrow`

- The arrow style.
  - _True_: the arrow will be drawn in 3D style.
  - _False_: it will be drawn as a flat arrow.

## Return Code

- A _Boolean_ specifying Succeeded or Failed.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {6,9,12,14}
#Prepare a model for view
Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
JPT.ViewFitToModel()

#Draw a cyan arrow from [0, 0, 0] to [10, 20, 30] with default width and style:
JPT.DrawArrow([0, 0, 0], [10, 20, 30])

#Draw a red arrow from [5, 5, 5] to [15, 15, 15] with width 2.5 pixels:
JPT.DrawArrow([5, 5, 5], [15, 15, 15], 255, 2.5)

#Draw a green arrow with arrows pointing in both directions:
JPT.DrawArrow([1, 1, 1], [4, 4, 4], 65280, 1.5, True)

#Draw a blue arrow in 2D style from [2, 2, 0] to [4, 4, 0] with default width:
JPT.DrawArrow([2, 2, 0], [4, 4, 0], 16711680, 1.0, False, False)
```
