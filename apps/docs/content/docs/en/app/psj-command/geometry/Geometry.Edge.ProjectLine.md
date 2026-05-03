---
title: "Geometry.Edge.ProjectLine()"
description: "Create new edges by projecting the selected edges onto the selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Edge > Project Line"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create new edges by projecting the selected edges onto the selected faces.

## Syntax

```psj
Geometry.Edge.ProjectLine(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The edges to be projected.

### `crlFaces` @type(List\[Cursor]) @required

- The target faces on which the edges are imprinted.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- Two nodes to define the projection direction. This argument must be specified i&#x66;_&#x69;Type=1_.

### `bBreakFace` @type(Boolean) @default(True)

- Whether to break the given faces where possible.

### `iType` @type(Integer) @default(0)

- The method to be used to project onto target faces.
  - I&#x66;_&#x69;Type=0_, project along to the face normal direction for the target faces.
  - I&#x66;_&#x69;Type=1_, project along to the direction defined by two nodes specified by th&#x65;_&#x63;rlNodes_.
  - I&#x66;_&#x69;Type=2_, project onto the face closest to the selected edge.

### `bCheckGap` @type(Boolean) @default(False)

- Whether to limit the projection distance to the input value.

### `dGap` @type(Double) @default(0.0)

- The gap value. This argument is to be used whe&#x6E;_&#x62;CheckGap=True_.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {5}
Geometry.Part.Cube(iPartColor=13064794)
line = Geometry.Edge.Line(dllPoints=[[0.004444444444444444, 0.01, 0.01], [0.007777777777777778, 0, 0.01]], 
                          crlFaces=[Face(26)])

project_lines = Geometry.Edge.ProjectLine(crlEdges=line, crlFaces=[Face(25)])
JPT.Debugger(project_lines)
```
