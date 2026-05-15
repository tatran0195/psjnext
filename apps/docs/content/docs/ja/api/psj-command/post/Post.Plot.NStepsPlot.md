---
title: "Post.Plot.NStepsPlot()"
description: "Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Plot > NStepsPlot"
macro _link: "[CmdNStepPlotNode](../../macro/post/CmdNStepPlotNode)"
---

## Description

Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history.

## Syntax

```psj
Post.Plot.NStepsPlot(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crPostJob

- Specify the processing post job.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the selected nodes to plot graph.

<!-- @since:5.1.0 @optional -->
### listPostStepItem

- Specify the attributes of each Post Step Item.
- The default value is POST\_STEP\_ITEM().

<!-- @since:5.1.0 @optional -->
### bCreateMarkup

- Specify whether to markup label for the selected note when plotting graph.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### strXResult

- Specify the result type to display on the X-axis.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strXComponent

- Specify the direction of the selected result to display on the X-axis.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### iDataLocation

- Specify the data location (Node & Element) that the result will display on.
- The default value is 0.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25-33}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Distance Plot (X,Y,Z Distance Plot)
Post.Plot.NStepsPlot(crPostJob=TSVPostJob(1), crlTargets=[Node(133)], listPostStepItem=[
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                    strXResult="Displacement", 
                    strXComponent="Translational", 
                    iDataLocation=1)
```
