---
title: "Calculation.FFTAnalysis.SectionGraph()"
description: "Make the section graph"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FFTAnalysis > SectionGraph"
macro _link: "[CmdFFTSectionGraph](../../macro/calculation/CmdFFTSectionGraph)"
---

## Description

Make the section graph.

## Syntax

```psj
Calculation.FFTAnalysis.SectionGraph(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iPointIndex

- Specify the point on the layer to make the section graph.
- The default value is 1.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {30}
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
Calculation.FFTAnalysis.CirclePlot(bOACircle=True, bDefineOA=True)

# Section graph
graph = Calculation.FFTAnalysis.SectionGraph(iPointIndex=19)
JPT.Debugger(graph)
```
