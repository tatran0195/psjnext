---
title: "Connections.Pretension.SunShine()"
description: "Create bolt pretension for the SunShine solver"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > Pretension > SunShine"
---

## Description

Create bolt pretension for the SunShine solver.

## Syntax

```psj
Connections.Pretension.SunShine(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets. It can be parts, faces or edges.

### `dForceValue` @type(Double) @required

- The value of pretension force.

### `strName` @type(String) @default("PreTensionSunShine1")

- The name of pretension force.

### `iLocalUnit` @type(Integer) @default(0)

- Local unit.

### `crLbcPretensionSunShine` @type(Cursor) @default(None)

- An existing pretension force (SunShine).
  - If this parameter is used, the specified pretension force (SunShine) will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new pretension force (SunShine) will be created.

## Return Code

A _Cursor_ specifying the created SunShine pretension.

## Sample Code

```psj {7}
Geometry.Part.Cylinder(dTopOuterRadius=0.003, dBottomOuterRadius=0.003, iPartColor=7697908)
Geometry.Part.Cylinder(strName="Cylinder_2", dlOrigin=[0.0, 0.01, 0.0], dTopOuterRadius=0.003, dBottomOuterRadius=0.003, iPartColor=7463537)
Meshing.SetMeshAttribute(crlParts=[Part(1, 2)], surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1, 2)], surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0))

#Pretension SunShine
Connections.Pretension.SunShine(dForceValue=123.0, crlTargets=[Part(1, 2)])
```
