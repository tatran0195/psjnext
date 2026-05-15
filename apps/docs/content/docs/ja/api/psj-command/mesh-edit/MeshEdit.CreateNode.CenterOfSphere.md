---
title: "MeshEdit.CreateNode.CenterOfSphere()"
description: "Create node at the center sphere or the center of curvature of 4 nodes."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfSphere"
macro _link: "[MeshEditCreateNodeSphereCenter](../../macro/mesh-edit/MeshEditCreateNodeSphereCenter)"
---

## Description

Create node at the center sphere or the center of curvature of 4 nodes.

## Syntax

```psj
MeshEdit.CreateNode.CenterOfSphere(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNewNodeID

- Specify the new node ID.
- The default value is the maximum node ID + 1.

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the sphere face or 4 nodes.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### crlNodesOrFace

- Specify the node or face.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iNodeID

- Specify the node ID.
- The default value is 1.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Sphere(iPartColor=6409934)

# Create center node of sphere
newNode = MeshEdit.CreateNode.CenterOfSphere(crlTargets=[Face(1)], iNewNodeID=383)
JPT.Debugger(newNode) # for checking the return value
```
