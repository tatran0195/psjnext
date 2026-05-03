---
title: "Post.SetNote.ResultPrnVector()"
description: "Set the display of principal stress/principal strain unit vector in the note window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ResultPrnVector"
macro_link: "[SetNoteResultPrnVector](../../macro/post/SetNoteResultPrnVector)"
---

## Description

Set the display of principal stress/principal strain unit vector in the note window.

## Syntax

```psj
Post.SetNote.ResultPrnVector(...)
```

## Inputs

### `bNoteResultPrnVector` @type(Boolean) @default(True)

- Whether to display the principal stress/principal strain unit vector in the note window.

### `iNoteResultPrnVector` @type(Integer) @default(0)

- The method to display the principal stress/principal strain unit vector title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

### `strNoteResultPrnVector` @type(String) @default("")

- An arbitrary user-defined name for the principal stress/principal strain vector. This option was used whe&#x6E;_&#x69;NoteResultPrnVector_= 1.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {28,30}
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
                strResultCompName="Max Principal Stress", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Stress", 
                    strResultCompName="Max Principal Stress"))
Post.Note.Node(crlTargets=[RONode(133)])

# Hide Principal stress direction
Post.SetNote.ResultPrnVector(bNoteResultPrnVector=False)
# User defines Principal stress direction title
Post.SetNote.ResultPrnVector(iNoteResultPrnVector=1, strNoteResultPrnVector="Direction")
```
