---
title: "MainWindow.RightClick.ShowAll()"
description: "Show all hidden entities"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > ShowAll"
macro _link: "[ViewShowAll](../../macro/main-window/ViewShowAll)"
---

## Description

Show all hidden entities.

## Syntax

```psj
MainWindow.RightClick.ShowAll(...)
```

## Inputs

This function does not require any input value.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {11}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube _4", iPartColor=7697908)
JPT.ViewFitToModel()

# Hide some parts
JPT.Exec("Show _Entity([3:2, 3:3], 0)")
# Show all parts again
MainWindow.RightClick.ShowAll()
```
