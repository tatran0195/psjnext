---
title: "Post.DisplayContour()"
description: "Display contour of loaded result."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > DisplayContour"
macro_link: "ShowContour()"
---

## Description

Display contour of loaded result.

## Syntax

```psj
Post.DisplayContour(...)
```

## Inputs

### `bDisplay` @type(Boolean) @default(True)

- Show (_True_) or hide (_False_)  contour display.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Show contour
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", 
                strResultCompName="Translational", iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])

Post.ShowDeformation(
    crPostJob=TSVPostJob(1), 
    postResultKey=PostResultKey(
        iAnalysisType=1, 
        iResultSet=1, 
        iTimeStep=1, 
        strResultName="Displacement", 
        strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Hide contour display
Post.DisplayContour(bDisplay=False)
```
