---
title: "Home.Windows.ViewControl.PanUp()"
description: "Move the view up by the entered amount of movement"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Windows > ViewControl > PanUp"
macro _link: ""
---

## Description

Move the view up by the entered amount of movement.

## Syntax

```psj
Home.Windows.ViewControl.PanUp(...)
```

## Inputs

<!-- @since:5.1.0 @type:Double @required -->
### `dDistance`

- The relative movement amounts on the screen that the view will move up.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.PanUp(dDistance=50)
```
