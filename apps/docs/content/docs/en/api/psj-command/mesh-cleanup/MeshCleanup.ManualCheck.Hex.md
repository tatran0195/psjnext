---
title: "MeshCleanup.ManualCheck.Hex()"
description: "Correct the solid mesh (Hex8) according to the selected quality standard"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > ManualCheck > Hex"
macro _link: ""
---

## Description

Correct the solid mesh (Hex8) according to the selected quality standard.

## Syntax

```psj
MeshCleanup.ManualCheck.Hex(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The targets to check mesh quality. The targets can be part or solid element.

<!-- @since:5.1.0 @type:Integer @required -->
### `iElemQualityType`

- The standard method used to check mesh quality.
  - 0: Stretch
  - 1: Aspect Ratio
  - 2: Edge Length
  - 3: Volume
  - 4: Unstable
  - 5: Time Step (Abaqus)

<!-- @since:5.1.0 @type:Integer @optional -->
### `iCheckCondition`

- The inequality sign for the threshold value.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 0 (Less than and equal).
  - If iElemQualityType = 5: The default value is 0 (Less than and equal).

<!-- @since:5.1.0 @type:Double @optional -->
### `dLimitValue`

- The threshold value will be used to detect and display the elements violated the specified mesh quality standard.
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 0.1.
  - If iElemQualityType = 3: The default value is 0.0.
  - If iElemQualityType = 4: The default value is 2.0.
  - If iElemQualityType = 5: The default value is 1.0E-10.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dSafetyFactor`

- The safety factor value of elements to be displayed. This argument is used when iElementQualityType = 5.

## Return Code

A _Tuple_ specifying 8 values of mesh quality check in order.
1\. Succeeded(1) or Failed(0)
2\. Cutoff value (Minimum)
3\. Cutoff value (Maximum)
4\. Cutoff value (Average)
5\. Number of measured elements.
6\. Number of error elements.
7\. A list of ID error elements.
8\. A list of error element edges.

## Sample Code

```psj {21}
# Prepare model
Geometry.Part.Cube()
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
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
HexModeling.Linear(crlFaces=[Face(26)], 
                dLength=0.0001, iLayer=1, 
                vecSweepDirection=[0.0, 0.0, 1.0], 
                bDeleteOriginalParts=True)

# Check mesh quality
result = MeshCleanup.ManualCheck.Hex(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1) 
(success _flag,min,max,avg,target _num,error _num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error _num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
```
