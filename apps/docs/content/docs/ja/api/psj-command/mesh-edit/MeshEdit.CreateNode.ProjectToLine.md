---
title: "MeshEdit.CreateNode.ProjectToLine()"
description: "Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > ProjectToLine"
macro _link: "[CreateNodeProjectToLine](../../macro/mesh-edit/CreateNodeProjectToLine)"
---

## Description

Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes.

## Syntax

```psj
MeshEdit.CreateNode.ProjectToLine(crlTa)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlNodes

- Specify the selected nodes.

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### crlTa

- Specify the list node.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create line projected node
newNode = MeshEdit.CreateNode.ProjectToLine(crlNodes=[Node(7, 8, 76)])
JPT.Debugger(newNode) # for checking the return value
```
