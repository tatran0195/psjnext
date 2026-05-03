---
title: "Geometry.Edge.Line()"
description: "Create edges based on the selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Line"
macro_link: "[ImprintLineS](../../macro/geometry/ImprintLineS)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create edges based on the selected nodes.

## Syntax

```psj
Geometry.Edge.Line(...)
```

## Inputs

### `dllPoints` @type(List\[Position]) @required

- Points on the target faces.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3,4}
Geometry.Part.Cube(iPartColor=6215639)

lines = Geometry.Edge.Line(dllPoints=[[0.01, 0, 0.01], [0, 0.01, 0.01]], 
                            crlFaces=[Face(26)])

JPT.Debugger(lines)
```
