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

<!-- @since:5.1.0 @required -->
### crlDesignedParts

- Specify designed parts.

<!-- @since:5.1.0 @optional -->
### crlNonDesignedParts

- Specify non-designed parts.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dDensityRatio

- Specify threshold density ratio to filter regions.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bKeepSharedNodeOnBody

- Specify whether to keep shared nodes on body interface.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iCycle

- Specify the number of smoothing cycles.
- The default value is 50.

<!-- @since:5.1.0 @optional -->
### dFactor

- Specify the smoothing intensity factor.
- The default value is 0.3.

<!-- @since:5.1.0 @optional -->
### dMeshSize

- Specify target mesh size for smoothing.
- The default value is 3.0.

<!-- @since:5.1.0 @optional -->
### iRemovedLayers

- Specify the number of boundary layers to remove.
- The default value is 1.

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
