---
title: "MeshEdit.CreateNode.Absolute()"
description: "Create a node by inputting the direct coordinate value"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Absolute"
macro_link: "[CreateNode](../../macro/mesh-edit/CreateNode)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node by input direct value","Create a node by inputting the direct coordinate value"]}
   [param_rename_candidate] 'iNewNodeID' may be a rename of 'ilNewNodeID' (91% similar)
     context: {"from":"ilNewNodeID","to":"iNewNodeID","similarity":0.9090909090909091}
   [param_removed_unexpectedly] Param 'veclNodeCoord' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a node by inputting the direct coordinate value.

## Syntax

```psj
MeshEdit.CreateNode.Absolute(...)
```

## Inputs

### `dlCoordinate` @type(List\[Double]) @default(\[]) @since(5.1.0)

- The node coordinate.

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `veclNodeCoord` @type(Vector List) @default(\[]) @deprecated @until(5.1.0)

- The node coordinate.

### `ilNewNodeID` @type(List\[Integer]) @default(\[]) @deprecated @until(5.1.0)

- The new node ID.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {2}
# Create an absolute node
newNode = MeshEdit.CreateNode.Absolute(dlCoordinate=[0.01, 0.0, 0.0], iNewNodeID=489)
JPT.Debugger(newNode) # for checking the return value
```
