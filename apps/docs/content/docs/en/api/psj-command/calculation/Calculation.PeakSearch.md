---
title: "Calculation.PeakSearch()"
description: "Find peak nodes with higher or lower results (peaked) than nearby vertices at each node in the model and flag them"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > PeakSearch"
macro _link: "[CmdPostPeakSearch](../../macro/calculation/CmdPostPeakSearch)"
---

## Description

Find peak nodes with higher or lower results (peaked) than nearby vertices at each node in the model and flag them.

## Syntax

```psj
Calculation.PeakSearch(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target. The target can be part or face.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlExcludedNodes`

- The excluded nodes.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iOption`

- The peak option.
  - 0: Max
  - 1: Min
  - 2: ABS Max

<!-- @since:5.1.0 @type:Double @optional @default:0.1 -->
### `dParameter`

- The value for micro peak removal.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bStep`

- Whether to use the Step option.

## Return Code

A _List of Cursor_ specifying the peak nodes.

## Sample Code

```psj {27}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
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
