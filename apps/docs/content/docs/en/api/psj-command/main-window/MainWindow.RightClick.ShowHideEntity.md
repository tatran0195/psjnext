---
title: "MainWindow.RightClick.ShowHideEntity()"
description: "Show/hide the specified targets"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > ShowHideEntity"
macro _link: ""
---

## Description

Show/hide the specified targets.

## Syntax

```psj
MainWindow.RightClick.ShowHideEntity(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target to be shown/hidden.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bShow`

- Whether to show or hide the selected target.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {7,11}
# Prepare the model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)

# Hide faces
target = MainWindow.RightClick.ShowHideEntity(crlTargets=[Face(26, 52, 78)], bShow=False)
JPT.Debugger(target)

# Show Face(26) only
target = MainWindow.RightClick.ShowHideEntity(crlTargets=[Face(26)], bShow=True)
JPT.Debugger(target)
```
