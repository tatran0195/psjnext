---
title: "Post.Note.Position()"
description: "Add a note indication to the arbitrary point specified on the main window, and input it to the data table in the Position tab of the Watch Data window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Note > Position"
macro _link: "[CmdMarkupFacePoint](../../macro/post/CmdMarkupFacePoint)"
---

## Description

Add a note indication to the arbitrary point specified on the main window, and input it to the data table in the Position tab of the Watch Data window.

## Syntax

```psj
Post.Note.Position(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @required -->
### `crElement`

- The element containing the specified point.

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlPosition`

- The coordinates of the specified point.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
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

# Display note at the selected point
Post.Note.Position(crElement=ROElem(448), dlPosition=[29.542965, 10.0, 1.642851])
```
