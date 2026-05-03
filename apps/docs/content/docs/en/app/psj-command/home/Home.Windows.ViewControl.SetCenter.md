---
title: "Home.Windows.ViewControl.SetCenter()"
description: "Set the center of rotation of the model"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > ViewControl > SetCenter"
macro_link: ""
---

## Description

Set the center of rotation of the model.

## Syntax

```psj
Home.Windows.ViewControl.SetCenter(...)
```

## Inputs

### `dlCenter` @type(List\[Double]) @required

- The rotation center coordinate of the model. The unit of the rotation center coordinate  is taken according to the current document unit.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.SetCenter(dlCenter=[0.0, 0.01, 0.0])
```
