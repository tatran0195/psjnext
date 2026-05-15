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

<!-- @since:5.1.0 @required -->
### crlParts

- Specify target parts.

<!-- @since:5.1.0 @optional -->
### dTolerance

- Specify tolerance to detect intersection.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### iDisplayTypeOption

- Specify which type of intersections displayed.
  - 0: Body Intersection Only
  - 1: All Intersection
  - 2: Between Bodies Intersection
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iElementLayers

- Specify the number of layers surrounding error elements id displayed.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bErrorText

- Specify whether or not output information about element intersections as text data to the output window and the Temp folder.
- The default value is _False_.

## Return Code

### `MESH _QUALITY _FREE _EDGE`

#### `bSuccess`

- A _Bool_ type value indicating whether the function succeeded or not.

#### `iIntersectElements`

- An _Integer_ type value indicating the number of intersection elements.

#### `crlElemEdges`

- A _List of Cursor_ type value indicating intersection elements.

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
