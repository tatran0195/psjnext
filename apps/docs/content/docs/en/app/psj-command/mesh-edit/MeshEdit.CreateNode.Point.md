---
title: "MeshEdit.CreateNode.Point()"
description: "Create a node by referring to the coordinate value of the arbitrary point"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Point"
macro_link: "[MeshEditCreateNodePoint](../../macro/mesh-edit/MeshEditCreateNodePoint)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node point","Create a node by referring to the coordinate value of the arbitrary point"]}
   [param_removed_unexpectedly] Param 'iNodeID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_decorator_changed] Param 'posPoint' @type changed from 'Position' to 'List[Double]' in v5.1.0
     context: {"param":"posPoint","fromVersion":"5.0.1","toVersion":"5.1.0","fromType":"Position","toType":"List[Double]"}
   [param_removed_unexpectedly] Param 'crShape' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a node by referring to the coordinate value of the arbitrary point.

## Syntax

```psj
MeshEdit.CreateNode.Point(...)
```

## Inputs

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `posPoint` @type(List\[Double]) @default(\[0,0,0])

- The coordinates of the specified point.

### `bImprint` @type(Boolean) @default(True)

- To imprint node to face.

### `crTarget` @type(Cursor) @default(None) @since(5.1.0)

- The target on which to create the node. The target can be a face or an edge.

### `iNodeID` @type(Integer) @default(1) @deprecated @until(5.1.0)

- The node ID.

### `crShape` @type(Cursor) @default(None) @deprecated @until(5.1.0)

- The shape.

## Return Code

- A _Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {5-7}
# Prepare model
Geometry.Part.Cube()

# Create node at point
newNode = MeshEdit.CreateNode.Point(iNewNodeID=490, 
                                    posPoint=[0.008331683464348316, 0.003326606005430222, 0.009999999776482582], 
                                    bImprint=False, crTarget=Face(26))
JPT.Debugger(newNode) # for checking the return value
```
