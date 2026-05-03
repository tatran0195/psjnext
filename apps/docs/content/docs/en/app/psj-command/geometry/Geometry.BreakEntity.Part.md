---
title: "Geometry.BreakEntity.Part()"
description: "Separate parts into separated units based on each closed geometries"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Break Entity > Part"
---

## Description

Separate parts into separated units based on each closed geometries.

## Syntax

```psj
Geometry.BreakEntity.Part(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- Parts to be separated.

## Return Code

A _List of Cursor_ specifying the speparated bodies.

## Sample Code

```psj {11}
Geometry.Part.Cube(iPartColor=16147556)
Geometry.DeleteEntity.Face([Face(24, 22, 26, 21, 25)])
Geometry.Edge.Line(dllPoints=[[0, 0.0022, 0], 
                              [0, 0.0022, 0.01]], 
                   crlFaces=[Face(23)])
Geometry.Edge.Line(dllPoints=[[0, 0.0067, 0], 
                              [0, 0.0067, 0.01]], 
                   crlFaces=[Face(23)])
Geometry.DeleteEntity.Face([Face(23)])

bodies = Geometry.BreakEntity.Part(crlParts=[Part(1)])

JPT.Debugger(bodies)
```
