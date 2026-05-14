---
title: "Geometry.Edge.IntersectionLine()"
description: "Create edge at the intersection line of the two selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Intersection Line"
---

## Description

Create edge at the intersection line of the two selected faces.

## Syntax

```psj
Geometry.Edge.IntersectionLine(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The intersection faces.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the given faces where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {6}
Geometry.Part.Cube()
Geometry.Face.Edges(crlEdges=[Edge(20, 10)], bCreatePart=True)
Geometry.Face.Edges(crlEdges=[Edge(18, 12)], bCreatePart=True)
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

intersection _line = Geometry.Edge.IntersectionLine(crlFaces=[Face(27), Face(30)], bBreakFace=True)
JPT.Debugger(intersection _line)
```
