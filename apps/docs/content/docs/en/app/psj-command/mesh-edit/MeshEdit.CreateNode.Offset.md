---
title: "MeshEdit.CreateNode.Offset()"
description: "Create a new node by offsetting a distance from the selected node or floating point"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Offset"
macro_link: "[CreateNodeOffset](../../macro/mesh-edit/CreateNodeOffset)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["MeshEdit CreateNode CreateNodeNodeOffset","Create a new node by offsetting a distance from the selected node or floating point"]}
   [param_decorator_changed] Param 'vecOffset' @type changed from 'Vector' to 'List[Double]' in v5.1.0
     context: {"param":"vecOffset","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"Vector","toType":"List[Double]"}
   [param_removed_unexpectedly] Param 'iRep' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a new node by offsetting a distance from the selected node or floating point.

## Syntax

```psj
MeshEdit.CreateNode.Offset(...)
```

## Inputs

### `vecOffset` @type(List\[Double]) @default(\[])

- The offset vector.

### `iRepeat` @type(Integer) @default(1) @since(5.1.0)

- The repeat times.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The selected nodes to create offset ones.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `iRep` @type(Integer) @default(1) @deprecated @until(5.1.0)

- The repeat times.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create offset node
newNode = MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(7)])
JPT.Debugger(newNode) # for checking the return value
```
