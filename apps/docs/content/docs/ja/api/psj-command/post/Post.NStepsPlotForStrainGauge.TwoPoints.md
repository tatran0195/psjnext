---
title: "Post.NStepsPlotForStrainGauge.TwoPoints()"
description: "Display a graph of the stress/strain in the direction of two points"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > NStepsPlotForStrainGauge > TwoPoints"
macro _link: "[CmdPlotStrainGaugeNodePoint](../../macro/post/CmdPlotStrainGaugeNodePoint)"
---

## Description

Display a graph of the stress/strain in the direction of two points.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.TwoPoints(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crPostJob

- Specify the processing post job.

<!-- @since:5.1.0 @required -->
### crFirstNode

- Specify the first selected node to get the result and plot chart. This argument can be used for both 2Nodes or Node-Point selection methods.

<!-- @since:5.1.0 @required -->
### crSecondNode

- Specify the second selected node to get the result and plot chart. This argument was used incase of the selection method is 2Nodes.

<!-- @since:5.1.0 @required -->
### dlPosition

- Specify the coordinate of the face point. This argument was used incase of the selection method is Node-Point.

<!-- @since:5.1.0 @optional -->
### listPostStepItem

- Specify the attributes of each Post Step Item.
- The default value is POST\_STEP\_ITEM().

<!-- @since:5.1.0 @required -->
### strXAxisType

- Specify the result type to plot on X-axis.

<!-- @since:5.1.0 @required -->
### strYAxisType

- Specify the result type to plot on Y-axis.

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

### `bCreateMarkup`

-A _Boolean_ specifying whether to mark up the selected note when plotting graph.

- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {27-41,45-59}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Strain", 
                strResultCompName="Solid Max Principal Strain", 
                iResultPos=4), 
                postDataOp=PostDataOp(iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2,
                    strResultName="Strain", 
                    strResultCompName="Solid Max Principal Strain"))

# NStepsPlotForStrainGauge > TwoPoints (2Nodes)
plotChart = Post.NStepsPlotForStrainGauge.TwoPoints(
            crPostJob=TSVPostJob(1), 
            crFirstNode=Node(113), 
            crSecondNode=Node(115), 
            listPostStepItem=[
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                strXAxisType="Time/Freq(Default)", 
                strYAxisType="Stress(Node)", 
            dLength=0.002, 
            dWidth=0.005, 
            iPhaseType=-1)
JPT.Debugger(plotChart)

# NStepsPlotForStrainGauge > TwoPoints (Node-Point)
plotChart = Post.NStepsPlotForStrainGauge.TwoPoints(
            crPostJob=TSVPostJob(1), 
            crFirstNode=Node(113), 
            dlPosition=[0.0176052, 0.00855172, 0.00343833], 
            listPostStepItem=[
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                strXAxisType="Time/Freq(Default)", 
                strYAxisType="Stress(Node)", 
            dLength=0.002, 
            dWidth=0.005, 
            iPhaseType=-1)
JPT.Debugger(plotChart)
```
