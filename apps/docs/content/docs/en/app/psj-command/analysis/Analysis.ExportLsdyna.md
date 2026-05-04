---
title: 'Analysis.ExportLsdyna()'
description: 'Export LS-Dyna Analysis Job'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ExportLsdyna'
---

## Description

Export LS-Dyna Analysis Job.

## Syntax

```psj
Analysis.ExportLsdyna(...)
```

## Inputs

### `strPath` @type(String) @default("")

- The destination path file to export.

### `crJob` @type(Cursor) @default(None)

- The LS-Dyna analysis job.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=12999622)

Analysis.LSDYNAJob()

Analysis.ExportLsdyna(strPath="C:/Job_1.k", crJob=LSDynaJob(1))
```
