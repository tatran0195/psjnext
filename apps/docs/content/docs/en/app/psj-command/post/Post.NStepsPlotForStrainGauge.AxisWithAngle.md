---
title: "Post.NStepsPlotForStrainGauge.AxisWithAngle()"
description: "Display a graph of the stress/strain at the entered rotation angle from the first defined axis on a two-axis plane"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > NStepsPlotForStrainGauge > AxisWithAngle"
macro_link: "[CmdPlotStrainGaugeAxisAngle](../../macro/post/CmdPlotStrainGaugeAxisAngle)"
---

## Description

Display a graph of the stress/strain at the entered rotation angle from the first defined axis on a two-axis plane.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.AxisWithAngle(...)
```

## Inputs

### `crPostJob` @type(Cursor) @required

- The processing post job.

### `listPostStepItem` @type(List\[POST\_STEP\_ITEM]) @default(POST\_STEP\_ITEM())

- The attributes of each Post Step Item.

### `crlTargets` @type(List\[Cursor]) @required

- The selected nodes to get the result and plot chart.

### `strXAxisType` @type(String) @required

- The result type to plot on X-axis.

### `strYAxisType` @type(String) @required

- The result type to plot on Y-axis.

### `iFirstAxis` @type(Integer) @default(0)

- The first axis from maximum principal stress, minimum principal stress, and middle principal stress.

### `iSecondAxis` @type(Integer) @default(0)

- The second axis from the minimum principal stress and the middle principal stress.

### `dAngle` @type(Double) @default(0.0)

- The value of rotation angle.

### `dLength` @type(Double) @default(0.0)

- The length of the selection when the node is picked.

### `dWidth` @type(Double) @default(0.0)

- The width of the selection when the node is picked.

### `dAmendFactor` @type(Double) @default(1.0)

- The coefficient for correction that is used for strain analysis results.

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

```psj {6-24}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > AxisWithAngle
plot = Post.NStepsPlotForStrainGauge.AxisWithAngle(
    crPostJob=TSVPostJob(1), 
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
    crlTargets=[Node(113, 111)], 
    strXAxisType="Time/Freq(Default)", 
    strYAxisType="Stress(Node)", 
    iSecondAxis=1, 
    dLength=0.002, 
    dWidth=0.001)
JPT.Debugger(plot)
```
