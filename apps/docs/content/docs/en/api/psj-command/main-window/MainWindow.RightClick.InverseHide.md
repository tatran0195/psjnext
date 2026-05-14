---
title: "MainWindow.RightClick.InverseHide()"
description: "Invert hide targets by context menu"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > InverseHide"
macro _link: "[ViewInverseHide](../../macro/main-window/ViewInverseHide)"
---

## Description

Invert hide targets by context menu

## Syntax

```psj
MainWindow.RightClick.InverseHide(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The targets to be inverted hide. The target can be Part or Face.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
JPT.ViewFitToModel()

# Invert hide Part(1)
target = MainWindow.RightClick.InverseHide(crlTargets=[Part(1)])
JPT.Debugger(target)
```
