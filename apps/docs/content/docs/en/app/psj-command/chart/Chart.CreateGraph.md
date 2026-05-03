---
title: "Chart.CreateGraph()"
description: "Make a graph of post result curve"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Chart > CreateGraph"
macro_link: "[PostCreateGraph](../../macro/chart/PostCreateGraph)"
---

## Description

Make a graph of post result curve.

## Syntax

```psj
Chart.CreateGraph(...)
```

## Inputs

### `crTargetCurve` @type(Cursor) @default(None)

- The post result curve.

### `iNumData` @type(Integer) @default(0)

- The number of data markers to plot the graph.

### `strLineTitle` @type(String) @default("")

- The chart line title.

### `dlAxisDataX` @type(List\[Double]) @default(\[])

- The data value on X-Axis.

### `dlAxisDataY` @type(List\[Double]) @default(\[])

- The data value on Y-Axis.

### `strChartTitle` @type(String) @default("")

- The chart title.

### `strAxisTitleX` @type(String) @default("")

- The X-axis title.

### `strAxisTitleY` @type(String) @default("")

- The Y-axis title

### `bNewChart` @type(Boolean) @default(True)

- Whether to plot graph on a new chart window

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {20-24}
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
                                                        crlTargets=[Node(1516)])

# Plot chart
newChart = Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), 
                            strChartTitle="Frequency Analysis Displacement", 
                            strAxisTitleX="Frequency", 
                            strAxisTitleY="Amplitude", 
                            bNewChart=False)
JPT.Debugger(newChart)
```
