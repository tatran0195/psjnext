---
title: "Post.NStepsPlotForStrainGauge.DirectionCosine()"
description: "Display a graph of the stress/strain in the direction cosine of the entered direction vector"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > NStepsPlotForStrainGauge > DirectionCosine"
macro_link: "[CmdPlotStrainGaugeDirCos](../../macro/post/CmdPlotStrainGaugeDirCos)"
---

## Description

Display a graph of the stress/strain in the direction cosine of the entered direction vector.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.DirectionCosine(...)
```

## Inputs

### `crPostJob` @type(Cursor) @required

- The processing post job.

### `crlTargets` @type(List\[Cursor]) @required

- The selected nodes to get the result and plot chart.

### `listPostStepItem` @type(List\[POST\_STEP\_ITEM]) @default(POST\_STEP\_ITEM())

- The attributes of each Post Step Item.

### `strXAxisType` @type(String) @required

- The result type to plot on X-axis.

### `strYAxisType` @type(String) @required

- The result type to plot on Y-axis.

### `dLength` @type(Double) @default(0.0)

- The length of the selection when the node is picked.

### `dWidth` @type(Double) @default(0.0)

- The width of the selection when the node is picked.

### `dAmendFactor` @type(Double) @default(1.0)

- The coefficient for correction that is used for strain analysis results.

### `dlDirection` @type(List\[Double]) @default(\[1,0,0])

- The direction vector in (X, Y, Z) format.

### `iPhaseType` @type(Integer) @default(0)

- The way to get the phase information when obtaining the strain (stress) in the specified direction for the frequency response result.
  - 0: User Defined
  - 1: Peak (Max)
  - 2: Peak (Min)

### `dPhaseAngle` @type(Double) @default(0.0)

- The value of phase angle.

### `bCreateMarkup` @type(Boolean) @default(True)

- Whether to markup label for the selected node when plotting graph.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-23}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > DirectionCosine
plot = Post.NStepsPlotForStrainGauge.DirectionCosine(
    crPostJob=TSVPostJob(1), 
    crlTargets=[Node(113, 111)], 
    listPostStepItem=[
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=1), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=2), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=3), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=4), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=5), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=6), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=7), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=8), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=9), 
        POST_STEP_ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=10)], 
    strXAxisType="Time/Freq(Default)", 
    strYAxisType="Stress(Node)", 
    dLength=0.002, 
    dWidth=0.001)
JPT.Debugger(plot)
```
