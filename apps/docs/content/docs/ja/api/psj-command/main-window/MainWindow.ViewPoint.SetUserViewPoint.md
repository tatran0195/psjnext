---
title: "MainWindow.ViewPoint.SetUserViewPoint()"
description: "Set the user ViewPoint"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > ViewPoint > SetUserViewPoint"
macro _link: ""
---

## Description

Set the user ViewPoint

## Syntax

```psj
MainWindow.ViewPoint.SetUserViewPoint(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strName

- Specify the name of ViewPoint.

<!-- @since:5.1.0 @optional -->
### bRotate

- Specify whether to rotate the view.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bPan

- Specify whether to pan the view.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bScale

- Specify whether to scale the view.
- The default value is _True_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}}
JPT.Exec('ViewReset()')
JPT.Exec('ViewControl _Rotate([0, -60, 0])')
JPT.Exec('ViewControl _SetCenter([0.005, 0.005, 0.005])')
JPT.Exec('AddUserViewPoint("New View Point")')
JPT.Exec('ViewReset()')
MainWindow.ViewPoint.SetUserViewPoint(strName="New View Point")
```
