---
title: "Geometry.Bar.Spline()"
description: "Create a spline-curve bar part passing though the selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Bar > Spline"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create Bar body by drawing spline","Create a spline-curve bar part passing though the selected nodes"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a spline-curve bar part passing though the selected nodes.

## Syntax

```psj
Geometry.Bar.Spline(...)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- Either a series of nodes (interpolation points) through which the curve passes. At least three nodes must be specified.

### `crPart` @type(Cursor) @default(None)

- The part that the spline bar will belong to. If set none, a new bar part will be created.

### `strName` @type(String) @default("Bar\_1")

- The name of new bar part.

## Return Code

A _Cursor_ specifying the created entity.
\- If _crPart_ = _None_ then return a cursor of new created bar part.
\- If _crPart_ is specified then return a cursor of new created edge.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.Spline(crlNodes=[Node(440, 463, 443, 474)])
JPT.Debugger(newBar)
```
