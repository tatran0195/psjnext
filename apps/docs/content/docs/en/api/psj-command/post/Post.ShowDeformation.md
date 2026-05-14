---
title: "Post.ShowDeformation()"
description: "Load deformation on the model."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ShowDeformation"
macro _link: "CmdShowPostDeformation"
---

## Description

Load deformation on the model.

## Syntax

```psj
Post.ShowDeformation(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @required -->
### `crPostJob`

- The Post job result (post data).

<!-- @since:5.1.0 @type:POST _RESULT _KEY @required -->
### `postResultKey`

- The result to show deformation.

<!-- @since:5.1.0 @type:PostDataOp @optional -->
### `postDataOption`

- The result options.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {19-26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Load contour
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
