---
title: "Home.RectangularCapture.Single()"
description: "Create a frame for Single capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the \"To PPT\" and \"To Image\" command"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > RectangularCapture > Single"
macro_link: "[ViewMakeUserFrame](../../macro/home/ViewMakeUserFrame)"
---

## Description

Create a frame for Single capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command.

## Syntax

```psj
Home.RectangularCapture.Single(...)
```

## Inputs

### `strFrameName` @type(String) @required

- The name of frame to be captured.

### `iStartPointX` @type(Integer) @required

- The x-coordinate of the start point of the frame.

### `iStartPointY` @type(Integer) @required

- The x-coordinate of the start point of the frame.

### `iWidth` @type(Integer) @required

- The width of the frame size.

### `iHeight` @type(Integer) @required

- The height of the frame size.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)

# Create a single frame
Home.RectangularCapture.Single(strFrameName="New_Frame_1 (Single)", iStartPointX=459, iStartPointY=212, 
                                iWidth=460, iHeight=214)
Home.ToPPTX()
```
