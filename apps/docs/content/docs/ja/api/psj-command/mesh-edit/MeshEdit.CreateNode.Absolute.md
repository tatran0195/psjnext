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

<!-- @since:5.1.0 @optional -->
### dlCoordinate

- Specify the node coordinate.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### veclNodeCoord

- Specify the node coordinate.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### ilNewNodeID

- Specify the new node ID.
- The default value is \[].

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {2}
# Create an absolute node
newNode = MeshEdit.CreateNode.Absolute(dlCoordinate=[0.01, 0.0, 0.0], iNewNodeID=489)
JPT.Debugger(newNode) # for checking the return value
```
