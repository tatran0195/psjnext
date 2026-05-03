---
title: "Calculation.FreqResp.ResponseCondition()"
description: "Output the result of the response point for frequency response"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > FreqResp > ResponseCondition"
macro_link: "[ResponseCondition](../../macro/calculation/ResponseCondition)"
---

## Description

Output the result of the response point for frequency response.

## Syntax

```psj
Calculation.FreqResp.ResponseCondition(...)
```

## Inputs

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target job to be processed.

### `crCoordinate` @type(Cursor) @default(None)

- The output coordinate system.

### `bAllModesUsed` @type(Boolean) @default(True)

- Whether to use all modes.

### `strlModesSelected` @type(List\[String]) @default(\[])

- The selected modes using for response calculation. This option was used if bAllModesUsed i&#x73;_&#x46;alse_.

### `bDampingFactor` @type(Boolean) @default(True)

- Whether to use damping factor for calculation.

### `dDampingFactor` @type(Double) @default(0.01)

- The value of damping factor.

### `crDampingFactor` @type(Cursor) @default(None)

- The field data of damping factor.

### `iCurveStyle` @type(Integer) @default(1)

- The style of time range for the calculation.
  - 0: Start + StepNumber + StepSize
  - 1: Start + StepSize + End
  - 2: Start + StepNumber + End

### `dStyleParamTop` @type(Double) @default(0.0)

- The analysis start value of the selected curve style.

### `dStyleParamMid` @type(Double) @default(1.0)

- The step size value of the selected curve style.

### `dStyleParamBot` @type(Double) @default(1.0)

- The analysis end value of the selected curve style.

### `bIncludeEigenValue` @type(Boolean) @default(False)

- Whether to plot the frequency of eigen value.

### `bCreateNewResult` @type(Boolean) @default(False)

- Whether to create new results (displacement and stress) for the entire model.

### `iResultType` @type(Integer) @default(0)

- The result type to be calculated.
  - 0: Displacement
  - 1: Velocity
  - 2: Acceleration
  - 3: Stress (Solid)
  - 4: Stress (Shell)
  - 5: Disp. + Stress. This result type was displayed when bCreateNewResult =_True_.

### `strlResultNames` @type(List\[String]) @default(\["TX"])

- The component results according to the selected result type.

### `iResultPosition` @type(Integer) @default(0)

- The output position of the result.

### `bAllLoadCases` @type(Boolean) @default(True)

- Whether to use all current load cases.

### `crSelectedLoadCase` @type(Cursor) @default(None)

- The selected load case to analyze. This option was used if bAllLoadCases i&#x73;_&#x46;alse_.

### `bSeparateLoad` @type(Boolean) @default(False)

- Whether to calculate the response to each set load.

### `crlTargets` @type(List\[Cursor]) @required

- The target to calculate the response. The target is node or solid element.

### `crEdit` @type(Cursor) @default(None)

- An existing response condition
  - If this parameter is used, the specified response condition will be modified.
  - If it is left None, a new response condition will be created.

## Return Code

A _Cursor_ specifying the created frequency response condition.

## Sample Code

```psj {14-17}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Create a load condition
Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)]) 

# Create a load case
Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
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
