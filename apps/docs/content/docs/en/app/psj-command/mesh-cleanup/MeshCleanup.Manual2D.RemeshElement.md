---
title: "MeshCleanup.Manual2D.RemeshElement()"
description: "local surface remesh"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual2D > RemeshElement"
---

## Description

Local surface remesh

## Syntax

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `surfaceMesh` @type(SURFACE\_MESH) @default(SURFACE\_MESH)

- The mesh.

### `bUseSetting` @type(Boolean) @default(False)

- The use setting.

### `bGrading` @type(Boolean) @default(False)

- The grading.

### `bFMesher` @type(Boolean) @default(False)

- The mesher.

### `iOverrideType` @type(Integer) @default(0)

- The override type.

### `bKeepConnection` @type(Boolean) @default(False)

- The keep connection.

### `bProjCAD` @type(Boolean) @default(False)

- The projection CAD.

### `bTinyFaceMerge` @type(Boolean) @default(False)

- The tiny face merge.

### `dMinFaceWidth` @type(Double) @default(0)

- The minimum face width.

### `dMaxFaceWidth` @type(Double) @default(0.001)

- The maximum face width.

### `bIDchcek` @type(Boolean) @default(False)

- The i dchcek.

### `bKeepRemeshEdge` @type(Boolean) @default(False)

- The keep remesh edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```
