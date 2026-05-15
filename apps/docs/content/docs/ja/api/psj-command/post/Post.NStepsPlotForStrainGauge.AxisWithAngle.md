---
title: "Post.NStepsPlotForStrainGauge.AxisWithAngle()"
description: "Display a graph of the stress/strain at the entered rotation angle from the first defined axis on a two-axis plane"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > NStepsPlotForStrainGauge > AxisWithAngle"
macro _link: "[CmdPlotStrainGaugeAxisAngle](../../macro/post/CmdPlotStrainGaugeAxisAngle)"
---

## Description

Display a graph of the stress/strain at the entered rotation angle from the first defined axis on a two-axis plane.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.AxisWithAngle(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crPostJob

- Specify the processing post job.

<!-- @since:5.1.0 @optional -->
### listPostStepItem

- Specify the attributes of each Post Step Item.
- The default value is POST\_STEP\_ITEM().

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the selected nodes to get the result and plot chart.

<!-- @since:5.1.0 @required -->
### strXAxisType

- Specify the result type to plot on X-axis.

<!-- @since:5.1.0 @required -->
### strYAxisType

- Specify the result type to plot on Y-axis.

<!-- @since:5.1.0 @optional -->
### iFirstAxis

- Specify the first axis from maximum principal stress, minimum principal stress, and middle principal stress.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iSecondAxis

- Specify the second axis from the minimum principal stress and the middle principal stress.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dAngle

- Specify the value of rotation angle.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dLength

- Specify the length of the selection when the node is picked.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dWidth

- Specify the width of the selection when the node is picked.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dAmendFactor

- Specify the coefficient for correction that is used for strain analysis results.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### iPhaseType

- Specify the way to get the phase information when obtaining the strain (stress) in the specified direction for the frequency response result.
  - 0: User Defined
  - 1: Peak (Max)
  - 2: Peak (Min)
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dPhaseAngle

- Specify the value of phase angle.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bCreateMarkup

- Specify whether to markup label for the selected node when plotting graph.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-24}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > AxisWithAngle
plot = Post.NStepsPlotForStrainGauge.AxisWithAngle(
    crPostJob=TSVPostJob(1), 
    listPostStepItem=[
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=1), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=2), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=3), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=4), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=5), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=6), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=7), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=8), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=9), 
        POST _STEP _ITEM(iAnalysisType=4, iResultSet=1, iTimeStep=10)], 
    crlTargets=[Node(113, 111)], 
    strXAxisType="Time/Freq(Default)", 
    strYAxisType="Stress(Node)", 
    iSecondAxis=1, 
    dLength=0.002, 
    dWidth=0.001)
JPT.Debugger(plot)
```
