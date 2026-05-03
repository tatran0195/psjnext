---
title: "MainWindow.RightClick.SelectDisplayed()"
description: "Select all targets of the same type as the specified target that are displayed in the current document"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > SelectDisplayed"
macro_link: "[ViewSelectDisplayed](../../macro/main-window/ViewSelectDisplayed)"
---

## Description

Select all targets of the same type as the specified target that are displayed in the current document.

## Syntax

```psj
MainWindow.RightClick.SelectDisplayed(...)
```

## Inputs

### `iTargetType` @type(Integer) @required

- The target type to be selected. The targets can only be faces or 2D elements.

## Return Code

A _List of Cursor_ specifying the selected faces or 2D elements.

## Sample Code

```psj {11}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Hide some faces
JPT.Exec("Show_Entity([6:52, 6:78], 0)")

# Select on displaying faces
displayFaces = MainWindow.RightClick.SelectDisplayed(iTargetType=3)
if displayFaces is None:
    print("There is no displaying faces")
elif len(displayFaces) == 1:
    print("1 displaying face was selected")
    print(displayFaces)
else:
    print(str(len(displayFaces)) + " displaying faces were selected")
    print(displayFaces)
```
