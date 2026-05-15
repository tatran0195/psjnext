---
title: "MeshCleanup.Cleanup.TetVolMesh()"
description: "Command for cleaning tetrahedral mesh by Metric:Volume."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > Manual Check > Tet"
macro _link: "[CleaningVolumeMesh](../../macro/mesh-cleanup/CleaningVolumeMesh)"
---

## Description

Command for cleaning tetrahedral mesh by Metric:Volume.

## Syntax

```psj
MeshCleanup.Cleanup.TetVolMesh(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlParts

- Specify the target parts.

<!-- @since:5.1.0 @required -->
### crlElems

- Specify the target elements.

<!-- @since:5.1.0 @optional -->
### dLimitValue

- Specify the cleaning threshold (e.g., minimum volume).
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iMode

- Specify the cleaning mode.
  - 0: Standard
  - 1: Aggressive
  - 2: Remove
- Default value is 0.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj {31-36}
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

MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=2,
  iCheckCondition=0,
  dLimitValue=2e-09
)

MeshCleanup.Cleanup.TetVolMesh(
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=2e-09,
  iMode=1
)

MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=2,
  iCheckCondition=0,
  dLimitValue=2e-09
)
```
