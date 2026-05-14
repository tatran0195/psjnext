---
title: "MeshCleanup.FreeEdges()"
description: "Check free edges and non-manifolds."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > FreeEdges"
macro _link: "[MC _FreeEdge](../../macro/mesh-cleanup/MC _FreeEdge)"
---

## Description

Check free edges and non-manifolds.

## Syntax

```psj
MeshCleanup.FreeEdges(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlParts`

- The target parts to check free edges / non-manifolds.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMeshColor`

- The mesh color in Free Edge mode.
  - 0: Original
  - 1: Gray

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplayAll`

- Whether or not display all the meshes.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iElemLayers`

- The number of display mesh layers around free edges / non-manifolds.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bDisplayFreeEdges`

- Whether or not check free edges.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFreeEdgeByPart`

- Whether or not check free edges by part.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bDisplayNonManifold`

- Whether or not check non-manifolds.

<!-- @since:5.1.0 @type:Integer @optional @default:3 -->
### `iNonManifoldThreshold`

- The minimum number of connected components for the non-manifold.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bHideBoundaryEdge`

- Whether or not ignores boundary edges as free edges.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bErrorText`

- Whether or not to export information of free edges / non-manifolds to a text file.

## Return Code

A Boolean specifying the function successfully executed or not.

## Sample Code

```psj {27}
#Create a model.
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
mating _face=Assemble.FindMatingFaceEx(
    crlTaBodies=[Part(1, 2)], 
    dMatingTol=0.000222222)
Assemble.AssembleFaceEx(
    ilPairFaceToMakeShareFace=mating _face, 
    dTolerance=0.000222222, 
    iTypeConnectPos=0)
JPT.Exec('DeleteFace([49], 1)')
Geometry.Part.Cube(dlOrigin=[0.01, 0.015, 0.0], strName="Cube _3", iPartColor=7697908)
Geometry.Edge.Angle([
    CursorPair(Node(1069), Node(1461)), 
    CursorPair(Node(1069), Node(1184)), 
    CursorPair(Node(1005), Node(1376)), 
    CursorPair(Node(989), Node(1085))])
Geometry.Face.Edges(crlEdges=[Edge(98, 97, 96, 95)])
Geometry.Part.Cube(dlOrigin=[0.0, 0.015, 0.0], strName="Cube _4", iPartColor=7463537)
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
