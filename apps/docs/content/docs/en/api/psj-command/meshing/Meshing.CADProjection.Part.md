---
title: "Meshing.CADProjection.Part()"
description: "Project nodes of the meshed part to the selected CAD (Reference) part."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > CADProjection > Part"
---

## Description

Project nodes of the meshed part to the selected CAD (Reference) part.

## Syntax

```psj
Meshing.CADProjection.Part(crCadPart,
                           crMeshedPart,
                           bProjectCornerNodes=False,
                           bProjectMidNodes=True,
                           bIDcheck=True)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crCadPart`

- The CAD Parts. CAD Faces in these parts will be the reference faces for projection.
  - Note that for CAD part, _Cursor_ type will take different format from normal cursor's format. Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefPart((1,2)) means a CAD part with ID (external id) = 1 and Key (internal id) = 2.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crMeshedPart`

- The Meshed Parts. Meshed Faces in these parts will be projected onto reference faces.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bProjectCornerNodes`

- The to enable/disable corner nodes projection. If _True_, corner nodes of elements will be projected.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bProjectMidNodes`

- The to enable/disable mid nodes projection. If _True_, mid nodes of elements will be projected.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bIDcheck`

- The to enable/disable ID check when projecting.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected the nodes of the meshed part to the CAD (Reference) part.
- _False_: Cannot project the nodes of the meshed part to the CAD (Reference) part.

## Sample Code

```psj {33,34,35}
cyl=Geometry.Part.Cylinder()

Meshing.SetMeshAttribute(crlParts=[cyl],
                         surfaceMesh=SURFACE _MESH(dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dGeomMinSize=0.0005,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[cyl],
                       surfaceMesh=SURFACE _MESH(dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
                                                dGeomMinSize=0.0005,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[cyl],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.Part(crCadPart=RefPart((1,1)),
                           crMeshedPart=cyl,
                           bProjectCornerNodes=True)
```
