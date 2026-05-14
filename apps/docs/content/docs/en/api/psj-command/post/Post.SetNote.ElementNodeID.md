---
title: "Post.SetNote.ElementNodeID()"
description: "Set the display of the node ID in the element's notes window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > ElementNodeID"
macro _link: "[SetNoteElementNodeID](../../macro/post/SetNoteElementNodeID)"
---

## Description

Set the display of the node ID in the element's notes window.

## Syntax

```psj
Post.SetNote.ElementNodeID(...)
```

## Inputs

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bNoteElemNodeID`

- Whether to display the node ID in element's notes window.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iNoteElemNodeID`

- The method to display the node ID title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strNoteElemNodeID`

- An arbitrary user-defined name for the node ID title. This option was used when _iNoteElemNodeID_= 1.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {24,26}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
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

# Hide Node ID information
Post.SetNote.ElementNodeID(bNoteElemNodeID=False)
# User defines Node ID title
Post.SetNote.ElementNodeID(iNoteElemNodeID=1, strNoteElemNodeID="Node IDs")
```
