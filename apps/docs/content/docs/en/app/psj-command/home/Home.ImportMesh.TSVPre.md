---
title: "Home.ImportMesh.TSVPre()"
description: "Convert a old TSV-Pre/Designer file into one or more jtdb files."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportMesh > TSVPre"
macro_link: "[ImportVDB](../../macro/home/ImportVDB)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Convert a old TSV-Pre/Designer file into one or more jtdb files.

## Syntax

```psj
Home.ImportMesh.TSVPre(...)
```

## Inputs

### `strImportPath` @type(String) @default("")

- The import path.

### `strExportPath` @type(String) @default("")

- The export path.

### `ilModelIndex` @type(List\[Integer]) @default(None)

- The model index.

### `iMerge` @type(Integer) @default(None)

- The merge.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
import os

VDB_file_path = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH), 
    "SampleData/PSJ/PSJ-Utility/VDBSample/sample.vdb")

export_file_path = os.environ["Temp"] + "/TechnoStar/"
Home.ImportMesh.TSVPre(strImportPath=VDB_file_path, strExportPath=export_file_path)
```
