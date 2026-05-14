---
title: "Geometry.BreakEntity.Face()"
description: "Break the faces into separate units that are surrounded by edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Break Entity > Face"
macro _link: "[BreakFace](../../macro/geometry/BreakFace)"
---

## Description

Break the faces into separate units that are surrounded by edges.

## Syntax

```psj
Geometry.BreakEntity.Face(...)
```

## Inputs

### \`crlFaces

- A _List of Cursor_ specifying faces to be separated.
- This is a required input.

## Return Code

A _List of Cursor_ specifying the faces after the break operation.

## Sample Code

```psj {8}
Geometry.Part.Cube()

Geometry.Edge.Line(dllPoints=[[0.01, 0, 0.01], 
                              [0, 0.01, 0.01]], 
                   crlFaces=[Face(26)],
                   bBreakFace=False)

faces = Geometry.BreakEntity.Face(crlFaces=[Face(26)])

JPT.Debugger(faces)
```
