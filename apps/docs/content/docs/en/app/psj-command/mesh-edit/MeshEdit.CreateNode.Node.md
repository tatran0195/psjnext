---
title: "MeshEdit.CreateNode.Node()"
description: "Create a node by referring to the coordinate value of the existing node"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Node"
macro_link: "[MeshEditCreateNodeAtNode](../../macro/mesh-edit/MeshEditCreateNodeAtNode)"
---

## Description

Create a node by referring to the coordinate value of the existing node.

## Syntax

```psj
MeshEdit.CreateNode.Node(...)
```

## Inputs

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1)

- The new node ID.

### `crTarget` @type(Cursor) @default(None)

- The target on which to create the node. The target can be a face or an edge.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create node at node
newNode = MeshEdit.CreateNode.Node(iNewNodeId=489, crTarget=Node(480))
JPT.Debugger(newNode) # for checking the return value
```
