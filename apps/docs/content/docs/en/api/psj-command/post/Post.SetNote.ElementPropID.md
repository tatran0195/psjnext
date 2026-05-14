---
title: "Post.SetNote.ElementPropID()"
description: "Set the display of the property ID in the element's notes window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > ElementPropID"
macro _link: "[SetNoteElementPropID](../../macro/post/SetNoteElementPropID)"
---

## Description

Set the display of the property ID in the element's notes window.

## Syntax

```psj
Post.SetNote.ElementPropID(...)
```

## Inputs

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bNoteElemPropID`

- Whether to display the property ID in element's notes window.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iNoteElemPropID`

- The method to display the property ID title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strNoteElemPropID`

- An arbitrary user-defined name for the property ID title. This option was used when _iNoteElemPropID_= 1.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25,27}
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

# Hide Property ID information
Post.SetNote.ElementPropID(bNoteElemPropID=False)
# User defines Property ID title
Post.SetNote.ElementPropID(iNoteElemPropID=1, strNoteElemPropID="Property ID")
```
