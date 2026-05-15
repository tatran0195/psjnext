---
title: "Chart.CreateGraph()"
description: "Make a graph of post result curve"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Chart > CreateGraph"
macro _link: "[PostCreateGraph](../../macro/chart/PostCreateGraph)"
---

## Description

Make a graph of post result curve.

## Syntax

```psj
Chart.CreateGraph(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crTargetCurve

- Specify the post result curve.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### iNumData

- Specify the number of data markers to plot the graph.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strLineTitle

- Specify the chart line title.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### dlAxisDataX

- Specify the data value on X-Axis.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dlAxisDataY

- Specify the data value on Y-Axis.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### strChartTitle

- Specify the chart title.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strAxisTitleX

- Specify the X-axis title.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strAxisTitleY

- Specify the Y-axis title
- The default value is "".

<!-- @since:5.1.0 @optional -->
### bNewChart

- Specify whether to plot graph on a new chart window
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {20-24}
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
                                                        crlTargets=[Node(1516)])

# Plot chart
newChart = Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), 
                            strChartTitle="Frequency Analysis Displacement", 
                            strAxisTitleX="Frequency", 
                            strAxisTitleY="Amplitude", 
                            bNewChart=False)
JPT.Debugger(newChart)
```
