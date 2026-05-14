---
title: "MainWindow.RightClick.SelectAll()"
description: "Select all faces or shell elements according to the specified target type"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > SelectAll"
macro _link: "[ViewSelectAll](../../macro/main-window/ViewSelectAll)"
---

## Description

Select all faces or shell elements according to the specified target type.

## Syntax

```psj
MainWindow.RightClick.SelectAll(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @required -->
### `iTargetType`

- The target type to be selected. The target can be face or 2D element only.

## Return Code

A _List of Cursor_ specifying the selected targets.

## Sample Code

```psj {7,11}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
JPT.ViewFitToModel()

# Select all faces
listFaces = MainWindow.RightClick.SelectAll(iTargetType=3)
print(listFaces)

# Select all 2D elements
listElems= MainWindow.RightClick.SelectAll(iTargetType=7)
print(listElems)
```
