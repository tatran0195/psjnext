---
title: "Post.SetNote.ElementType()"
description: "Set the display of the element type in the element's notes window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ElementType"
macro_link: "[SetNoteElementType](../../macro/post/SetNoteElementType)"
---

## Description

Set the display of the element type in the element's notes window.

## Syntax

```psj
Post.SetNote.ElementType(...)
```

## Inputs

### `bNoteElemType` @type(Boolean) @default(True)

- Whether to display the element type in the element's notes window.

### `iNoteElemType` @type(Integer) @default(0)

- The method to display the element type title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

### `strNoteElemType` @type(String) @default("")

- An arbitrary user-defined name for the element type title. This option was used whe&#x6E;_&#x69;NoteElemType_= 1.

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

# Hide Element type information
Post.SetNote.ElementType(bNoteElemType=False)
# User defines Element type title
Post.SetNote.ElementType(iNoteElemType=1, strNoteElemType="Element Type")
```
