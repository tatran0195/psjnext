---
title: "MeshEdit.FindDuplicatedNodes()"
description: "Find nodes with overlapping positions."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshEdit > FindDuplicatedNodes > Find"
macro_link: "FindDuplicatedNodes"
---

## Description

Find nodes with overlapping positions.

## Syntax

```psj
MeshEdit.FindDuplicatedNodes(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- Target entities to search duplicate nodes among them.

### `dTolerance` @type(Double) @default(1e-5)

- Torelance to search nodes duplication.

### `bCreateGroup` @type(Bool) @default(False)

- Flag to create group of detected nodes.

### `bSelect` @type(Bool) @default(False)

- Flag to select detected nodes.

### `bPreview` @type(Bool) @default(False)

- Flag to display preview after execution.

## Return Code

A _List of CursorStr_ specifying the detected nodes.

## Sample Code

```psj {9-11}
# Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlLength=[0.0105, 0.011, 0.01], 
    strName="Cube_2", 
    iPartColor=7961077)

# Find duplication
dupnodes=MeshEdit.FindDuplicatedNodes(
    crlTargets=[Part(1, 2)], 
    bSelect=True)

print(f"{len(dupnodes)} nodes are duplicated")
print(f"nodes' id:{[i.getID() for i in dupnodes]}")
```
