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

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The sphere face or 4 nodes.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlNodesOrFace`

- The node or face.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iNodeID`

- The node ID.

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
