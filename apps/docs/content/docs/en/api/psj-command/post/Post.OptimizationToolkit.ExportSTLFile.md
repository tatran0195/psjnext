---
title: "Post.OptimizationToolkit.ExportSTLFile()"
description: "Output the currently displayed shape as an .stl file based on density threshold values."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > OptimizationToolkit > ExportSTLFile"
macro _link: "CmdOptimizeOuterShellExport"
---

## Description

Output the currently displayed shape as an .stl file based on density threshold values.

## Syntax

```psj
Post.OptimizationToolkit.ExportSTLFile(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strSTLPath`

- The Output path to save the STL file.

<!-- @since:5.1.0 @type:list of Cursor @required -->
### `crlBodies`

- The identifying the parts to export.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dDensityRatio`

- The Density Ratio used to filter outer shell geometry.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {20}
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
Post.OptimizationToolkit.EnableOptimizationMode()

# Set appropriate density value
Post.OptimizationToolkit.OptimizedShape(dTopologyDensity=0.75)

Post.OptimizationToolkit.ExportSTLFile(strSTLPath="C:/Temp/temp.stl")
```
