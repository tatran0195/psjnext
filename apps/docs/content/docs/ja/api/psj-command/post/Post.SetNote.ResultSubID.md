---
title: "Post.SetNote.ResultSubID()"
description: "Set the display of the subcase ID in the note window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > ResultSubID"
macro _link: "[SetNoteResultSubID](../../macro/post/SetNoteResultSubID)"
---

## Description

Set the display of the subcase ID in the note window.

## Syntax

```psj
Post.SetNote.ResultSubID(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### bNoteResultSubID

- Specify whether to display the subcase ID in the note window.
- The default value is _True_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

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

# Hide Subcase ID
Post.SetNote.ResultSubID(bNoteResultSubID=False)
```
