---
title: "Geometry.DeleteEntity.Vertex()"
description: "Delete the specified vertexes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Delete Entity > Vertex"
---

## Description

Delete the specified vertexes.

## Syntax

```psj
Geometry.DeleteEntity.Vertex(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlVertices`

- The vertexes to be deleted.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {6}
Geometry.Part.Cube()

Geometry.BreakEntity.Edge(crlEdges=[Edge(18)],
                          crlNodes=[Node(85)])

deleting _status = Geometry.DeleteEntity.Vertex(crlVertices=[Vertex(27)])

JPT.Debugger(deleting _status)
```
