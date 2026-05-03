---
title: "MeshCleanup.FreeEdges()"
description: "Check free edges and non-manifolds."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > FreeEdges"
macro_link: "[MC_FreeEdge](../../macro/mesh-cleanup/MC_FreeEdge)"
---

## Description

Check free edges and non-manifolds.

## Syntax

```psj
MeshCleanup.FreeEdges(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- Target parts to check free edges / non-manifolds.

### `iMeshColor` @type(Integer) @default(0)

- Mesh color in Free Edge mode.
  - 0: Original
  - 1: Gray

### `bDisplayAll` @type(Boolean) @default(False)

- Whether or not display all the meshes.

### `iElemLayers` @type(Integer) @default(1)

- Number of display mesh layers around free edges / non-manifolds.

### `bDisplayFreeEdges` @type(Boolean) @default(True)

- Whether or not check free edges.

### `bFreeEdgeByPart` @type(Boolean) @default(False)

- Whether or not check free edges by part.

### `bDisplayNonManifold` @type(Boolean) @default(True)

- Whether or not check non-manifolds.

### `iNonManifoldThreshold` @type(Integer) @default(3)

- The minimum number of connected components for the non-manifold.

### `bHideBoundaryEdge` @type(Boolean) @default(False)

- Whether or not ignores boundary edges as free edges.

### `bErrorText` @type(Boolean) @default(False)

- Whether or not to export information of free edges / non-manifolds to a text file.

## Return Code

A Boolean specifying the function successfully executed or not.

## Sample Code

```psj {27}
#Create a model.
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
mating_face=Assemble.FindMatingFaceEx(
    crlTaBodies=[Part(1, 2)], 
    dMatingTol=0.000222222)
Assemble.AssembleFaceEx(
    ilPairFaceToMakeShareFace=mating_face, 
    dTolerance=0.000222222, 
    iTypeConnectPos=0)
JPT.Exec('DeleteFace([49], 1)')
Geometry.Part.Cube(dlOrigin=[0.01, 0.015, 0.0], strName="Cube_3", iPartColor=7697908)
Geometry.Edge.Angle([
    CursorPair(Node(1069), Node(1461)), 
    CursorPair(Node(1069), Node(1184)), 
    CursorPair(Node(1005), Node(1376)), 
    CursorPair(Node(989), Node(1085))])
Geometry.Face.Edges(crlEdges=[Edge(98, 97, 96, 95)])
Geometry.Part.Cube(dlOrigin=[0.0, 0.015, 0.0], strName="Cube_4", iPartColor=7463537)
JPT.Exec('DeleteFace([133], 1)')
JPT.Exec('DeleteFace([129], 1)')
JPT.Exec('DeleteFace([132], 1)')
JPT.Exec('DeleteFace([128], 1)')
JPT.Exec('DeleteFace([131], 1)')

#Check free edges and non-manifolds.
ret=MeshCleanup.FreeEdges(crlParts=[Part(1, 2, 3, 4)], bFreeEdgeByPart=True, bErrorText=True)
print(f"{ret.iFreeEdges}/72")
print(f"{ret.iNonManifoldEdges}/36")
```
