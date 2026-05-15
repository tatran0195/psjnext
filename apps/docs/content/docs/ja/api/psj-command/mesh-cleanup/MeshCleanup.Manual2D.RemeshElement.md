---
title: "MeshCleanup.Manual2D.RemeshElement()"
description: "local surface remesh"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual2D > RemeshElement"
---

## Description

Local surface remesh

## Syntax

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE _MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### surfaceMesh

- Specify the mesh.
- The default value is _[SURFACE\_MESH](./../../data-type/psj-command/parameter-types/SURFACE _MESH)_.

<!-- @since:5.0.1 @optional -->
### bUseSetting

- Specify the use setting.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bGrading

- Specify the grading.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bFMesher

- Specify the mesher.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iOverrideType

- Specify the override type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bKeepConnection

- Specify the keep connection.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bProjCAD

- Specify the projection CAD.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bTinyFaceMerge

- Specify the tiny face merge.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dMinFaceWidth

- Specify the minimum face width.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxFaceWidth

- Specify the maximum face width.
- The default value is 0.001.

<!-- @since:5.0.1 @optional -->
### bIDchcek

- Specify the i dchcek.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bKeepRemeshEdge

- Specify the keep remesh edge.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE _MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```
