---
title: "MainWindow.RightClick.ShowHideFlip()"
description: "Toggle the display of hidden parts or faces on the current document"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > ShowHideFlip"
macro_link: "[ShowHideFlip](../../macro/main-window/ShowHideFlip)"
---

## Description

Toggle the display of hidden parts or faces on the current document.

## Syntax

```psj
MainWindow.RightClick.ShowHideFlip(...)
```

## Inputs

### `iType` @type(Integer) @default(0)

- The target type to toggle the displaying. The target is  Part or Face.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {9}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Show hide flip parts
flipPart = MainWindow.RightClick.ShowHideFlip(iType=0)
print(flipPart)
```
