---
title: "Post.SetNote.ResultPos()"
description: "Set the display of coordinates of the selected position in the note window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > ResultPos"
macro _link: "[SetNoteResultPos](../../macro/post/SetNoteResultPos)"
---

## Description

Set the display of coordinates of the selected position in the note window.

## Syntax

```psj
Post.SetNote.ResultPos(...)
```

## Inputs

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bNoteResultPos`

- Whether to display the coordinates of the selected position in the note window.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iNoteResultPos`

- The method to display the coordinate title as default or user-defined name.
  - 0: Default
  - 1: User-Defined

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strNoteResultPos`

- An arbitrary user-defined name for the coordinate title. This option was used when _iNoteResultPos_= 1.

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
Post.Note.Position(crElement=ROElem(448), dlPosition=[28.588114, 6.313289, 5.0])

# Hide Position information
Post.SetNote.ResultPos(bNoteResultPos=False)
# User defines Position title
Post.SetNote.ResultPos(iNoteResultPos=1, strNoteResultPos="Position")
```
