---
title: "Post.SetNote.ResultNumber()"
description: "Set the display of result number in the note window."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ResultNumber"
---

## Description

Set the display of result number in the note window.

## Syntax

```psj
Post.SetNote.ResultNumber(...)
```

## Inputs

### `bNoteResultNumber` @type(Boolean) @default(True)

- Whether to display the result number in the note window.

### `iNoteResultNumber` @type(Integer) @default(0)

- The method to display the result number title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

### `strNoteResultNumber` @type(String) @default("")

- An arbitrary user-defined name for the result number title. This option is used whe&#x6E;_&#x69;NoteResultNumber_= 1.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25,27}
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
Post.Note.Position(crElement=ROElem(448), dlPosition=[28.588114, 6.313289, 5.0])

# Hide Result Number information
Post.SetNote.ResultNumber(bNoteResultNumber=False)
# User defines Result Number title
Post.SetNote.ResultNumber(iNoteResultNumber=1, strNoteResultNumber="Result Number")
```
