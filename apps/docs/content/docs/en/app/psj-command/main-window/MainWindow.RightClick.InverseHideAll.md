---
title: "MainWindow.RightClick.InverseHideAll()"
description: "Hide all targets other than the specified face. (Display only the specified faces)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > InverseHideAll"
macro_link: "[ViewInverseHideAll](../../macro/main-window/ViewInverseHideAll)"
---

## Description

Hide all targets other than the specified face.(Display only the specified faces)

## Syntax

```psj
MainWindow.RightClick.InverseHideAll(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target faces to display only.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Invert hide Part(1)
target = MainWindow.RightClick.InverseHideAll(crlTargets=[Face(26)])
JPT.Debugger(target)
```
