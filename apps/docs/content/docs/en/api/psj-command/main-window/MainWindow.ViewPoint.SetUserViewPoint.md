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

<!-- @since:5.1.0 @type:String @required -->
### `strName`

- The name of ViewPoint.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bRotate`

- Whether to rotate the view.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bPan`

- Whether to pan the view.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bScale`

- Whether to scale the view.

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
