---
title: "Home.Windows.ViewControl.ZoomOut()"
description: "Zoom out the view by the zoom ratio"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > ViewControl > ZoomOut"
macro_link: ""
---

## Description

Zoom out the view by the zoom ratio.

## Syntax

```psj
Home.Windows.ViewControl.ZoomOut(...)
```

## Inputs

### `dZoom` @type(Double) @default(1.2)

- The zoom out ratio. The zoom ratio should be larger than 1.
- If the inputted value is in range (0:1), then the  zoom ratio = 1/(inputted value).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
Home.Windows.ViewControl.ZoomOut(dZoom=1.15)
```
