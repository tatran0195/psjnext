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

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The list of targets. It can be parts, faces or edges.

<!-- @since:5.1.0 @type:Double @required -->
### `dForceValue`

- The value of pretension force.

<!-- @since:5.1.0 @type:String @optional @default:"PreTensionSunShine1" -->
### `strName`

- The name of pretension force.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLocalUnit`

- The local unit.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crLbcPretensionSunShine`

- An existing pretension force (SunShine).
  - If this parameter is used, the specified pretension force (SunShine) will be modified.
  - If it is left _None_, a new pretension force (SunShine) will be created.

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
