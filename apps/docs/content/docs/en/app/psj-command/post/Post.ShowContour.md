---
title: "Post.ShowContour()"
description: "Load result on model and show contour."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ShowContour"
macro_link: "CmdShowPostContour"
---

## Description

Load result on model and show contour.

## Syntax

```psj
Post.ShowContour(...)
```

## Inputs

### `crPostJob` @type(Cursor) @required

- The Post job result (post data).

### `lContourSettings` @type(list of POST\_CONTOUR\_SETTINGS) @required

- The setting for contour of 1st result (required) and 2 additional results (optional).

### `bEnableMidNode` @type(Boolean) @default(False)

- Whether or not enable result option.

### `bApplyAll` @type(Boolean) @default(False)

- Whether or not apply above settings to all active Post documents.

## Return Code

- A _Boolean_ specifying if the contour can be showed or not.

## Sample Code

```psj {6-17}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
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
