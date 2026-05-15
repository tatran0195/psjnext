---
title: "Tools.ContourCopy()"
description: "Display the contour of the current Post document in the specified Pre document"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > ContourCopy"
macro _link: "[ContourCopy](../../macro/tools/ContourCopy)"
---

## Description

Display the contour of the current Post document in the specified Pre document.

## Syntax

```psj
Tools.ContourCopy(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPostDocName

- Specify the Post document name to copy the contour.

<!-- @since:5.1.0 @required -->
### strPreDocName

- Specify the Pre document name to be copied the contour.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:
\- _True_: The process is executed successfully.
\- _False_: Cannot execute the function.

## Sample Code

```psj {31}
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)

# Prepare Pre model
Tools.ToPre(strName="101 _solid", ilOptions=[0, 1, 2, 3, 4])
# Plot the result
JPT.SetActiveDocumentByName("101 _solid",1)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=1, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Copy contour
dataCopy = Tools.ContourCopy(strPostDocName="101 _solid", strPreDocName="101 _solid _Converted _Pre")
JPT.Debugger(dataCopy)
```
