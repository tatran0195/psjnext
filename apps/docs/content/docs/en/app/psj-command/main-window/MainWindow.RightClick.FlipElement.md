---
title: "MainWindow.RightClick.FlipElement()"
description: "Flip normal of surface."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MainWindow > RightClick > FlipElement"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["flip element","Flip normal of surface."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Flip normal of surface (face or element).

## Syntax

```psj
MainWindow.RightClick.FlipElement(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-3}
Geometry.Part.Cube()
MainWindow.RightClick.FlipElement(crlTargets=[Face(21, 23, 26)])
MainWindow.RightClick.FlipElement(crlTargets=[Elem(1009, 1025, 968)])
```
