---
title: "Post.Note.Node()"
description: "Add a note indication to the selected node on the main window, and input it to the data table in the Node tab of the Watch Data window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Note > Node"
macro _link: "[CmdMarkupNode](../../macro/post/CmdMarkupNode)"
---

## Description

Add a note indication to the selected node on the main window, and input it to the data table in the Node tab of the Watch Data window.

## Syntax

```psj
Post.Note.Node(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the selected nodes to markup the notes.

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
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=4))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))

# Display note at the selected nodes
Post.Note.Node(crlTargets=[RONode(129,133)])
```
