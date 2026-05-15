---
title: "Meshing.LocalSettings.Model()"
description: "Set the mesh setting for the whole model (Define the settings before surface mesh creation)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > LocalSettings > Model"
---

## Description

Set the mesh setting for the whole model (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.Model(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name of the local mesh setting.

<!-- @since:5.0.1 @required -->
### localMesh

- Specify the local mesh setting's parameter.

<!-- @since:5.0.1 @required -->
### spaceMesh

- Specify the space mesh setting's parameter.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target Faces of the local mesh setting.

<!-- @since:5.0.1 @optional -->
### crEditTarget

- Specify the edit target.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created local mesh setting.

## Sample Code

```psj {7,8,9,10,11,12,13,14,15,16,17}
Geometry.Part.Cube()

Meshing.LocalSetting.SearchTargetFaces(dlLength=[0.003, 0.003, 0.003],
                                       dlAxisPt1=[0.0, 0.0, 0.01],
                                       dlAxisPt2=[0.005, 0.0, 0.0])

created _local _mesh _setting = Meshing.LocalSettings.Model(strName="MeshParam _1",
                                                         localMesh=LOCAL _MESH(iEntityType=11,
                                                                              bEnableSizeParams=True,
                                                                              dAvgElemSize=0.001,
                                                                              dMaxElemSize=0.01,
                                                                              dMinElemSize=0.0005,
                                                                              dTrimAngle=0.7853981634),
                                                         spaceMesh=SPACE _MESH(vLength=[0.003, 0.003, 0.003],
                                                                              vAxisPt2=[0.005, 0.0, 0.0],
                                                                              dMinElemSize=0.001),
                                                         crlTargets=[Face(21, 23, 25)])

JPT.Debugger(created _local _mesh _setting)
```
