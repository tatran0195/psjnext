---
title: "MeshCleanup.CloseHoles()"
description: "close holes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > CloseHoles"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Close holes

## Syntax

```psj
MeshCleanup.CloseHoles(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor]) @default(\[])

- The edge.

### `dAreaMin` @type(Double) @default(0.0)

- The area minimum.

### `dAreaMax` @type(Double) @default(543210.0)

- The area maximum.

### `bMergeFace` @type(Boolean) @default(False)

- The merge face.

### `bMergeEdge` @type(Boolean) @default(False)

- The merge edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
# Prepare a model - a cylinder with holes 
Geometry.Part.Cylinder(
    bHollow=True, 
    dTopInnerRadius=0.003, 
    dBottomInnerRadius=0.003, 
    iPartColor=7829501
)

JPT.Exec('DeleteFace([7], 1)')

# Find hole edges
result = MeshCleanup.FindHoles()
flag, edge_list = JPT.MacroResultParser(result,["number","list_cursor"])

# Input edges to close hole
MeshCleanup.CloseHoles(
    crlEdges=edge_list, 
    dAreaMin=0.0, 
    dAreaMax=0.54321, 
    bMergeFace=False, 
    bMergeEdge=False
)
```
