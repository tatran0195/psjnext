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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The target Parts.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTet10`

- The to enable (_True_) or disable (_False_) the Tet10 creation. If enabled, solid elements Tet4 will be converted to Tet10.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dGradingFactor`

- The grading factor. This parameter affects the change of mesh size from small mesh area to large mesh area.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dStretchLimit`

- The stretch limit of the result mesh. Created mesh will be adjusted in order to reduce the amount of elements whose stretch is greater than this parameter.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSpeedVsQual`

- The priority between mesh quality and mesh generation speed.
  - If 0: Speed is prioritized (Fastest).
  - If 1: Mesh quality is prioritized (Optimized).

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSpeedVsMem`

- The priority between memory usage and mesh generation speed.
  - If 0: Speed is prioritized (Standard).
  - If 1: The reduction of memory usage is prioritized (Low Memory).

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRegion`

- The region where mesh will be generated.
  - If 0: Create the solid elements in only the main area of part (Main region).
  - If 1: Create solid element to all the area of the part (All Region).

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bInternalNodes`

- The to enable (_True_) or disable (_False_) the creation of extra nodes. If disabled, nodes on surfaces will be modified. If enabled, only nodes will only be created inside target parts.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bSafeMode`

- The to enable (_True_) or disable (_False_) safe mode. This mode is used to enhance very small element's quality.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iParallel`

- The number of CPU threads for parallel meshing. This parameter must be smaller than the maximum number of CPU cores.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bSurfaceNodes`

- The to enable (_True_) or disable (_False_) the cleaning of surface nodes. This parameter is for clean-up step. If enabled, surface nodes will be slightly moved to improve mesh quality.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bEdgeNodes`

- The to enable (_True_) or disable (_False_) the cleaning of edge nodes. This parameter is for clean-up step. If enabled, edge nodes will be slightly moved to improve mesh quality.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bPreservation`

- The to enable (_True_) or disable (_False_) the preservation of nodes. This parameter is for clean-up step. If disabled, nodes can be moved to improve mesh quality.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bInternalMeshOnly`

- The to enable (_True_) or disable (_False_) the correction of internal mesh only. This parameter is for clean-up step.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMeshColor`

- The to enable (_True_) or disable (_False_) the use of mesh color. If enabled, target parts' color will be changed according to `iPartColor`.

<!-- @since:5.0.1 @type:Integer @optional @default:2763429 -->
### `iPartColor`

- The color of the result mesh parts.

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
