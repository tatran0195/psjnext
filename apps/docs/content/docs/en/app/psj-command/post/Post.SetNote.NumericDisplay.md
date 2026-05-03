---
title: "Post.SetNote.NumericDisplay()"
description: "Set the method to display the numerical value in the note window"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > SetNote > NumericDisplay"
macro_link: "[SetNoteNumericDisplay](../../macro/post/SetNoteNumericDisplay)"
---

## Description

Set the method to display the numerical value in the note window.

## Syntax

```psj
Post.SetNote.NumericDisplay(...)
```

## Inputs

### `iNumericDisplay` @type(Integer) @default(1)

- The method to display the numerical value.
  - I&#x66;_&#x69;NumericDisplay_= 0: Real Type - Display the numerical values in real number format. The precision is five decimal places.
  - I&#x66;_&#x69;NumericDisplay_= 1: Power Type - Display the numerical values in exponential/scientific format.

### `iWidth` @type(Integer) @default(10)

- The display width of the numerical value.

### `iPrecision` @type(Integer) @default(5)

- The number of digits in the decimal part.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {25}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
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
