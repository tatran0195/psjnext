---
title: "Meshing.SolidMeshing()"
description: "Do 3D meshing (Tetrahedral) for the selected parts"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > SolidMeshing"
macro _link: "[VolMeshing](../../macro/meshing/VolMeshing)"
---

## Description

Do 3D meshing (Tetrahedral) for the selected parts.

:::note

In case the total number of selected parts = 0, all the existing parts will be used as an input.

:::

## Syntax

```psj
Meshing.SolidMeshing(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the target Parts.

### `bTet10`

- A _Boolean_ to enable (_True_) or disable (_False_) the Tet10 creation. If enabled, solid elements Tet4 will be converted to Tet10.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dGradingFactor

- Specify the grading factor. This parameter affects the change of mesh size from small mesh area to large mesh area.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dStretchLimit

- Specify the stretch limit of the result mesh. Created mesh will be adjusted in order to reduce the amount of elements whose stretch is greater than this parameter.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSpeedVsQual

- Specify the priority between mesh quality and mesh generation speed.
  - If 0: Speed is prioritized (Fastest).
  - If 1: Mesh quality is prioritized (Optimized).
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSpeedVsMem

- Specify the priority between memory usage and mesh generation speed.
  - If 0: Speed is prioritized (Standard).
  - If 1: The reduction of memory usage is prioritized (Low Memory).
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRegion

- Specify the region where mesh will be generated.
  - If 0: Create the solid elements in only the main area of part (Main region).
  - If 1: Create solid element to all the area of the part (All Region).
- The default value is 0.

### `bInternalNodes`

- A _Boolean_ to enable (_True_) or disable (_False_) the creation of extra nodes. If disabled, nodes on surfaces will be modified. If enabled, only nodes will only be created inside target parts.
- The default value is _True_.

### `bSafeMode`

- A _Boolean_ to enable (_True_) or disable (_False_) safe mode. This mode is used to enhance very small element's quality.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### iParallel

- Specify the number of CPU threads for parallel meshing. This parameter must be smaller than the maximum number of CPU cores.
- The default value is 0.

### `bSurfaceNodes`

- A _Boolean_ to enable (_True_) or disable (_False_) the cleaning of surface nodes. This parameter is for clean-up step. If enabled, surface nodes will be slightly moved to improve mesh quality.
- The default value is _True_.

### `bEdgeNodes`

- A _Boolean_ to enable (_True_) or disable (_False_) the cleaning of edge nodes. This parameter is for clean-up step. If enabled, edge nodes will be slightly moved to improve mesh quality.
- The default value is _True_.

### `bPreservation`

- A _Boolean_ to enable (_True_) or disable (_False_) the preservation of nodes. This parameter is for clean-up step. If disabled, nodes can be moved to improve mesh quality.
- The default value is _True_.

### `bInternalMeshOnly`

- A _Boolean_ to enable (_True_) or disable (_False_) the correction of internal mesh only. This parameter is for clean-up step.
- The default value is _True_.

### `bMeshColor`

- A _Boolean_ to enable (_True_) or disable (_False_) the use of mesh color. If enabled, target parts' color will be changed according to `iPartColor`.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iPartColor

- Specify the color of the result mesh parts.
- The default value is 2763429.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {3,4,5,6,7,8,9,10,11,12,13,14}
Geometry.Part.Cube()

meshing _status = Meshing.SolidMeshing(crlParts=[Part(1)], 
                                      bTet10=True, 
                                      dGradingFactor=1.05, 
                                      dStretchLimit=0.1,
                                      iSpeedVsQual=1, 
                                      iRegion=1, 
                                      bSafeMode=False, 
                                      iParallel=24, 
                                      bSurfaceNodes=False, 
                                      bEdgeNodes=False,
                                      bInternalMeshOnly=False,
                                      iPartColor=65280)

JPT.Debugger(meshing _status)
```
