---
title: "MeshCleanup.Cleanup.TetVolMesh()"
description: "Command for cleaning tetrahedral mesh by Metric:Volume."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > Manual Check > Tet"
macro_link: "[CleaningVolumeMesh](../../macro/mesh-cleanup/CleaningVolumeMesh)"
---

## Description

Command for cleaning tetrahedral mesh by Metric:Volume.

## Syntax

```psj
MeshCleanup.Cleanup.TetVolMesh(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The target parts.

### `crlElems` @type(List\[Cursor]) @required

- The target elements.

### `dLimitValue` @type(Double)

- The cleaning threshold (e.g., minimum volume).
- Default value is 0.0.

### `iMode` @type(Integer)

- The cleaning mode.
  - 0: Standard
  - 1: Aggressive
  - 2: Remove
- Default value is 0.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{31-36}
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
