---
title: "Post.Plot.NStepsPlot()"
description: "Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Plot > NStepsPlot"
macro_link: "[CmdNStepPlotNode](../../macro/post/CmdNStepPlotNode)"
---

## Description

Get results within multiple subcases for a particular node/element/arbitrary point and plot the graph by steps or time history.

## Syntax

```psj
Post.Plot.NStepsPlot(...)
```

## Inputs

### `crPostJob` @type(Cursor) @required

- The processing post job.

### `crlTargets` @type(List\[Cursor]) @required

- The selected nodes to plot graph.

### `listPostStepItem` @type(List\[POST\_STEP\_ITEM]) @default(POST\_STEP\_ITEM())

- The attributes of each Post Step Item.

### `bCreateMarkup` @type(Boolean) @default(True)

- Whether to markup label for the selected note when plotting graph.

### `strXResult` @type(String) @default("")

- The result type to display on the X-axis.

### `strXComponent` @type(String) @default("")

- The direction of the selected result to display on the X-axis.

### `iDataLocation` @type(Integer) @default(0)

- The data location (Node & Element) that the result will display on.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25-33}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
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
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                    POST_STEP_ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                    strXResult="Displacement", 
                    strXComponent="Translational", 
                    iDataLocation=1)
```
