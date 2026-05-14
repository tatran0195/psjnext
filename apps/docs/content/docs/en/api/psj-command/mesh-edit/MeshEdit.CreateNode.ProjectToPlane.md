---
title: "MeshEdit.CreateNode.ProjectToPlane()"
description: "Create a node by projecting the selected node/floating node to the selected face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > ProjectToPlane"
macro _link: "[MeshEditCreateNodeProjectNode](../../macro/mesh-edit/MeshEditCreateNodeProjectNode)"
---

## Description

Create a node by projecting the selected node/floating node to the selected face.

## Syntax

```psj
MeshEdit.CreateNode.ProjectToPlane(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The selected nodes.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face on which the node will project.

:::note Note
This version does not support multi-faces printing, so `crlFaces` should be specified with a single face for each operation.
:::

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dX`

- The x.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dY`

- The y.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dZ`

- The z.

## Return Code

- A _List of Cursor_ specifying the imprinted nodes.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Meshing.GridMesh(listGridMesh=[GRID _MESH(crlFace=[Face(26)], crlCorner=[Node(6, 7, 8, 5)], 
                ilMeshCount=[5, 5], iShape=4, bOptimize=True)], bProjectToCad=True)

# Create plan projected node
newNode = MeshEdit.CreateNode.ProjectToPlane(crlNodes=[Node(501)], crlFaces=[Face(25)])
JPT.Debugger(newNode) # for checking the return value
```
