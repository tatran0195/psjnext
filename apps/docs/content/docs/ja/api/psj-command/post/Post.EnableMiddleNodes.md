---
title: "Post.EnableMiddleNodes()"
description: "Enable/disable middle nodes to draw the contour"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > EnableMiddleNodes"
macro _link: "[CmdEnableMiddleNodes](../../macro/post/CmdEnableMiddleNodes)"
---

## Description

Enable/disable middle nodes to draw the contour.

## Syntax

```psj
Post.EnableMiddleNodes(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### bShow

- Specify whether to enable or disable the middle nodes.
- The default value is _True_.

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

# Enable/Disable the middle nodes
Post.EnableMiddleNodes(bShow=False)
```
