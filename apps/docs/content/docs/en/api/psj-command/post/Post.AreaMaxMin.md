---
title: "Post.AreaMaxMin()"
description: "Detect the maximum and minimum values of nodes within a specified range"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > AreaMaxMin"
macro _link: "[CmdPostAreaMaxMin](../../macro/post/CmdPostAreaMaxMin)"
---

## Description

Detect the maximum and minimum values of nodes within a specified range.

## Syntax

```psj
Post.AreaMaxMin(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The selected nodes to detect max/min value.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bCheckMax`

- Whether to enable/disable detecting and displaying the maximum value.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bCheckMin`

- Whether to enable/disable detecting and displaying the minimum value.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSave`

- Whether to save the detected max/min result into AreaMax/Min tab of the Watch Data Window.

## Return Code

A Dictionary containing the Max/Min values.

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

# Detect the Max/Min value in the selected range
MaxMinArea = Post.AreaMaxMin(crlTargets=[Node(45, 53, 133, 132, 48, 130, 127, 39, 47, 38, 28, 46)])
print("The Max value in range is:", MaxMinArea['Max']['value']) 
print("The Min value in range is:", MaxMinArea['Min']['value'])
```
