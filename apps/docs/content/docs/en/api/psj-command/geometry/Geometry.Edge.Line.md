---
title: "Geometry.Edge.Line()"
description: "Create edges based on the selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Line"
macro _link: "[ImprintLineS](../../macro/geometry/ImprintLineS)"
---

## Description

Create edges based on the selected nodes.

## Syntax

```psj
Geometry.Edge.Line(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Position] @required -->
### `dllPoints`

- The points on the target faces.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The target faces on which the edges are imprinted.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bBreakFace`

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
