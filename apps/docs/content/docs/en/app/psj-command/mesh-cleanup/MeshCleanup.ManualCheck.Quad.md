---
title: "MeshCleanup.ManualCheck.Quad()"
description: "Correct the surface mesh (Quad4/Quad8) according to the selected quality standard"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > ManualCheck > Quad"
macro_link: ""
---

## Description

Correct the surface mesh (Quad4/Quad8) according to the selected quality standard.

## Syntax

```psj
MeshCleanup.ManualCheck.Quad(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- Specifying the targets to check mesh quality. The targets can be part, face or 2D element.

### `iElemQualityType` @type(Integer) @required

- The standard method used to check mesh quality.
  - 0: Stretch
  - 1: Aspect Ratio
  - 2: Warping
  - 3: Skewness
  - 4: Edge Length
  - 5: Area
  - 6: Node Valence
  - 7: Interior Angle
  - 8: Taper
  - 9: Duplicate Element
  - 10: Node Free Edge
  - 11: Percentage of TRIs

### `iCheckCondition` @type(Integer)

- The inequality sign for the threshold value.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 0 (Less than and equal).
  - If iElemQualityType = 5: The default value is 0 (Less than and equal).
  - If iElemQualityType = 6: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 7: The default value is 0 (Less than and equal).
  - If iElemQualityType = 8: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 10: The default value is 2 (Greater than and equal).

### `dLimitValue` @type(Double)

- The threshold value will be used to detect and display the elements violated the specified mesh quality standard.
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 1.0.
  - If iElemQualityType = 3: The default value is 70.0.
  - If iElemQualityType = 4: The default value is 0.1.
  - If iElemQualityType = 5: The default value is 0.01.
  - If iElemQualityType = 6: The default value is 10.0.
  - If iElemQualityType = 7: The default value is 10.0.
  - If iElemQualityType = 8: The default value is 0.5.
  - If iElemQualityType = 10: The default value is 4.

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

```psj {20}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGradingFactor=0.5, iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        bFMesher=True, 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.ManualCheck.Quad(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1)
(success_flag,min,max,avg,target_num,error_num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error_num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
```
