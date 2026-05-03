---
title: "Analysis.ACTRAN.ExportBdf()"
description: "Export Analysis Model Nastran BDF Files"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ACTRAN > ExportBdf"
---

## Description

## Syntax

```psj
Analysis.ACTRAN.ExportBdf(...)
```

## Inputs

### `strPath` @type(String) @default("")

- The destination path file to export.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.ExportBdf(strPath="Job1.bdf")
```
