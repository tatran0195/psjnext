---
title: "MainWindow.RightClick.ShowHideAllToolbar()"
description: "Show/hide the toolbar on working document"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > ShowHideAllToolbar"
macro _link: "[ShowHideAllToolbar](../../macro/main-window/ShowHideAllToolbar)"
---

## Description

Show/hide the toolbar on working document.

## Syntax

```psj
MainWindow.RightClick.ShowHideAllToolbar(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iType

- Specify toolbar type to be shown/hidden.
  - 0: View selection toolbar.
  - 1: Main window toolbar.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bShow

- Specify whether to show/hide the toolbar.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj
MainWindow.RightClick.ShowHideAllToolbar(bShow=True)
```
