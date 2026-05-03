---
title: "Home.Windows.ViewControl.ZoomIn()"
description: "Zoom in the view by the zoom ratio"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > ViewControl > ZoomIn"
macro_link: ""
---

## Description

Zoom in the view by the zoom ratio.

## Syntax

```psj
Home.Windows.ViewControl.ZoomIn(...)
```

## Inputs

### `dZoom` @type(Double) @default(0.83333333)

- The zoom in ratio. The zoom ratio should be in range (0:1).
- If the inputted larger than 1, then the  zoom ratio = 1/(inputted value).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.ZoomIn(dZoom=0.3)
```
