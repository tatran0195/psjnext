---
title: "MeshEdit.CreateNode.Between3Nodes()"
description: "Create a center node of 3 selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Between3Nodes"
macro_link: "[MeshEditCreateNodeBetween3Nodes](../../macro/mesh-edit/MeshEditCreateNodeBetween3Nodes)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node point","Create a center node of 3 selected nodes"]}
   [param_removed_unexpectedly] Param 'iNodeID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dX' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dY' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dZ' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a center node of 3 selected nodes.

## Syntax

```psj
MeshEdit.CreateNode.Between3Nodes(...)
```

## Inputs

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `bImprint` @type(Boolean) @default(False)

- Whether to imprint the creating node to face.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- Three target nodes.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face on which the node will imprint.

:::note Note
This version does not support multi-faces printing, so`crlFaces`should be specified with a single face for each operation.
:::

### `iNodeID` @type(Integer) @default(0) @deprecated @until(5.1.0)

- The node ID.

### `dX` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The x.

### `dY` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The y.

### `dZ` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The z.

## Return Code

- A _Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create a node at the center of three nodes
newNode = MeshEdit.CreateNode.Between3Nodes(iNewNodeID=490, crlNodes=[Node(8, 7, 5)])
JPT.Debugger(newNode) # for checking the return value
```
