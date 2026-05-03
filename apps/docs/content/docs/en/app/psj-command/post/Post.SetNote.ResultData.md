---
title: "Post.SetNote.ResultData()"
description: "Set the display of result data title in the note window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ResultData"
macro_link: "[SetNoteResultData](../../macro/post/SetNoteResultData)"
---

## Description

Set the display of result data title in the note window.

## Syntax

```psj
Post.SetNote.ResultData(...)
```

## Inputs

### `iNoteResultTitle` @type(Integer) @default(0)

- The method to display the result data title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

### `strNoteResultTitle` @type(String) @default("")

- An arbitrary user-defined name for result data title. This option was used whe&#x6E;_&#x69;NoteResultTitle_= 1.

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
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.Note.Node(crlTargets=[RONode(133)])

# User defines Result Data title
Post.SetNote.ResultData(iNoteResultTitle=1, strNoteResultTitle="Result Data")
```
