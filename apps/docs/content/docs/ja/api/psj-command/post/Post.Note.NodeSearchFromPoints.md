---
title: "Post.Note.NodeSearchFromPoints()"
description: "Search the nearest node from the specified point and markup its node note"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Note > NodeSearchFromPoints"
macro _link: "[CmdMarkupSearchNodeFromPoint](../../macro/post/CmdMarkupSearchNodeFromPoint)"
---

## Description

Search the nearest node from the specified point and markup its node note

## Syntax

```psj
Post.Note.NodeSearchFromPoints(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### dlPositions

- Specify the coordinates of points to search the nearest nodes.

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
                    
# Search nodes from points and markup notes
node = Post.Note.NodeSearchFromPoints(dlPositions=[[30.0, 3.0, 2.5], [28.0, 8.0, 4.0]])
if len(node) >=1:
    for i in range(len(node)):
        print("The searched node is:", str(node[i]))
else:
    print("Cannot search the node from point")
```
