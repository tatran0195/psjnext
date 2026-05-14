---
title: "MeshCleanup.Cleanup.TetTriangleHeight()"
description: "Command for cleaning tetrahedral mesh by Metric:Triangle Height."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > Manual Check > Tet"
---

## Description

Command for cleaning tetrahedral mesh by Metric:Triangle Height.

## Syntax

```psj
MeshCleanup.Cleanup.TetTriangleHeight(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlParts`

- The target parts.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlElems`

- The target elements.

<!-- @since:5.1.0 @type:Double @optional -->
### `dLimitValue`

- The cleaning threshold (e.g., minimum volume).
- Default value is 0.0.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iCondition`

- The condition.
  - 0: <=, Collapse the elements to cleanup.
  - 1: >=, Split the elements to cleanup.
  - 2: <, Collapse the elements to cleanup.
  - 3: >, Split the elements to cleanup.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj {34-39}
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

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=9,
  iCheckCondition=0,
  dLimitValue=0.0003
)

print(f"Number of the error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetTriangleHeight(
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=0.0003,
  iCondition=0
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=9,
  iCheckCondition=0,
  dLimitValue=0.0003
)

print(f"Number of the error elements: {result[5]}")
```
