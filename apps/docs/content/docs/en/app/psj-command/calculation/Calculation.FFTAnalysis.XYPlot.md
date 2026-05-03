---
title: "Calculation.FFTAnalysis.XYPlot()"
description: "Display the circularity XY plot graph and export it to a specified file"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > FFTAnalysis > XYPlot"
macro_link: "[CmdFFTXYPlot](../../macro/calculation/CmdFFTXYPlot)"
---

## Description

Display the circularity XY plot graph and export it to a specified file.

## Syntax

```psj
Calculation.FFTAnalysis.XYPlot(...)
```

## Inputs

### `iFFTCondition` @type(Integer) @default(1)

- The ID of the specified FFT condition.

### `bDefineOA` @type(Boolean) @default(False)

- Whether to display the OA result.

### `strDefineOA` @type(String) @default("2-4")

- The mode to display the graph of OA result.

### `strDefineMode` @type(String) @default("2, 3, 4")

- The mode to display the circularity XY plot graph.

### `b3DPlot` @type(Boolean) @default(False)

- Whether to display the circularity plot graph in 3D space.

### `bExportData` @type(Boolean) @default(False)

- Whether to save the FFT analysis result to file.

### `strPath` @type(String) @default("")

- The path of CSV file to save the FFT analysis results.

### `bOriginalShift` @type(Boolean) @default(False)

- Whether to shift the values of all layers when outputting amplitude data (except for the 0th order mode).

### `bExportAllPlot` @type(Boolean) @default(False)

- Whether to save all resulting roundness XY plots and deformation plots to a CSV file.

### `b2DPlot` @type(Boolean) @default(False)

- Whether to display the circularity plot graph in 3D space.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {27-28}
# Please set path to your result sample file.
filePath="C:/Temp/Sample..."

# Please set path to your exported CSV file.
fileExport="C:/Temp/ExportFile.csv"

# Prepare result model
Home.ImportResults.ADVC(filePath, iImportType=1, dFaceAngle=60, dEdgeAngle=60)

# Set FFT condition
Calculation.FFTAnalysis.SetCondition(crlTargets=[Elem(...)], crl2DElems=[Elem(...)], dAngle=0.349066, 
                                    crTopNode=RONode(7663), crBottomNode=RONode(9606), 
                                    dlCenterPoint=[332.71, -191.12, 190.81], dBoreRadius=50.0001, 
                                    dBoreHeight=170.13, dlAxisDefined=[0.0, 0.71, -0.71], iDepthDirection=-1, 
                                    iNumOfLayerPoint=20, dlLayers=[0.0, 56.71, 113.42, 170.13], 
                                    dlAxisX=[0.14, 0.7, 0.7])

# Show translational displacement results
Post.ShowContour(crPostJob=TSVPostJob(1), lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                    iAnalysisType=1, strResultName="Displacement", strResultCompName="Translational", 
                    iResultPos=1), postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), postResultKey=PostResultKey(iAnalysisType=1, 
                    strResultName="Displacement", strResultCompName="Translational"))
Post.EnableMiddleNodes()

# XY plot and export result to file 
XYPlot = Calculation.FFTAnalysis.XYPlot(bDefineOA=True, strPath=fileExport, bExportData=True, 
                                        bExportAllPlot=True, b2DPlot=True)
JPT.Debugger(XYPlot)
```
