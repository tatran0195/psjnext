---
title: "MeshCleanup.Intersection()"
description: "Detect element intersection errors."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > Intersection"
macro _link: "[MC _Intersection](../../macro/mesh-cleanup/MC _Intersection)"
---

## Description

Detect element intersection errors.

## Syntax

```psj
MeshCleanup.Intersection(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlParts`

- The target parts.

<!-- @since:5.1.0 @type:Double @optional @default:0.001 -->
### `dTolerance`

- The tolerance to detect intersection.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDisplayTypeOption`

- Which type of intersections displayed.
  - 0: Body Intersection Only
  - 1: All Intersection
  - 2: Between Bodies Intersection

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iElementLayers`

- The number of layers surrounding error elements id displayed.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bErrorText`

- Whether or not output information about element intersections as text data to the output window and the Temp folder.

## Return Code

<!-- @since:5.1.0 @type:Bool @optional -->
### `MESH _QUALITY _FREE _EDGE`

#### `bSuccess`

- The type value indicating whether the function succeeded or not.

<!-- @since:5.1.0 @type:Integer @optional -->

#### `iIntersectElements`

- The type value indicating the number of intersection elements.

<!-- @since:5.1.0 @type:List[Cursor] @optional -->

#### `crlElemEdges`

- The type value indicating intersection elements.

## Sample Code

```psj {13,17}
#Prepare Model
Geometry.Part.Cube(strName="Cube _1", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=13259210)
Geometry.Edge.Angle(
    [CursorPair(Node(452), Node(460)), 
    CursorPair(Node(92), Node(200)), 
    CursorPair(Node(28), Node(392)), 
    CursorPair(Node(12), Node(108))])

Geometry.Face.Edges(crlEdges=[Edge(60, 58)])

#Check body intersection
res=MeshCleanup.Intersection(crlParts=[Part(1,2)], dTolerance=1e-06, iDisplayTypeOption=0)
JPT.Debugger(res)

#Check intersection between bodies
res=MeshCleanup.Intersection(crlParts=[Part(1,2)], dTolerance=1e-06, iDisplayTypeOption=2)
JPT.Debugger(res)
```
