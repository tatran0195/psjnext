---
title: "Home.Windows.ViewControl.FitToModel()"
description: "Fit the entire model to the main window size"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > ViewControl > FitToModel"
macro_link: ""
---

## Description

Fit the entire model to the main window size.

## Syntax

```psj
Home.Windows.ViewControl.FitToModel(...)
```

## Inputs

This function does not contain any input values.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {2}
Geometry.Part.Cube()
Home.Windows.ViewControl.FitToModel()
```
