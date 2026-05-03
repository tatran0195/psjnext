---
title: "Tools.Measure.Angle.TwoElemEdges()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Angle > TwoElemEdges"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

## Syntax

```psj
Tools.Measure.Angle.TwoElemEdges(...)
```

## Inputs

### `crpElemEdge1` @type(Cursor Pair) @required

- The element edge1 - two nodes.

### `crpElemEdge2` @type(Cursor Pair) @required

- The element edge2 - two nodes.

### `strTarget` @type(String) @default("Angle")

- The target.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

Value measured with the precision set in iPrecision in _String_ format.

## Sample Code

```psj {3-5}
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoElemEdges(
            crpElemEdge1=CursorPair(Node(95), Node(487)), 
            crpElemEdge2=CursorPair(Node(453), Node(462)))

JPT.Debugger(angle)
```
