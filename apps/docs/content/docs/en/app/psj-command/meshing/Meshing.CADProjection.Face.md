---
title: "Meshing.CADProjection.Face()"
description: "Project nodes of the meshed faces to the selected CAD (Reference) part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > CAD Projection > Face"
---

## Description

Project nodes of the meshed faces to the selected CAD (Reference) part.

## Syntax

```psj
Meshing.CADProjection.Face(...)
```

## Inputs

### `crCadPart` @type(Cursor) @required

- The CAD parts. Faces on selected parts will be the referenced faces for projection.
  - Note that for CAD part,_Curso&#x72;_&#x74;ype will take different format from normal cursor's format.
    Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefPart((1,2)) means a CAD part with ID (external id) = 1 and Key (internal id) = 2.

### `crlMeshedFaces` @type(List\[Cursor]) @required

- List of meshed faces. Nodes on these faces will be projected onto referenced faces.

### `bForceProject` @type(Boolean) @default(False)

- Whether to force projection or not. I&#x66;_&#x54;rue_, Jupiter will try to do projection more aggressively, hence may takes more time to finish.

### `bProjectCornerNodes` @type(Boolean) @default(True)

- Whether to project corner nodes or not. I&#x66;_&#x54;rue_, corner nodes of elements will be projected.

### `bProjectMidNodes` @type(Boolean) @default(False)

- Whether to project mid nodes or not. I&#x66;_&#x54;rue_, mid nodes of elements will be projected.

### `bIDcheck` @type(Boolean) @default(False)

- Whether to check ID when projecting or not.
  - I&#x66;_&#x54;rue_, nodes (on selected meshed faces) will only be projected to CAD faces (in the selected CAD Parts) whose ID is the same as the meshed face of those nodes. For example, if one node is on face 5, that node will only be projected to CAD face (in selected CAD Parts) with the same ID (i.e. 5).
  - I&#x66;_&#x46;alse_, ID check will be skipped, and projection takes place when nodes and CAD faces (in the selected CAD parts) are at the closest distance.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected the nodes of the meshed faces to the CAD (Reference) part.
- _False_: Cannot project the nodes of the meshed faces to the CAD (Reference) part.

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

Meshing.CADProjection.Face(crCadPart=RefPart((2, 2)),
                           crlMeshedFaces=[Face(10)],
                           bProjectMidNodes=True,
                           bIDcheck=True)
```
