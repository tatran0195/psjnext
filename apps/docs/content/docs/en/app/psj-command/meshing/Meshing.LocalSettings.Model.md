---
title: "Meshing.LocalSettings.Model()"
description: "Set the mesh setting for the whole model (Define the settings before surface mesh creation)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalSettings > Model"
---

## Description

Set the mesh setting for the whole model (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.Model(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the local mesh setting.

### `localMesh` @type(LOCAL\_MESH) @required

- The local mesh setting's parameter.

### `spaceMesh` @type(SPACE\_MESH) @required

- The space mesh setting's parameter.

### `crlTargets` @type(List\[Cursor]) @required

- The target Faces of the local mesh setting.

### `crEditTarget` @type(Cursor) @default(None)

- The edit target.

## Return Code

A _Cursor_ specifying the created local mesh setting.

## Sample Code

```psj {7,8,9,10,11,12,13,14,15,16,17}
Geometry.Part.Cube()

Meshing.LocalSetting.SearchTargetFaces(dlLength=[0.003, 0.003, 0.003],
                                       dlAxisPt1=[0.0, 0.0, 0.01],
                                       dlAxisPt2=[0.005, 0.0, 0.0])

created_local_mesh_setting = Meshing.LocalSettings.Model(strName="MeshParam_1",
                                                         localMesh=LOCAL_MESH(iEntityType=11,
                                                                              bEnableSizeParams=True,
                                                                              dAvgElemSize=0.001,
                                                                              dMaxElemSize=0.01,
                                                                              dMinElemSize=0.0005,
                                                                              dTrimAngle=0.7853981634),
                                                         spaceMesh=SPACE_MESH(vLength=[0.003, 0.003, 0.003],
                                                                              vAxisPt2=[0.005, 0.0, 0.0],
                                                                              dMinElemSize=0.001),
                                                         crlTargets=[Face(21, 23, 25)])

JPT.Debugger(created_local_mesh_setting)
```
