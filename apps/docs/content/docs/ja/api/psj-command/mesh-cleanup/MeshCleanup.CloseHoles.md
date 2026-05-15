---
title: "MeshCleanup.CloseHoles()"
description: "close holes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > CloseHoles"
---

## Description

Close holes

## Syntax

```psj
MeshCleanup.CloseHoles(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlEdges

- Specify the edge.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dAreaMin

- Specify the area minimum.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dAreaMax

- Specify the area maximum.
- The default value is 543210.0.

<!-- @since:5.0.1 @optional -->
### bMergeFace

- Specify the merge face.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bMergeEdge

- Specify the merge edge.
- The default value is False.

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
flag, edge _list = JPT.MacroResultParser(result,["number","list _cursor"])

# Input edges to close hole
MeshCleanup.CloseHoles(
    crlEdges=edge _list, 
    dAreaMin=0.0, 
    dAreaMax=0.54321, 
    bMergeFace=False, 
    bMergeEdge=False
)
```
