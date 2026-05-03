---
title: "Calculation.TransResp.ResponseCondition()"
description: "Output the result of the response point for transient response"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > TransResp > ResponseCondition"
macro_link: "[CmdSaveOpenTsdv](../../macro/calculation/CmdSaveOpenTsdv)"
---

## Description

Output the result of the response point for transient response.

## Syntax

```psj
Calculation.TransResp.ResponseCondition(...)
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

A _Cursor_ specifying the created transient response condition.

## Sample Code

```psj {15-17}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, dT2=0.5, 
                                    dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase_1",
                                        crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])

# Create response condition
respCondition = Calculation.TransResp.ResponseCondition(crTargetAnalysis=PostTransAnalysis(1), dDampingFactor=0.02, 
                                                        iCurveStyle=0, dStyleParamMid=80.0, dStyleParamBot=0.0125, 
                                                        strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])
Chart.CreateGraph(crTargetCurve=PostTransResultCurve(1), strChartTitle="Transient Analysis Displacement", 
                strAxisTitleX="Time", strAxisTitleY="Data")
Chart.CreateGraph(crTargetCurve=PostTransResultCurve(3), strChartTitle="Transient Analysis Displacement", 
                strAxisTitleX="Time", strAxisTitleY="Data", bNewChart=False)
JPT.Debugger(respCondition) # for checking the return value
```
