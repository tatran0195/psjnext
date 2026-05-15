---
title: "MeshEdit.CreateNode.Point()"
description: "Create a node by referring to the coordinate value of the arbitrary point"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Point"
macro _link: "[MeshEditCreateNodePoint](../../macro/mesh-edit/MeshEditCreateNodePoint)"
---

## Description

Create a node by referring to the coordinate value of the arbitrary point.

## Syntax

```psj
MeshEdit.CreateNode.Point(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### posPoint

- Specify the coordinates of the specified point.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### bImprint

- Specify to imprint node to face.
- The default value is True.

<!-- @since:5.1.0 @optional -->
### crTarget

- Specify the target on which to create the node. The target can be a face or an edge.
- The default value is None.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iNodeID

- Specify the node ID.
- The default value is 1.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### crShape

- Specify the shape.
- The default value is None.

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
