---
title: "MeshEdit.FindDuplicatedNodes()"
description: "Find nodes with overlapping positions."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshEdit > FindDuplicatedNodes > Find"
macro _link: "FindDuplicatedNodes"
---

## Description

Find nodes with overlapping positions.

## Syntax

```psj
MeshEdit.FindDuplicatedNodes(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify target entities to search duplicate nodes among them.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dTolerance

- Specify torelance to search nodes duplication.
- The default value is 1e-5.

<!-- @since:5.1.0 @optional -->
### bCreateGroup

- Specify flag to create group of detected nodes.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bSelect

- Specify flag to select detected nodes.
- The default value is False.

<!-- @since:5.1.0 @optional -->
### bPreview

- Specify flag to display preview after execution.
- The default value is False.

## Return Code

A _List of CursorStr_ specifying the detected nodes.

## Sample Code

```psj {9-11}
# Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlLength=[0.0105, 0.011, 0.01], 
    strName="Cube _2", 
    iPartColor=7961077)

# Find duplication
dupnodes=MeshEdit.FindDuplicatedNodes(
    crlTargets=[Part(1, 2)], 
    bSelect=True)

print(f"{len(dupnodes)} nodes are duplicated")
print(f"nodes' id:{[i.getID() for i in dupnodes]}")
```
