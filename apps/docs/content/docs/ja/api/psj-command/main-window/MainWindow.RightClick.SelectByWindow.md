---
title: "MainWindow.RightClick.SelectByWindow()"
description: "Select all targets of the same type as the specified one that is displaying the working window region"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > SelectByWindow"
macro _link: "[ViewSelectByWindow](../../macro/main-window/ViewSelectByWindow)"
---

## Description

Select all targets of the same type as the specified one that is displaying the working window region.

## Syntax

```psj
MainWindow.RightClick.SelectByWindow(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### iTargetType

- Specify the target type to be selected.

## Return Code

A _List of Cursor_ specifying the selected faces or 2D elements

## Sample Code

```psj {8}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
JPT.ViewFitToModel()

# Select on displaying faces  
displayFaces = MainWindow.RightClick.SelectByWindow(iTargetType=3)
if displayFaces is None:
    print("There is no face on current window")
elif len(displayFaces) == 1:
    print("1 displaying face was selected")
    print(displayFaces)
else:
    print(str(len(displayFaces)) + " displaying faces were selected")
    print(displayFaces)
```
