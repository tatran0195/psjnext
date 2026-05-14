---
title: "MeshEdit.CreateNode.Absolute()"
description: "Create a node by inputting the direct coordinate value"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Absolute"
macro _link: "[CreateNode](../../macro/mesh-edit/CreateNode)"
---

## Description

Create a node by inputting the direct coordinate value.

## Syntax

```psj
MeshEdit.CreateNode.Absolute(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Double] @optional @default:[] -->
### `dlCoordinate`

- The node coordinate.

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.0.1 @type:Vector List @removed:5.1.0 @optional @deprecated @default:[] -->
### `veclNodeCoord`

- The node coordinate.

<!-- @since:5.0.1 @type:List[Integer] @removed:5.1.0 @optional @deprecated @default:[] -->
### `ilNewNodeID`

- The new node ID.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {2}
# Create an absolute node
newNode = MeshEdit.CreateNode.Absolute(dlCoordinate=[0.01, 0.0, 0.0], iNewNodeID=489)
JPT.Debugger(newNode) # for checking the return value
```
