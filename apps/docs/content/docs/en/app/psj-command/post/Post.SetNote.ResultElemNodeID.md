---
title: "Post.SetNote.ResultElemNodeID()"
description: "Set the node ID or element ID of the entity to be displayed in the note window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > ResultElemNodeID"
macro_link: "[SetNoteResultElemNodeID](../../macro/post/SetNoteResultElemNodeID)"
---

## Description

Set the node ID or element ID of the entity to be displayed in the note window.

## Syntax

```psj
Post.SetNote.ResultElemNodeID(...)
```

## Inputs

### `bNoteResultElemNodeID` @type(Boolean) @default(True)

- Whether to display the ID of Elements/Nodes in the note window.

### `iNoteResultElemNodeID` @type(Integer) @default(0)

- The method to display the Element/Node ID title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

### `strNoteResultElemNodeID` @type(String) @default("")

- An arbitrary user-defined name for the Element/Node ID title. This option was used whe&#x6E;_&#x69;NoteResultElemNodeID_= 1.

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

# Hide Element ID information
Post.SetNote.ResultElemNodeID(bNoteResultElemNodeID=False)
# User defines Element ID title
Post.SetNote.ResultElemNodeID(iNoteResultElemNodeID=1, strNoteResultElemNodeID="ELem/NodeID")
```
