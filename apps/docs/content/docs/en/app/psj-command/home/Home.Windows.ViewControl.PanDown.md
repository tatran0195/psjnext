---
title: "Home.Windows.ViewControl.PanDown()"
description: "Move the view down by the entered amount of movement"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > ViewControl > PanDown"
macro_link: ""
---

## Description

Move the view down by the entered amount of movement.

## Syntax

```psj
Home.Windows.ViewControl.PanDown(...)
```

## Inputs

### `dDistance` @type(Double) @required

- The relative movement amounts on the screen that the view will move down.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.PanDown(dDistance=50)
```
