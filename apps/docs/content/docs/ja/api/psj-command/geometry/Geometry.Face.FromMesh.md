---
title: "Geometry.Face.FromMesh()"
description: "Create a new geometric face from the specified mesh face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Face > Face from Mesh Face"
macro _link: "[CreateFaceFromMeshFace](../../macro/geometry/CreateFaceFromMeshFace)"
---

## Description

Create a new part entity containing the new geometric face from the specified mesh face.

## Syntax

```psj
Geometry.Face.FromMesh(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crFace

- Specify the mesh face that the new face is created base on.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created _face = Geometry.Face.FromMesh(crFace=Face(26))
JPT.Debugger(created _face)
```
