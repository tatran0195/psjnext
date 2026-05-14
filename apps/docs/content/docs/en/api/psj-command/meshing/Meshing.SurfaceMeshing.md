---
title: "Meshing.SurfaceMeshing()"
description: "Do 2D meshing for the selected parts. The Meshing.SetMeshAttribute function will be used as input parameters"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > Surface Meshing"
macro _link: "[SurfaceMeshing2D](../../macro/meshing/SurfaceMeshing2D)"
---

## Description

Do 2D meshing for the selected parts. The _[Meshing.SetMeshAttribute](Meshing.SetMeshAttribute)_ function will be used as input parameters.

:::note

This function support triangular and quadrilateral element.

:::

## Syntax

```psj
Meshing.SurfaceMeshing(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts needed to create mesh.

<!-- @since:5.0.1 @type:SURFACE _MESH @required -->
### `surfaceMesh`

- The mesh parameter.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUseSetting`

- The to enable or disable the use of local setting. If this parameter is disabled (_False_), the existing local mesh setting will not be used.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFMesher`

- The status of F-mesher (Disabled/Enabled). F-mesher is a mesher to create only Quad4 elements. If_`surfaceMesh`_ is set to create Tri3 element, this options does not have any effect.

<!-- @since:5.0.1 @type:Integer @optional @default:8 -->
### `iThreadNum`

- The number of CPU threads for parallel meshing. This mesher create parallel meshing for each independent (no assembled face) part on each thread. If 2 parts are assembled together, they will be treated as a single part for parallel meshing. This parameter must be smaller than the maximum number of CPU cores.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRefData`

- The status of the creating of Reference data (Disabled/Enabled). Reference data is used to store CAD model. If this parameter is enabled (_True_), Reference data will be kept after meshing.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMeshColor`

- The to enable or disable the use of mesh color. If this parameter is enabled (_True_), the result meshed parts will be colored as described by _`iPartColor`_.

<!-- @since:5.0.1 @type:Integer @optional @default:65280 (White) -->
### `iPartColor`

- The color of result meshed parts.

<!-- Issue 15618 (old redmine)
### `bPartialQuadRemesh`

- A _Boolean_ to enable or disable Partial Quad Remesh option.
- The default value is _False_.
-->

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {9,10,11,12,13,14}
Geometry.Part.Cube()
Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                         surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                  iOptLevel=5, 
                                                  dAutoMergeTinyFacesAngle=0.5235987756, 
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))

meshing _status = Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                                        surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                                 iOptLevel=5, 
                                                                 dAutoMergeTinyFacesAngle=0.5235987756, 
                                                                 bGeomApprox=True, 
                                                                 iNextEntityOffsetId=0))

JPT.Debugger(meshing _status)
```
