---
title: "Post.OptimizationToolkit.ExportSTLFile()"
description: "Output the currently displayed shape as an .stl file based on density threshold values."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > OptimizationToolkit > ExportSTLFile"
macro_link: "CmdOptimizeOuterShellExport"
---

## Description

Output the currently displayed shape as an .stl file based on density threshold values.

## Syntax

```psj
Post.OptimizationToolkit.ExportSTLFile(...)
```

## Inputs

### `strSTLPath` @type(String) @required

- Output path to save the STL file.

### `crlBodies` @type(list of Cursor) @required

- Identifying the parts to export.

### `dDensityRatio` @type(Double) @default(0.0)

- Density Ratio used to filter outer shell geometry.

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
