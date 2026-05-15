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

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dAngle

- Specify the angle.
- The default value is 360.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is 0.0000001.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify the layer.
- The default value is 36.

<!-- @since:5.0.1 @optional -->
### vecAxisPt

- Specify the axis point.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### vecAxisVect

- Specify the axis vector.
- The default value is \[1.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### bInterfaceElem

- Specify the interface element.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bExtrusion

- Specify the extrusion.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dTranslationExtrusion

- Specify the translation extrusion.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dBDeleteOriginalParts

- Specify the delete original parts.
- The default value is 0.0.

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
