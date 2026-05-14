---
title: "Report.PPTMultiShots()"
description: "Capture the image of the result type being loaded at each frequency within the specified range, and automatically paste into Microsoft Office PowerPoint"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Report > PPTMultiShots"
macro _link: "[CmdPostPPTMultiShots](../../macro/report/CmdPostPPTMultiShots)"
---

## Description

Capture the image of the result type being loaded at each frequency within the specified range, and automatically paste into Microsoft Office PowerPoint.

## Syntax

```psj
Report.PPTMultiShots(...)
```

## Inputs

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dStartFrequency`

- The start frequency.

<!-- @since:5.1.0 @type:Double @optional @default:100.0 -->
### `dEndFrequency`

- The end frequency.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# PPT Multi Shots
reportFile = Report.PPTMultiShots(dStartFrequency=10000.0, dEndFrequency=100000.0)
JPT.Debugger(reportFile)
```
