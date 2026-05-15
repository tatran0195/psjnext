---
title: "JPT.DrawPoint()"
description: "Draw a point in Main Window"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Draw a point in Main Window.

## Syntax

```psj
JPT.DrawPoint()
```

## Inputs

<!-- @since:5.1.0 @optional -->
### listPosition

- Specify the coordinates of the the position of the point (e.g., \[x, y, z]).
  - The value is in SI units \[meters].

<!-- @since:5.1.0 @optional -->
### color

- Specify the arrow's color.
- The default color is cyan (RGB(0, 255, 255)).

### `width`

- A _Float_ (float): The width of the arrow's shaft in pixels. The default is 1.0.

## Return Code

- A _Boolean_ specifying Succeeded or Failed.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {6,9,12}
#Prepare a model for view
Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
JPT.ViewFitToModel()

# Draw a green point at position [10, 20, 30] with the default color and width:
JPT.DrawPoint([10, 20, 30])

# Draw a red point at position [5, 15, 25] with a width of 2.5:
JPT.DrawPoint([5, 15, 25], 255, 2.5)

# Draw a blue point at position [0, 0, 0] with a width of 1.5:
JPT.DrawPoint([0, 0, 0], 16711680, 1.5)
```
