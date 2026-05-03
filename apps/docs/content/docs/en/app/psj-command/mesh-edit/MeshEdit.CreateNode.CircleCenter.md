---
title: "MeshEdit.CreateNode.CircleCenter()"
description: "Create a node/floating node at the center of the selected circular edge"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > CircleCenter"
macro_link: "[CreateNodeEdgeCenter](../../macro/mesh-edit/CreateNodeEdgeCenter)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node at center of circle","Create a node/floating node at the center of the selected circular edge"]}
   [param_removed_unexpectedly] Param 'iNodeID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_decorator_changed] Param 'crFace' @default changed from 'None' to '[]' in v5.1.0
     context: {"param":"crFace","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"None","toDefault":"[]"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a node/floating node at the center of the selected circular edge.

## Syntax

```psj
MeshEdit.CreateNode.CircleCenter(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @required

- The circular edge.

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `bImprint` @type(Boolean) @default(False)

- Whether to imprint the creating node to face.

### `crFace` @type(Cursor) @default(\[])

- The face on which the node will imprint.

### `iNodeID` @type(Integer) @required @deprecated @until(5.1.0)

- The node ID.

## Return Code

- A _List of Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Edge.Circle(veclPositions=[[0.005555555555555556, 0.005555555555555556, 0.01]], 
                                    crlTargetFace=[Face(26)], dOutRadius=1.5)

# Create center node of circle
newNode = MeshEdit.CreateNode.CircleCenter(crlEdges=[Edge(55)], iNewNodeID=540)
JPT.Debugger(newNode) # for checking the return value
```
