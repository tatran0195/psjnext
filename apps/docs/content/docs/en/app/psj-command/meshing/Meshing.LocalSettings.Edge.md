---
title: "Meshing.LocalSettings.Edge()"
description: "Set the mesh setting for the selected edges (Define the settings before surface mesh creation)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalSettings > Edge"
---

## Description

Set the mesh setting for the selected edges (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.Edge(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the local mesh setting.

### `localMesh` @type(LOCAL\_MESH) @required

- The local mesh setting's parameter.

### `crlTargets` @type(List\[Cursor]) @required

- The target Edges of the local mesh setting.

### `crEditTarget` @type(Cursor) @default(None)

- An existed local mesh setting Edge. When this parameter is used, the specified local mesh setting Edge will be overwritten. When it is not used, a new local mesh setting Edge will be created.

## Return Code

A _Cursor_ specifying the created local mesh setting if success, or None if fail.

## Sample Code

```psj {3,4,5,6,7,8,9,10,11}
Geometry.Part.Cube()

local_mesh = Meshing.LocalSettings.Edge(strName="MeshParam_1", 
                                        localMesh=LOCAL_MESH(iEntityType=3, 
                                                             dAvgElemSize=0.005, 
                                                             dMaxElemSize=0.01, 
                                                             dMinElemSize=0.001, 
                                                             dTrimAngle=0.7853981634, 
                                                             bEnableMeshCount=True, 
                                                             iNodeCount=8), 
                                        crlTargets=[Edge(18)])

JPT.Debugger(local_mesh)

Geometry.FCircVertexAdjust(crlParts=[Part(1)])

Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015, 
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634, 
                                                  dGeomMinSize=0.0005, 
                                                  dMinStretchVal=0.0, 
                                                  iPerformanceMode=1, 
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                       surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015, 
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634, 
                                                dGeomMinSize=0.0005, 
                                                dMinStretchVal=0.0, 
                                                iPerformanceMode=1, 
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True, 
                                                iNextEntityOffsetId=0), 
                       iThreadNum=4)
```
