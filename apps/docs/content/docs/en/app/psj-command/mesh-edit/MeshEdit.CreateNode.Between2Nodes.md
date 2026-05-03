---
title: "MeshEdit.CreateNode.Between2Nodes()"
description: "Create node between two selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Between2Nodes"
macro_link: "[MeshEditCreateNodeBetween2Nodes](../../macro/mesh-edit/MeshEditCreateNodeBetween2Nodes)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node point","Create node between two selected nodes"]}
   [param_rename_candidate] 'iNumberOfNodes' may be a rename of 'iNumberofNodes' (100% similar)
     context: {"from":"iNumberofNodes","to":"iNumberOfNodes","similarity":1}
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

Create node between two selected nodes.

## Syntax

```psj
MeshEdit.CreateNode.Between2Nodes(...)
```

## Inputs

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `iNumberOfNodes` @type(Integer) @default(0) @since(5.1.0)

- The number of new nodes to be created between two target nodes.

### `bImprint` @type(Boolean) @default(False)

- Whether to imprint the creating node to face.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- Two target nodes.

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

### `iNumberofNodes` @type(Integer) @default(0) @deprecated @until(5.1.0)

- The number of nodes.

## Return Code

- A _List of Cursor_ specifying the created floating or imprinted nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create a node between two nodes
newNodes = MeshEdit.CreateNode.Between2Nodes(iNewNodeID=490, iNumberofNodes=2, crlNodes=[Node(6, 7)])
JPT.Debugger(newNodes) # for checking the return value
```
