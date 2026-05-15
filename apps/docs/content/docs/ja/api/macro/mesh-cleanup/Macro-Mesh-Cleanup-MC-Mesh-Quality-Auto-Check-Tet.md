---
title: "MC _Mesh _Quality _Auto _Check _Tet()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the solid mesh (TET4/TET10) by using multiple mesh quality standard.

## Syntax

```psj
MC _Mesh _Quality _Auto _Check _Tet(Cursor[] Part Cursor,Cursor[] Element Cursor,
    int nElemType, bool nStretchCheck, bool nAspectRatioCheck, bool nVolumeCheck,
    bool nJacobFactCheck, bool nTetCollapseCheck, bool nTetSkewCheck,
    double dStretchLimitValue,double dAspectRatioLimitValue, double dVolumeLimitValue,
    double dJacobFactLimitValue,double dTetCollapseLimitValue,double dTetSkewLimitValue)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Part Cursor(\[3:\*]\*=Part ID)

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Element Cursor(\[11:\*]\*=Element ID)

<!-- @since:5.0.1 -->
### 3. Int

Elem Type(2-Tet Element)

<!-- @since:5.0.1 -->
### 4. Bool

Stretch Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 5. Bool

Aspect Ratio Check flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 6. Bool

Volume Bool flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 7. Bool

Jacob factor Bool flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 8. Bool

Tet Collapse Bool flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 9. Bool

Tet skew flag,true = 1,false=0

<!-- @since:5.0.1 -->
### 10. Double

Stretch limit value

<!-- @since:5.0.1 -->
### 11. Double

Aspect Ratio limit value

<!-- @since:5.0.1 -->
### 12. Double

Volume limit value

<!-- @since:5.0.1 -->
### 13. Double

Jacob factor limit value

<!-- @since:5.0.1 -->
### 14. Double

Tet Collapse limit value

<!-- @since:5.0.1 -->
### 15. Double

Tet skew limit value

## Return Code

It returns a string separated by commas contains 3 values.

<!-- @since:5.1.0 -->
### 1. Succeeded(1) or Failed(0).

<!-- @since:5.1.0 -->
### 2. Number of error elements.

<!-- @since:5.1.0 -->
### 3. A list of erorr elements.

## Sample Code

```psj {32}
import re

Geometry.Part.Cube(
    dlLength=[0.01, 0.01, 0.0001], 
    ilAxialNodes=[10, 10, 2], 
    strName="Cube _1", 
    iPartColor=13259210)

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dMaxElemSize=0.1, 
        dGeomAngle=0.7853981634, 
        dMinStretchVal=0.0, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SolidMeshing(
    crlParts=[Part(1)], 
    bTet10=True, 
    dGradingFactor=1.0, 
    iSpeedVsQual=1, 
    bSafeMode=False, 
    iParallel=8, 
    bSurfaceNodes=False, 
    bEdgeNodes=False, 
    bInternalMeshOnly=False, 
    iPartColor=65280)

result=JPT.Exec('MC _Mesh _Quality _Auto _Check _Tet([3:1], [], 2, 1, 1, 1, 1, 1, 1, 0.1, 10, 0, 0, 0.05, 0.9)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)

if splitted[0]=='1':
    success _flag,error _num,errors=splitted
    print(f'The number of error elements {error _num}.')
```
