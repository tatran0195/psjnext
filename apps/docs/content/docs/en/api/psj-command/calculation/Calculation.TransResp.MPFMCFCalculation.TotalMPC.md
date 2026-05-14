---
title: "Calculation.TransResp.MPFMCFCalculation.TotalMPC()"
description: "Display a graph (a chart) of total MPC"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > MPFMCFCalculation > TotalMPC"
macro _link: "[TotalMPC](../../macro/calculation/TotalMPC)"
---

## Description

Display a graph (a chart) of total MPC.

## Syntax

```psj
Calculation.TransResp.MPFMCFCalculation.TotalMPC(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crResponse`

- The response to calculate total MPC.

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

# Create a loadcase
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

# Total MPC
totalMPC = Calculation.TransResp.MPFMCFCalculation.TotalMPC(crResponse=PostTransResultCurve(1))
JPT.Debugger(totalMPC)
```
