---
title: "Meshing.CADProjection.NodeToEdge()"
description: "Project nodes of the meshed faces to the selected CAD (Reference) edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > CADProjection > NodeToEdge"
---

## Description

Project nodes of the meshed faces to the selected CAD (Reference) edges.

## Syntax

```psj
Meshing.CADProjection.NodeToEdge(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crCadEdge

- Specify the CAD Edges. These Edges will be the reference edges for projection.
  - Note that for CAD edge, _Cursor_ type will take different format from normal cursor's format. Two parameters are now needed: the former is ID (external id) and the latter is Key (internal id).
  - For example: RefEdge((1,2)) means a CAD edge with ID (external id) = 1 and Key (internal id) = 2.

<!-- @since:5.0.1 @required -->
### crlMeshedNodes

- Specify the Meshed Nodes. These Nodes will be projected onto the reference edges.

<!-- @since:5.0.1 @optional -->
### iDirection

- Specify the direction for projection.
- The default value is 0.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: Projected nodes to the CAD (Reference) edges.
- _False_: Cannot project nodes to the CAD (Reference) edges.

## Sample Code

```psj {42,43}
Geometry.Part.Cylinder(iPartColor=12603072)

Meshing.SetMeshAttribute(crlParts=[Part(1)],
                         surfaceMesh=SURFACE _MESH(dAvgElemSize=0.004,
                                                  dMaxElemSize=0.015,
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dGeomMinSize=0.0005,
                                                  dMinStretchVal=0.0,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)],
                       surfaceMesh=SURFACE _MESH(dAvgElemSize=0.004,
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

Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

targetn=MainWindow.RightClick.AssociatedPick(crlInput=[Edge(1)],
                                             strTarget="Node")

Meshing.CADProjection.NodeToEdge(crCadEdge=RefEdge((1,1)),
                                 crlMeshedNodes=targetn)
```
