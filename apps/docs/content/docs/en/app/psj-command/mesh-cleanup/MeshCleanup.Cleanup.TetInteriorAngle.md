---
title: "MeshCleanup.Cleanup.TetInteriorAngle()"
description: "Command for cleaning tetrahedral mesh by Metric:Interior Angle."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > Manual Check > Tet"
---

## Description

Command for cleaning tetrahedral mesh by Metric:Interior Angle.

## Syntax

```psj
MeshCleanup.Cleanup.TetInteriorAngle(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The target parts.

### `crlElems` @type(List\[Cursor]) @required

- The target elements.

### `dLimitValue` @type(Double)

- The cleaning threshold (e.g., minimum volume).
- Default value is 0.0.

### `iCondition` @type(Integer)

- The condition.
  - 0: <=, Collapse the elements to cleanup.
  - 1: >=, Split the elements to cleanup.
  - 2: <, Collapse the elements to cleanup.
  - 3: >, Split the elements to cleanup.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{24-28}
Geometry.Part.Cube()

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  bTet10=True, 
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=False,
  iPartColor=65280
)

# 110 elements found
result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=10,
  iCheckCondition=0,
  dLimitValue=30
)
print(f"Number of error elements is {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetInteriorAngle(
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=30
)

# Half of them are cleanupped
result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=10,
  iCheckCondition=0,
  dLimitValue=30
)
print(f"Number of error elements is {result[5]}")
```
