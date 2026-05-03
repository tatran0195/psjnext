---
title: "Geometry.Bar.Arc()"
description: "Create an arc-shaped bar part passing though the 3 selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Bar > Arc (3 Nodes)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create Bar body by arc (three nodes)","Create an arc-shaped bar part passing though the 3 selected nodes"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create an arc-shaped bar part passing though the 3 selected nodes.

## Syntax

```psj
Geometry.Bar.Arc(...)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- Three specified nodes to create arc.

### `crPart` @type(Cursor) @default(None)

- The part that the arc-shaped bar will belong to. If set none, a new bar part will be created.

### `strName` @type(String) @default("Bar\_1")

- The name of new bar part.

## Return Code

A _Cursor_ specifying the created entity.
\- If _crPart_ = _None_ then return a cursor of new created bar part.
\- If _crPart_ is specified then return a cursor of new created edge.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.Arc(crlNodes=[Node(446, 451, 474)])
JPT.Debugger(newBar)
```
