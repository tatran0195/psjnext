---
title: "MeshCleanup.Cleanup.TetEdge()"
description: "Command for cleaning tetrahedral mesh elements by edge length."
version _introduced: "5.1.0"
available _versions: "all"
macro _link: "[MC _TET _EDGE](../../macro/mesh-cleanup/MC _TET _EDGE)"
---

## Description

Command for cleaning tetrahedral mesh elements by edge length.

## Syntax

```psj
MeshCleanup.Cleanup.TetEdge(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor Pair] @required -->
### `crplElemEdges`

- The target element edges.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iCondition`

- The condition.
  - 0: <=, Collapse the elements to cleanup.
  - 1: >=, Split the elements to cleanup.
  - 2: <, Collapse the elements to cleanup.
  - 3: >, Split the elements to cleanup.

<!-- @since:5.1.0 @type:Double @optional -->
### `dLimitValue`

- The cleanup threshold.
- Default value is 0.0.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iMode`

- The cleanup mode.
  - 0: Standard
  - 1: Aggressive
- Default value is 0.

<!-- @since:5.1.0 @type:Integer @optional -->
### `iNonManifold`

- Whether to include non-manifold elements.
  - 0: Exclude
  - 1: Include
- Default value is 0.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj {32-36}
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537,
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(7), Node(15))], 
    dRatio=0.99)

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  iRegion=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=True,
  iPartColor=65280,
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=6,
  iCheckCondition=0,
  dLimitValue=0.0001,
)

print(result[7])
print(f"Number of error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetEdge(
  crplElemEdges=result[7],
  iCondition=0,
  dLimitValue=0.0001,
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=6,
  iCheckCondition=0,
  dLimitValue=0.0001,
)
print(f"Number of error elements: {result[5]}")
```
