---
title: "MeshEdit.CreateNode.CenterOfCylinder()"
description: "Create a floating node at the center of the cylindrical surface in the longitudinal direction"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfCylinder"
macro_link: "[MeshEditCreateNodeCylindCenter](../../macro/mesh-edit/MeshEditCreateNodeCylindCenter)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create node of center cylinder","Create a floating node at the center of the cylindrical surface in the longitudinal direction"]}
   [param_removed_unexpectedly] Param 'iNodeID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a floating node at the center of the cylindrical surface in the longitudinal direction

## Syntax

```psj
MeshEdit.CreateNode.CenterOfCylinder(...)
```

## Inputs

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The selected cylindrical faces.

### `iNodeID` @type(Integer) @default(1) @deprecated @until(5.1.0)

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
