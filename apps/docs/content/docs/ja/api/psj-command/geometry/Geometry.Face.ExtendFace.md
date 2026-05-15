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

<!-- @since:5.1.0 @required -->
### crEdge

- Specify source edge.

<!-- @since:5.1.0 @optional -->
### crFace

- Specify target face when Metric is set "Offset" or "Cylinder".
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crRefFace

- Specify reference face when Metric is set "Cylinder", Method is "To Face".
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crFirstNode

- Specify the first node to set axis by Metric "2Nodes".
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crSecondNode

- Specify the second node to set axis by Metric "2Nodes".
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crElemEdge

- Specify element edge to set axis by Metric "Element Edge".
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### extendFaceDirection

- Specify the direction settings for the extended face in 3D dimension.
- The default value is [EXTEND\_FACE\_DIRECTION](../../data-type/psj-command/parameter-types/EXTEND _FACE _DIRECTION).

<!-- @since:5.1.0 @optional -->
### extendFaceMesh

- Specify the mesh settings for the extended face.
- The default value is [EXTEND\_FACE\_MESH](../../data-type/psj-command/parameter-types/EXTEND _FACE _MESH).

<!-- @since:5.1.0 @optional -->
### extendFaceOption

- Specify the geometric settings for the extended face.
- The default value is [EXTEND\_FACE\_OPTION](../../data-type/psj-command/parameter-types/EXTEND _FACE _OPTION).

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
