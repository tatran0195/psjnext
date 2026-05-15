---
title: "MeshEdit.CreateNode.Between2Nodes()"
description: "Create node between two selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Between2Nodes"
macro _link: "[MeshEditCreateNodeBetween2Nodes](../../macro/mesh-edit/MeshEditCreateNodeBetween2Nodes)"
---

## Description

Create node between two selected nodes.

## Syntax

```psj
MeshEdit.CreateNode.Between2Nodes(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.1.0 @optional -->
### iNumberOfNodes

- Specify the number of new nodes to be created between two target nodes.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bImprint

- Specify whether to imprint the creating node to face.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify two target nodes.
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

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iNumberofNodes

- Specify the number of nodes.
- The default value is 0.

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
