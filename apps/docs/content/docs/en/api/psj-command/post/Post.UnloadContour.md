---
title: "Post.UnloadContour()"
description: "Unload result from current model."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > UnloadContour"
macro _link: "ShowContour()"
---

## Description

Unload result from current model.

## Syntax

```psj
Post.UnloadContour(...)
```

## Inputs

This utility function does not require any input value.

## Return Code

True if success, or False if failed.

## Sample Code

```psj {26}
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath=samplePath)

# Load result
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

# Unload result
Post.UnloadContour()
```
