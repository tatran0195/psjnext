---
title: "MainWindow.RightClick.SelectReverse()"
description: "Reverse the selection on the displaying bodies."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > SelectReverse"
macro _link: "[ViewSelectReverse](../../macro/main-window/ViewSelectReverse)"
---

## Description

Reverse the selection on the displaying bodies.

## Syntax

```psj
MainWindow.RightClick.SelectReverse(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### iTargetType

- Specify the target type to select entities in reverse. The targets can only be faces or 2D elements.

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the targets will reverse the selection.
- The default value is \[].

## Return Code

A _List of Cursor_ specifying the selected entities in revert.

## Sample Code

```psj {8}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
JPT.ViewFitToModel()

# Revert selection from Face(26)
revertFaces = MainWindow.RightClick.SelectReverse(iTargetType=3, crlTargets=[Face(26)])
print(revertFaces)
```
