---
title: "MC _Mesh _Quality _Manual _Check _Hex()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Correct the solid mesh (Hex8) according to the selected quality standard.

## Syntax

```psj
MC _Mesh _Quality _Manual _Check _Hex(cursor[] crBody, cursor[] crFace, cursor[] crElem,
    int iElemType, int elemQualityType, int iCond, double dSafeFact, double dDispValue)
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

Element type (3-Hex Element)

<!-- @since:5.0.1 -->
### 5. Int

Element quality metric type

- 0: Stretch
- 1: Aspect Ratio
- 2: Edge Length
- 3: Volume
- 4: Unstable
- 5: Time Step (Abaqus)

<!-- @since:5.0.1 -->
### 6. Int

Condition Display

<!-- @since:5.0.1 -->
### 7. double

Safety factor

<!-- @since:5.0.1 -->
### 8. double

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
### 7. A list of erorr elements.

<!-- @since:5.1.0 -->
### 8. A list of error element edge.

## Sample Code

```psj {25}
import re

Geometry.Part.Cube()

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

HexModeling.Linear(
    crlFaces=[Face(26)], 
    dLength=0.0001, iLayer=1, 
    vecSweepDirection=[0.0, 0.0, 1.0], 
    bDeleteOriginalParts=True)

result=JPT.Exec('MC _Mesh _Quality _Manual _Check _Hex([3:1], [], [], 3, 0, 0, 1, 0.1)')

splitted = re.split(r',\s*(?![^(\[\]]*\])', result)
if splitted[0]=='1':
    success _flag,min,max,avg,target _num,error _num,errors1,errors2=splitted
    print(f'The number of elements that have stretch error is {error _num}. max value={max}, min value={min}')
```
