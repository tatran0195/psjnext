---
title: "HexModeling.Circular()"
description: "A hexahedral mesh model is generated from a hollow axisymmetric model."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Circular"
---

## Description

A hexahedral mesh model is generated from a hollow axisymmetric model.

## Syntax

```psj
HexModeling.Circular(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double @optional @default:360 -->
### `dAngle`

- The angle.

<!-- @since:5.0.1 @type:Double @optional @default:0.0000001 -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:36 -->
### `iLayer`

- The layer.

<!-- @since:5.0.1 @type:Vector @optional @default:[0.0,0.0,0.0] -->
### `vecAxisPt`

- The axis point.

<!-- @since:5.0.1 @type:Vector @optional @default:[1.0,0.0,0.0] -->
### `vecAxisVect`

- The axis vector.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bInterfaceElem`

- The interface element.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bExtrusion`

- The extrusion.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTranslationExtrusion`

- The translation extrusion.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBDeleteOriginalParts`

- The delete original parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {26}
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.003, dBottomInnerRadius=0.003, iCircularNodes=128)
Geometry.BodyCut.XXYYOnOnePoint(crPart=Part(1), posCutPoint=[0, 0.01, 0.01], iCuttingPlane=2)
Geometry.BodyCut.XXYYOnOnePoint(crPart=Part(1), posCutPoint=[-0.01, 0.01, 0])
Geometry.DeleteEntity.Part(crlParts=[Part(3, 5)])

Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(dAvgElemSize=0.002,
        dGeomAngle=0.7853981634, iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1,
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bOutputQuadMesh=True, 
         bGeomApprox=True, 
         iNextEntityOffsetId=0))

HexModeling.Circular(crlFaces=[58], dAngle=90.0, iLayer=6, vecAxisVect=[0.0, -1.0, 0.0], dBDeleteOriginalParts=1.0)
```
