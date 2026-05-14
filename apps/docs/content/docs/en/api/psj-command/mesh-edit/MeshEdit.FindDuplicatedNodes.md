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

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target entities to search duplicate nodes among them.

<!-- @since:5.1.0 @type:Double @optional @default:1e-5 -->
### `dTolerance`

- The torelance to search nodes duplication.

<!-- @since:5.1.0 @type:Bool @optional @default:False -->
### `bCreateGroup`

- The flag to create group of detected nodes.

<!-- @since:5.1.0 @type:Bool @optional @default:False -->
### `bSelect`

- The flag to select detected nodes.

<!-- @since:5.1.0 @type:Bool @optional @default:False -->
### `bPreview`

- The flag to display preview after execution.

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
