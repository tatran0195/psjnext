---
title: 'Analysis.ExportAnsys()'
description: 'Export Ansys Analysis Job'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ExportAnsys'
macro_link: '[ExportAnsys](../../macro/analysis/ExportAnsys)'
---

<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export Ansys Analysis Job.
\*This command is no more displayed in the latest Jupiter.

## Syntax

```psj
Analysis.ExportAnsys(...)
```

## Inputs

### `strName` @type(String) @default("")

- The destination path file to export.

### `crAnsysJob` @type(Cursor) @default(None)

- The Ansys analysis job.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}
Geometry.Part.Cube()

Analysis.Ansys.LinearStatic(strJobName="Job_1", iJobdataAnatype=1, iJobdataSoltype=3, strJobdataJobname="Job_1",
    bBasicdataBoutputdisplacements=True, bBasicdataBoutputstress=True, iLCId=1, dTransientdataFalpha=0.252506)

Analysis.ExportAnsys(strName="D:/Job_1.dat", crAnsysJob=AnsysJob(1))
```
