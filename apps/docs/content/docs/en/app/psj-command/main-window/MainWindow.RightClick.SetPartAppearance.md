---
title: "MainWindow.RightClick.SetPartAppearance()"
description: "Set the appearance of the selected parts"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > SetPartAppearance"
macro_link: "SetPartAppearance"
---

## Description

Set the appearance of the selected parts.

## Syntax

```psj
MainWindow.RightClick.SetPartAppearance(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- Specifying

### `strType` @type(String) @required

- Appearance target.
  - "Surface"
  - "Mesh"
  - "Edge"
  - "Node"

### `bShow` @type(Boolean) @default(True (Show))

- Show or Hide.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-13}
# Prepare model
JPT.Exec('ViewShowMesh(1)')
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)

MainWindow.RightClick.SetPartAppearance(crlParts=[Part(1)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(2)], strType="Edge", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(3)], strType="Mesh", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Node", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Mesh", bShow=False)

JPT.ViewFitToModel()
```
