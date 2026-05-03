---
title: "Meshing.SetMeshAttribute()"
description: "Set mesh attribute for the selected part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > SetMeshAttribute"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Set mesh attribute for the selected part.

:::note

This function will be used with _[Meshing.SurfaceMeshing](Meshing.SurfaceMeshing)_ function.

:::

## Syntax

```psj
Meshing.SetMeshAttribute(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The Parts to be set up with mesh setting.

### `surfaceMesh` @type(SURFACE\_MESH) @required

- The surface mesh parameter. This parameter will change the mesher's setting.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {5,6,7,8,9,10,11,12,13,14,15}
Geometry.Part.Cube()

Geometry.FCircVertexAdjust(crlParts=[Part(1)])

mesh_attribute = Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                                          surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004,
                                                                   dMaxElemSize=0.015, 
                                                                   dMinElemSize=0.0005, 
                                                                   dGeomAngle=0.7853981634, 
                                                                   dGeomMinSize=0.0005,
                                                                   dMinStretchVal=0.0, 
                                                                   iPerformanceMode=1, 
                                                                   dAutoMergeTinyFacesAngle=0.5235987756, 
                                                                   bGeomApprox=True,
                                                                   iNextEntityOffsetId=0))

JPT.Debugger(mesh_attribute)

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                       surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004, 
                                                dMaxElemSize=0.015,
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
