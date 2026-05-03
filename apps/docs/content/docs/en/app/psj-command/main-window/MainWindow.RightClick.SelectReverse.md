---
title: "MainWindow.RightClick.SelectReverse()"
description: "Reverse the selection on the displaying bodies."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > SelectReverse"
macro_link: "[ViewSelectReverse](../../macro/main-window/ViewSelectReverse)"
---

## Description

Reverse the selection on the displaying bodies.

## Syntax

```psj
MainWindow.RightClick.SelectReverse(...)
```

## Inputs

### `iTargetType` @type(Integer) @required

- The target type to select entities in reverse. The targets can only be faces or 2D elements.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The targets will reverse the selection.

## Return Code

A _List of Cursor_ specifying the selected entities in revert.

## Sample Code

```psj {8}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Revert selection from Face(26)
revertFaces = MainWindow.RightClick.SelectReverse(iTargetType=3, crlTargets=[Face(26)])
print(revertFaces)
```
