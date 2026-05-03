---
title: "Geometry.Bar.TwoNodes()"
description: "Create a Bar part from two selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Bar > 2 Nodes"
macro_link: "[CreateBar](../../macro/geometry/CreateBar)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create Bar body by two nodes","Create a Bar part from two selected nodes"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a Bar part from two selected nodes.

## Syntax

```psj
Geometry.Bar.TwoNodes(...)
```

## Inputs

### `crStartNode` @type(Cursor) @required

- The start node.

### `crEndNode` @type(Cursor) @required

- The end node.

### `strName` @type(String) @default("Bar\_1")

- The name of new part.

### `iMeshOption` @type(Integer) @default(0)

- The option to generate element on Bar body.
  - I&#x66;_&#x69;MeshOption=0_: The new Bar body has the number of 1D elements equal t&#x6F;_&#x69;MeshCount_.
  - I&#x66;_&#x69;MeshOption=1_: The new Bar body has the size of 1D elements on the Bar body equal t&#x6F;_&#x64;MeshSize_.

### `iMeshCount` @type(Integer) @default(5)

- The number of 1D elements on the Bar body. This argument should be specified whe&#x6E;_&#x69;MeshOption=0_.

### `dMeshSize` @type(Double) @default(0.0)

- The size of 1D elements on the Bar body. This argument should be specified whe&#x6E;_&#x69;MeshOption=1_.

## Return Code

A _Cursor_ specifying the created bar part.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.TwoNodes(crStartNode=Node(5), crEndNode=Node(7))
JPT.Debugger(newBar)
```
