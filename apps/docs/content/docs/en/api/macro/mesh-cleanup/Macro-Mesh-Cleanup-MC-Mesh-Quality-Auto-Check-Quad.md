---
title: "MC _Mesh _Quality _Auto _Check _Quad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the surface mesh (QUAD4/QUAD8) by using multiple mesh quality standards.

## Syntax

```psj
MC _Mesh _Quality _Auto _Check _Quad(Cursor[] Part Cursor,Cursor[] Face Cursor,Cursor[] Element Cursor,
int nElemType, bool nStretchCheck, bool nAspectRatioCheck, bool nWarpingCheck, bool nSkewnessCheck,
bool nEdgeLengthCheck, bool nAreaCheck, bool nNodeValenceCheck, bool nInteriorAngleCheck,
bool nTaperCheck, bool nDuplicateElemsCheck,double dStretchLimitValue,double dAspectRatioLimitValue,
double dWarpingLimitValue,double dSkewnessLimitValue,double dEdgeLengthLimitValue,
double dAreaLimitValue,double dNodeValenceLimitValue,double dInteriorAngleLimitValue,double dTaperLimitValue)
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

Elem Type(1-Quad Element)

<!-- @since:5.0.1 -->
### 5. Bool

Stretch Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 6. Bool

AspectRatio Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 7. Bool

Warping Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 8. Bool

Skewness Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 9. Bool

EdgeLength Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 10. Bool

Area Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 11. Bool

NodeValence Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 12. Bool

InteriorAngle Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 13. Bool

Taper Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 14. Bool

DuplicateElems Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 15. Double

Stretch limit value

<!-- @since:5.0.1 -->
### 16. Double

Aspect Ratio limit value

<!-- @since:5.0.1 -->
### 17. Double

Warping limit value

<!-- @since:5.0.1 -->
### 18. Double

Skewness limit value

<!-- @since:5.0.1 -->
### 19. Double

Edge Length limit value

<!-- @since:5.0.1 -->
### 20. Double

Area limit value

<!-- @since:5.0.1 -->
### 21. Double

NodeValence limit value

<!-- @since:5.0.1 -->
### 22. Double

Interior Angle limit value

<!-- @since:5.0.1 -->
### 23. Double

Taper limit value

## Return Code

It returns a string separated by commas contains 3 values.

<!-- @since:5.1.0 -->
### 1. Succeeded(1) or Failed(0).

<!-- @since:5.1.0 -->
### 2. Number of error elements.

<!-- @since:5.1.0 -->
### 3. A list of erorr elements.

## Sample Code

```psj
import re

Geometry.Part.Cube(
    dlLength=[0.01, 0.01, 0.0001], 
    ilAxialNodes=[10, 10, 2], 
    strName="Cube _1", 
    iPartColor=13259210)

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

result=JPT.Exec('MC _Mesh _Quality _Auto _Check _Quad([3:1], [], [], \
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
    0.1, 10, 0.0174533, 1.22173, 0.0001, 1e-08, 10, 0.174533, 0.5)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)
if splitted[0]=='1':
    success _flag,min,error _num,errors=splitted
    print(f'The number of error elements is {error _num}.')
```
