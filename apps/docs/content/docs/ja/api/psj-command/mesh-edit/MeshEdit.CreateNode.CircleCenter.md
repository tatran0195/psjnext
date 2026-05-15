---
title: "MeshEdit.CreateNode.CircleCenter()"
description: "Create a node/floating node at the center of the selected circular edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > CircleCenter"
macro _link: "[CreateNodeEdgeCenter](../../macro/mesh-edit/CreateNodeEdgeCenter)"
---

## Description

Create a node/floating node at the center of the selected circular edge.

## Syntax

```psj
MeshEdit.CreateNode.CircleCenter(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify the circular edge.

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.0.1 @optional -->
### bImprint

- Specify whether to imprint the creating node to face.
- The default value is False.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### crFace

- Specify the face on which the node will imprint.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### iNodeID

- Specify the node ID.

## Return Code

- A _List of Cursor_ specifying the created floating or imprinted node.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Geometry.Edge.Circle(veclPositions=[[0.005555555555555556, 0.005555555555555556, 0.01]], 
                                    crlTargetFace=[Face(26)], dOutRadius=1.5)

# Create center node of circle
newNode = MeshEdit.CreateNode.CircleCenter(crlEdges=[Edge(55)], iNewNodeID=540)
JPT.Debugger(newNode) # for checking the return value
```
