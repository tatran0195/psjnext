---
title: "MC _Mesh _Quality _Manual _Check _TriQuad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the surface mesh (TRI3/TRI6/QUAD4/QUAD8) according to the selected quality standard.

## Syntax

```psj
MC _Mesh _Quality _Manual _Check _TriQuad(Cursor[] targetBody, Cursor[] targetFace,
    Cursor[] targetElements, int nElemType, int nElemQuality, int nCheckConditionTri,
    double dLimitValueTri, double TSSFACTri, int nCheckConditionQuad, dLimitValueQuad,
    double TSSFACQuad, bool bIncludeDiagobalQuad, int nNonPrimary)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Part Cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Face Cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Element Cursor(\[11:Element ID])

<!-- @since:5.0.1 -->
### 4. Int

Elements type, default elements TriQuad = 4

<!-- @since:5.0.1 -->
### 5. Int

Elemenets Quality: Stretch = 0, Aspect Ratio = 1, Edge Length = 2, Area = 3. Node Valence = 4, Interior Angle = 5, Unstable = 6, Time Step (LS-Dyna) = 7, Time Step (Abaqus) = 8

<!-- @since:5.0.1 -->
### 6. Int

Check condition Tri "{'<='}" = 0, "{'<'}" = 1, "{'>='}" = 2, "{'>'}" = 3

<!-- @since:5.0.1 -->
### 7. Double

Limit value Tri

<!-- @since:5.0.1 -->
### 8. Double

TSSFAC tri value

<!-- @since:5.0.1 -->
### 9. Int

Check condition Quad "{'<='}" = 0, "{'<'}" = 1, "{'>='}" = 2, "{'>'}" = 3

<!-- @since:5.0.1 -->
### 10. Double

Limit value for Quad

<!-- @since:5.0.1 -->
### 11. Double

TSSFAC quad value

<!-- @since:5.0.1 -->
### 12. Bool

Include diagonal flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 13. Bool

Nonprimary

## Return Code

<!-- @since:5.1.0 -->
### 1. Succeeded(1) or Failed(0).

<!-- @since:5.1.0 -->
### 2. Cutoff Value (Minimum) (Tri check).

<!-- @since:5.1.0 -->
### 3. Cutoff Value (Maximum) (Tri check).

<!-- @since:5.1.0 -->
### 4. Cutoff Value (Average) (Tri check).

<!-- @since:5.1.0 -->
### 5. Number of measured elements (Tri check).

<!-- @since:5.1.0 -->
### 6. Number of error elements (Tri check).

<!-- @since:5.1.0 -->
### 7. A list of error elements (Tri check).

<!-- @since:5.1.0 -->
### 8. A list of error element edge (Tri check).

<!-- @since:5.1.0 -->
### 9. Cutoff Value (Minimum) (Quad check).

<!-- @since:5.1.0 -->
### 10. Cutoff Value (Maximum) (Quad check).

<!-- @since:5.1.0 -->
### 11. Cutoff Value (Average) (Quad check).

<!-- @since:5.1.0 -->
### 12. Number of measured elements (Quad check).

<!-- @since:5.1.0 -->
### 13. Number of error elements (Quad check).

<!-- @since:5.1.0 -->
### 14. A list of error elements (Quad check).

<!-- @since:5.1.0 -->
### 15. A list of error element edge (Quad check).

## Sample Code

```psj
Geometry.Part.Trapezoid(
    dlLength=[0.01, 0.001, 0.01], 
    dTopXLength=0.1, 
    strName="Trapezoid _1", 
    iPartColor=7697908)

Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dMaxElemSize=0.005, 
        dMinElemSize=0.005, 
        dGeomAngle=0.7853981634, 
        dMinStretchVal=0.0, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dMaxElemSize=0.005, 
        dMinElemSize=0.005, 
        dGeomAngle=0.7853981634, 
        dMinStretchVal=0.0, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0), 
    bFMesher=True)

result=JPT.Exec('MC _Mesh _Quality _Manual _Check _TriQuad([3:1], [], [], 4, 2, 0, 0.0001, 1, 0, 0.0001, 1, 1, 0)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)
if splitted[0]=='1':
    print(f'The number of tri elements that have Edge Length error is {splitted[5]}. max value={splitted[2]}, min value={splitted[1]}')
    print(f'The number of quad elements that have Edge Length error is {splitted[12]}. max value={splitted[9]}, min value={splitted[8]}')
```
