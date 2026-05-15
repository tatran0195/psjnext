---
title: "Connections.Pretension.SunShine()"
description: "Create bolt pretension for the SunShine solver"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > Pretension > SunShine"
---

## Description

Create bolt pretension for the SunShine solver.

## Syntax

```psj
Connections.Pretension.SunShine(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the list of targets. It can be parts, faces or edges.

<!-- @since:5.1.0 @required -->
### dForceValue

- Specify the value of pretension force.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of pretension force.
- The default value is "PreTensionSunShine1".

<!-- @since:5.1.0 @optional -->
### iLocalUnit

- Specify local unit.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crLbcPretensionSunShine

- Specify an existing pretension force (SunShine).
  - If this parameter is used, the specified pretension force (SunShine) will be modified.
  - If it is left _None_, a new pretension force (SunShine) will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created SunShine pretension.

## Sample Code

```psj {7}
Geometry.Part.Cylinder(dTopOuterRadius=0.003, dBottomOuterRadius=0.003, iPartColor=7697908)
Geometry.Part.Cylinder(strName="Cylinder _2", dlOrigin=[0.0, 0.01, 0.0], dTopOuterRadius=0.003, dBottomOuterRadius=0.003, iPartColor=7463537)
Meshing.SetMeshAttribute(crlParts=[Part(1, 2)], surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1, 2)], surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0))

#Pretension SunShine
Connections.Pretension.SunShine(dForceValue=123.0, crlTargets=[Part(1, 2)])
```
