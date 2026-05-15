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

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the selected cylindrical faces.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iNodeID

- Specify the node ID.
- The default value is 1.

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
