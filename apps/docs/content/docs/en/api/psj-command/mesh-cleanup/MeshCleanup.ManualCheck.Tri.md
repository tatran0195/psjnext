---
title: "MeshCleanup.ManualCheck.Tri()"
description: "Correct the surface mesh (TRI3/TRI6) according to the selected quality standard"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > ManualCheck > Tri"
macro _link: ""
---

## Description

Correct the surface mesh (TRI3/TRI6) according to the selected quality standard.

## Syntax

```psj
MeshCleanup.ManualCheck.Tri(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The targets to check mesh quality. The targets can be part, face or 2D element.

<!-- @since:5.1.0 @type:Integer @required -->
### `iElemQualityType`

- The standard method used to check mesh quality.
  - 0: Stretch
  - 1: Aspect Ratio
  - 2: Edge Length
  - 3: Area
  - 4: Node Valence
  - 5: Interior Angle
  - 6: Duplicate Element
  - 7: Node Free Edge

<!-- @since:5.1.0 @type:Integer @optional -->
### `iCheckCondition`

- The inequality sign for the threshold value.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 5: The default value is 0 (Less than and equal).
  - If iElemQualityType = 7: The default value is 2 (Greater than and equal).

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
<!-- @since:5.1.0 -->
### `dLimitValue`

- The threshold value will be used to detect and display the elements violated the specified mesh quality standard.
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 0.1.
  - If iElemQualityType = 3: The default value is 0.01.
  - If iElemQualityType = 4: The default value is 10.0.
  - If iElemQualityType = 5: The default value is 10.0.
  - If iElemQualityType = 7: The default value is 4.0.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:N _ELEM _TYPE @removed:5.1.0 @optional @deprecated @default:0 -->
### `nElemType`

- The element type.

<!-- @since:5.0.1 @type:VE _QUALITY @removed:5.1.0 @optional @deprecated @default:0 -->
### `veQuality`

- The quality.

<!-- @since:5.0.1 @type:N _CHECK _CONDITION @removed:5.1.0 @optional @deprecated @default:0 -->
### `nCheckCondition`

- The check condition.

<!-- @since:5.0.1 @type:CFLVALUE @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `CFLValue`

- The l value.

<!-- @since:5.0.1 @type:N _NON _MANIFOLD @removed:5.1.0 @optional @deprecated @default:0 -->
### `nNonManifold`

- The non manifold.

<!-- @since:5.0.1 @type:N _CLEANUP _MODE @removed:5.1.0 @optional @deprecated @default:0 -->
### `nCleanupMode`

- The cleanup mode.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlElems`

- The element.

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

```psj {16}
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE _MESH(
                        dMaxElemSize=0.1, 
                        dGeomAngle=0.7853981634, 
                        dMinStretchVal=0.0, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0))

# Check mesh quality
result = MeshCleanup.ManualCheck.Tri(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1)
(success _flag,min,max,avg,target _num,error _num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error _num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
```
