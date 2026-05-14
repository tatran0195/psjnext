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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:SURFACE _MESH @optional @default:SURFACE _MESH -->
### `surfaceMesh`

- The mesh.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bUseSetting`

- The use setting.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bGrading`

- The grading.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFMesher`

- The mesher.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOverrideType`

- The override type.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bKeepConnection`

- The keep connection.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bProjCAD`

- The projection CAD.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTinyFaceMerge`

- The tiny face merge.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMinFaceWidth`

- The minimum face width.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dMaxFaceWidth`

- The maximum face width.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIDchcek`

- The i dchcek.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bKeepRemeshEdge`

- The keep remesh edge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual2D.RemeshElement(crlTargets=[], surfaceMesh=SURFACE _MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```
