---
title: "MainWindow.RightClick.ShowHideAllToolbar()"
description: "Show/hide the toolbar on working document"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > ShowHideAllToolbar"
macro_link: "[ShowHideAllToolbar](../../macro/main-window/ShowHideAllToolbar)"
---

## Description

Show/hide the toolbar on working document.

## Syntax

```psj
MainWindow.RightClick.ShowHideAllToolbar(...)
```

## Inputs

### `iType` @type(Integer) @default(0)

- Toolbar type to be shown/hidden.
  - 0: View selection toolbar.
  - 1: Main window toolbar.

### `bShow` @type(Boolean) @default(True)

- Whether to show/hide the toolbar.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj
MainWindow.RightClick.ShowHideAllToolbar(bShow=True)
```
