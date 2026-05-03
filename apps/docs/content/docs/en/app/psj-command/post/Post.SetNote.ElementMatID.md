---
title: "Post.SetNote.ElementMatID()"
description: "Set the display of the material ID in the element's notes window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ElementMatID"
macro_link: "[SetNoteElementMatID](../../macro/post/SetNoteElementMatID)"
---

## Description

Set the display of the material ID in the element's notes window.

## Syntax

```psj
Post.SetNote.ElementMatID(...)
```

## Inputs

### `bNoteElemMatID` @type(Boolean) @default(True)

- Whether to display the material ID in element's notes window.

### `iNoteElemMatID` @type(Integer) @default(0)

- The method to display the material ID title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

### `strNoteElemMatID` @type(String) @default("")

- An arbitrary user-defined name for the material ID title. This option was used whe&#x6E;_&#x69;NoteElemMatID_= 1.

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
Post.Note.Element(crlTargets=[ROElem(448)])

# Hide Material ID information
Post.SetNote.ElementMatID(bNoteElemMatID=False)
# User defines Material ID title
Post.SetNote.ElementMatID(iNoteElemMatID=1, strNoteElemMatID="Material ID")
```
