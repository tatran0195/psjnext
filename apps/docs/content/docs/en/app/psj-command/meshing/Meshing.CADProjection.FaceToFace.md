---
title: "Meshing.CADProjection.FaceToFace()"
description: "Project nodes of the meshed faces to the selected CAD (Reference) faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > CADProjection > FaceToFace"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Project nodes of the meshed faces to the selected CAD (Reference) faces.

## Syntax

```psj
Meshing.CADProjection.FaceToFace(...)
```

## Inputs

### `crlCadFaces` @type(List\[Cursor]) @required

- The CAD Faces. These Faces will be the reference faces for projection.
  - Note that for CAD face,_Curso&#x72;_&#x74;ype will take different format from normal cursor's format. Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefFace((1,2)) means a CAD face with ID (external id) = 1 and Key (internal id) = 2.

### `crlMeshedFaces` @type(List\[Cursor]) @required

- The Meshed Faces. This face will be projected onto reference faces.

### `bForceProject` @type(Boolean) @default(False) @since(5.1.0)

- To enable/disable forcing projection. I&#x66;_&#x54;rue_, Jupiter will try to do projection more aggressively, hence may takes more time to finish.

### `bProjectCornerNodes` @type(Boolean) @default(False)

- To enable/disable corner nodes projection. I&#x66;_&#x54;rue_, corner nodes of elements will be projected.

### `bProjectMidNodes` @type(Boolean) @default(True)

- To enable/disable mid nodes projection. I&#x66;_&#x54;rue_, mid nodes of elements will be projected.

### `bIDcheck` @type(Boolean) @default(True)

- To enable/disable ID check when projecting.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected the nodes of the meshed faces to the CAD (Reference) faces.
- _False_: Cannot project the nodes of the meshed faces to the CAD (Reference) faces.

## Sample Code

```psj {37,38,39,40}
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.0, 0.0, 0.02], strName="Cylinder_2", iPartColor=6409934)

Geometry.FCircVertexAdjust(crlParts=[Part(1, 2)])
Meshing.SetMeshAttribute(crlParts=[Part(1, 2)],
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dMinStretchVal=0.0,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1, 2)],
                       surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
                                                dMinStretchVal=0.0,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[Part(1, 2)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.FaceToFace(crlCadFaces=[RefFace((5, 5))],
                                 crlMeshedFaces=[Face(10)],
                                 bProjectCornerNodes=True,
                                 bIDcheck=False)
```
