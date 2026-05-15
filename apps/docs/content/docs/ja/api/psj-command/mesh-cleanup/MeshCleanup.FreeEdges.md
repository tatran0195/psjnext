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

<!-- @since:5.1.0 @required -->
### crlParts

- Specify target parts to check free edges / non-manifolds.

<!-- @since:5.1.0 @optional -->
### iMeshColor

- Specify mesh color in Free Edge mode.
  - 0: Original
  - 1: Gray
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bDisplayAll

- Specify whether or not display all the meshes.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iElemLayers

- Specify number of display mesh layers around free edges / non-manifolds.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bDisplayFreeEdges

- Specify whether or not check free edges.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bFreeEdgeByPart

- Specify whether or not check free edges by part.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bDisplayNonManifold

- Specify whether or not check non-manifolds.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### iNonManifoldThreshold

- Specify the minimum number of connected components for the non-manifold.
- The default value is 3.

<!-- @since:5.1.0 @optional -->
### bHideBoundaryEdge

- Specify whether or not ignores boundary edges as free edges.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bErrorText

- Specify whether or not to export information of free edges / non-manifolds to a text file.
- The default value is _False_.

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
