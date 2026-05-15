---
title: "MeshCleanup.Cleanup.Tet()"
description: "Command for cleaning tetrahedral mesh elements based on quality check results."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > ManualCheck > Tet"
macro _link: "[MC _Mesh _Quality _Manual _Check _Tet](../../macro/mesh-cleanup/MC _Mesh _Quality _Manual _Check _Tet)"
---

## Description

Command for cleaning tetrahedral mesh elements based on quality check results.

## Syntax

```psj
MeshCleanup.Cleanup.Tet(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the target entities. The targets can be a mix of Body, Face, or Element.

<!-- @since:5.1.0 @optional -->
### iElemType

- Specify the element type.
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### iElemQualityType

- Specify the quality metric.
  - 0: Stretch
  - 3: Jacob. Factor
  - 7: Unstable
  - 8: Time Step (Abaqus)
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### dMinValue

- Specify the minimum quality value (statistics).
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dMaxValue

- Specify the maximum quality value (statistics).
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dAverageValue

- Specify the average quality value (statistics).
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iTotalEntities

- Specify the total number of target entities (statistics).
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### iCheckCondition

- Specify the check condition.
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### dLimitValue

- Specify the cleanup threshold.
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dSafetyFactor

- Specify the safety factor.
- Default value is 1.0.

<!-- @since:5.1.0 @optional -->
### iFailedElements

- Specify the number of failed elements (statistics).
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### iMode

- Specify the cleanup mode.
  - 0: Standard
  - 1: Aggressive
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### bNonmanifold

- Specify whether to include elements with non-manifold edges.
- Default value is False.

<!-- @since:5.1.0 @optional -->
### bInternalMeshOnly

- Specify whether to target internal mesh only.
- Default value is False.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```pj {35-41}
# Prepare model
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537
)

MeshEdit.MoveNode.CADFollows(
  crlNodes=[Node(15)],
  dMovedPosX=10.0,
  dMovedPosY=10.0,
  dMovedPosZ=9.60758
)

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  iRegion=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=False,
  iPartColor=65280
)

# Check
ret = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=0,
  iCheckCondition=0,
  dLimitValue=0.1
)
print(f"number of error elements: {ret[5]}")

# Cleanup
MeshCleanup.Cleanup.Tet(
    crlTargets=[Part(1)], 
    dMinValue=ret[1], 
    dMaxValue=ret[2], 
    dAverageValue=ret[3], 
    iTotalEntities=ret[4], 
    iCheckCondition=0, 
    dLimitValue=0.1, 
    iFailedElements=ret[5],
    iCleanupCheck=1,
    iMode=1
)

ret = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=0,
  iCheckCondition=0,
  dLimitValue=0.1
)
print(f"number of error elements: {ret[5]}")
```
