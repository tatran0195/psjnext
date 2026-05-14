---
title: "Analysis.ExportAnsys()"
description: "Export Ansys Analysis Job"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ExportAnsys"
macro _link: "[ExportAnsys](../../macro/analysis/ExportAnsys)"
---

## Description

Export Ansys Analysis Job.
\*This command is no more displayed in the latest Jupiter.

## Syntax

```psj
Analysis.ExportAnsys(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The destination path file to export.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crAnsysJob`

- The Ansys analysis job.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}
Geometry.Part.Cube()

Analysis.Ansys.LinearStatic(strJobName="Job _1", iJobdataAnatype=1, iJobdataSoltype=3, strJobdataJobname="Job _1",
    bBasicdataBoutputdisplacements=True, bBasicdataBoutputstress=True, iLCId=1, dTransientdataFalpha=0.252506)

Analysis.ExportAnsys(strName="D:/Job _1.dat", crAnsysJob=AnsysJob(1))
```
