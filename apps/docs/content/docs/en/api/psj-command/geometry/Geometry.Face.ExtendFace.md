---
title: "Geometry.Face.ExtendFace()"
description: "Create a face extended from an edge."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Geometry > Face > ExtendFace"
macro _link: "ExtendFace"
---

## Description

Create a face extended from an edge.

## Syntax

```psj
Geometry.Face.ExtendFace(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @required -->
### `crEdge`

- The source edge.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crFace`

- The target face when Metric is set "Offset" or "Cylinder".

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crRefFace`

- The reference face when Metric is set "Cylinder", Method is "To Face".

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crFirstNode`

- The first node to set axis by Metric "2Nodes".

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crSecondNode`

- The second node to set axis by Metric "2Nodes".

<!-- @since:5.1.0 @type:CursorPair @optional @default:[] -->
### `crElemEdge`

- The element edge to set axis by Metric "Element Edge".

<!-- @since:5.1.0 @type:Class of EXTEND _FACE _DIRECTION @optional @default:EXTEND _FACE _DIRECTION -->
### `extendFaceDirection`

- The direction settings for the extended face in 3D dimension.

<!-- @since:5.1.0 @type:Class of EXTEND _FACE _MESH @optional @default:EXTEND _FACE _MESH -->
### `extendFaceMesh`

- The mesh settings for the extended face.

<!-- @since:5.1.0 @type:Class of EXTEND _FACE _OPTION @optional @default:EXTEND _FACE _OPTION -->
### `extendFaceOption`

- The geometric settings for the extended face.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {2-7}
Geometry.Part.Cube()
created _face = Geometry.Face.ExtendFace(crEdge=Edge(19), 
                                      extendFaceDirection=EXTEND _FACE _DIRECTION(
                                          dComponentX=0, 
                                          dComponentZ=0), 
                                      extendFaceMesh=EXTEND _FACE _MESH(), 
                                      extendFaceOption=EXTEND _FACE _OPTION())
JPT.Debugger(created _face)
```
