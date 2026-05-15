---
title: "MC _Mesh _Quality _Manual _Check _Quad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the surface mesh (Quad4/Quad8) according to the selected quality standard.

## Syntax

```psj
MC _Mesh _Quality _Manual _Check _Quad(cursor[] crBody, cursor[] crFace, cursor[] crElem,
    int iElemType, int iCond, int dSafeFact, double dDispValue)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target element cursor(\[11:Elem ID])

<!-- @since:5.0.1 -->
### 4. Int

Element type (1-Quad Element)

<!-- @since:5.0.1 -->
### 5. Int

Element quality metric type

- 0: Stretch
- 1: Aspect Ratio
- 2: Warping
- 3: Skewness
- 4: Edge length
- 5: Area
- 6: Node Valence
- 7: Interior angle
- 8: Taper
- 9: Duplicate Elements
- 10: Node free edges

<!-- @since:5.0.1 -->
### 6. Int

Condition Display

- 0: {'<='}
- 1: {'>='}
- 2: {'<'}
- 3: {'>'}

<!-- @since:5.0.1 -->
### 7. double

Display value

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
### 7. A list of error elements.

<!-- @since:5.1.0 -->
### 8. A list of error element edge.

## Sample Code

```psj {23}
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

result=JPT.Exec('MC _Mesh _Quality _Manual _Check _Quad([3:1], [], [], 1, 0, 0, 0.1)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)
if splitted[0]=='1':
    success _flag,min,max,avg,target _num,error _num,errors1,errors2=splitted
    print(f'The number of elements that have stretch error is {error _num}. max value={max}, min value={min}')
```
