---
title: "Home.Windows.ViewControl.Rotate()"
description: "Rotate the entire models around each axis by the entered angle"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Windows > ViewControl > Rotate"
macro _link: ""
---

## Description

Rotate the entire models around each axis by the entered angle.

## Syntax

```psj
Home.Windows.ViewControl.Rotate(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlAngle`

- The angle (degree) in each axis (X, Y, Z) to rotate the entire model.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.Rotate(dlAngle=[0, 20, 20])
```
