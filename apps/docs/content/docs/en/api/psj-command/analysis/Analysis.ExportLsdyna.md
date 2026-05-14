---
title: "Analysis.ExportLsdyna()"
description: "Export LS-Dyna Analysis Job"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ExportLsdyna"
---

## Description

Export LS-Dyna Analysis Job.

## Syntax

```psj
Analysis.ExportLsdyna(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The destination path file to export.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crJob`

- The LS-Dyna analysis job.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=12999622)

Analysis.LSDYNAJob()

Analysis.ExportLsdyna(strPath="C:/Job _1.k", crJob=LSDynaJob(1))
```
