---
title: "Home.Windows.ViewControl.PanLeft()"
description: "Move the view to the left by the entered amount of movement"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > ViewControl > PanLeft"
macro_link: ""
---

## Description

Move the view to the left by the entered amount of movement.

## Syntax

```psj
Home.Windows.ViewControl.PanLeft(...)
```

## Inputs

### `dDistance` @type(Double) @required

- The relative movement amounts on the screen that the view will move to the left.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.PanLeft(dDistance=50)
```
