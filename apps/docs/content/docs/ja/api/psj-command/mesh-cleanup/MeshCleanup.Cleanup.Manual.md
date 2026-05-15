---
title: "MeshCleanup.Cleanup.Manual()"
description: "Command for cleaning surface mesh elements that do not meet the specified quality criteria."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MeshCleanup > Auto Check > Cleanup"
macro _link: "[CleanupManual](../../macro/mesh-cleanup/CleanupManual)"
---

## Description

Command for cleaning surface mesh elements that do not meet the specified quality criteria.

## Syntax

```psj
MeshCleanup.Cleanup.Manual(...)
```

## Inputs

### `crlParts`

- A _List of Cursor_ of parts to be cleaned up.
- Default value is \[].

<!-- @since:5.1.0 @optional -->
### iElemType

- Specify the type of target elements.
  - 0: Tri
  - 1: Quad
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### iVeQuality

- Specify the quality metric.
  - 0: Stretch
  - 1: Aspect Ratio
  - 2: Edge Length
  - 3: Area
  - 4: Warp
  - 5: Skew
  - 6: VDS Stretch
  - 7: Node Valence
  - 8: Volume
  - 9: Interior Angle
  - 10: Jacobian
  - 11: Taper
  - 12: Node Free Edges
  - 13: Duplicate Elements
  - 14: Tet Collapse
  - 15: Tet Skew
  - 16: Tet Collapse 2
  - 17: Vol Aspect Ratio
  - 18: Unstable
  - 19: CFL Condition
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### iCheckCondition

- Specify the check condition.
  - 0: <=
  - 1: >=
  - 2: <
  - 3: >
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### dLimitValue

- Specify the quality threshold.
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dCFLValue

- Specify the CFL threshold value.
- Default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iNonManifold

- Specify whether to include non-manifold elements.
  - 0: Exclude
  - 1: Include
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### iCleanupMode

- Specify the cleanup mode.
  - 0: Standard
  - 1: Aggressive
- Default value is 0.

<!-- @since:5.1.0 @optional -->
### crlElems

- Specify the target elements.
- Default value is \[].

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```pj {20-25}
# Prepare Model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)
MeshEdit.CreateNode.Point(
  iNewNodeID=27,
  posPoint=[
    0.005225089844316244,
    0.00481416005641222,
    0.009999999776482582,
  ],
  crTarget=Face(26),
)

# Check
ret = MeshCleanup.ManualCheck.Tri(
  crlTargets=[Part(1)],
  iCheckCondition=0,
  dLimitValue=0.1,
)
print(f"number of error elements: {ret[5]}")
MeshCleanup.Cleanup.Manual(
  crlParts=[Part(1)],
  dLimitValue=0.1,
  dCFLValue=0.1,
  crlElems=ret[6],
)

ret = MeshCleanup.ManualCheck.Tri(
  crlTargets=[Part(1)],
  iCheckCondition=0,
  dLimitValue=0.1,
)
print(f"number of error elements: {ret[5]}")
```
