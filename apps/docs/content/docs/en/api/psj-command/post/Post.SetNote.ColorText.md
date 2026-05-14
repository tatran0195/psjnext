---
title: "Post.SetNote.ColorText()"
description: "Set the text color and thickness of the character in the Note window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > ColorText"
macro _link: "[SetNoteColorText](../../macro/post/SetNoteColorText)"
---

## Description

Set the text color and thickness of the character in the Note window.

## Syntax

```psj
Post.SetNote.ColorText(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTextColor`

- The text color.

<!-- @since:5.1.0 @type:Integer @optional @default:14 -->
### `iTextSize`

- The text size.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
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

# Modify the text color and text size
Post.Note.Node(crlTargets=[RONode(133)])
Post.SetNote.ColorText(iTextColor=42495, iTextSize=18)
```
