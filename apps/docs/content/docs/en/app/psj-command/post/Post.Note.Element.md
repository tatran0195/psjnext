---
title: "Post.Note.Element()"
description: "Add a note indication to the selected element on the main window, and input it to the data table in the Element tab of the Watch Data window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Note > Element"
macro_link: "[CmdMarkupElement](../../macro/post/CmdMarkupElement)"
---

## Description

Add a note indication to the selected element on the main window, and input it to the data table in the Element tab of the Watch Data window.

## Syntax

```psj
Post.Note.Element(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The selected elements to markup the notes.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {23}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Stress", 
                strResultCompName="Mises", 
                iResultPos=2), 
                postDataOp=PostDataOp(iResultLocation=2))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Mises"))

# Display the note at the selected elements
Post.Note.Element(crlTargets=[ROElem(445,448)])
```
