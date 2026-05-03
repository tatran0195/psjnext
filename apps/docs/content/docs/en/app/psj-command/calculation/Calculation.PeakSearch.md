---
title: "Calculation.PeakSearch()"
description: "Find peak nodes with higher or lower results (peaked) than nearby vertices at each node in the model and flag them"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > PeakSearch"
macro_link: "[CmdPostPeakSearch](../../macro/calculation/CmdPostPeakSearch)"
---

## Description

Find peak nodes with higher or lower results (peaked) than nearby vertices at each node in the model and flag them.

## Syntax

```psj
Calculation.PeakSearch(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target. The target can be part or face.

### `crlExcludedNodes` @type(List\[Cursor]) @default(\[])

- The excluded nodes.

### `iOption` @type(Integer) @default(0)

- The peak option.
  - 0: Max
  - 1: Min
  - 2: ABS Max

### `dParameter` @type(Double) @default(0.1)

- The value for micro peak removal.

### `bStep` @type(Boolean) @default(True)

- Whether to use the Step option.

## Return Code

A _List of Cursor_ specifying the peak nodes.

## Sample Code

```psj {27}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Stress", 
                strResultCompName="Max Principal Stress", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2, 
                    strResultName="Stress", 
                    strResultCompName="Max Principal Stress"))

# Peak search
peakNodes = Calculation.PeakSearch(bStep=False)
print(peakNodes)
```
