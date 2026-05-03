---
title: "MeshEdit.CreateNode.ProjectToPlane()"
description: "Create a node by projecting the selected node/floating node to the selected face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > ProjectToPlane"
macro_link: "[MeshEditCreateNodeProjectNode](../../macro/mesh-edit/MeshEditCreateNodeProjectNode)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node point","Create a node by projecting the selected node/floating node to the selected face"]}
   [param_removed_unexpectedly] Param 'dX' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dY' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dZ' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a node by projecting the selected node/floating node to the selected face.

## Syntax

```psj
MeshEdit.CreateNode.ProjectToPlane(...)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The selected nodes.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face on which the node will project.

:::note Note
This version does not support multi-faces printing, so`crlFaces`should be specified with a single face for each operation.
:::

### `dX` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The x.

### `dY` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The y.

### `dZ` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The z.

## Return Code

- A _List of Cursor_ specifying the imprinted nodes.

## Sample Code

```psj {7}
# Prepare model
Geometry.Part.Cube()
Meshing.GridMesh(listGridMesh=[GRID_MESH(crlFace=[Face(26)], crlCorner=[Node(6, 7, 8, 5)], 
                ilMeshCount=[5, 5], iShape=4, bOptimize=True)], bProjectToCad=True)

# Create plan projected node
newNode = MeshEdit.CreateNode.ProjectToPlane(crlNodes=[Node(501)], crlFaces=[Face(25)])
JPT.Debugger(newNode) # for checking the return value
```
