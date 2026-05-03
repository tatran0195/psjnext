---
title: "Meshing.LocalSettings.Points()"
description: "LocalSettings.Points"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalSettings > Points"
---

## Description

Specify setting for fixed node position (Hard Point) when you create surface mesh, to ensure node creation at a specified location.

## Syntax

```psj
Meshing.LocalSettings.Points(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the local mesh setting.

### `localMesh` @type(LOCAL\_MESH) @required

- The local mesh setting's parameter.

### `veclHardPointXYZ` @type(Vector List) @required

- The list of hard points' position in terms of x, y, z.

### `crlHardPointTarget` @type(List\[Cursor]) @required

- The list of hard points' target. If point is on Face, target is that Face. If point is on Edge, target is that Edge.

### `crEditTarget` @type(Cursor) @default(None)

- An existed local mesh setting Point. When this parameter is used, the specified local mesh setting Point will be overwritten. When it is not used, a new local mesh setting Point will be created.

## Return Code

A _Cursor_ of the newly created local mesh setting.

## Sample Code

```psj {2-4}
Geometry.Part.Cube(iPartColor=7731705)
Meshing.LocalSettings.Points(strName="MeshParam_1", localMesh=LOCAL_MESH(bEnableSizeParams=True,
  dAvgElemSize=0.002, dMaxElemSize=0.01, dMinElemSize=0.001), veclHardPointXYZ=[[0.002078861077076959,
  0.008516764027639453, 0.01]], crlHardPointTarget=[Face(26)])
Meshing.SetMeshAttribute(crlParts=[Part(1)], surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
  dGeomAngle=0.7853981634, dGeomMinSize=0.0005, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756,
  bGeomApprox=True, iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1)], surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005, dGeomAngle=0.7853981634,
  dGeomMinSize=0.0005, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True,
  iNextEntityOffsetId=0), iThreadNum=4)
```
