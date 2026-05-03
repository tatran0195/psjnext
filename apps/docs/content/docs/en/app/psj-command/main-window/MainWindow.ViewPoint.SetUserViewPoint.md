---
title: "MainWindow.ViewPoint.SetUserViewPoint()"
description: "Set the user ViewPoint"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > ViewPoint > SetUserViewPoint"
macro_link: ""
---

## Description

Set the user ViewPoint

## Syntax

```psj
MainWindow.ViewPoint.SetUserViewPoint(...)
```

## Inputs

### `strName` @type(String) @required

- The name of ViewPoint.

### `bRotate` @type(Boolean) @default(True)

- Whether to rotate the view.

### `bPan` @type(Boolean) @default(True)

- Whether to pan the view.

### `bScale` @type(Boolean) @default(True)

- Whether to scale the view.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}}
JPT.Exec('ViewReset()')
JPT.Exec('ViewControl_Rotate([0, -60, 0])')
JPT.Exec('ViewControl_SetCenter([0.005, 0.005, 0.005])')
JPT.Exec('AddUserViewPoint("New View Point")')
JPT.Exec('ViewReset()')
MainWindow.ViewPoint.SetUserViewPoint(strName="New View Point")
```
