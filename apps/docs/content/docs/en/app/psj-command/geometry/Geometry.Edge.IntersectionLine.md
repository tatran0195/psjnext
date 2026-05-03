---
title: "Geometry.Edge.IntersectionLine()"
description: "Create edge at the intersection line of the two selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Intersection Line"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create Edge along the intersection line of faces","Create edge at the intersection line of the two selected faces"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create edge at the intersection line of the two selected faces.

## Syntax

```psj
Geometry.Edge.IntersectionLine(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The intersection faces.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {6}
Geometry.Part.Cube()
Geometry.Face.Edges(crlEdges=[Edge(20, 10)], bCreatePart=True)
Geometry.Face.Edges(crlEdges=[Edge(18, 12)], bCreatePart=True)
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

intersection_line = Geometry.Edge.IntersectionLine(crlFaces=[Face(27), Face(30)], bBreakFace=True)
JPT.Debugger(intersection_line)
```
