---
title: "Post.Note.Position()"
description: "Add a note indication to the arbitrary point specified on the main window, and input it to the data table in the Position tab of the Watch Data window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Note > Position"
macro_link: "[CmdMarkupFacePoint](../../macro/post/CmdMarkupFacePoint)"
---

## Description

Add a note indication to the arbitrary point specified on the main window, and input it to the data table in the Position tab of the Watch Data window.

## Syntax

```psj
Post.Note.Position(...)
```

## Inputs

### `crElement` @type(Cursor) @required

- The element containing the specified point.

### `dlPosition` @type(List\[Double]) @required

- The coordinates of the specified point.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
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
