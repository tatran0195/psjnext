---
title: "HexModeling.Linear()"
description: "Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Linear"
---

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in a specified direction.

## Syntax

```psj
HexModeling.Linear(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dLength`

- The length.

<!-- @since:5.0.1 @type:Integer @optional @default:10 -->
### `iLayer`

- The layer.

<!-- @since:5.0.1 @type:Vector @optional @default:[] -->
### `vecSweepDirection`

- The sweep direction.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bInterfaceElemFlag`

- The interface element flag.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLinearMethod`

- The linear method.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDeleteOriginalParts`

- The delete original parts.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDeleteTargetParts`

- The delete target parts.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethodBias`

- The method bias.

<!-- @since:5.0.1 @type:Double @optional @default:2.0 -->
### `dFactor`

- The factor.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iProgression`

- The progression.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, vecSweepDirection=[0.0, 0.0, 1.0])
```
