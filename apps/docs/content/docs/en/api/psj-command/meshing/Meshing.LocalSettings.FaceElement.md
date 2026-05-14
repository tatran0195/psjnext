---
title: "Meshing.LocalSettings.FaceElement()"
description: "Set the mesh setting for the selected elements (Define the settings before surface mesh creation)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > LocalSettings > FaceElement"
---

## Description

Set the mesh setting for the selected elements (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.FaceElement(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name of the local mesh setting.

<!-- @since:5.0.1 @type:LOCAL _MESH @required -->
### `localMesh`

- The local mesh setting's parameter.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target Elements of the local mesh setting.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEditTarget`

- An existed local mesh setting Face. When this parameter is used, the specified local mesh setting Face will be overwritten. When it is not used, a new local mesh setting Face will be created.

## Return Code

A _Cursor_ specifying the created local mesh setting.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created _local _mesh _setting = Meshing.LocalSettings.FaceElement(strName="MeshParam _1", 
                                                               localMesh=LOCAL _MESH(iEntityType=2,
                                                                                    bEnableSizeParams=True, 
                                                                                    dAvgElemSize=0.005, 
                                                                                    dMaxElemSize=0.01, 
                                                                                    dMinElemSize=0.001), 
                                                               crlTargets=[Elem(970)])

JPT.Debugger(created _local _mesh _setting)
```
