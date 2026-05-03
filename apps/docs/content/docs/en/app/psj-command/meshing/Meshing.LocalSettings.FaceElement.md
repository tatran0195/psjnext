---
title: "Meshing.LocalSettings.FaceElement()"
description: "Set the mesh setting for the selected elements (Define the settings before surface mesh creation)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalSettings > FaceElement"
---

## Description

Set the mesh setting for the selected elements (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.FaceElement(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the local mesh setting.

### `localMesh` @type(LOCAL\_MESH) @required

- The local mesh setting's parameter.

### `crlTargets` @type(List\[Cursor]) @required

- The target Elements of the local mesh setting.

### `crEditTarget` @type(Cursor) @default(None)

- An existed local mesh setting Face. When this parameter is used, the specified local mesh setting Face will be overwritten. When it is not used, a new local mesh setting Face will be created.

## Return Code

A _Cursor_ specifying the created local mesh setting.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created_local_mesh_setting = Meshing.LocalSettings.FaceElement(strName="MeshParam_1", 
                                                               localMesh=LOCAL_MESH(iEntityType=2,
                                                                                    bEnableSizeParams=True, 
                                                                                    dAvgElemSize=0.005, 
                                                                                    dMaxElemSize=0.01, 
                                                                                    dMinElemSize=0.001), 
                                                               crlTargets=[Elem(970)])

JPT.Debugger(created_local_mesh_setting)
```
