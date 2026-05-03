---
title: "HexModeling.Circular()"
description: "A hexahedral mesh model is generated from a hollow axisymmetric model."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Circular"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create Hexa mesh by revolving a surface","A hexahedral mesh model is generated from a hollow axisymmetric model."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

A hexahedral mesh model is generated from a hollow axisymmetric model.

## Syntax

```psj
HexModeling.Circular(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dAngle` @type(Double) @default(360)

- The angle.

### `dTol` @type(Double) @default(0.0000001)

- The tolerance.

### `iLayer` @type(Integer) @default(36)

- The layer.

### `vecAxisPt` @type(Vector) @default(\[0.0,0.0,0.0])

- The axis point.

### `vecAxisVect` @type(Vector) @default(\[1.0,0.0,0.0])

- The axis vector.

### `bInterfaceElem` @type(Boolean) @default(False)

- The interface element.

### `bExtrusion` @type(Boolean) @default(False)

- The extrusion.

### `dTranslationExtrusion` @type(Double) @default(0.0)

- The translation extrusion.

### `dBDeleteOriginalParts` @type(Double) @default(0.0)

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
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002,
        dGeomAngle=0.7853981634, iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1,
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bOutputQuadMesh=True, 
         bGeomApprox=True, 
         iNextEntityOffsetId=0))

HexModeling.Circular(crlFaces=[58], dAngle=90.0, iLayer=6, vecAxisVect=[0.0, -1.0, 0.0], dBDeleteOriginalParts=1.0)
```
