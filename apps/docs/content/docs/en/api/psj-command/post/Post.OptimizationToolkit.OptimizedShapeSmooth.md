---
title: "Post.OptimizationToolkit.OptimizedShapeSmooth()"
description: "Create iso-surfaces (smoothing) based on nodal density and element density within optimization results, and convert them into a mesh."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > OptimizationToolkit > OptimizedShapeSmooth"
macro _link: "[CmdOptimizeShapeSmoothFunc](../../macro/post/CmdOptimizeShapeSmoothFunc)"
---

## Description

Create iso-surfaces (smoothing) based on nodal density and element density within optimization results, and convert them into a mesh.

## Syntax

```psj
Post.OptimizationToolkit.OptimizedShapeSmooth(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlDesignedParts`

- The designed parts.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlNonDesignedParts`

- The non-designed parts.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dDensityRatio`

- The threshold density ratio to filter regions.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bKeepSharedNodeOnBody`

- Whether to keep shared nodes on body interface.

<!-- @since:5.1.0 @type:Integer @optional @default:50 -->
### `iCycle`

- The number of smoothing cycles.

<!-- @since:5.1.0 @type:Double @optional @default:0.3 -->
### `dFactor`

- The smoothing intensity factor.

<!-- @since:5.1.0 @type:Double @optional @default:3.0 -->
### `dMeshSize`

- The target mesh size for smoothing.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iRemovedLayers`

- The number of boundary layers to remove.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {17-21}
# Import arbitrary topology optimization result
Home.ImportResults.ADVC("C:/Temp/ADVCResult", iImportType=1)

Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(postResultKey=PostResultKey(
            iAnalysisType=11, 
            iResultSet=10, 
            iTimeStep=-1, 
            strResultName="DensityRatio", 
            strResultCompName="DensityRatio", 
            iResultPos=2), 
        postDataOp=PostDataOp(iResultLocation=2, iOptionCoord=1))])

# Set appropriate values
Post.OptimizationToolkit.OptimizedShapeSmooth(
    crlDesignedParts=[Part(1)], 
    dDensityRatio=0.75, 
    bKeepSharedNodeOnBody=True, 
    dMeshSize=0.002845)
```
