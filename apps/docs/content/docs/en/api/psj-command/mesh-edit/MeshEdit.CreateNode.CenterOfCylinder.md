---
title: "MeshEdit.CreateNode.CenterOfCylinder()"
description: "Create a floating node at the center of the cylindrical surface in the longitudinal direction"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfCylinder"
macro _link: "[MeshEditCreateNodeCylindCenter](../../macro/mesh-edit/MeshEditCreateNodeCylindCenter)"
---

## Description

Create a floating node at the center of the cylindrical surface in the longitudinal direction

## Syntax

```psj
MeshEdit.CreateNode.CenterOfCylinder(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The selected cylindrical faces.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iNodeID`

- The node ID.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cylinder()

# Create center node of cylinder
newNode = MeshEdit.CreateNode.CenterOfCylinder(crlFaces=[Face(5)], iNewNodeID=363)
JPT.Debugger(newNode) # for checking the return value
```
