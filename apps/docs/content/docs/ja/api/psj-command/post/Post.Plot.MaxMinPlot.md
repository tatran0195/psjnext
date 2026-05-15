---
title: "Post.Plot.MaxMinPlot()"
description: "Display the maximum/minimum values in multiple steps on the graph in steps or time history"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Plot > MaxMinPlot"
macro _link: "[CmdMaxMinPlot](../../macro/post/CmdMaxMinPlot)"
---

## Description

Display the maximum/minimum values in multiple steps on the graph in steps or time history.

## Syntax

```psj
Post.Plot.MaxMinPlot(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### listPostStepItem

- Specify the attributes of each Post Step Item.
- The default value is POST\_STEP\_ITEM().

<!-- @since:5.1.0 @optional -->
### bExportCSV

- Specify whether to export the result to CSV file.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### strExportCSVPath

- Specify the path of CSV file to be exported.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {26-32}
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

# Distance Plot (X,Y,Z Distance Plot)
Post.Plot.MaxMinPlot(listPostStepItem=[
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=1), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=2), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=3), \
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=4), 
                    POST _STEP _ITEM(iAnalysisType=2, iResultSet=1, iTimeStep=5)], 
                    bExportCSV=False)
```
