---
title: "Tools.Measure.Distance.FaceNode()"
description: "Measure Distance By FaceNode"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Measure > Distance > FaceNode"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Measure Distance By FaceNode

## Syntax

```psj
Tools.Measure.Distance.FaceNode(crlFaces, crlNodes, iPrecision=6)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlNodes` @type(List\[Cursor]) @required

- The node.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A _Double_ specifying the distance between face - node.

## Sample Code

```psj {2}
Geometry.Part.Trapezoid()
dist=Tools.Measure.Distance.FaceNode(crlFaces=[Face(23)], crlNodes=[Node(306)],iPrecision=15)
print(dist)
```
