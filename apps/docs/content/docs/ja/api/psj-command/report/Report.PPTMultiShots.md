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

<!-- @since:5.1.0 @optional -->
### dStartFrequency

- Specify the start frequency.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dEndFrequency

- Specify the end frequency.
- The default value is 100.0.

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
