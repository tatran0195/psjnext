---
title: "Home.Windows.ViewControl.PanRight()"
description: "Move the view to the right by the entered amount of movement"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Windows > ViewControl > PanRight"
macro _link: ""
---

## Description

Move the view to the right by the entered amount of movement.

## Syntax

```psj
Home.Windows.ViewControl.PanRight(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### dDistance

- Specify the relative movement amounts on the screen that the view will move to the right.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.PanRight(dDistance=50)
```
