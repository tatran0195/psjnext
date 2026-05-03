---
title: "MainWindow.RightClick.ShowAllHiddenFaces()"
description: "Show all hidden faces of displaying bodies"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > ShowAllHiddenFaces"
macro_link: "[ViewShowAllHiddenFaces](../../macro/main-window/ViewShowAllHiddenFaces)"
---

## Description

Show all hidden faces of displaying bodies

## Syntax

```psj
MainWindow.RightClick.ShowAllHiddenFaces(...)
```

## Inputs

This function does not require any input value.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {12}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Hide some faces
JPT.Exec("Show_Entity([6:52, 6:78], 0)")

# Show all hidden faces
MainWindow.RightClick.ShowAllHiddenFaces()
```
