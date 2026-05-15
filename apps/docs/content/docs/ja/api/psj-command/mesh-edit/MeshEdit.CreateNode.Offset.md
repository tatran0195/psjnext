---
title: "MeshEdit.CreateNode.Offset()"
description: "Create a new node by offsetting a distance from the selected node or floating point"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Offset"
macro _link: "[CreateNodeOffset](../../macro/mesh-edit/CreateNodeOffset)"
---

## Description

Create a new node by offsetting a distance from the selected node or floating point.

## Syntax

```psj
MeshEdit.CreateNode.Offset(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### vecOffset

- Specify the offset vector.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iRepeat

- Specify the repeat times.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the selected nodes to create offset ones.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iRep

- Specify the repeat times.
- The default value is 1.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create offset node
newNode = MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(7)])
JPT.Debugger(newNode) # for checking the return value
```
