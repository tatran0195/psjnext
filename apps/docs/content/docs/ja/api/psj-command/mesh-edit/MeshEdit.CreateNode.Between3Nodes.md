---
title: "MeshEdit.CreateNode.Between3Nodes()"
description: "Create a center node of 3 selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Between3Nodes"
macro _link: "[MeshEditCreateNodeBetween3Nodes](../../macro/mesh-edit/MeshEditCreateNodeBetween3Nodes)"
---

## Description

Create a center node of 3 selected nodes.

## Syntax

```psj
MeshEdit.CreateNode.Between3Nodes(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.0.1 @optional -->
### bImprint

- Specify whether to imprint the creating node to face.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify three target nodes.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face on which the node will imprint.
- The default value is \[].

:::note Note
This version does not support multi-faces printing, so `crlFaces` should be specified with a single face for each operation.
:::

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iNodeID

- Specify the node ID.
- The default value is 0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dX

- Specify the x.
- The default value is 0.0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dY

- Specify the y.
- The default value is 0.0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### dZ

- Specify the z.
- The default value is 0.0.

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
