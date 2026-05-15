---
title: "MeshCleanup.Cleanup.Auto()"
description: "Command for automatically cleaning triangle or quadrilateral mesh elements based on quality check results."
version _introduced: "5.1.0"
available _versions: "all"
macro _link: "[CleanupAuto](../../macro/mesh-cleanup/CleanupAuto)"
---

## Description

Command for automatically cleaning triangle or quadrilateral mesh elements based on quality check results.

## Syntax

```psj
MeshCleanup.Cleanup.Auto(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlParts

- Specify the target parts.

<!-- @since:5.1.0 @required -->
### iElemType

- Specify the type of target elements.
  - 0: Triangle
  - 1: Quadrilateral

<!-- @since:5.1.0 @required -->
### blCheckCondition

- Specify the condition check enable flags for each cleanup condition.

<!-- @since:5.1.0 @required -->
### blElemQuality

- Specify the enable flags for each element quality metric.

<!-- @since:5.1.0 @required -->
### dlLimitValue

- Specify the threshold value for each quality metric.

<!-- @since:5.1.0 @required -->
### crlElems

- Specify the target elements.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj {38-45}
#Prepare Model
Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    iPartColor=7463537
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(7), Node(15))], 
    dRatio=0.99
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(16), Node(22))], 
    dRatio=0.99
)

# Check
result = MeshCleanup.AutoCheck.Tri(
    crlTargets=[Part(1)], 
    bStretchCheck=True, 
    bAspectRatioCheck=True, 
    bEdgeLengthCheck=True, 
    bAreaCheck=True, 
    bNodeValenceCheck=True, 
    bInteriorAngleCheck=True, 
    bDuplicateElemsCheck=True, 
    dStretchLimit=0.1, 
    dAspectRatioLimit=10, 
    dEdgeLengthLimit=0.0001, 
    dAreaLimit=1e-08, 
    dNodeValenceLimit=10, 
    dInteriorAngleLimit=0.174533
)

print(f"Number of error elements: {result[1]}")

# Auto cleanup
MeshCleanup.Cleanup.Auto(
    crlParts=[Part(1)], 
    iElemType=0, 
    blCheckCondition=[False, True, False, False, True, False, False], 
    blElemQuality=[False, True, True, True, True, True, True],
     dlLimitValue=[0.1, 10.0, 0.0001, 1e-08, 10.0, 10.0, 0.0], 
    crlElems=result[2]
)

result = MeshCleanup.AutoCheck.Tri(
    crlTargets=[Part(1)], 
    bStretchCheck=True, 
    bAspectRatioCheck=True, 
    bEdgeLengthCheck=True, 
    bAreaCheck=True, 
    bNodeValenceCheck=True, 
    bInteriorAngleCheck=True, 
    bDuplicateElemsCheck=True, 
    dStretchLimit=0.1, 
    dAspectRatioLimit=10, 
    dEdgeLengthLimit=0.0001, 
    dAreaLimit=1e-08, 
    dNodeValenceLimit=10, 
    dInteriorAngleLimit=0.174533
)

print(f"Number of error elements: {result[1]}")
```
