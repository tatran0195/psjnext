---
title: "MC _Mesh _Quality _Auto _Check _TriQuad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the surface mesh (TRI3/TRI6/Quad4/Quad8) by using multiple mesh quality standards.

## Syntax

```psj
MC _Mesh _Quality _Auto _Check _TriQuad(Cursor[] Part Cursor,Cursor[] Face Cursor,
    Cursor[] Element Cursor,int nElemType,bool nStretchCheck,bool nAspectRatioCheck,
    bool nEdgeLengthCheck,bool nAreaCheck,bool nNodeValenceCheck,bool nInteriorAngleCheck,
    bool nDuplicateElemsCheck,double dStretchLimitValueTri,double dAspectRatioLimitValueTri,
    double dEdgeLengthLimitValueTri,double dAreaLimitValueTri,double dNodeValenceLimitValueTri,
    double dInteriorAngleLimitValueTri,double dStretchLimitValueQuad,
    double dAspectRatioLimitValueQuad,double dEdgeLengthLimitValueQuad,
    double dAreaLimitValueQuad,double dNodeValenceLimitValueQuad,double dInteriorAngleLimitValueQuad)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Part Cursor(\[3:\*]\*=Part ID)

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Face Cursor(\[6:\*]\*=Face ID)

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Element Cursor(\[11:\*]\*=Element ID)

<!-- @since:5.0.1 -->
### 4. Int

Elem Type(3-Tri and Quad Element)

<!-- @since:5.0.1 -->
### 5. Bool

Stretch Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 6. Bool

AspectRatio Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 7. Bool

EdgeLength Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 8. Bool

Area Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 9. Bool

NodeValence Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 10. Bool

InteriorAngle Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 11. Bool

DuplicateElems Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 12. Double

Stretch limit value Tri

<!-- @since:5.0.1 -->
### 13. Double

AspectRatio limit value Tri

<!-- @since:5.0.1 -->
### 14. Double

EdgeLength limit value Tri

<!-- @since:5.0.1 -->
### 15. Double

Area limit value Tri

<!-- @since:5.0.1 -->
### 16. Double

NodeValence limit value Tri

<!-- @since:5.0.1 -->
### 17. Double

InteriorAngle limit value Tri

<!-- @since:5.0.1 -->
### 18. Double

Stretch limit value Quad

<!-- @since:5.0.1 -->
### 19. Double

AspectRatio limit value Quad

<!-- @since:5.0.1 -->
### 20. Double

EdgeLength limit value Quad

<!-- @since:5.0.1 -->
### 21. Double

Area limit value Quad

<!-- @since:5.0.1 -->
### 22. Double

NodeValence limit value Quad

<!-- @since:5.0.1 -->
### 23. Double

InteriorAngle limit value Quad

## Return Code

It returns a string separated by commas contains 15 values.

<!-- @since:5.1.0 -->
### 1. Succeeded(1) or Failed(0).

<!-- @since:5.1.0 -->
### 2. Number of error elements (Tri check).

<!-- @since:5.1.0 -->
### 3. Number of error elements (Quad check).

<!-- @since:5.1.0 -->
### 4. A list of error elements.

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

result=result=JPT.Exec('MC _Mesh _Quality _Auto _Check _TriQuad([3:1], [], [], \
    3, 1, 1, 1, 1, 1, 1, 1, \
    0.1, 10, 0.0001, 1e-08, 10, 0.174533, 0.1, 10, 0.0001, 1e-08, 10, 0.174533)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)
if splitted[0]=='1':
    success _flag,error _num _tri,error _num _quad,errors=splitted
    print(f'The number error elements for tri and quad are {error _num _tri} and {error _num _quad}, respectively.')
```
