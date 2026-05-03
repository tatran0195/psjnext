---
title: "Meshing.LocalSettings.Face()"
description: "Set the mesh setting for the selected faces (Define the settings before surface mesh creation)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalSettings > Face"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Set the mesh setting for the selected faces (Define the settings before surface mesh creation).

## Syntax

```psj
Meshing.LocalSettings.Face(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the local mesh setting.

### `localMesh` @type(LOCAL\_MESH) @required

- The local mesh setting's parameter.

### `crlTargets` @type(List\[Cursor]) @required

- The target Faces of the local mesh setting.

### `crEditTarget` @type(Cursor) @default(None)

- An existed local mesh setting Face. When this parameter is used, the specified local mesh setting Face will be overwritten. When it is not used, a new local mesh setting Face will be created.

## Return Code

A _Cursor_ specifying the created local mesh setting if success, or None if fail.

## Sample Code

```psj {3,4,5,6,7,8,9,10,11}
Geometry.Part.Cube()

local_mesh = Meshing.LocalSettings.Face(strName="MeshParam_1", 
                                        localMesh=LOCAL_MESH(iEntityType=3, 
                                                             dAvgElemSize=0.005, 
                                                             dMaxElemSize=0.01, 
                                                             dMinElemSize=0.001, 
                                                             dTrimAngle=0.7853981634, 
                                                             bEnableMeshCount=True, 
                                                             iNodeCount=8), 
                                        crlTargets=[Face(26)])

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
