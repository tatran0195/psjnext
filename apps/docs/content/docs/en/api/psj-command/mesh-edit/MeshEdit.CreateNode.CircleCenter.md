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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdges`

- The circular edge.

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bImprint`

- Whether to imprint the creating node to face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
<!-- @since:5.1.0 @default:[] -->
### `crFace`

- The face on which the node will imprint.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @required @deprecated -->
### `iNodeID`

- The node ID.

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
