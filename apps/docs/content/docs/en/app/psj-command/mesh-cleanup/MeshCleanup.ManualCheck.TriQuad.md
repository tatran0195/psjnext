---
title: "MeshCleanup.ManualCheck.TriQuad()"
description: "Correct the surface mesh (TRI3/TRI6/QUAD4/QUAD8) according to the selected quality standard"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > ManualCheck > TriQuad"
macro_link: ""
---

## Description

Correct the surface mesh (TRI3/TRI6/QUAD4/QUAD8) according to the selected quality standard.

## Syntax

```psj
MeshCleanup.ManualCheck.TriQuad(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The targets to check mesh quality. The targets can be part, face or 2D element.

### `iElemQualityType` @type(Integer) @required

- The standard method used to check mesh quality.
  - 0: Stretch
  - 1: Aspect Ratio
  - 2: Edge Length
  - 3: Area
  - 4: Node Valence
  - 5: Interior Angle
  - 6: Unstable
  - 7: Time Step (LS-Dyna)
  - 8: Time Step (Abaqus)

### `iCheckConditionTri` @type(Integer)

- The inequality sign for the threshold value of TRI element.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 5: The default value is 0 (Less than and equal).
  - If iElemQualityType = 6: The default value is 0 (Less than and equal).
  - If iElemQualityType = 7: The default value is 0 (Less than and equal).
  - If iElemQualityType = 8: The default value is 0 (Less than and equal).

### `dLimitValueTri` @type(Double)

- The threshold value will be used to detect and display the TRI elements violated the specified mesh quality standard.
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 0.1.
  - If iElemQualityType = 3: The default value is 0.01.
  - If iElemQualityType = 4: The default value is 10.0.
  - If iElemQualityType = 5: The default value is 10.0.
  - If iElemQualityType = 5: The default value is 1.0.
  - If iElemQualityType = 7: The default value is 9.9E-06.
  - If iElemQualityType = 8: The default value is 1.0E-10.

### `dSafetyFactorTri` @type(Double) @default(1.0)

- The safety factor value of TRI elements to be displayed. This argument is used when iElementQualityType = 7, or 8.

### `iCheckConditionQuad` @type(Integer)

- The inequality sign for the threshold value of QUAD element.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 5: The default value is 0 (Less than and equal).
  - If iElemQualityType = 6: The default value is 0 (Less than and equal).
  - If iElemQualityType = 7: The default value is 0 (Less than and equal).
  - If iElemQualityType = 8: The default value is 0 (Less than and equal).

### `dLimitValueQuad` @type(Double)

- The threshold value will be used to detect and display the QUAD elements violated the specified mesh quality standard
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 0.1.
  - If iElemQualityType = 3: The default value is 0.01.
  - If iElemQualityType = 4: The default value is 10.0.
  - If iElemQualityType = 5: The default value is 10.0.
  - If iElemQualityType = 5: The default value is 1.0.
  - If iElemQualityType = 7: The default value is 9.9E-06.
  - If iElemQualityType = 8: The default value is 1.0E-10.

### `dSafetyFactorQuad` @type(Double) @default(1.0)

- The safety factor value of QUAD elements to be displayed. This argument is used when iElementQualityType = 7, or 8.

### `bIncludeDiagonalQuad` @type(Boolean) @default(True)

- To include diagonal line for QUAD. This argument is used when iElementQualityType = 7 (Time Step (LS-Dyna)).

### `iNonPrimary` @type(Integer) @default(0)

- The non primary.

## Return Code

A _Tuple_ specifying 8 values of mesh quality check in order.
1\. Succeeded(1) or Failed(0)
2\. Cutoff value (Minimum) (Tri check)
3\. Cutoff value (Maximum) (Tri check)
4\. Cutoff value (Average) (Tri check)
5\. Number of measured elements (Tri check)
6\. Number of error elements (Tri check)
7\. A list of ID error elements (Tri check)
8\. A list of error element edges (Tri check)
9\. Cutoff value (Minimum) (Quad check)
10\. Cutoff value (Maximum) (Quad check)
11\. Cutoff value (Average) (Quad check)
12\. Number of measured elements (Quad check)
13\. Number of error elements (Quad check)
14\. A list of ID error elements (Quad check)
15\. A list of error element edges (Quad check)

## Sample Code

```psj {23-27}
# Prepare model
Geometry.Part.Trapezoid(dlLength=[0.01, 0.001, 0.01], 
                        dTopXLength=0.1, 
                        strName="Trapezoid_1", 
                        iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGeomMinSize=0.0001, 
                        dGradingFactor=0.5, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                    bFMesher=True, 
                    iThreadNum=16)

# Check mesh quality
result = MeshCleanup.ManualCheck.TriQuad(crlTargets=[Part(1)], 
                                        iCheckConditionTri=0, 
                                        dLimitValueTri=0.2, 
                                        iCheckConditionQuad=0, 
                                        dLimitValueQuad=0.1)
if result[0] == 1:
    if result[5] > 0:
        print(f'The number of Tri elements that have stretch error is {result[5]}. max value={result[1]}, min value={result[2]}')
        print(f'The error elements are {result[6]}')
    else:
        print("There is no Tri error element")
    if result[12] > 0:
        print(f'The number of Quad elements that have stretch error is {result[12]}. max value={result[8]}, min value={result[9]}')
        print(f'The error elements are {result[13]}')
    else:
        print("There is no Quad error element")
else:
    print("There is no error element")
```
