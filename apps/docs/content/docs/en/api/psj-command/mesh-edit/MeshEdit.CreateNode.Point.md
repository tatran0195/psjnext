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

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
<!-- @since:5.1.0 @type:List[Double] -->
### `posPoint`

- The coordinates of the specified point.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bImprint`

- The to imprint node to face.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTarget`

- The target on which to create the node. The target can be a face or an edge.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iNodeID`

- The node ID.

<!-- @since:5.0.1 @type:Cursor @removed:5.1.0 @optional @deprecated @default:None -->
### `crShape`

- The shape.

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
