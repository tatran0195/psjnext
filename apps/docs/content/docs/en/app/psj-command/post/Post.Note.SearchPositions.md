---
title: "Post.Note.SearchPositions()"
description: "Search point and markup its position note"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Note > SearchPositions"
macro_link: "[CmdMarkupSearchPoint](../../macro/post/CmdMarkupSearchPoint)"
---

## Description

Search point and markup its position note.

## Syntax

```psj
Post.Note.SearchPositions(...)
```

## Inputs

### `dlPositions` @type(List\[Double]) @required

- The coordinates of points for searching.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance value for searching.

### `bSearch` @type(Boolean) @default(False)

- Whether to search only on the displayed parts or all parts of the model.

## Return Code

- A list of _Boolean_ specifying whether the search target is successfully found or not.
  - _True_: The target is found.
  - _False_: The target is not found.

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

# Search and display note at points
ret=Post.Note.SearchPositions(
        dlPositions=[
            [0.0, 0.0, 0.0], 
            [22.0, 5.0, 5.0], 
            [22.0, 10.0, 5.0], 
            [10.0, 10.0, 10.0]], 
        dTolerance=0.01)
        
# >> [1,1,1,0] First 3 points are found, last 1 point is not found.
print(ret)
```
