---
title: "Calculation.FreqResp.ResponseCondition()"
description: "Output the result of the response point for frequency response"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FreqResp > ResponseCondition"
macro _link: "[ResponseCondition](../../macro/calculation/ResponseCondition)"
---

## Description

Output the result of the response point for frequency response.

## Syntax

```psj
Calculation.FreqResp.ResponseCondition(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crTargetAnalysis

- Specify the target job to be processed.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify the output coordinate system.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bAllModesUsed

- Specify whether to use all modes.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### strlModesSelected

- Specify the selected modes using for response calculation. This option was used if bAllModesUsed is _False_.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bDampingFactor

- Specify whether to use damping factor for calculation.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### dDampingFactor

- Specify the value of damping factor.
- The default value is 0.01.

<!-- @since:5.1.0 @optional -->
### crDampingFactor

- Specify the field data of damping factor.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### iCurveStyle

- Specify the style of time range for the calculation.
  - 0: Start + StepNumber + StepSize
  - 1: Start + StepSize + End
  - 2: Start + StepNumber + End
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dStyleParamTop

- Specify the analysis start value of the selected curve style.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dStyleParamMid

- Specify the step size value of the selected curve style.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### dStyleParamBot

- Specify the analysis end value of the selected curve style.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### bIncludeEigenValue

- Specify whether to plot the frequency of eigen value.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bCreateNewResult

- Specify whether to create new results (displacement and stress) for the entire model.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iResultType

- Specify the result type to be calculated.
  - 0: Displacement
  - 1: Velocity
  - 2: Acceleration
  - 3: Stress (Solid)
  - 4: Stress (Shell)
  - 5: Disp. + Stress. This result type was displayed when bCreateNewResult = _True_.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strlResultNames

- Specify the component results according to the selected result type.
- The default value is \["TX"].

<!-- @since:5.1.0 @optional -->
### iResultPosition

- Specify the output position of the result.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bAllLoadCases

- Specify whether to use all current load cases.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### crSelectedLoadCase

- Specify the selected load case to analyze. This option was used if bAllLoadCases is _False_.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bSeparateLoad

- Specify whether to calculate the response to each set load.
- The default value is _False_.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the target to calculate the response. The target is node or solid element.

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing response condition
  - If this parameter is used, the specified response condition will be modified.
  - If it is left None, a new response condition will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created frequency response condition.

## Sample Code

```psj {14-17}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Create a load condition
Calculation.FreqResp.LoadCondition(strName="FRQLoad _1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)]) 

# Create a load case
Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase _1", 
                                crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Create a response condition
respCondition = Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), 
                                                        dDampingFactor=0.02, dStyleParamMid=10.0, 
                                                        dStyleParamBot=200.0, strlResultNames=["TZ"], 
                                                        crlTargets=[Node(1516, 1016)])
Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), strChartTitle="Frequency Analysis Displacement", 
                strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(3), strChartTitle="Frequency Analysis Displacement", 
                strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
JPT.Debugger(respCondition) # for checking the return value
```
