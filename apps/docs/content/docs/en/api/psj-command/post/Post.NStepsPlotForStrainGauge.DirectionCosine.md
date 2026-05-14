---
title: "Post.NStepsPlotForStrainGauge.DirectionCosine()"
description: "Display a graph of the stress/strain in the direction cosine of the entered direction vector"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > NStepsPlotForStrainGauge > DirectionCosine"
macro _link: "[CmdPlotStrainGaugeDirCos](../../macro/post/CmdPlotStrainGaugeDirCos)"
---

## Description

Display a graph of the stress/strain in the direction cosine of the entered direction vector.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.DirectionCosine(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @required -->
### `crPostJob`

- The processing post job.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The selected nodes to get the result and plot chart.

<!-- @since:5.1.0 @type:List[POST _STEP _ITEM] @optional @default:POST _STEP _ITEM() -->
### `listPostStepItem`

- The attributes of each Post Step Item.

<!-- @since:5.1.0 @type:String @required -->
### `strXAxisType`

- The result type to plot on X-axis.

<!-- @since:5.1.0 @type:String @required -->
### `strYAxisType`

- The result type to plot on Y-axis.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dLength`

- The length of the selection when the node is picked.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dWidth`

- The width of the selection when the node is picked.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dAmendFactor`

- The coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[1,0,0] -->
### `dlDirection`

- The direction vector in (X, Y, Z) format.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iPhaseType`

- The way to get the phase information when obtaining the strain (stress) in the specified direction for the frequency response result.
  - 0: User Defined
  - 1: Peak (Max)
  - 2: Peak (Min)

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dPhaseAngle`

- The value of phase angle.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bCreateMarkup`

- Whether to markup label for the selected node when plotting graph.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-23}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > DirectionCosine
plot = Post.NStepsPlotForStrainGauge.DirectionCosine(
    crPostJob=TSVPostJob(1), 
    crlTargets=[Node(113, 111)], 
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
    strXAxisType="Time/Freq(Default)", 
    strYAxisType="Stress(Node)", 
    dLength=0.002, 
    dWidth=0.001)
JPT.Debugger(plot)
```
