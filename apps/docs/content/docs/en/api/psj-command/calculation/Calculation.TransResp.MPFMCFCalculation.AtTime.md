---
title: "Calculation.TransResp.MPFMCFCalculation.AtTime()"
description: "Display MPC result of specific time in Model Participation Factor dialog"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > MPFMCFCalculation > AtTime"
macro _link: "[CalculateMPCAtTime](../../macro/calculation/CalculateMPCAtTime)"
---

## Description

Display MPC result of specific time in Model Participation Factor dialog.

## Syntax

```psj
Calculation.TransResp.MPFMCFCalculation.AtTime(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crResponse`

- The response to calculate MPC.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dTime`

- The time to calculate MPC.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {23}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
Calculation.TransResp.LoadCondition(strName="TRNLoad _2", iLoadType=1, iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10, dT1=0.1, dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])

# Create a load case
Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase _1", 
                                        crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])

# Create response condition
Calculation.TransResp.ResponseCondition(crTargetAnalysis=PostTransAnalysis(1), dDampingFactor=0.02, 
                                        iCurveStyle=0, dStyleParamMid=80.0, dStyleParamBot=0.0125, 
                                        strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])
Chart.CreateGraph(crTargetCurve=PostTransResultCurve(1), strChartTitle="Transient Analysis Displacement", 
                    strAxisTitleX="Time", strAxisTitleY="Data")
Chart.CreateGraph(crTargetCurve=PostTransResultCurve(3), strChartTitle="Transient Analysis Displacement", 
                    strAxisTitleX="Time", strAxisTitleY="Data", bNewChart=False)

# MPFMCF Calculation At Time
atTime = Calculation.TransResp.MPFMCFCalculation.AtTime(crResponse=PostTransResultCurve(1), dTime=0.1625)
JPT.Debugger(atTime)
```
