---
title: "Post.OptimizationToolkit.OptimizedShapeSmooth()"
description: "Create iso-surfaces (smoothing) based on nodal density and element density within optimization results, and convert them into a mesh."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > OptimizationToolkit > OptimizedShapeSmooth"
macro_link: "[CmdOptimizeShapeSmoothFunc](../../macro/post/CmdOptimizeShapeSmoothFunc)"
---

## Description

Create iso-surfaces (smoothing) based on nodal density and element density within optimization results, and convert them into a mesh.

## Syntax

```psj
Post.OptimizationToolkit.OptimizedShapeSmooth(...)
```

## Inputs

### `crlDesignedParts` @type(List\[Cursor]) @required

- Designed parts.

### `crlNonDesignedParts` @type(List\[Cursor]) @default(\[])

- Non-designed parts.

### `dDensityRatio` @type(Double) @default(0.0)

- Threshold density ratio to filter regions.

### `bKeepSharedNodeOnBody` @type(Boolean) @default(False)

- Whether to keep shared nodes on body interface.

### `iCycle` @type(Integer) @default(50)

- The number of smoothing cycles.

### `dFactor` @type(Double) @default(0.3)

- The smoothing intensity factor.

### `dMeshSize` @type(Double) @default(3.0)

- Target mesh size for smoothing.

### `iRemovedLayers` @type(Integer) @default(1)

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
