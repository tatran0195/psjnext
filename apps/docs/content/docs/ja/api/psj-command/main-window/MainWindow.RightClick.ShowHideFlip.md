---
title: "MainWindow.RightClick.ShowHideFlip()"
description: "Toggle the display of hidden parts or faces on the current document"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > ShowHideFlip"
macro _link: "[ShowHideFlip](../../macro/main-window/ShowHideFlip)"
---

## Description

Toggle the display of hidden parts or faces on the current document.

## Syntax

```psj
MainWindow.RightClick.ShowHideFlip(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iType

- Specify the target type to toggle the displaying. The target is  Part or Face.
- The default value is 0.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {9}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube _4", iPartColor=7697908)
JPT.ViewFitToModel()

# Show hide flip parts
flipPart = MainWindow.RightClick.ShowHideFlip(iType=0)
print(flipPart)
```
