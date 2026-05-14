---
title: "Calculation.TransResp.ResponseCondition()"
description: "Output the result of the response point for transient response"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > ResponseCondition"
macro _link: "[CmdSaveOpenTsdv](../../macro/calculation/CmdSaveOpenTsdv)"
---

## Description

Output the result of the response point for transient response.

## Syntax

```psj
Calculation.TransResp.ResponseCondition(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target job to be processed.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The output coordinate system.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bAllModesUsed`

- Whether to use all modes.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlModesSelected`

- The selected modes using for response calculation. This option was used if bAllModesUsed is _False_.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bDampingFactor`

- Whether to use damping factor for calculation.

<!-- @since:5.1.0 @type:Double @optional @default:0.01 -->
### `dDampingFactor`

- The value of damping factor.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crDampingFactor`

- The field data of damping factor.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iCurveStyle`

- The style of time range for the calculation.
  - 0: Start + StepNumber + StepSize
  - 1: Start + StepSize + End
  - 2: Start + StepNumber + End

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dStyleParamTop`

- The analysis start value of the selected curve style.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dStyleParamMid`

- The step size value of the selected curve style.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dStyleParamBot`

- The analysis end value of the selected curve style.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bIncludeEigenValue`

- Whether to plot the frequency of eigen value.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCreateNewResult`

- Whether to create new results (displacement and stress) for the entire model.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iResultType`

- The result type to be calculated.
  - 0: Displacement
  - 1: Velocity
  - 2: Acceleration
  - 3: Stress (Solid)
  - 4: Stress (Shell)
  - 5: Disp. + Stress. This result type was displayed when bCreateNewResult = _True_.

<!-- @since:5.1.0 @type:List[String] @optional @default:["TX"] -->
### `strlResultNames`

- The component results according to the selected result type.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iResultPosition`

- The output position of the result.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bAllLoadCases`

- Whether to use all current load cases.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crSelectedLoadCase`

- The selected load case to analyze. This option was used if bAllLoadCases is _False_.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSeparateLoad`

- Whether to calculate the response to each set load.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The target to calculate the response. The target is node or solid element.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing response condition
  - If this parameter is used, the specified response condition will be modified.
  - If it is left None, a new response condition will be created.

## Return Code

A _Cursor_ specifying the created transient response condition.

## Sample Code

```psj {15-17}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
Calculation.TransResp.LoadCondition(strName="TRNLoad _2", iLoadType=1, iLoadDirection=2, 
                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, dT2=0.5, 
                                    dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase _1",
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
