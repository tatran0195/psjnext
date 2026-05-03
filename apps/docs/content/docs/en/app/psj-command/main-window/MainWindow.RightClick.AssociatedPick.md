---
title: "MainWindow.RightClick.AssociatedPick()"
description: "pick associated entity"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MainWindow > RightClick > AssociatedPick"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Pick associated entity

## Syntax

```psj
MainWindow.RightClick.AssociatedPick(...)
```

## Inputs

### `crlInput` @type(List\[Cursor]) @required

- The input.

### `strTarget` @type(String) @required

- The target.

### `strConnect` @type(String) @default("UNKNOWN")

- The connect.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{2}
Geometry.Part.Cube()
connectFace=MainWindow.RightClick.AssociatedPick(crlInput=[Node(1)], strTarget="Face")
JPT.Debugger(connectFace)
```
