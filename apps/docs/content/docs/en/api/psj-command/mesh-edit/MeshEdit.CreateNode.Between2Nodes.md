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

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iNumberOfNodes`

- The number of new nodes to be created between two target nodes.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bImprint`

- Whether to imprint the creating node to face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The two target nodes.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face on which the node will imprint.

:::note Note
This version does not support multi-faces printing, so `crlFaces` should be specified with a single face for each operation.
:::

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:0 -->
### `iNodeID`

- The node ID.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dX`

- The x.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dY`

- The y.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dZ`

- The z.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:0 -->
### `iNumberofNodes`

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
