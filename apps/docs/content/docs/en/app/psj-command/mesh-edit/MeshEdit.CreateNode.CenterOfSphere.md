---
title: "MeshEdit.CreateNode.CenterOfSphere()"
description: "Create node at the center sphere or the center of curvature of 4 nodes."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfSphere"
macro_link: "[MeshEditCreateNodeSphereCenter](../../macro/mesh-edit/MeshEditCreateNodeSphereCenter)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create node of center sphere","Create node at the center sphere or the center of curvature of 4 nodes."]}
   [param_removed_unexpectedly] Param 'crlNodesOrFace' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'iNodeID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create node at the center sphere or the center of curvature of 4 nodes.

## Syntax

```psj
MeshEdit.CreateNode.CenterOfSphere(...)
```

## Inputs

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `crlTargets` @type(List\[Cursor]) @default(\[]) @since(5.1.0)

- The sphere face or 4 nodes.

### `crlNodesOrFace` @type(List\[Cursor]) @default(\[]) @deprecated @until(5.1.0)

- The node or face.

### `iNodeID` @type(Integer) @default(1) @deprecated @until(5.1.0)

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
