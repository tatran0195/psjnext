---
title: "Calculation.FFTAnalysis.CirclePlot()"
description: "Display the deformation plot graph"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FFTAnalysis > CirclePlot"
macro _link: "[CmdFFTCirclePlot](../../macro/calculation/CmdFFTCirclePlot)"
---

## Description

Display the deformation plot graph.

## Syntax

```psj
Calculation.FFTAnalysis.CirclePlot(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iFFTCondition

- Specify the ID of the specified FFT condition.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bOACircle

- Specify whether to use the OA Circle option.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### strOACircle

- Specify the number of layers to display the deformation plot graph of the OA results.
- The default value is "2".

<!-- @since:5.1.0 @optional -->
### bDefineOA

- Specify whether to use the Define OA Circle option.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### strDefineOA

- Specify the mode to be used for the OA curve.
- The default value is "2-4".

<!-- @since:5.1.0 @optional -->
### strDefineMode

- Specify the mode in which deformation plots are displayed graphically.
- The default value is "2".

<!-- @since:5.1.0 @optional -->
### strModeLayer

- Specify the layer to be displayed graphically in each mode.
- The default value is "2".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {27}
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
                                    dBoreHeight=170.13, dlAxisDefined=[0.0, 0.71, -0.71], 
                                    iDepthDirection=-1, iNumOfLayerPoint=20, dlLayers=[0.0, 56.71, 113.42, 170.13], 
                                    dlAxisX=[0.14, 0.7, 0.7])

# Show translational displacement results
Post.ShowContour(crPostJob=TSVPostJob(1), lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                    iAnalysisType=1, strResultName="Displacement", strResultCompName="Translational", 
                    iResultPos=1), postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), postResultKey=PostResultKey(iAnalysisType=1, 
                    strResultName="Displacement", strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Circle plot
circlePlot = Calculation.FFTAnalysis.CirclePlot(bOACircle=True, bDefineOA=True)
JPT.Debugger(circlePlot)
```
