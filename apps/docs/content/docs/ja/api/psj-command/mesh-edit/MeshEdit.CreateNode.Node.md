---
title: "MeshEdit.CreateNode.Node()"
description: "Create a node by referring to the coordinate value of the existing node"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Node"
macro _link: "[MeshEditCreateNodeAtNode](../../macro/mesh-edit/MeshEditCreateNodeAtNode)"
---

## Description

Create a node by referring to the coordinate value of the existing node.

## Syntax

```psj
MeshEdit.CreateNode.Node(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.1.0 @optional -->
### crTarget

- Specify the target on which to create the node. The target can be a face or an edge.
- The default value is None.

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
