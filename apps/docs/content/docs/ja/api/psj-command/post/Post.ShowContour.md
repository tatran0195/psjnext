---
title: "Post.ShowContour()"
description: "Load result on model and show contour."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ShowContour"
macro _link: "CmdShowPostContour"
---

## Description

Load result on model and show contour.

## Syntax

```psj
Post.ShowContour(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crPostJob

- Specify the Post job result (post data).

<!-- @since:5.1.0 @required -->
### lContourSettings

- Specify the setting for contour of 1st result (required) and 2 additional results (optional).

<!-- @since:5.1.0 @optional -->
### bEnableMidNode

- Specify whether or not enable result option.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bApplyAll

- Specify whether or not apply above settings to all active Post documents.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying if the contour can be showed or not.

## Sample Code

```psj {6-17}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Show contour
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Displacement", 
                strResultCompName="Translational", 
                iResultPos=1), 
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
```
