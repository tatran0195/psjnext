---
title: "MainWindow.RightClick.SelectAllParts()"
description: "Select all parts in the current document"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MainWindow > RightClick > SelectAllParts"
macro _link: "[ViewSelectAllParts](../../macro/main-window/ViewSelectAllParts)"
---

## Description

Select all parts in the current document

## Syntax

```psj
MainWindow.RightClick.SelectAllParts(...)
```

## Inputs

This function does not require any input value.

## Return Code

A _List of Cursor_ specifying the selected parts.

## Sample Code

```psj {9}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube _4", iPartColor=7697908)
JPT.Exec("View Fit To Model()")

# Select all parts
listParts = MainWindow.RightClick.SelectAllParts()
print(listParts)
```
