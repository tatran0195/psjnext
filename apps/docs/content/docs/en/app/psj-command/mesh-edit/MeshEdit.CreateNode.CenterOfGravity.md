---
title: "MeshEdit.CreateNode.CenterOfGravity()"
description: "create node Center Of Gravity"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfGravity"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'iNodeID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dX' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dY' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'dZ' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create node Center Of Gravity

## Syntax

```psj
MeshEdit.CreateNode.CenterOfGravity(...)
```

## Inputs

### `iCreationType` @type(Integer) @default(1)

- The creation type.
  - 0: Gravity
  - 1: Shape

### `iNewNodeID` @type(Integer) @default(the maximum node ID + 1) @since(5.1.0)

- The new node ID.

### `crlParts` @type(List\[Cursor]) @default(\[])

- The selected part.

### `crlBarPart` @type(List\[Cursor]) @default(\[])

- The selected bar part.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The selected face.

### `iNodeID` @type(Integer) @default(0) @deprecated @until(5.1.0)

- The node ID.

### `dX` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The x.

### `dY` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The y.

### `dZ` @type(Double) @default(0.0) @deprecated @until(5.1.0)

- The z.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create center node of gravity
newNode = MeshEdit.CreateNode.CenterOfGravity(iNodeID=489, crlTargets=[Part(1)])
JPT.Debugger(newNode) # for checking the return value
```
