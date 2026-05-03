---
title: "Geometry.Face.ExtendFace()"
description: "Create a face extended from an edge."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Geometry > Face > ExtendFace"
macro_link: "ExtendFace"
---

## Description

Create a face extended from an edge.

## Syntax

```psj
Geometry.Face.ExtendFace(...)
```

## Inputs

### `crEdge` @type(Cursor) @required

- Source edge.

### `crFace` @type(Cursor) @default(None)

- Target face when Metric is set "Offset" or "Cylinder".

### `crRefFace` @type(Cursor) @default(None)

- Reference face when Metric is set "Cylinder", Method is "To Face".

### `crFirstNode` @type(Cursor) @default(None)

- The first node to set axis by Metric "2Nodes".

### `crSecondNode` @type(Cursor) @default(None)

- The second node to set axis by Metric "2Nodes".

### `crElemEdge` @type(CursorPair) @default(\[])

- Element edge to set axis by Metric "Element Edge".

### `extendFaceDirection` @type(Class of EXTEND\_FACE\_DIRECTION) @default(EXTEND\_FACE\_DIRECTION)

- The direction settings for the extended face in 3D dimension.

### `extendFaceMesh` @type(Class of EXTEND\_FACE\_MESH) @default(EXTEND\_FACE\_MESH)

- The mesh settings for the extended face.

### `extendFaceOption` @type(Class of EXTEND\_FACE\_OPTION) @default(EXTEND\_FACE\_OPTION)

- The geometric settings for the extended face.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {2-7}
Geometry.Part.Cube()
created_face = Geometry.Face.ExtendFace(crEdge=Edge(19), 
                                      extendFaceDirection=EXTEND_FACE_DIRECTION(
                                          dComponentX=0, 
                                          dComponentZ=0), 
                                      extendFaceMesh=EXTEND_FACE_MESH(), 
                                      extendFaceOption=EXTEND_FACE_OPTION())
JPT.Debugger(created_face)
```
