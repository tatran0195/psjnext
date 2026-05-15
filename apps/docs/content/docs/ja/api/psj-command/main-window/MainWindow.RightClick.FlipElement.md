---
title: "MainWindow.RightClick.FlipElement()"
description: "Flip normal of surface."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MainWindow > RightClick > FlipElement"
---

## Description

Flip normal of surface (face or element).

## Syntax

```psj
MainWindow.RightClick.FlipElement(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-3}
Geometry.Part.Cube()
MainWindow.RightClick.FlipElement(crlTargets=[Face(21, 23, 26)])
MainWindow.RightClick.FlipElement(crlTargets=[Elem(1009, 1025, 968)])
```
