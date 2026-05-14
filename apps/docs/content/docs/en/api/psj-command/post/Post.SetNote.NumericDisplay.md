---
title: "Post.SetNote.NumericDisplay()"
description: "Set the method to display the numerical value in the note window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > SetNote > NumericDisplay"
macro _link: "[SetNoteNumericDisplay](../../macro/post/SetNoteNumericDisplay)"
---

## Description

Set the method to display the numerical value in the note window.

## Syntax

```psj
Post.SetNote.NumericDisplay(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iNumericDisplay`

- The method to display the numerical value.
  - If _iNumericDisplay_ = 0: Real Type - Display the numerical values in real number format. The precision is five decimal places.
  - If _iNumericDisplay_ = 1: Power Type - Display the numerical values in exponential/scientific format.

<!-- @since:5.1.0 @type:Integer @optional @default:10 -->
### `iWidth`

- The display width of the numerical value.

<!-- @since:5.1.0 @type:Integer @optional @default:5 -->
### `iPrecision`

- The number of digits in the decimal part.

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

# Display the numerical value as Real Type
Post.SetNote.NumericDisplay(iNumericDisplay=0, iPrecision=6)
```
