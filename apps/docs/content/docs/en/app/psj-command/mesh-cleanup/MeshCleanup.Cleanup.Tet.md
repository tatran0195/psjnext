---
title: "MeshCleanup.Cleanup.Tet()"
description: "Command for cleaning tetrahedral mesh elements based on quality check results."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > ManualCheck > Tet"
macro_link: "[MC_Mesh_Quality_Manual_Check_Tet](../../macro/mesh-cleanup/MC_Mesh_Quality_Manual_Check_Tet)"
---

## Description

Command for cleaning tetrahedral mesh elements based on quality check results.

## Syntax

```psj
MeshCleanup.Cleanup.Tet(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The target entities. The targets can be a mix of Body, Face, or Element.

### `iElemType` @type(Integer)

- The element type.
- Default value is 0.

### `iElemQualityType` @type(Integer)

- The quality metric.
  - 0: Stretch
  - 3: Jacob. Factor
  - 7: Unstable
  - 8: Time Step (Abaqus)
- Default value is 0.

### `dMinValue` @type(Double)

- The minimum quality value (statistics).
- Default value is 0.0.

### `dMaxValue` @type(Double)

- The maximum quality value (statistics).
- Default value is 0.0.

### `dAverageValue` @type(Double)

- The average quality value (statistics).
- Default value is 0.0.

### `iTotalEntities` @type(Integer)

- The total number of target entities (statistics).
- Default value is 0.

### `iCheckCondition` @type(Integer)

- The check condition.
- Default value is 0.

### `dLimitValue` @type(Double)

- The cleanup threshold.
- Default value is 0.0.

### `dSafetyFactor` @type(Double)

- The safety factor.
- Default value is 1.0.

### `iFailedElements` @type(Integer)

- The number of failed elements (statistics).
- Default value is 0.

### `iMode` @type(Integer)

- The cleanup mode.
  - 0: Standard
  - 1: Aggressive
- Default value is 0.

### `bNonmanifold` @type(Boolean)

- Whether to include elements with non-manifold edges.
- Default value is False.

### `bInternalMeshOnly` @type(Boolean)

- Whether to target internal mesh only.
- Default value is False.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj{35-41}
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
