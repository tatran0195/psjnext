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

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetCurve`

- The post result curve.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iNumData`

- The number of data markers to plot the graph.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strLineTitle`

- The chart line title.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[] -->
### `dlAxisDataX`

- The data value on X-Axis.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[] -->
### `dlAxisDataY`

- The data value on Y-Axis.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strChartTitle`

- The chart title.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strAxisTitleX`

- The X-axis title.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strAxisTitleY`

- The Y-axis title

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bNewChart`

- Whether to plot graph on a new chart window

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
