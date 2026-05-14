---
title: "Meshing.CADProjection.NodeToFace()"
description: "Project nodes to the selected CAD (Reference) faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > CADProjection > NodeToFace"
---

## Description

Project nodes to the selected CAD (Reference) faces.

## Syntax

```psj
Meshing.CADProjection.NodeToFace(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlCadFaces`

- The CAD Faces. These Faces will be the reference faces for projection.
  - Note that for CAD face, _Cursor_ type will take different format from normal cursor's format. Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefFace((1,2)) means a CAD face with ID (external id) = 1 and Key (internal id) = 2.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlMeshedNodes`

- The Meshed Nodes. These Nodes will be projected onto the reference faces.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDirection`

- The direction for projection. Cannot be used together with`iImproveQuality`.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iImproveQuality`

- Whether improve quality is needed or not. Improve quality means to adjust the elements after creation, to optimize the quality.

:::note

Selected projection direction (`iDirection`) is ignored in this case.

:::

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected nodes to the CAD (Reference) faces.
- _False_: Cannot project nodes to the CAD (Reference) faces.

## Sample Code

```psj {28,29}
Geometry.Part.Cylinder(iPartColor=15658599)

Meshing.SetMeshAttribute(crlParts=[Part(1)],
                         surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)],
                       surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0))

Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=8,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.NodeToFace(crlCadFaces=[RefFace((5,5))],
                                 crlMeshedNodes=[Node(691)])
```
