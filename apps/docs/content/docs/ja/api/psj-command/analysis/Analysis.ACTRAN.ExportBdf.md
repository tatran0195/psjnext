---
title: "Analysis.ACTRAN.ExportBdf()"
description: "Export Analysis Model Nastran BDF Files"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ACTRAN > ExportBdf"
---

## Description

## Syntax

```psj
Analysis.ACTRAN.ExportBdf(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the destination path file to export.
- The default value is "".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.ExportBdf(strPath="Job1.bdf")
```
