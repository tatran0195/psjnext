---
title: "Post.SetNote.ColorBackground()"
description: "Set the background color of note window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ColorBackground"
macro_link: "[SetNoteColorBackground](../../macro/post/SetNoteColorBackground)"
---

## Description

Set the background color of note window.

## Syntax

```psj
Post.SetNote.ColorBackground(...)
```

## Inputs

### `iBackground` @type(Integer) @default(16777215)

- The background color.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {27}
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

# Modify the background color
Post.Note.Node(crlTargets=[RONode(133)])
Post.SetNote.ColorBackground(iBackground=42495)
```
