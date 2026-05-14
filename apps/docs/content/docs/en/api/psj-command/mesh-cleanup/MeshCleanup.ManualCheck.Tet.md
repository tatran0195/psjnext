---
title: "MeshCleanup.ManualCheck.Tet()"
description: "Correct the solid mesh (Tet4/Tet10) according to the selected quality standard"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > ManualCheck > Tet"
macro _link: ""
---

## Description

Correct the solid mesh (Tet4/Tet10) according to the selected quality standard.

## Syntax

```psj
MeshCleanup.ManualCheck.Tet(...)
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
  - 2: Volume
  - 3: Jacob. Factor
  - 4: Tet Collapse
  - 5: Tet Skew
  - 6: Edge Length
  - 7: Unstable
  - 8: Time Step (Abaqus)
  - 9: Triangle Height
  - 10: Interior Angle

<!-- @since:5.1.0 @type:Integer @optional -->
### `iCheckCondition`

- The inequality sign for the threshold value.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 0 (Less than and equal).
  - If iElemQualityType = 5: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 6: The default value is 0 (Less than and equal).
  - If iElemQualityType = 7: The default value is 0 (Less than and equal).
  - If iElemQualityType = 8: The default value is 0 (Less than and equal).
  - If iElemQualityType = 9: The default value is 0 (Less than and equal).
  - If iElemQualityType = 10: The default value is 0 (Less than and equal).

<!-- @since:5.1.0 @type:Double @optional -->
### `dLimitValue`

- The threshold value will be used to detect and display the elements violated the specified mesh quality standard.
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 0.0.
  - If iElemQualityType = 3: The default value is 0.0.
  - If iElemQualityType = 4: The default value is 0.05.
  - If iElemQualityType = 5: The default value is 0.9
  - If iElemQualityType = 6: The default value is 0.1.
  - If iElemQualityType = 7: The default value is 2.0.
  - If iElemQualityType = 8: The default value is 1.0E-10.
  - If iElemQualityType = 9: The default value is 0.1.
  - If iElemQualityType = 10: The default value is 10.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dSafetyFactor`

- The safety factor value of elements to be displayed. This argument is used when iElementQualityType = 8, 9, or 10.

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

```psj {29}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                ilAxialNodes=[10, 10, 2], 
                strName="Cube _1", 
                iPartColor=13259210)

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE _MESH(
                        dMaxElemSize=0.1, 
                        dGeomAngle=0.7853981634, 
                        dMinStretchVal=0.0, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0))

Meshing.SolidMeshing(crlParts=[Part(1)], 
                    bTet10=True, 
                    dGradingFactor=1.0, 
                    iSpeedVsQual=1, 
                    bSafeMode=False, 
                    iParallel=8, 
                    bSurfaceNodes=False, 
                    bEdgeNodes=False, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

# Check mesh quality
result = MeshCleanup.ManualCheck.Tet(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1)
(success _flag,min,max,avg,target _num,error _num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error _num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
```
