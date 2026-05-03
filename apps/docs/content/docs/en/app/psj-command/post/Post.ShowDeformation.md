---
title: "Post.ShowDeformation()"
description: "Load deformation on the model."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ShowDeformation"
macro_link: "CmdShowPostDeformation"
---

## Description

Load deformation on the model.

## Syntax

```psj
Post.ShowDeformation(...)
```

## Inputs

### `crPostJob` @type(Cursor) @required

- The Post job result (post data).

### `postResultKey` @type(POST\_RESULT\_KEY) @required

- Result to show deformation.

### `postDataOption` @type(PostDataOp)

- Result options.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {19-26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
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
