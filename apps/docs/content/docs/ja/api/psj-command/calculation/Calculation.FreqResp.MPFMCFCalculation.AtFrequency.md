---
title: "Calculation.FreqResp.MPFMCFCalculation.AtFrequency()"
description: "Display MPC result of specific frequency in Model Participation Factor dialog"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FreqResp > MPFMCFCalculation > AtFrequency"
macro _link: "[CalculateMPCAtFrequency](../../macro/calculation/CalculateMPCAtFrequency)"
---

## Description

Display MPC result of specific frequency in Model Participation Factor dialog.

## Syntax

```psj
Calculation.FreqResp.MPFMCFCalculation.AtFrequency(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crResponse

- Specify the response to calculate MPC.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### dFrequency

- Specify the frequency to calculate MPC.
- The default value is 0.0.

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
Calculation.FreqResp.LoadCondition(strName="FRQLoad _1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                    dAmplitude=10.0, crlTargets=[Node(1516)])

# Create a load case
Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase _1", 
                            crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Create a response condition
Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), dDampingFactor=0.02, 
                                        dStyleParamMid=10.0, dStyleParamBot=200.0, strlResultNames=["TZ"], 
                                        crlTargets=[Node(1516, 1016)])
Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), strChartTitle="Frequency Analysis Displacement", 
                    strAxisTitleX="Frequency", strAxisTitleY="Amplitude")
Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(3), strChartTitle="Frequency Analysis Displacement", 
                    strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)

# MPFMCF calculation at frequency 
atFreq = Calculation.FreqResp.MPFMCFCalculation.AtFrequency(crResponse=PostFreqResultCurve(3), dFrequency=70.0)
JPT.Debugger(atFreq)
```
