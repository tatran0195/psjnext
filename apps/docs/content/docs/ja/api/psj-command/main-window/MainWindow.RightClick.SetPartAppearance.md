---
title: "MainWindow.RightClick.SetPartAppearance()"
description: "Set the appearance of the selected parts"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > SetPartAppearance"
macro _link: "SetPartAppearance"
---

## Description

Set the appearance of the selected parts.

## Syntax

```psj
MainWindow.RightClick.SetPartAppearance(...)
```

## Inputs

### `crlParts`

- A _List of Cursor_ specifying

<!-- @since:5.1.0 @required -->
### strType

- Specify appearance target.
  - "Surface"
  - "Mesh"
  - "Edge"
  - "Node"

<!-- @since:5.1.0 @optional -->
### bShow

- Specify Show or Hide.
- The default value is _True_ (Show).

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-13}
# Prepare model
JPT.Exec('ViewShowMesh(1)')
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube _4", iPartColor=7697908)

MainWindow.RightClick.SetPartAppearance(crlParts=[Part(1)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(2)], strType="Edge", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(3)], strType="Mesh", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Node", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Mesh", bShow=False)

JPT.ViewFitToModel()
```
