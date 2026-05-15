---
title: "Post.DisplayContour()"
description: "Display contour of loaded result."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > DisplayContour"
macro _link: "ShowContour()"
---

## Description

Display contour of loaded result.

## Syntax

```psj
Post.DisplayContour(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### bDisplay

- Specify show (_True_) or hide (_False_)  contour display.
- The default value is _True_.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
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
