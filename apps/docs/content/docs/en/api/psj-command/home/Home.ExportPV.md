---
title: "Home.ExportPV()"
description: "Export PV File"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ExportPV"
macro _link: "[Export _Post _Viewer _File](../../macro/home/Export _Post _Viewer _File)"
---

## Description

Export PV File

## Syntax

```psj
Home.ExportPV(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iGroupType

- Specify the group type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strFileName

- Specify the file.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
import os

program _path=JPT.GetAppPathInfo(JPT.PathType.PROGRAM _PATH)
temp _path=JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)

Home.ImportResults.Nastran(
    strPath=os.path.join(
        program _path, 
        'SampleData/PSJ/PSJ-Utility/PostSample/101 _solid.op2')
)

Groups.RightClick.PropertyGroup()

Home.ExportGeometrySurface(strFolderName=temp _path)
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, 
                iResultSet=1, 
                iTimeStep=1, 
                strResultName="Stress", 
                strResultCompName="Mises", 
                iResultPos=4), 
        postDataOp=PostDataOp(
            iResultLocation=1, 
            iOptionConversion=1, 
            iOptionContinuous=8)
        )
    ]
)

Post.ShowDeformation(
        crPostJob=TSVPostJob(1), 
        postResultKey=PostResultKey(
            iAnalysisType=1, 
            iResultSet=1, 
            iTimeStep=1, 
            strResultName="Stress", 
            strResultCompName="Mises"))

Home.ExportPV(
    iGroupType=3, 
    strFileName=os.path.join(temp _path,'pv _test.tspv')
)
```
