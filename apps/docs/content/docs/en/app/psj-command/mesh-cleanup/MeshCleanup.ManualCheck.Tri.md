---
title: "MeshCleanup.ManualCheck.Tri()"
description: "Correct the surface mesh (TRI3/TRI6) according to the selected quality standard"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > ManualCheck > Tri"
macro_link: ""
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Correct the surface mesh (TRI3/TRI6) according to the selected quality standard"]}
   [param_rename_candidate] 'iCheckCondition' may be a rename of 'nCheckCondition' (93% similar)
     context: {"from":"nCheckCondition","to":"iCheckCondition","similarity":0.9333333333333333}
   [param_removed_unexpectedly] Param 'crlParts' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'nElemType' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'veQuality' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_decorator_changed] Param 'dLimitValue' @default changed from '0.0' to '(none)' in v5.1.0
     context: {"param":"dLimitValue","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0"}
   [param_removed_unexpectedly] Param 'CFLValue' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'nNonManifold' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'nCleanupMode' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'crlElems' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Correct the surface mesh (TRI3/TRI6) according to the selected quality standard.

## Syntax

```psj
MeshCleanup.ManualCheck.Tri(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required @since(5.1.0)

- The targets to check mesh quality. The targets can be part, face or 2D element.

### `iElemQualityType` @type(Integer) @required @since(5.1.0)

- The standard method used to check mesh quality.
  - 0: Stretch
  - 1: Aspect Ratio
  - 2: Edge Length
  - 3: Area
  - 4: Node Valence
  - 5: Interior Angle
  - 6: Duplicate Element
  - 7: Node Free Edge

### `iCheckCondition` @type(Integer) @since(5.1.0)

- The inequality sign for the threshold value.
  - If iElemQualityType = 0: The default value is 0 (Less than and equal).
  - If iElemQualityType = 1: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 2: The default value is 0 (Less than and equal).
  - If iElemQualityType = 3: The default value is 0 (Less than and equal).
  - If iElemQualityType = 4: The default value is 2 (Greater than and equal).
  - If iElemQualityType = 5: The default value is 0 (Less than and equal).
  - If iElemQualityType = 7: The default value is 2 (Greater than and equal).

### `dLimitValue` @type(Double)

- The threshold value will be used to detect and display the elements violated the specified mesh quality standard.
  - If iElemQualityType = 0: The default value is 0.1.
  - If iElemQualityType = 1: The default value is 10.0.
  - If iElemQualityType = 2: The default value is 0.1.
  - If iElemQualityType = 3: The default value is 0.01.
  - If iElemQualityType = 4: The default value is 10.0.
  - If iElemQualityType = 5: The default value is 10.0.
  - If iElemQualityType = 7: The default value is 4.0.

### `crlParts` @type(List\[Cursor]) @default(\[]) @deprecated @until(5.1.0)

- The part.

### `nElemType` @type(N\_ELEM\_TYPE) @default(0) @deprecated @until(5.1.0)

- The element type.

### `veQuality` @type(VE\_QUALITY) @default(0) @deprecated @until(5.1.0)

- The quality.

### `nCheckCondition` @type(N\_CHECK\_CONDITION) @default(0) @deprecated @until(5.1.0)

- The check condition.

### `CFLValue` @type(CFLVALUE) @default(0.0) @deprecated @until(5.1.0)

- The l value.

### `nNonManifold` @type(N\_NON\_MANIFOLD) @default(0) @deprecated @until(5.1.0)

- The non manifold.

### `nCleanupMode` @type(N\_CLEANUP\_MODE) @default(0) @deprecated @until(5.1.0)

- The cleanup mode.

### `crlElems` @type(List\[Cursor]) @default(\[]) @deprecated @until(5.1.0)

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
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.1, 
                        dGeomAngle=0.7853981634, 
                        dMinStretchVal=0.0, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0))

# Check mesh quality
result = MeshCleanup.ManualCheck.Tri(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1)
(success_flag,min,max,avg,target_num,error_num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error_num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
```
