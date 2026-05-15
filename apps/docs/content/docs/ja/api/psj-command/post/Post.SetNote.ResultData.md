---
title: "Post.SetNote.ResultData()"
description: "Set the display of result data title in the note window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > ResultData"
macro _link: "[SetNoteResultData](../../macro/post/SetNoteResultData)"
---

## Description

Set the display of result data title in the note window.

## Syntax

```psj
Post.SetNote.ResultData(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNoteResultTitle

- Specify the method to display the result data title as default or user-defined name.
  - 0: Default
  - 1: User-Defined
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strNoteResultTitle

- Specify an arbitrary user-defined name for result data title. This option was used when _iNoteResultTitle_= 1.
- The default value is "".

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
Post.Note.Node(crlTargets=[RONode(133)])

# User defines Result Data title
Post.SetNote.ResultData(iNoteResultTitle=1, strNoteResultTitle="Result Data")
```
