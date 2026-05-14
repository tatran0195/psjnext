---
title: "MainWindow.RightClick.AssociatedPick()"
description: "pick associated entity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MainWindow > RightClick > AssociatedPick"
---

## Description

Pick associated entity

## Syntax

```psj
MainWindow.RightClick.AssociatedPick(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlInput`

- The input.

<!-- @since:5.0.1 @type:String @required -->
### `strTarget`

- The target.

<!-- @since:5.0.1 @type:String @optional @default:"UNKNOWN" -->
### `strConnect`

- The connect.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2}
Geometry.Part.Cube()
connectFace=MainWindow.RightClick.AssociatedPick(crlInput=[Node(1)], strTarget="Face")
JPT.Debugger(connectFace)
```
