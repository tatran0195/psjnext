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

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bImprint`

- Whether to imprint the creating node to face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The three target nodes.

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
