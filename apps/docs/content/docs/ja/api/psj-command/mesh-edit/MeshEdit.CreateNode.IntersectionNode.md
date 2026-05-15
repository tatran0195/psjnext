---
title: "MeshEdit.CreateNode.IntersectionNode()"
description: "Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > IntersectionNode"
macro _link: "[CreateNodeIntersectionNode](../../macro/mesh-edit/CreateNodeIntersectionNode)"
---

## Description

Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes

## Syntax

```psj
MeshEdit.CreateNode.IntersectionNode(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.1.0 @required -->
### crEdge

- Specify the edge.

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify two nodes to make line.

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### crlEdges

- Specify the edge.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {7-8}
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(324)])
MeshEdit.CreateNode.Offset(vecOffset=[-0.003, 0.0, 0.0], crlNodes=[Node(259)])

# Create Intersection Node
newNode = MeshEdit.CreateNode.IntersectionNode(crlFaces=[Face(24, 23)], crlParts=[], crlEdges=[], 
                                                crlNodes=[Node(489, 490)])
JPT.Debugger(newNode) # for checking the return value
```
