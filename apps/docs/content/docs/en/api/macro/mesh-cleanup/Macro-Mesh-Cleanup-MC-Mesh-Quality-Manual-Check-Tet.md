---
title: "MC _Mesh _Quality _Manual _Check _Tet()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the solid mesh (Tet4/Tet10) according to the selected quality standard.

## Syntax

```psj
MC _Mesh _Quality _Manual _Check _Tet(Cursor[] targetBody, Cursor[] targetFace,
    Cursor[] targetElements, int nElemType, int nElemQuality, int nCheckCondition,
    double dLimitValue, double dSafeFactor, 0)
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

Elements type, default elements Tet = 2

<!-- @since:5.0.1 -->
### 5. Int

Elemenets Quality: Stretch = 0, Aspect Ratio = 1, Volume = 2, Jacob = 3. Factor = 4, Tet Collapse = 5, Tet Skew = 6,Edge Length = 7, Unstable = 8,Time Step (Abaqus) = 9

<!-- @since:5.0.1 -->
### 6. Int

Check condition "{'<='}" = 0, "{'<'}" = 1, "{'>='}" = 2, "{'>'}" = 3

<!-- @since:5.0.1 -->
### 7. Double

Limit value

<!-- @since:5.0.1 -->
### 8. Double

Safe factor value

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 1. Succeeded:1 Failed: 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 2. Final Min Value displayed in dialog

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Final Max Value displayed in dialog

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 4. Final AVG Value displayed in dialog

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Total number of entities calculated

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. Number of failed elements within limit value

## Return Code

It returns a string separated by commas contains 8 values.

<!-- @since:5.1.0 -->
### 1. Succeeded(1) or Failed(0).

<!-- @since:5.1.0 -->
### 2. Cutoff Value (Minimum).

<!-- @since:5.1.0 -->
### 3. Cutoff Value (Maximum).

<!-- @since:5.1.0 -->
### 4. Cutoff Value (Average).

<!-- @since:5.1.0 -->
### 5. Number of measured elements.

<!-- @since:5.1.0 -->
### 6. Number of error elements.

<!-- @since:5.1.0 -->
### 7. A list of erorr elements.

<!-- @since:5.1.0 -->
### 8. A list of error element edge.

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

result = JPT.Exec('MC _Mesh _Quality _Manual _Check _Tet([3:1], [], [], 2, 0, 0, 0.1, 1, 0)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)
if splitted[0]=='1':
    success _flag,min,max,avg,target _num,error _num,errors1,errors2=splitted
    print(f'The number of elements that have stretch error is {error _num}. max value={max}, min value={min}')
```
