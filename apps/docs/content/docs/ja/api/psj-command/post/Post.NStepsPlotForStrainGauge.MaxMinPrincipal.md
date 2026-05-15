---
title: "Post.NStepsPlotForStrainGauge.MaxMinPrincipal()"
description: "Display a graph of the stress/strain in the maximum or minimum principal stress direction"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > NStepsPlotForStrainGauge > MaxMinPrincipal"
macro _link: "[CmdPlotStrainGaugePrincipal](../../macro/post/CmdPlotStrainGaugePrincipal)"
---

## Description

Display a graph of the stress/strain in the maximum or minimum principal stress direction.

## Syntax

```psj
Post.NStepsPlotForStrainGauge.MaxMinPrincipal(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crPostJob

- Specify the processing post job.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the selected nodes to get the result and plot chart.

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
### bMaxPrincipal

- Specify the direction is maximum principal stress or minimum principal stress.
- The default value is _True_.

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

```psj {6-20}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\111 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# NStepsPlotForStrainGauge > MaxMinPrincipal
plot = Post.NStepsPlotForStrainGauge.MaxMinPrincipal(crPostJob=TSVPostJob(1), 
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
                                            crlTargets=[Node(133, 132)], 
                                            strXAxisType="Time/Freq(Default)", 
                                            strYAxisType="Stress(Node)")
JPT.Debugger(plot)
```
