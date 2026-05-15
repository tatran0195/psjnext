---
title: "Home.RectangularCapture.Multiple()"
description: "Create a frame for Multiple capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the \"To PPT\" and \"To Image\" command"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > RectangularCapture > Multiple"
macro _link: "[ViewMakeUserFrame](../../macro/home/ViewMakeUserFrame)"
---

## Description

Create a frame for Multiple capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command.

## Syntax

```psj
Home.RectangularCapture.Multiple(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strFrameName

- Specify the name of frame to be captured.

<!-- @since:5.1.0 @required -->
### iStartPointX

- Specify the x-coordinate of the start point of the frame.

<!-- @since:5.1.0 @required -->
### iStartPointY

- Specify the y-coordinate of the start point of the frame.

<!-- @since:5.1.0 @required -->
### iWidth

- Specify the width of the frame size.

<!-- @since:5.1.0 @required -->
### iHeight

- Specify the height of the frame size.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {26-27}
# Prepare model
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

# Create a multiple frames
Home.RectangularCapture.Multiple(strFrameName="New _Frame _1 ((Multiple))", iStartPointX=459, iStartPointY=212, 
                                iWidth=460, iHeight=214)
Home.ToPPTX()
```
